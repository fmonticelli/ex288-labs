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
→ OpenShift Templates (conteúdo praticado; falta ganhar fluência sob tempo)
→ Helm (núcleo praticado; falta repetição a frio)
→ Kustomize (base/overlay/patches praticados; falta troubleshooting + repetição)
→ timings e thresholds de probes
→ ImageChange trigger no Deployment
→ troubleshooting de ImageStreams
→ Custom Builder
→ save-artifacts / incremental S2I

ainda não coberto de forma suficiente
→ Pipelines / Tekton
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

- 🟡 Entender estrutura de um Chart
- 🟡 `Chart.yaml`
- 🟡 `values.yaml`
- 🟡 Diretório `templates/`
- 🟡 Criar Chart
- 🟡 `helm template` e `helm lint`
- 🟡 `helm install`
- 🟡 `helm list` e `helm status`
- 🟡 `helm get values` e `helm get manifest`
- 🟡 `helm upgrade`
- 🟡 `helm history`
- 🟡 `helm rollback`
- 🟡 `helm uninstall`
- 🟡 Sobrescrever values com `-f` e `--set`
- 🟡 Troubleshooting de Helm

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
- 🟡 Simulado de Templates
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

## Fase 12 — Kustomize

### Helm — núcleo praticado

O bloco de Helm foi percorrido de ponta a ponta, mas permanece 🟡 até uma repetição a frio.

Fluxo praticado:

```text
Chart.yaml + values.yaml + templates/
        ↓
helm lint
        ↓
helm template
        ↓
dry-run contra a API
        ↓
helm install
        ↓
Release
        ↓
upgrade / history / rollback
        ↓
uninstall
```

Comandos usados:

```bash
helm create review-app
helm lint ./ex288-app
helm template teste ./ex288-app

helm template teste ./ex288-app \
  -f ex288-app/values-prod.yaml \
  --set replicaCount=4

helm template teste ./ex288-app \
| oc apply --dry-run=server -f -

helm install ex288-release ./ex288-app
helm list
helm status ex288-release
helm get values ex288-prod
helm get manifest ex288-prod
helm upgrade ex288-release ./ex288-app --reuse-values --set replicaCount=3
helm history ex288-release
helm rollback ex288-release 1
helm uninstall ex288-release
```

Troubleshooting praticado em três camadas:

```text
template Helm inválido
→ helm lint / helm template falham

Helm renderiza, mas manifest é inválido
→ dry-run=server rejeita

manifest válido + Pod Running, mas aplicação não responde
→ investigar com oc get / logs / exec / Service
```

Pegadinha consolidada:

```text
containerPort
→ não faz o processo escutar naquela porta

porta real
→ definida pelo processo da aplicação
```

### Kustomize — em andamento

Modelo mental atual:

```text
base/
→ YAML Kubernetes normal

overlay/
→ reutiliza a base
→ aplica diferenças

kustomization.yaml
→ resources
→ replicas
→ images
→ labels
→ patches
```

Estrutura praticada:

```text
labs/12-kustomize/
├── base/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── kustomization.yaml
└── overlays/
    └── prod/
        ├── kustomization.yaml
        └── deployment-patch.yaml
```

Fluxos usados:

```bash
oc kustomize .
oc kustomize overlays/prod
oc apply -k overlays/prod --dry-run=server
oc apply -k overlays/prod --dry-run=server -o yaml
```

Transformações já praticadas:

```text
resources ✅
base + overlay ✅
replicas ✅
images ✅
labels ✅
patches ✅
oc apply -k ✅
troubleshooting ⬜
repetição sem ajuda ⬜
```

Regra importante:

```text
kustomization.yaml
→ configuração local do Kustomize
→ não é recurso da API do cluster
→ oc explain não descreve sua sintaxe

conteúdo do patch
→ estrutura Kubernetes normal
→ oc explain ajuda a reconstruir campos
```

---

# Próxima atividade

## Fechar Kustomize e iniciar Tekton

```text
Kustomize troubleshooting
→ repetição curta sem ajuda
→ Tekton / OpenShift Pipelines
```

Kustomize continuará 🟡 até o troubleshooting e uma repetição a frio. Helm também permanece 🟡 até um exercício posterior sem ajuda.
