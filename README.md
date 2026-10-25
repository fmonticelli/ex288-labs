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
  <img src="assets/dashboard-84.svg" alt="EX288 Dashboard de Estudos — 84%" width="920">
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
→ Helm (cold sim completo; construção + lifecycle + troubleshooting)

em andamento / precisa reforço
→ OpenShift Templates (cold sim completo; técnica forte, falta ganhar velocidade/atenção ao enunciado)
→ Kustomize (base/overlay/patches praticados; troubleshooting adiado por prioridade)
→ timings e thresholds de probes
→ ImageChange trigger no Deployment
→ troubleshooting de ImageStreams
→ Custom Builder
→ save-artifacts / incremental S2I

ainda não coberto de forma suficiente
→ Pipelines / Tekton (Task/TaskRun, params e workspaces praticados; Pipeline é o próximo passo)
→ Operators
→ console web
```

A métrica acompanha **cobertura de conteúdo**, não domínio sob pressão de prova. A prontidão real será validada por exercícios sem ajuda e simulados integrados.

---

<!-- TOPICS_INDEX_START -->

# Material estudado

- [🧭 Mindmap navegável](mindmap/)
- [🧪 Índice de laboratórios](labs/)
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
- [10 — OpenShift Templates — labs](labs/10-templates/)
- [11 — Helm — labs](labs/11-helm/)
- [12 — Kustomize — labs](labs/12-kustomize/)
- [13 — OpenShift Pipelines / Tekton](topics/13-tekton/) — [labs](labs/13-tekton/)

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

- 🟡 Entender Templates
- 🟡 Criar Template
- 🟡 Trabalhar com `parameters`
- 🟡 Trabalhar com `objects`
- 🟡 Processar Template
- 🟡 Fornecer parâmetros
- 🟡 Utilizar Templates existentes
- 🟡 Troubleshooting de Templates

## 11. Helm

- ✅ Entender estrutura de um Chart
- ✅ `Chart.yaml`
- ✅ `values.yaml`
- ✅ Diretório `templates/`
- ✅ Criar Chart
- ✅ `helm template` e `helm lint`
- ✅ `helm install`
- ✅ `helm list` e `helm status`
- ✅ `helm get values` e `helm get manifest`
- ✅ `helm upgrade`
- ✅ `helm history`
- ✅ `helm rollback`
- ✅ `helm uninstall`
- ✅ Sobrescrever values com `-f` e `--set`
- ✅ Troubleshooting de Helm

## 12. Kustomize

- 🟡 Criar `kustomization.yaml`
- 🟡 Trabalhar com resources
- 🟡 Trabalhar com bases e overlays
- 🟡 Aplicar patches
- 🟡 Alterar imagens
- 🟡 Alterar réplicas
- 🟡 Trabalhar com labels
- 🟡 Renderizar com `oc kustomize`
- 🟡 Aplicar com `oc apply -k`
- ⬜ Troubleshooting de Kustomize

## 13. OpenShift Pipelines / Tekton

- ✅ Entender Task
- ✅ Criar Task
- ✅ Executar TaskRun
- ⬜ Criar Pipeline
- ⬜ Executar PipelineRun
- ✅ Utilizar parameters
- ✅ Utilizar workspaces em Task/TaskRun
- ⬜ Conectar Tasks
- ✅ Acompanhar execução
- ✅ Consultar logs por Step
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
- 🟡 Simulado de Templates
- ✅ Simulado de Helm
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

## Fase 13 — OpenShift Pipelines / Tekton

### Cold sim de OpenShift Templates

Arquivo:

```text
labs/10-templates/template-cold-sim.yaml
```

O exercício foi feito após alguns dias sem prática e cobriu:

```text
Template armazenável no cluster
→ parameters
→ required
→ generate: expression
→ Deployment + Service + Route
→ processamento local
→ processamento pelo nome
→ dry-run contra a API
→ criação dos recursos
→ validação de env
→ HTTP pela Route
```

Resultado:

```text
técnica de Templates          ✅ forte
retenção após pausa           ✅
fluxo oc apply / oc process   ✅
troubleshooting               ✅
velocidade / leitura rigorosa 🟡
```

O bloco continua 🟡 porque o cold sim exigiu uma intervenção para revisar duas evidências do enunciado, apesar da implementação técnica ter sido concluída corretamente.

### Cold sim de Helm — concluído

Estrutura criada do zero:

```text
labs/11-helm/helm-cold-sim/
├── Chart.yaml
├── values.yaml
├── values-prod.yaml
└── templates/
    ├── deployment.yaml
    └── service.yaml
