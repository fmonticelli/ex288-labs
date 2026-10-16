# EX288 Labs

Repositório pessoal de estudos para a certificação Red Hat EX288, com foco em prática hands-on no OpenShift.

O estudo será realizado progressivamente, construindo os recursos e aplicações conforme os tópicos forem sendo praticados.

## Status

Legenda:

- ⬜ não estudado
- 🟡 revisar
- ✅ consigo fazer sozinho

### Cobertura estimada do conteúdo

> Estimativa de cobertura prática do conteúdo da EX288 com base no que já foi estudado e executado em laboratório. Não representa peso oficial de questões nem probabilidade de aprovação.

```text
Cobertura atual: ~60%

████████████░░░░░░░░ 60%
```

Leitura rápida:

```text
forte / praticado
→ Git e CLI oc
→ Container Images
→ BuildConfig e Builds
→ ImageStreams
→ S2I
→ Deployments e rollouts
→ Troubleshooting
→ Health Monitoring / Probes

em andamento / precisa reforço
→ timings e thresholds de probes
→ ImageChange trigger no Deployment
→ troubleshooting de ImageStreams
→ Custom Builder
→ save-artifacts / incremental S2I

ainda não coberto de forma suficiente
→ ConfigMaps e Secrets
→ multi-container Pods
→ OpenShift Templates
→ Helm
→ Kustomize
→ Pipelines / Tekton
→ Operators
→ console web
```

A métrica acompanha **cobertura de conteúdo**, não domínio sob pressão de prova. A prontidão real será validada por exercícios sem ajuda e simulados integrados.

---

<!-- TOPICS_INDEX_START -->

# Material estudado

- [🧭 Mindmap navegável](mindmap/)
- [01 — Fundamentos OpenShift e Git](topics/01-openshift-git/)
- [02 — Container Images](topics/02-container-images/)
- [03 — BuildConfig e Builds](topics/03-buildconfig-builds/)
- [04 — ImageStreams](topics/04-imagestreams/)
- [S2I — aplicação prática](s2i-python/)
- [S2I — troubleshooting prático](s2i-troubleshooting/)
- [07 — Health Monitoring / Probes](topics/07-health-monitoring/)
- [08 — Deployments e aplicações](topics/08-deployments-applications/)
- [09 — Troubleshooting](topics/09-troubleshooting/)

O `mindmap/` mostra como os objetos e fluxos se conectam. Os diretórios em `topics/` guardam conceitos, comandos, exercícios, validações e troubleshooting realizados durante os laboratórios.

<!-- TOPICS_INDEX_END -->

# Checklist EX288

## 1. Fundamentos OpenShift e Git

- ✅ Trabalhar com Projects / Namespaces
- ✅ Trabalhar com Pods
- ✅ Criar e gerenciar Deployments
- ✅ Entender ReplicaSets e revisões de rollout
- ✅ Criar e utilizar Services
- ✅ Criar e utilizar Routes
- ✅ Trabalhar com Git no fluxo de deployment
- ⬜ Utilizar o console web do OpenShift
- ✅ Utilizar a CLI `oc`

## 2. Container Images

- ✅ Criar Containerfile
- ✅ `FROM`
- ✅ `WORKDIR`
- ✅ `COPY`
- ✅ `RUN`
- ✅ `ENV`
- ✅ `EXPOSE`
- ✅ `ENTRYPOINT` e `CMD`
- ✅ Build de imagem
- ✅ Cache de layers
- 🟡 Multi-stage builds
- ✅ Execução com usuário não-root
- ✅ Compatibilidade com UID arbitrário
- ✅ Permissões de arquivos e diretórios
- ✅ Utilizar imagens no OpenShift

## 3. BuildConfig e Builds

- ✅ Criar BuildConfig
- ✅ Build a partir de Git
- ✅ Utilizar `contextDir`
- ✅ Docker / Containerfile build strategy
- ✅ Configurar output do build
- ✅ Iniciar build manualmente
- ✅ Acompanhar logs de build
- ✅ Cancelar builds
- ✅ Reiniciar builds com `oc cancel-build --restart`
- ✅ Reexecutar build com `oc start-build --from-build`
- ✅ Build triggers
- ✅ ImageChange trigger no BuildConfig
- ✅ Configurar histórico de builds
- ✅ Build Run Policy: `Serial`, `Parallel` e `SerialLatestOnly`
- ✅ Post-commit build hook
- 🟡 Custom builder
- ✅ Troubleshooting de builds

