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
→ OpenShift Templates (fundamentos praticados; falta troubleshooting + mini-simulado)
→ timings e thresholds de probes
→ ImageChange trigger no Deployment
→ troubleshooting de ImageStreams
→ Custom Builder
→ save-artifacts / incremental S2I

ainda não coberto de forma suficiente
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

## Fase 10 — OpenShift Templates

Status:

```text
🟡 estrutura básica de Template
🟡 parameters
🟡 objects
🟡 substituição com ${PARAMETER}
🟡 valores default
🟡 sobrescrita com -p
🟡 parâmetros required
🟡 generate: expression / from
🟡 oc process --parameters
🟡 oc process
🟡 oc process | oc apply
🟡 Template gerando Deployment + Service
🟡 validação do Service ponta a ponta
🟡 consulta de Template existente no namespace openshift
🟡 descoberta de apiVersion com oc explain (GROUP + VERSION)
🟡 uso de labels globais do Template
🟡 Template armazenado no cluster e processamento por nome
⬜ troubleshooting de Templates
⬜ mini-simulado sem ajuda
```

### Modelo mental

```text
Template
├── parameters
└── objects
      ↓
  oc process
      ↓
manifests normais
      ↓
   oc apply
      ↓
recursos no cluster
```

O Template não executa nem gerencia a aplicação depois da criação. Ele funciona como uma fábrica parametrizada de manifests.

### Labs criados

```text
labs/10-templates/
├── template-basic.yaml
├── template-parameters.yaml
└── template-review.yaml
```

Fluxos praticados:

```bash
oc process --parameters -f labs/10-templates/template-basic.yaml

oc process -f labs/10-templates/template-basic.yaml

oc process -f labs/10-templates/template-basic.yaml \
  -p APP_NAME=ex288-template \
| oc apply -f -
```

Também foi validado parâmetro obrigatório:

```text
ENVIRONMENT
→ required: true
→ sem valor: oc process falha
→ -p ENVIRONMENT=dev: processamento funciona
```

E parâmetro gerado:

```yaml
- name: RANDOM_ID
  generate: expression
  from: '[a-zA-Z0-9]{8}'
```

Execuções consecutivas do `oc process` geraram valores diferentes, confirmando que a expressão é avaliada a cada processamento.

Para reconstruir a sintaxe, além de `oc explain`, foi consultado um Template real disponível no cluster:

```bash
oc get template -n openshift mariadb-ephemeral -o yaml
```

### Revisão de criação de Template

Foi refeita a criação de um Template do zero para reforçar a estrutura e o `apiVersion`.

Fluxo usado para descobrir a API correta:

```bash
oc explain template | head
oc explain deployment | head
oc explain service | head
```

Regra consolidada:

```text
se GROUP existe
→ apiVersion = GROUP/VERSION

se GROUP não aparece
→ recurso pertence ao core API group
→ apiVersion = VERSION
```

Exemplos praticados:

```text
Template   → template.openshift.io/v1
Deployment → apps/v1
Service    → v1
```

Também foi praticado o uso de `labels:` no próprio Template:

```yaml
labels:
  app: ${APP_NAME}
```

Esse label é aplicado ao `metadata.labels` dos objetos processados, reduzindo repetição. Ele não substitui:

```text
Deployment.spec.selector.matchLabels
Deployment.spec.template.metadata.labels
Service.spec.selector
```

### Template armazenado no cluster

O lab `template-review.yaml` foi atualizado com `metadata.name` e salvo no cluster.

Fluxos praticados:

```bash
oc apply -f labs/10-templates/template-review.yaml

oc get template

oc process template-review-app

oc process template-review-app \
  -p APP_NAME=review-from-cluster

oc process --parameters template-review-app
```

Modelo mental:

```text
arquivo local
→ oc process -f template.yaml

Template armazenado no cluster
→ oc process nome-do-template
```

Para criar os recursos a partir do Template armazenado:

```bash
oc process template-review-app \
  -p APP_NAME=review-from-cluster \
| oc apply -f -
```

A revisão ainda permanece como 🟡 porque a criação de Templates precisa ficar mais natural antes de ser considerada domínio sem consulta.

---

# Próxima atividade

## Continuar OpenShift Templates

```text
Template armazenado no cluster
→ oc process <nome>
→ troubleshooting
→ mini-simulado sem ajuda
```
