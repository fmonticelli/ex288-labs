# 08 — Deployments e aplicações

## Objetivo

Executar imagens já construídas no OpenShift, expor aplicações usando Deployment, Service e Route e controlar o ciclo de vida de rollouts.

Este capítulo registra os comandos e comportamentos praticados nos laboratórios, incluindo:

- criação de Deployment;
- Service e Route;
- ImageChange trigger;
- ReplicaSets e revisões;
- `RollingUpdate`;
- `Recreate`;
- `maxSurge` e `maxUnavailable`;
- `revisionHistoryLimit`;
- `progressDeadlineSeconds`;
- rollout history;
- rollback;
- troubleshooting de `ImagePullBackOff`;
- validação com `oc exec`.

---

# Fluxo de runtime

```text
ImageStream / Registry
        ↓
Deployment
        ↓
ReplicaSet
        ↓
Pod
        ↓
Service
        ↓
Route
```

Uma alteração no `spec.template` do Deployment cria uma nova revisão e, normalmente, um novo ReplicaSet.

Exemplos de mudanças no PodTemplate:

```text
imagem
variável de ambiente
command / args
probes
resources
volumes
labels do template
```

---

# Criar Deployment

Exemplo praticado com a aplicação `vote`:

```bash
oc create deployment vote \
  --image=image-registry.openshift-image-registry.svc:5000/monticelli-ex288/vote:latest
```

Exemplo praticado com `s2i-broken-run`:

```bash
oc create deployment s2i-broken-run \
  --image=image-registry.openshift-image-registry.svc:5000/monticelli-ex288/s2i-broken-run:latest
```

## Dry-run

```bash
oc create deployment vote \
  --image=image-registry.openshift-image-registry.svc:5000/monticelli-ex288/vote:latest \
  --dry-run=server \
  -o yaml
```

Foi observado que `oc create deployment` gera labels como:

```yaml
metadata:
  labels:
    app: vote
```

e reutiliza o label no selector e no PodTemplate.

---

# Deployment → ReplicaSet → Pod

```bash
oc get deployment vote
oc get rs -l app=vote
oc get po -l app=vote
```

Modelo mental:

```text
Deployment
   ↓
controla ReplicaSets
   ↓
ReplicaSet
   ↓
mantém os Pods daquela revisão
```

Quando o PodTemplate muda:

```text
Deployment
   ↓
novo ReplicaSet
   ↓
novos Pods
```

ReplicaSets antigos normalmente permanecem com:

```text
DESIRED   0
CURRENT   0
READY     0
```

Isso permite histórico e rollback.

---

# Service

```bash
oc expose deployment vote \
  --port=8080 \
  --target-port=8080
```

Validação:

```bash
oc get svc vote
oc describe svc vote
oc get endpoints vote
```

`oc expose deployment` cria um Service, não uma Route.

---

# Route

## Route HTTP

```bash
oc expose service vote
```

## Route HTTPS com edge termination

```bash
oc create route edge vote \
  --service=vote \
  --insecure-policy=Redirect
```

Também foi validado que o nome da Route pode ser omitido:

```bash
oc create route edge \
  --service=tasks \
  --insecure-policy=Redirect
```

Nesse caso a Route pode assumir o nome do Service.

Fluxo:

```text
HTTP
 ↓
Redirect
 ↓
HTTPS
 ↓
OpenShift Router
 ↓
HTTP
 ↓
Service
 ↓
Pod
```

`Redirect` é case-sensitive.

---

# ImageChange trigger no Deployment

Configurar:

```bash
oc set triggers deployment/vote \
  --from-image=vote:latest \
  -c vote
```

Consultar:

```bash
oc set triggers deployment/vote
```

Exemplo usado no laboratório S2I:

```bash
oc set triggers deployment/s2i-broken-run \
  --from-image=s2i-broken-run:latest \
  -c s2i-broken-run
```

Modelo mental:

```text
ImageStreamTag muda
       ↓
ImageChange trigger
       ↓
Deployment atualiza PodTemplate
       ↓
novo ReplicaSet
       ↓
novo Pod
```

## Trigger x rollout restart

Não são equivalentes.