## 4. ImageStreams

- ✅ Entender ImageStreams
- ✅ Criar ImageStream
- ✅ Trabalhar com ImageStreamTag
- ✅ Entender tag x digest
- ✅ Publicar imagens no ImageStream
- ✅ Utilizar o registry interno do OpenShift
- ✅ Consumir ImageStream em aplicações
- ✅ Image change triggers
- 🟡 Troubleshooting de ImageStreams

## 5. Source-to-Image (S2I)

- ✅ Entender o fluxo S2I
- ✅ Identificar builder images
- ✅ Criar builds S2I
- ✅ Utilizar `sourceStrategy`
- ✅ Deployar aplicações construídas com S2I
- ✅ Entender `assemble` como etapa de build
- ✅ Entender `run` como etapa de runtime
- ✅ Customizar `.s2i/bin/assemble`
- ✅ Customizar `.s2i/bin/run`
- ✅ Comparar S2I e Containerfile/Docker strategy
- ✅ Troubleshooting de S2I
- ✅ Diagnosticar dependência inválida durante `assemble`
- ✅ Diagnosticar custom `assemble` com erro de permissão
- ✅ Diagnosticar custom `run` com Build `Complete` e Pod falhando
- 🟡 `save-artifacts` / incremental build
- 🟡 Automatizar rollout após build com ImageChange trigger no Deployment

## 6. ConfigMaps e Secrets

- ⬜ Criar ConfigMap
- ⬜ Criar ConfigMap a partir de arquivo
- ⬜ Criar ConfigMap a partir de valores literais
- ⬜ Injetar ConfigMap como variável de ambiente
- ⬜ Utilizar `envFrom`
- ⬜ Montar ConfigMap como volume
- ⬜ Criar Secret
- ⬜ Injetar Secret como variável de ambiente
- ⬜ Montar Secret como volume
- ⬜ Atualizar configuração de aplicações

## 7. Health Monitoring

- ✅ Entender readiness probe
- ✅ Entender liveness probe
- ✅ Entender startup probe
- ✅ Criar HTTP probes
- ✅ Criar exec probes
- ✅ Criar TCP probes
- 🟡 Configurar delays, períodos e thresholds sem consulta
- ✅ Diagnosticar falhas de probes

## 8. Deployments e aplicações

- ✅ Criar aplicação single-container
- ⬜ Criar aplicação multi-container
- ✅ Criar Deployment
- ✅ Atualizar aplicações
- ✅ Acompanhar rollouts
- 🟡 Configurar ImageChange trigger no Deployment com naturalidade
- ✅ Consultar histórico de rollout
- ✅ Inspecionar revisão específica
- ✅ Executar rollback
- ✅ Configurar estratégia `RollingUpdate`
- ✅ Configurar estratégia `Recreate`
- ✅ Entender `maxSurge`
- ✅ Entender `maxUnavailable`
- ✅ Entender `revisionHistoryLimit`
- ✅ Entender `progressDeadlineSeconds`
- ✅ Criar Service
- ✅ Criar Route
- ✅ Validar aplicação ponta a ponta

## 9. Troubleshooting

- ✅ `oc get`
- ✅ `oc describe`
- ✅ `oc logs`
- ✅ `oc logs --previous`
- ✅ `oc exec`
- ✅ Consultar Events
- ⬜ Diagnosticar `Pending`
- ✅ Diagnosticar `CrashLoopBackOff` / container reiniciando
- ✅ Diagnosticar `ImagePullBackOff`
- ✅ Diagnosticar falhas de Deployment / rollout
- ⬜ Diagnosticar Services
- ⬜ Diagnosticar Routes
- ✅ Diagnosticar Builds
- 🟡 Diagnosticar ImageStreams
- 🟡 Diagnosticar problemas de configuração

## 10. OpenShift Templates

- ⬜ Entender Templates
- ⬜ Criar Template
- ⬜ Trabalhar com `parameters`
- ⬜ Trabalhar com `objects`
- ⬜ Processar Template
- ⬜ Fornecer parâmetros
- ⬜ Utilizar Templates existentes
- ⬜ Troubleshooting de Templates

## 11. Helm