```

Fluxo executado:

```text
Chart do zero
→ helm lint
→ values.yaml
→ values-prod.yaml
→ --set
→ dry-run
→ install
→ list / status
→ get values / get manifest
→ upgrade
→ history
→ rollback
```

O exercício incluiu erro real durante a criação, diagnóstico, correção, nova validação e aplicação bem-sucedida.

Revisões comprovadas:

```text
revision 1 → Install complete
revision 2 → Upgrade complete
revision 3 → Rollback to 1
```

Também foi comprovado:

```text
Service :9090 respondendo
ENVIRONMENT=prod no Pod
upgrade 2 → 4 réplicas
rollback 4 → 2 réplicas
```

**Helm agora está marcado como ✅ consigo fazer sozinho.**

### Kustomize — mantido como 🟡

Já praticado:

```text
resources
base + overlays
replicas
images
labels
patches
oc kustomize
oc apply -k
```

O troubleshooting e o cold sim foram adiados deliberadamente para priorizar tópicos ainda não cobertos.

### Tekton — núcleo de Task/TaskRun praticado

O cluster expõe os recursos principais em `tekton.dev/v1`:

```text
Task
TaskRun
Pipeline
PipelineRun
```

O bloco inicial foi praticado do zero usando `oc`, sem depender do `tkn`.

Estrutura atual dos labs:

```text
labs/13-tekton/
├── 01-task-single/
├── 02-task-multi/
├── 03-task-params/
└── 04-task-workspace/
    ├── 01-emptydir-basic/
    └── 02-workspace-path/
```

Fluxo comprovado:

```text
Task
→ definição dos Steps

TaskRun
→ execução concreta

TaskRun
→ cria Pod

Steps
→ containers do Pod
→ executam em sequência
```

Conceitos praticados:

```text
1 Task + 1 Step                 ✅
1 Task + vários Steps           ✅
TaskRun                         ✅
Pod gerado pelo TaskRun         ✅
logs por step                   ✅
params obrigatórios             ✅
params com default              ✅
TaskRun sobrescrevendo params   ✅
workspace em Task/TaskRun       ✅
emptyDir entre Steps            ✅
$(workspaces.<nome>.path)       ✅
```

Substituições importantes:

```text
$(params.NAME)
→ substituição de parâmetro do Tekton

$(workspaces.NAME.path)
→ caminho do workspace resolvido pelo Tekton

$(cat arquivo)
→ command substitution do shell
```

Workspace praticado:

```text
Task.spec.workspaces
→ declara necessidade

TaskRun.spec.workspaces
→ fornece storage concreto

emptyDir
→ suficiente para compartilhar arquivos entre Steps do MESMO TaskRun/Pod
```

Limite importante já identificado:

```text
Task A → TaskRun A → Pod A
Task B → TaskRun B → Pod B

emptyDir de A ≠ emptyDir de B

Para compartilhar arquivos entre Tasks diferentes:
→ usar workspace com storage compartilhado, como PVC
```

Comandos usados:

```bash
oc api-resources | grep -Ei 'task|pipeline'
oc get crd | grep -Ei 'tekton|pipeline'

oc explain task
oc explain task.spec
oc explain task.spec.steps
oc explain task.spec.params
oc explain task.spec.workspaces

oc explain taskrun
oc explain taskrun.spec
oc explain taskrun.spec.taskRef
oc explain taskrun.spec.params
oc explain taskrun.spec.workspaces

oc apply --dry-run=server -f <arquivo>
oc apply -f <arquivo>

oc get task
oc get taskrun
oc describe task <nome>
oc describe taskrun <nome>
oc get pods --sort-by=.metadata.creationTimestamp
oc logs <pod> -c step-<nome>
```

---

# Próxima atividade

## Tekton — Pipeline e PipelineRun

```text
Task A
   ↓
Task B

Pipeline
   ↓
PipelineRun
   ↓
TaskRun A + TaskRun B
   ↓
Pod A + Pod B
```

Depois do Pipeline básico:
```text
params em Pipeline
→ workspace compartilhado entre Tasks
→ PVC
→ troubleshooting
```