```bash
oc rollout restart deployment/<nome>
```

significa:

```text
crie novos Pods agora
```

Já:

```bash
oc set triggers deployment/<nome> \
  --from-image=<imagestream>:latest \
  -c <container>
```

significa:

```text
quando a ImageStreamTag mudar,
atualize o Deployment automaticamente
```

Para recuperar a sintaxe:

```bash
oc set --help
oc set triggers --help
```

---

# Validar imagem / digest

Imagem usada pelo Deployment:

```bash
oc get deployment vote \
  -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```

Imagem atual de um ImageStreamTag:

```bash
oc get istag vote:latest \
  -o jsonpath='{.image.dockerImageReference}{"\n"}'
```

Uma mudança em `:latest` não provoca rollout automaticamente sem trigger apropriado.

`imagePullPolicy: Always` também não monitora continuamente uma tag e não reinicia Pods existentes.

---

# Estratégia de Deployment

Consultar:

```bash
oc get deployment s2i-broken-run \
  -o jsonpath='{.spec.strategy.type}{"\n"}'
```

Ou:

```bash
oc get deployment s2i-broken-run -o yaml | less
```

Exemplo observado:

```yaml
spec:
  progressDeadlineSeconds: 600
  replicas: 1
  revisionHistoryLimit: 10
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
```

---

# RollingUpdate

`RollingUpdate` tenta substituir a versão antiga progressivamente.

Fluxo simplificado:

```text
Pod antigo Running
        ↓
cria Pod novo
        ↓
Pod novo fica Ready
        ↓
remove Pod antigo
```

Durante o rollout, Pods de versões antiga e nova podem coexistir.

Isso prioriza disponibilidade.

## Gerar nova revisão

Foi usada uma variável de ambiente para alterar o PodTemplate:

```bash
oc set env deployment/s2i-broken-run LAB_VERSION=v2
```

Acompanhar:

```bash
oc rollout status deployment/s2i-broken-run
```

Validar:

```bash
oc get pods -l app=s2i-broken-run
oc get rs -l app=s2i-broken-run
oc rollout history deployment/s2i-broken-run
```

Validar a variável dentro do container:

```bash
oc exec deployment/s2i-broken-run -- env | grep LAB_VERSION
```

Resultado observado:

```text
LAB_VERSION=v2
```

---

# `maxUnavailable`

Define quantos Pods podem ficar indisponíveis durante um `RollingUpdate`.

Exemplo:

```yaml
replicas: 3

strategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 1
```

Significa:

```text
3 réplicas desejadas
- 1 indisponível permitido
= mínimo de 2 Pods disponíveis
```

Também pode ser percentual:

```yaml
maxUnavailable: 25%
```

Percentuais são arredondados para baixo.

Com:

```text
replicas = 3
maxUnavailable = 25%
```

temos:

```text
25% de 3 = 0,75
arredonda para baixo
→ 0
```

Portanto nenhum Pod disponível pode ser perdido durante o rollout antes que outro esteja disponível.

Modelo mental:

```text
maxUnavailable
→ quantos Pods posso perder temporariamente?
```

---

# `maxSurge`

Define quantos Pods extras podem existir temporariamente durante um `RollingUpdate`.

Exemplo:

```yaml
replicas: 3

strategy:
  type: RollingUpdate
  rollingUpdate:
    maxSurge: 1
```

Permite:

```text
3 desejados
+ 1 extra
= até 4 Pods temporariamente
```

Também pode ser percentual:

```yaml
maxSurge: 25%
```

Percentuais são arredondados para cima.

Com:

```text
replicas = 3
maxSurge = 25%
```

temos:

```text
25% de 3 = 0,75
arredonda para cima
→ 1
```

Modelo mental:

```text
maxSurge
→ quantos Pods extras posso criar durante o rollout?
```

---

# Exemplo: 3 réplicas, máximo de 6 Pods, mínimo de 1 disponível

Requisito:

```text
réplicas desejadas = 3
máximo durante rollout = 6
mínimo disponível = 1
```

Configuração:

```yaml
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 3
      maxUnavailable: 2
```

Cálculo:

```text
máximo:
3 + 3 = 6

mínimo disponível:
3 - 2 = 1
```

Com `maxSurge: 3`, o controller pode criar os 3 novos Pods praticamente ao mesmo tempo se houver capacidade no cluster.

`RollingUpdate` não significa obrigatoriamente "um Pod por vez".

Exemplo possível:

```text
old=3 new=0
      ↓
old=3 new=3
      ↓
novos ficam Ready
      ↓
old=0 new=3
```

Os valores são limites permitidos, não um roteiro rígido.

---

# Capacidade do cluster e `maxSurge`

Exemplo:

```text
3 workers
3 Pods atuais
1 Pod em cada worker
maxUnavailable=0
maxSurge=1
```

Se houver CPU/memória disponível, o scheduler pode colocar temporariamente dois Pods no mesmo worker.

Mas se não houver capacidade para o Pod extra:

```text
3 Pods antigos Running
+
novo Pod Pending
```

E como:

```text
maxUnavailable=0
```

o Deployment não pode remover um Pod antigo para liberar capacidade.

Resultado:

```text
rollout sem progresso
```

Isso pode parecer problema do Deployment, mas `oc describe pod` pode mostrar que a causa real é scheduling/recursos.

---

# Recreate

Alteração realizada com:

```bash
oc edit deployment/s2i-broken-run
```

De:

```yaml
strategy:
  rollingUpdate:
    maxSurge: 25%
    maxUnavailable: 25%
  type: RollingUpdate
```

Para:

```yaml
strategy:
  type: Recreate
```

Validar:

```bash
oc get deployment s2i-broken-run \
  -o jsonpath='{.spec.strategy.type}{"\n"}'
```

Resultado:

```text
Recreate
```

## Comportamento observado

Foi gerada nova revisão:

```bash
oc set env deployment/s2i-broken-run DEPLOY_TEST=recreate-v2
```

Watcher:

```bash
oc get pods -l app=s2i-broken-run -w
```

Comportamento observado:

```text
Pod antigo Running
        ↓
Pod antigo Terminating
        ↓
Pod antigo removido
        ↓
novo Pod Pending
        ↓
ContainerCreating
        ↓
Running
```

Ou seja:

```text
Recreate
→ remove a versão antiga
→ depois cria a nova
```

Há possibilidade de downtime.

Mesmo com várias réplicas, a estratégia busca eliminar os Pods antigos antes de escalar o novo ReplicaSet.

## Quando `Recreate` pode ser útil

Quando não é aceitável ter versão antiga e nova coexistindo.

Exemplos:

- migração de banco incompatível entre versões;
- aplicação legada que não suporta múltiplas instâncias;
- consumidor de fila que não pode ter duas versões concorrentes;
- recursos externos exclusivos;
- mudança incompatível no formato de dados.

Modelo mental:

```text
RollingUpdate
→ prioridade: disponibilidade
→ old + new podem coexistir

Recreate
→ prioridade: não coexistir versões
→ aceita possível downtime
```

---

# `revisionHistoryLimit`

Exemplo:

```yaml
revisionHistoryLimit: 10
```

Define quantos ReplicaSets antigos o Deployment tenta preservar para histórico/rollback.

Modelo mental:

```text
ReplicaSet atual
+
até 10 ReplicaSets antigos
```

Exemplo:

```text
RS atual        replicas > 0
RS antigo #1   replicas = 0
RS antigo #2   replicas = 0
...
RS antigo #10  replicas = 0
```

O ReplicaSet atual não entra no limite de históricos antigos.

Portanto:

```text
revisionHistoryLimit: X
→ até X ReplicaSets antigos
→ além do ReplicaSet atual
```

Não significa obrigatoriamente `X + 1` ReplicaSets em todos os instantes, porque durante rollouts e cleanup podem existir estados transitórios.

Consultar:

```bash
oc rollout history deployment/s2i-broken-run
```

Exemplo observado:

```text
REVISION
1
2
3
4
```

Detalhar uma revisão:

```bash
oc rollout history deployment/s2i-broken-run --revision=4
```

Isso mostra o PodTemplate daquela revisão, incluindo imagem e variáveis de ambiente.

