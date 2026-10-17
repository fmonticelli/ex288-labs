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

<p align="center">
  <img src="assets/dashboard.svg?v=72" alt="EX288 Dashboard de Estudos — 72%" width="920">
</p>

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
→ ConfigMaps e Secrets
→ multi-container Pods

em andamento / precisa reforço
→ timings e thresholds de probes
→ ImageChange trigger no Deployment
→ troubleshooting de ImageStreams
→ Custom Builder
→ save-artifacts / incremental S2I

ainda não coberto de forma suficiente
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
- [06 — ConfigMaps e Secrets](topics/06-configmaps-secrets/)
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

- ✅ Criar ConfigMap
- ✅ Criar ConfigMap a partir de arquivo
- ✅ Criar ConfigMap a partir de valores literais
- ✅ Injetar ConfigMap como variável de ambiente
- 🟡 Utilizar `envFrom` diretamente em manifest
- ✅ Montar ConfigMap como volume
- ✅ Criar Secret
- ✅ Injetar Secret como variável de ambiente
- ✅ Montar Secret como volume
- ✅ Atualizar configuração de aplicações

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
- ✅ Criar aplicação multi-container
- ✅ Entender o padrão sidecar
- ✅ Compartilhar volume entre containers com `emptyDir`
- ✅ Utilizar `initContainers`
- ✅ Entender rede compartilhada entre containers do mesmo Pod
- ✅ Utilizar `localhost` entre containers do mesmo Pod
- ✅ Utilizar `oc logs -c` e `oc exec -c`
- ✅ Diagnosticar falha em `initContainer`
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
- ✅ Simulado de ConfigMaps e Secrets
- ✅ Simulado de multi-container Pods
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

## Fase 8 — Pods com múltiplos contêineres

Status:

```text
✅ Pod com dois containers
✅ sidecar
✅ volume compartilhado com emptyDir
✅ leitura de arquivo compartilhado entre containers
✅ oc logs -c
✅ oc exec -c
✅ initContainer
✅ initContainer + volume compartilhado
✅ troubleshooting de initContainer
✅ rede compartilhada no mesmo Pod
✅ comunicação via localhost
✅ mini-simulado de multi-container
```

### Sidecar + volume compartilhado

Lab praticado:

```text
Pod sidecar-lab
├── app
│   └── escreve continuamente em /logs/app.log
│
├── sidecar
│   └── tail -F /logs/app.log
│
└── emptyDir
    └── montado em /logs pelos dois containers
```

Comandos de validação:

```bash
oc get pod sidecar-lab

oc logs sidecar-lab -c app
oc logs sidecar-lab -c sidecar

oc exec sidecar-lab -c app -- tail -5 /logs/app.log
oc exec sidecar-lab -c sidecar -- tail -5 /logs/app.log
```

Modelo mental consolidado:

```text
oc logs
→ stdout / stderr do processo do container

arquivo dentro do container
→ cat / tail via oc exec
→ ou um processo precisa enviar o conteúdo para stdout
```

No lab:

```text
app
→ grava no arquivo

sidecar
→ lê o arquivo
→ escreve em stdout

oc logs -c sidecar
→ mostra o conteúdo produzido pela aplicação
```

Também foi explorado como bônus o crescimento de `emptyDir`, `sizeLimit` e uma versão de sidecar com rotação/compressão de logs. Esse detalhe é complementar e não é tratado como habilidade central da prova.

### initContainer + volume compartilhado

Lab praticado:

```text
Pod init-lab
├── initContainer
│   └── cria /shared/ready.txt
│
├── app
│   └── lê /shared/ready.txt
│
└── emptyDir
    └── montado em /shared
```

Estados observados durante a inicialização:

```text
Pending
→ Init:0/1
→ PodInitializing
→ Running 1/1
```

Regra validada:

```text
initContainer precisa terminar com sucesso
→ somente depois os containers normais iniciam
```

Troubleshooting praticado com um initContainer quebrado:

```text
cat /shared/ready.txt
→ arquivo ainda não existe
→ exit code 1
→ Init:Error
→ Init:CrashLoopBackOff
→ app permanece em PodInitializing
```

Fluxo de diagnóstico:

```bash
oc get pod init-lab
oc describe pod init-lab
oc logs init-lab -c init-setup
oc events --for pod/init-lab
```

A causa mais direta apareceu em:

```text
oc logs init-lab -c init-setup

cat: /shared/ready.txt: No such file or directory
```

### Rede compartilhada no mesmo Pod

Lab praticado:

```text
Pod network-lab
├── app
│   └── servidor HTTP :8080
│
└── sidecar
    └── curl http://localhost:8080
```

Validação:

```bash
oc apply -f network-lab.yaml
oc get pod -l app=network-lab
oc logs network-lab -c sidecar
```

Modelo mental:

```text
mesmo Pod
→ mesmo namespace de rede
→ mesmo IP do Pod
→ localhost compartilhado
→ Service não é necessário para comunicação entre containers do mesmo Pod

Pods diferentes
→ localhost aponta para o próprio Pod
→ normalmente usar Service para descoberta estável
```

### Arquivos de laboratório

Os manifests usados nesta fase foram organizados em:

```text
labs/08-multicontainer/
├── init-lab.yaml
├── init-lab-broken.yaml
├── network-lab.yaml
├── sidecar-lab.yaml
├── sidecar-log-rotation.yaml
├── exam-multicontainer.yaml
└── exam-multicontainer-broken.yaml
```

---

### Mini-simulado concluído

Cenário resolvido sem solução pronta:

```text
Pod exam-multicontainer
├── initContainer prepare
│   └── cria /shared/index.html
├── app
│   └── serve /shared em HTTP :8080
├── sidecar
│   └── curl -s http://localhost:8080/index.html
└── emptyDir shared-data
```

Validações realizadas:

```text
✅ Pod 2/2 Running
✅ initContainer concluiu com sucesso
✅ app respondeu HTTP 200
✅ sidecar recebeu "EX288 multi-container ready"
✅ troubleshooting de versão quebrada
```

Na versão quebrada, o initContainer ficou sem o `volumeMount` de `/shared`. O diagnóstico mostrou:

```text
Init:Error
→ Init:CrashLoopBackOff
→ app e sidecar em PodInitializing
→ oc logs -c prepare
→ /shared/index.html: No such file or directory
```

Fluxo de prova consolidado:

```bash
oc get pod <pod>
oc describe pod <pod>
oc logs <pod> -c <container>
oc exec <pod> -c <container> -- <comando>
oc events --for pod/<pod>
```

---

# Próxima atividade

## OpenShift Templates

Próximo bloco principal:

```text
Template
→ parameters
→ objects
→ oc process
→ criação de recursos
→ troubleshooting
```