- ⬜ Entender estrutura de um Chart
- ⬜ `Chart.yaml`
- ⬜ `values.yaml`
- ⬜ Diretório `templates/`
- ⬜ Criar Chart
- ⬜ `helm install`
- ⬜ `helm upgrade`
- ⬜ Sobrescrever values
- ⬜ Troubleshooting de Helm

## 12. Kustomize

- ⬜ Criar `kustomization.yaml`
- ⬜ Trabalhar com resources
- ⬜ Trabalhar com bases e overlays
- ⬜ Aplicar patches
- ⬜ Alterar imagens
- ⬜ Alterar réplicas
- ⬜ Aplicar com `oc apply -k`
- ⬜ Troubleshooting de Kustomize

## 13. OpenShift Pipelines / Tekton

- ⬜ Entender Task
- ⬜ Criar Task
- ⬜ Executar TaskRun
- ⬜ Criar Pipeline
- ⬜ Executar PipelineRun
- ⬜ Utilizar parameters
- ⬜ Utilizar workspaces
- ⬜ Conectar Tasks
- ⬜ Acompanhar execução
- ⬜ Consultar logs
- ⬜ Troubleshooting de pipelines

## 14. Operators

- ⬜ Identificar Operators disponíveis
- ⬜ Identificar CRDs
- ⬜ Consultar Custom Resources
- ⬜ Criar recursos usando Operators existentes
- ⬜ Consultar status e conditions
- ⬜ Troubleshooting básico de recursos gerenciados por Operators

## 15. Simulados

- ⬜ Simulado de builds
- ⬜ Simulado de ImageStreams
- ⬜ Simulado de S2I
- ⬜ Simulado de deployments
- ⬜ Simulado de ConfigMaps e Secrets
- ⬜ Simulado de probes
- ⬜ Simulado de Templates
- ⬜ Simulado de Helm
- ⬜ Simulado de Kustomize
- ⬜ Simulado de Tekton
- ⬜ Simulado de troubleshooting
- ⬜ Simulado completo
- ⬜ Simulado completo sem ajuda

---

# Ambiente de laboratório

Cluster OpenShift disponível para prática.

Projeto utilizado nos estudos:

```text
monticelli-ex288
```

Repositório de estudos:

```text
ex288-labs
```

---

# Metodologia

Cada tópico será estudado por meio de tarefas práticas semelhantes às atividades esperadas em um ambiente OpenShift.

```text
conceito
   ↓
atividade prática
   ↓
validação
   ↓
troubleshooting
   ↓
repetição sem ajuda
```

Um item só recebe ✅ quando consigo executar a tarefa prática sem depender de uma solução pronta.

Se o assunto já foi praticado mas ainda precisa de reforço, recebe 🟡.

Ao concluir cada etapa:

```text
atualizar checklist
      ↓
atualizar README técnico do tópico
      ↓
atualizar mindmap
```

---

# Etapa atual

## Fase 6 — Health Monitoring / Probes

Status:

```text
✅ readinessProbe
✅ livenessProbe
✅ startupProbe
✅ HTTP probes
✅ exec probes
✅ TCP probes
✅ troubleshooting de probes
✅ Running x Ready
✅ restart de container por liveness
✅ startup bloqueando liveness/readiness até sucesso
✅ readiness protegendo RollingUpdate
✅ progressDeadlineSeconds observado em rollout sem progresso
✅ oc events --for
🟡 timings / thresholds: reforçar criação sem consulta
```

### Readiness validada

Foi configurada uma readiness HTTP saudável em `/health` e depois quebrada propositalmente apontando para um caminho inexistente.

Com a probe quebrada:

```text
Pod
STATUS=Running
READY=0/1
RESTARTS=0
```

A aplicação continuou executando, mas o Pod deixou de ficar Ready. Em RollingUpdate, o Pod antigo saudável permaneceu atendendo enquanto o novo Pod não passou na readiness.

Diagnóstico observado:

```text
Readiness probe failed: HTTP probe failed with statuscode: 404
```

### Liveness validada

A liveness HTTP foi configurada inicialmente em `/health` e depois quebrada propositalmente.

Foi observado o mesmo Pod reiniciando seu container:

```text
READY alternando entre 0/1 e 1/1
RESTARTS aumentando
nome do Pod permanecendo o mesmo
```

Events utilizados no diagnóstico:

```text
Liveness probe failed: HTTP probe failed with statuscode: 404
Back-off restarting failed container
```