---

# `progressDeadlineSeconds`

Exemplo:

```yaml
progressDeadlineSeconds: 600
```

Define quanto tempo o Deployment tolera ficar sem progresso suficiente no rollout antes de registrar que o rollout não está progredindo.

```text
600 segundos
= 10 minutos
```

Exemplo:

```text
novo Pod
↓
ImagePullBackOff
↓
não fica Ready
↓
rollout não progride
↓
deadline excedido
```

O Deployment pode registrar uma condição semelhante a:

```text
Progressing=False
Reason=ProgressDeadlineExceeded
```

Consultar:

```bash
oc describe deployment s2i-broken-run
```

ou:

```bash
oc get deployment s2i-broken-run -o yaml
```

Importante:

```text
progressDeadlineSeconds
NÃO faz rollback automático
```

Ele sinaliza:

```text
"o rollout não está fazendo progresso"
```

A correção/rollback continua sendo uma ação separada.

---

# Rollout history

Consultar:

```bash
oc rollout history deployment/s2i-broken-run
```

Detalhar revisão:

```bash
oc rollout history deployment/s2i-broken-run --revision=4
```

Exemplo observado na revisão quebrada:

```text
Image:
image-registry.openshift-image-registry.svc:5000/monticelli-ex288/s2i-broken-run:this-tag-does-not-exist

Environment:
LAB_VERSION=v2
```

Isso permitiu identificar qual revisão introduziu o problema.

---

# Rollback

Rollback para a revisão anterior:

```bash
oc rollout undo deployment/s2i-broken-run
```

Rollback para uma revisão específica:

```bash
oc rollout undo deployment/s2i-broken-run --to-revision=3
```

Validação:

```bash
oc rollout status deployment/s2i-broken-run
oc get pods -l app=s2i-broken-run
oc get rs -l app=s2i-broken-run
oc rollout history deployment/s2i-broken-run
```

Também foi validado:

```bash
oc exec deployment/s2i-broken-run -- env | grep LAB_VERSION
```

## Comportamento importante do rollback

O rollback não simplesmente "volta o Deployment para revision 3".

Ele reaplica o PodTemplate daquela revisão como um novo estado.

Exemplo observado:

```text
revision 3
→ estado saudável

rollback --to-revision=3
→ configuração reaplicada

nova revisão
→ revision 5
```

Por isso uma revisão antiga pode desaparecer da lista e reaparecer como uma revisão nova.

---

# Troubleshooting: imagem inexistente com RollingUpdate

Foi configurada propositalmente uma imagem inexistente:

```bash
oc set image deployment/s2i-broken-run \
  s2i-broken-run=image-registry.openshift-image-registry.svc:5000/monticelli-ex288/s2i-broken-run:this-tag-does-not-exist
```

Resultado com `RollingUpdate`:

```text
Pod antigo
1/1 Running

Pod novo
0/1 ImagePullBackOff
```

ReplicaSets:

```text
RS antigo
DESIRED 1
READY   1

RS novo
DESIRED 1
READY   0
```

A aplicação manteve uma instância saudável porque o novo Pod nunca ficou Ready.

Comandos usados:

```bash
oc get pods -l app=s2i-broken-run
oc get rs -l app=s2i-broken-run
oc rollout history deployment/s2i-broken-run
oc rollout status deployment/s2i-broken-run --timeout=20s
```

Diagnóstico detalhado:

```bash
oc describe pod <pod-quebrado>
```

Status:

```text
ImagePullBackOff
```

Causa:

```text
Deployment referenciando uma tag de imagem inexistente
```

---

# Troubleshooting: imagem inexistente com Recreate

Foi repetida a mesma falha usando:

```yaml
strategy:
  type: Recreate
```

Resultado:

```text
Pod antigo
→ encerrado

novo Pod
→ ErrImagePull
→ ImagePullBackOff
```

Não havia Pod saudável antigo para continuar servindo a aplicação.

Comandos usados:

```bash
oc get pods -l app=s2i-broken-run
oc get rs -l app=s2i-broken-run
oc get pods -l app=s2i-broken-run -w
oc rollout status deployment/s2i-broken-run --timeout=20s
```

