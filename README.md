# EX288 Labs

Repositório pessoal de estudos para a certificação Red Hat EX288, com foco em prática hands-on no OpenShift.

O estudo será realizado progressivamente, construindo os recursos e aplicações conforme os tópicos forem sendo praticados.

## Status

Legenda:

- ⬜ não estudado
- 🟡 revisar
- ✅ consigo fazer sozinho

---

<!-- TOPICS_INDEX_START -->

# Material estudado

- [🧭 Mindmap navegável](mindmap/)
- [01 — Fundamentos OpenShift e Git](topics/01-openshift-git/)
- [02 — Container Images](topics/02-container-images/)
- [03 — BuildConfig e Builds](topics/03-buildconfig-builds/)
- [04 — ImageStreams](topics/04-imagestreams/)
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
- 🟡 Troubleshooting de builds

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

- ⬜ Entender o fluxo S2I
- ⬜ Identificar builder images
- ⬜ Criar builds S2I
- ⬜ Deployar aplicações construídas com S2I
- ⬜ Customizar scripts S2I
- ⬜ Comparar S2I e Containerfile builds
- ⬜ Troubleshooting de S2I

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

- ⬜ Entender readiness probe
- ⬜ Entender liveness probe
- ⬜ Entender startup probe
- ⬜ Criar HTTP probes
- ⬜ Criar exec probes
- ⬜ Configurar delays e períodos
- ⬜ Diagnosticar falhas de probes

## 8. Deployments e aplicações

- ✅ Criar aplicação single-container
- ⬜ Criar aplicação multi-container
- ✅ Criar Deployment
- ✅ Atualizar aplicações
- ✅ Acompanhar rollouts
- 🟡 Consultar histórico de rollout
- ⬜ Executar rollback
- ✅ Criar Service
- ✅ Criar Route
- ✅ Validar aplicação ponta a ponta

## 9. Troubleshooting

- ✅ `oc get`
- ✅ `oc describe`
- 🟡 `oc logs`
- ⬜ `oc logs -p`
- ⬜ `oc exec`
- 🟡 Consultar Events
- ⬜ Diagnosticar `Pending`
- ⬜ Diagnosticar `CrashLoopBackOff`
- ⬜ Diagnosticar `ImagePullBackOff`
- ⬜ Diagnosticar falhas de Deployment
- ⬜ Diagnosticar Services
- ⬜ Diagnosticar Routes
- 🟡 Diagnosticar Builds
- 🟡 Diagnosticar ImageStreams
- ⬜ Diagnosticar problemas de configuração

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

Estrutura atual:

```text
ex288-labs/
├── README.md
├── .gitignore
├── hello/
│   ├── Dockerfile
│   ├── package.json
│   └── server.js
├── mindmap/
│   └── README.md
├── tasks/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── topics/
│   ├── 01-openshift-git/
│   │   └── README.md
│   ├── 02-container-images/
│   │   └── README.md
│   ├── 03-buildconfig-builds/
│   │   └── README.md
│   ├── 04-imagestreams/
│   │   └── README.md
│   ├── 08-deployments-applications/
│   │   └── README.md
│   └── 09-troubleshooting/
│       └── README.md
└── vote/
    ├── app.py
    ├── Dockerfile
    └── requirements.txt
```

As aplicações, manifests e demais artefatos serão adicionados conforme os tópicos forem estudados.

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

## Fase 3 — BuildConfig e Builds

Status:

```text
✅ Conteúdo principal concluído
🟡 Custom Builder: revisar execução com uma builder image real
```

### Fluxo de build validado

```text
Git
 ↓
BuildConfig
 ↓
Build
 ↓
ImageStreamTag
 ↓
Registry interno
```

### ImageChange encadeado validado

```text
ImageStreamTag da imagem-base muda
 ↓
ImageChange trigger do BuildConfig
 ↓
novo Build automático
 ↓
ImageStreamTag da aplicação muda
 ↓
ImageChange trigger do Deployment
 ↓
novo ReplicaSet / Pod
```

O fluxo foi validado utilizando `python-base-lab:latest`, alternando entre imagens Python 3.11 e 3.12. A alteração de digest disparou automaticamente `tasks-12` e `tasks-13`, sem `oc start-build` manual.

### Operações de Build praticadas

```text
oc start-build
oc start-build --follow
oc cancel-build
oc cancel-build --restart
oc start-build --from-build
```

Também foram praticados:

- `successfulBuildsHistoryLimit`
- `oc edit bc/...` e `oc patch bc/...`
- `Serial`, `Parallel` e `SerialLatestOnly`
- `postCommit` com sucesso e falha intencional
- configuração de `customStrategy`
- webhook e troubleshooting de RBAC

### Post-commit validado

```text
imagem construída
 ↓
postCommit exit 0
 ↓
Build Complete
 ↓
imagem publicada
```

E o cenário de falha:

```text
imagem construída
 ↓
postCommit exit != 0
 ↓
Build Failed
 ↓
imagem não publicada
```

### Recapitulação prática — aplicação `tasks`

```text
Git
 ↓
BuildConfig/tasks
 ↓
Build/tasks-N
 ↓
ImageStreamTag tasks:latest
 ↓
Deployment/tasks
 ↓
ReplicaSet
 ↓
Pod
 ↓
Service/tasks
 ↓
Route/tasks
```

A Route utiliza TLS termination `edge` e `Redirect` para HTTP. O Deployment acompanha `tasks:latest` através de ImageChange trigger.

---

# Próxima etapa

## Fase 4 — Source-to-Image (S2I)

Próximo bloco de estudo:

```text
builder image
 ↓
source Git
 ↓
S2I build
 ↓
ImageStream
 ↓
Deployment
```

O objetivo será entender o fluxo S2I, identificar builder images, criar builds, customizar scripts quando necessário e comparar S2I com Docker/Containerfile strategy.