Regra prática validada:

```text
readiness falha
→ não reinicia o container
→ Pod deixa de ficar Ready
→ sai do tráfego elegível do Service

liveness falha
→ kubelet reinicia o container
→ RESTARTS aumenta
→ o mesmo Pod continua existindo
```

### Startup validada

Foi configurada uma startup probe propositalmente quebrada:

```text
periodSeconds: 5
failureThreshold: 3
```

Modelo mental validado:

```text
startupProbe
→ testa a inicialização repetidamente
→ liveness/readiness ficam bloqueadas até sucesso
→ ao atingir failureThreshold, o container é reiniciado
→ falhas repetidas podem resultar em CrashLoopBackOff
```

Os Events mostraram somente falhas de startup enquanto ela não passava:

```text
Startup probe failed: HTTP probe failed with statuscode: 404
Container ... failed startup probe, will be restarted
```

Após corrigir a startup para `/health`, o novo Pod ficou:

```text
READY 1/1
STATUS Running
RESTARTS 0
```

### Exec probe validada

A `readinessProbe` foi alterada de HTTP para execução de comando dentro do container:

```bash
oc set probe deploy/probes-lab --readiness -- test -f /opt/app-root/src/app.py
```

Inspeção rápida da probe:

```bash
oc get deploy probes-lab \
  -o jsonpath='{.spec.template.spec.containers[0].readinessProbe}' | jq
```

Regra prática validada:

```text
exit code 0
→ probe passou

exit code diferente de 0
→ probe falhou
```

Com a readiness exec quebrada, o Pod permaneceu `Running`, ficou `READY 0/1` e o container não reiniciou.

### TCP probe validada

A readiness também foi testada com socket TCP.

Com a aplicação ouvindo em `8080`, a probe passou. Ao apontar para `9999`, o novo Pod permaneceu `Running 0/1` e o Pod antigo saudável foi preservado pelo RollingUpdate.

Evento observado:

```text
Readiness probe failed: dial tcp <pod-ip>:9999: connect: connection refused
```

O rollout sem progresso acabou atingindo o `progressDeadlineSeconds`, conectando na prática probes, readiness e estratégia de rollout.

### Timings e thresholds

Modelo mental consolidado:

```text
initialDelaySeconds
→ quanto esperar antes da primeira tentativa

periodSeconds
→ periodicidade entre tentativas

timeoutSeconds
→ prazo máximo de uma tentativa individual

failureThreshold
→ quantidade de falhas consecutivas para considerar a probe falha

successThreshold
→ quantidade de sucessos consecutivos para considerar a probe saudável
```

Exemplo estudado:

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 3
  periodSeconds: 4
  timeoutSeconds: 2
  failureThreshold: 3
```

Linha do tempo:

```text
t=3  primeira tentativa
t=7  segunda tentativa
t=11 terceira tentativa
```

Um sucesso no meio das falhas reinicia a contagem de `failureThreshold`.

O conceito de `failureThreshold` é o mesmo entre probes; muda o efeito da falha:

```text
readiness falha
→ Pod fica NotReady / sai do tráfego elegível

liveness falha
→ container é reiniciado

startup falha
→ container é reiniciado antes de liberar liveness/readiness
```

Os timings foram entendidos e praticados, mas ficam 🟡 para reforçar cálculo rápido sem consulta. Em prova, `oc explain` é o fallback para confirmar semântica e restrições dos campos.

### Troubleshooting com Events

Comando incorporado ao fluxo de diagnóstico:

```bash
oc events --for pod/<pod>
```

Também continuam úteis:

```bash
oc get pods
oc describe pod <pod>
oc logs <pod>
oc logs --previous <pod>
```

---

# Próxima atividade

## Fase 7 — ConfigMaps e Secrets

O bloco principal de Health Monitoring / Probes foi concluído.

Pendência de revisão:

```text
🟡 timings / thresholds
→ reforçar cálculo rápido sem consulta
```

Próximo domínio:

```text
ConfigMap
→ literal / arquivo
→ env / envFrom
→ volume

Secret
→ literal / arquivo
→ env / envFrom
→ volume

alteração de configuração
→ rollout / validação / troubleshooting
```

Documentação detalhada do bloco concluído:

- [07 — Health Monitoring / Probes](topics/07-health-monitoring/)
