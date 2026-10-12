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
- [S2I — aplicação prática](s2i-python/)
- [S2I — troubleshooting prático](s2i-troubleshooting/)
- [08 — Deployments e aplicações](topics/08-deployments-applications/)
- [09 — Troubleshooting](topics/09-troubleshooting/)

O `mindmap/` mostra como os objetos e fluxos se conectam. Os diretórios em `topics/` guardam conceitos, comandos, exercícios, validações e troubleshooting realizados durante os laboratórios. Os diretórios `s2i-python/` e `s2i-troubleshooting/` guardam os exercícios práticos realizados no bloco de Source-to-Image.

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
- 🟡 Configurar ImageChange trigger no Deployment com naturalidade
- 🟡 Consultar histórico de rollout
- ⬜ Executar rollback
- ⬜ Configurar estratégia `RollingUpdate`
- ⬜ Configurar estratégia `Recreate`
- ✅ Criar Service
- ✅ Criar Route
- ✅ Validar aplicação ponta a ponta

## 9. Troubleshooting

- ✅ `oc get`
- ✅ `oc describe`
- ✅ `oc logs`
- ✅ `oc logs --previous`
- ⬜ `oc exec`
- 🟡 Consultar Events
- ⬜ Diagnosticar `Pending`
- ✅ Diagnosticar `CrashLoopBackOff` / container reiniciando
- ⬜ Diagnosticar `ImagePullBackOff`
- 🟡 Diagnosticar falhas de Deployment
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
├── s2i-python/
│   ├── app.py
│   └── requirements.txt
├── s2i-troubleshooting/
│   ├── 01-broken-requirements/
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   ├── README.md
│   │   └── versions/
│   ├── 02-broken-assemble/
│   │   ├── .s2i/bin/assemble
│   │   ├── app.py
│   │   ├── requirements.txt
│   │   ├── README.md
│   │   └── versions/
│   └── 03-broken-run/
│       ├── .s2i/bin/run
│       ├── app.py
│       ├── requirements.txt
│       ├── README.md
│       └── versions/
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

## Fase 4 — Source-to-Image (S2I)

Status:

```text
✅ Núcleo S2I concluído
✅ Build S2I com sourceStrategy
✅ Custom assemble e custom run
✅ Troubleshooting S2I prático
🟡 save-artifacts / incremental build
🟡 ImageChange trigger no Deployment: reforçar hábito operacional
```

### Fluxo S2I validado

```text
Git source
    +
Builder Image
    ↓
BuildConfig
sourceStrategy
    ↓
Build
    ↓
assemble
    ↓
ImageStreamTag
    ↓
Deployment
    ↓
run
    ↓
Pod
```

### Diferença fundamental

```text
assemble
→ build time
→ falha normalmente deixa Build Failed

run
→ runtime
→ Build pode ficar Complete e o Pod falhar depois
```

### Troubleshooting S2I praticado

#### Cenário 01 — requirements inválido

```text
Flask==99.99.99
    ↓
/usr/libexec/s2i/assemble
    ↓
pip falha
    ↓
Build Failed
```

Diagnóstico:

```bash
oc get build -l app=s2i-broken-deps
oc logs build/s2i-broken-deps-1
```

Correção validada com novo Build `Complete`.

#### Cenário 02 — custom assemble com erro de permissão

```text
.s2i/bin/assemble
    ↓
RUN /tmp/scripts/assemble
    ↓
USER 1001 tenta gravar em /root
    ↓
Permission denied
    ↓
Build Failed
```

Foi identificado que o script customizado do source substituiu o comportamento padrão do `assemble`.

#### Cenário 03 — custom run quebrado

```text
Build Complete
    ↓
Deployment
    ↓
container inicia
    ↓
.s2i/bin/run
    ↓
missing.py não existe
    ↓
container reinicia
```

Diagnóstico realizado com:

```bash
oc logs --previous pod/<pod>
```

Após corrigir `missing.py` para `app.py`, gerar novo build e executar novo rollout, a aplicação permaneceu em execução.

### Trigger de Deployment — ponto de reforço

Foi reforçada a diferença entre:

```bash
oc rollout restart deployment/<nome>
```

e:

```bash
oc set triggers deployment/<nome> \
  --from-image=<imagestream>:latest \
  -c <container>
```

```text
rollout restart
→ cria novos Pods agora

ImageChange trigger
→ configura rollout automático quando a ImageStreamTag mudar
```

Para recuperar sintaxe durante a prática:

```bash
oc set --help
oc set triggers --help
```

---

# Próxima etapa

## Fase 5 — Deployments avançados

Próximo bloco de estudo:

```text
RollingUpdate / Recreate
        ↓
rollout history
        ↓
rollback
        ↓
probes
        ↓
requests / limits
        ↓
stateful / persistência
```

O próximo objetivo é aprender a controlar e diagnosticar o ciclo de vida de uma aplicação depois que a imagem já está pronta, incluindo estratégias de rollout, rollback e falhas de saúde da aplicação.