Resultado do rollout:

```text
0 of 1 updated replicas are available
error: timed out waiting for the condition
```

Comparação:

```text
RollingUpdate + nova imagem quebrada
→ Pod antigo permanece saudável
→ aplicação pode continuar disponível

Recreate + nova imagem quebrada
→ Pod antigo já foi removido
→ aplicação fica sem instância saudável
```

---

# `oc rollout status`

Acompanhar rollout:

```bash
oc rollout status deployment/s2i-broken-run
```

Limitar espera:

```bash
oc rollout status deployment/s2i-broken-run --timeout=20s
```

Útil durante troubleshooting para não esperar indefinidamente.

---

# `oc exec`

Foi utilizado para validar configuração dentro do container:

```bash
oc exec deployment/s2i-broken-run -- env | grep LAB_VERSION
```

E:

```bash
oc exec deployment/s2i-broken-run -- env | grep DEPLOY_TEST
```

Isso permite validar o estado real dentro do Pod, não apenas o YAML desejado do Deployment.

---

# Comandos principais praticados

## Inspeção

```bash
oc get deployment <nome>
oc get deployment <nome> -o yaml
oc describe deployment <nome>

oc get rs -l app=<nome>
oc get pods -l app=<nome>
oc get pods -l app=<nome> -w
```

## Alteração

```bash
oc edit deployment/<nome>

oc set env deployment/<nome> CHAVE=valor

oc set image deployment/<nome> \
  <container>=<imagem>
```

## Rollout

```bash
oc rollout status deployment/<nome>
oc rollout status deployment/<nome> --timeout=20s

oc rollout history deployment/<nome>
oc rollout history deployment/<nome> --revision=<N>

oc rollout undo deployment/<nome>
oc rollout undo deployment/<nome> --to-revision=<N>

oc rollout restart deployment/<nome>
```

## Trigger

```bash
oc set triggers deployment/<nome>

oc set triggers deployment/<nome> \
  --from-image=<imagestream>:latest \
  -c <container>
```

## Runtime

```bash
oc exec deployment/<nome> -- <comando>
```

---

# `oc explain` e `--help`

Para reconstruir sintaxe e campos durante a prova:

```bash
oc rollout --help
oc rollout undo --help
oc set --help
oc set triggers --help
```

Para consultar campos do objeto:

```bash
oc explain deployment.spec.strategy
oc explain deployment.spec.strategy.rollingUpdate
```

Essa abordagem é preferível a tentar decorar todas as flags.

---

# Pegadinhas para a EX288

```text
oc expose deployment
→ cria Service

oc expose service
→ cria Route
```

```text
oc rollout restart
→ força rollout agora

ImageChange trigger
→ automatiza rollout quando a imagem mudar
```

```text
RollingUpdate
→ versões antiga e nova podem coexistir

Recreate
→ versão antiga é removida antes da nova
```

```text
maxUnavailable
→ quantos Pods podem ficar indisponíveis

maxSurge
→ quantos Pods extras podem existir temporariamente
```

```text
revisionHistoryLimit
→ até quantos ReplicaSets antigos são preservados
```

```text
progressDeadlineSeconds
→ deadline para detectar rollout sem progresso
→ não faz rollback automático
```

```text
ImagePullBackOff
→ olhar oc describe pod e Events
```

---

# Exercícios realizados

- criação manual de Deployment;
- Service;
- Route HTTP;
- Route HTTPS edge/Redirect;
- labels e selectors;
- ReplicaSets;
- rollout automático via ImageChange;
- alteração de PodTemplate com `oc set env`;
- validação com `oc exec`;
- `RollingUpdate`;
- `Recreate`;
- acompanhamento com `oc get pods -w`;
- `maxSurge`;
- `maxUnavailable`;
- `revisionHistoryLimit`;
- `progressDeadlineSeconds`;
- rollout history;
- inspeção de revisão específica;
- rollback para revisão específica;
- geração proposital de `ImagePullBackOff`;
- comparação de disponibilidade entre `RollingUpdate` e `Recreate`;
- troubleshooting de rollout.
