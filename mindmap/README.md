# EX288 — Mindmap navegável

[← Voltar para o README principal](../README.md)

Este mapa cresce junto com os estudos. O objetivo é mostrar **como os objetos do OpenShift se conectam** e fornecer atalhos para os capítulos técnicos do repositório.

## Navegação rápida

| Área | Status | Material |
|---|---|---|
| Fundamentos OpenShift e Git | ✅ | [Abrir](../topics/01-openshift-git/) |
| Container Images | ✅ / 🟡 multi-stage | [Abrir](../topics/02-container-images/) |
| BuildConfig e Builds | ✅ / 🟡 custom builder | [Abrir](../topics/03-buildconfig-builds/) |
| ImageStreams | ✅ / 🟡 troubleshooting | [Abrir](../topics/04-imagestreams/) |
| S2I | ⬜ próximo | README técnico será criado ao iniciar |
| Deployments e aplicações | ✅ / 🟡 rollout history | [Abrir](../topics/08-deployments-applications/) |
| Troubleshooting | 🟡 | [Abrir](../topics/09-troubleshooting/) |

## Visão geral do fluxo já praticado

```mermaid
flowchart LR
    GIT[Git / Source] --> BC[BuildConfig]
    BASE[ImageStreamTag<br/>imagem-base] -->|ImageChange| BC
    BC --> BUILD[Build]
    BUILD --> APPIS[ImageStreamTag<br/>da aplicação]
    APPIS -->|ImageChange| DEPLOY[Deployment]
    DEPLOY --> RS[ReplicaSet]
    RS --> POD[Pod]
    POD --> SVC[Service]
    SVC --> ROUTE[Route]

    REG[(Registry interno)]
    BUILD --> REG
    REG --> APPIS
```

### Fluxo automático que já foi validado

```text
imagem-base muda de digest
        ↓
ImageChange do BuildConfig
        ↓
Build automático
        ↓
imagem da aplicação muda
        ↓
ImageChange do Deployment
        ↓
rollout automático
```

---

## Mapa dos domínios

```mermaid
mindmap
  root((EX288))
    Fundamentos ✅
      Projects / Namespaces
      oc CLI
      Git
      Pods
      Services
      Routes
    Container Images ✅
      Dockerfile
      Layers / cache
      UID arbitrário
      Grupo 0
      Healthcheck de imagem
      Multi-stage 🟡
    BuildConfig ✅
      Git source
      contextDir
      Docker strategy
      Output ImageStreamTag
      Triggers
        ConfigChange
        ImageChange
        Webhook
      Build operations
        start-build
        cancel-build
        restart
        from-build
      History limits
      Run Policy
        Serial
        Parallel
        SerialLatestOnly
      postCommit
      Custom Builder 🟡
    ImageStreams ✅
      ImageStream
      ImageStreamTag
      Tag mutável
      Digest imutável
      Registry interno
      ImageChange
    Deployments ✅
      Deployment
      ReplicaSet
      Pod
      Service
      Route
      ImageChange rollout
    Troubleshooting 🟡
      get
      describe
      logs
      Events
      Build failures
      ImageStream / digest
    S2I ⬜
      Builder image
      Source
      Assemble
      Run
      Custom scripts
```

---

## BuildConfig — mapa operacional

```mermaid
flowchart TD
    BC[BuildConfig]

    BC --> SRC[Source]
    SRC --> GIT[Git repository]
    SRC --> CTX[contextDir]

    BC --> STRAT[Strategy]
    STRAT --> DOCKER[Docker / Containerfile]
    STRAT --> CUSTOM[Custom Strategy 🟡]
    STRAT -. próximo .-> S2I[S2I]

    BC --> TRIG[Triggers]
    TRIG --> CONFIG[ConfigChange]
    TRIG --> IMAGE[ImageChange]
    TRIG --> WEBHOOK[GitHub / Generic webhook]

    BC --> OPS[Operações]
    OPS --> START[oc start-build]
    OPS --> CANCEL[oc cancel-build]
    OPS --> RESTART[oc cancel-build --restart]
    OPS --> FROMBUILD[oc start-build --from-build]

    BC --> POLICY[Run Policy]
    POLICY --> SERIAL[Serial]
    POLICY --> PARALLEL[Parallel]
    POLICY --> LATEST[SerialLatestOnly]

    BC --> HISTORY[History limits]
    HISTORY --> SUCCESS[successfulBuildsHistoryLimit]
    HISTORY --> FAILED[failedBuildsHistoryLimit]

    BC --> HOOK[postCommit]
```

### Comandos-chave

```bash
oc new-build --name <nome> -l app=<nome> --strategy=docker <git-url> --context-dir=<dir>
oc get bc
oc describe bc <nome>
oc set triggers bc/<nome>
oc start-build <nome> --follow
oc cancel-build <build>
oc cancel-build <build> --restart
oc start-build --from-build=<build>
oc set build-hook bc/<nome> --post-commit --script='<comando>'
oc edit bc/<nome>
```

---

## ImageStreams — modelo mental

```mermaid
flowchart LR
    EXT[Imagem externa] --> IS[ImageStream]
    IS --> TAG[ImageStreamTag<br/>ex: tasks:latest]
    TAG --> DIGEST[Digest<br/>sha256:...]
    DIGEST --> REG[(Registry)]

    BUILD[Build] -->|publica| TAG
    TAG -->|ImageChange| DEPLOY[Deployment]
```

```text
Tag
→ ponteiro mutável

Digest
→ referência imutável de uma imagem específica
```

Pegadinha já validada:

```text
oc tag A B

A e B apontam para o mesmo digest
→ não há mudança real de imagem
→ não é um bom teste de ImageChange
```

---

## Deployment — fluxo de runtime

```mermaid
flowchart LR
    IST[ImageStreamTag] -->|ImageChange| DEP[Deployment]
    DEP --> RS1[ReplicaSet atual]
    DEP -. histórico .-> RS0[ReplicaSet antigo<br/>replicas=0]
    RS1 --> POD[Pod]
    POD --> SVC[Service]
    SVC --> ROUTE[Route]
    ROUTE --> CLIENT[Cliente]
```

Comandos-chave:

```bash
oc create deployment <nome> --image=<imagem>
oc expose deployment <nome> --port=8080 --target-port=8080
oc create route edge --service=<nome> --insecure-policy=Redirect
oc set triggers deployment/<nome> --from-image=<imagestream>:latest -c <container>
oc rollout history deployment/<nome>
```

Observação já validada: ao omitir o nome em `oc create route edge --service=<service>`, a Route pode usar o nome do Service.

---

## Troubleshooting — fluxo de decisão

```mermaid
flowchart TD
    START[Aplicação não funciona] --> GET[oc get]
    GET --> DESCRIBE[oc describe]
    DESCRIBE --> EVENTS[Events / Conditions]
    EVENTS --> LOGS[oc logs]

    LOGS --> BUILDQ{Problema no build?}
    BUILDQ -->|sim| BC[BuildConfig / Build / ImageStream]
    BUILDQ -->|não| PODQ{Pod saudável?}

    PODQ -->|não| POD[Pod / probes / imagem / config]
    PODQ -->|sim| SVCQ{Service seleciona o Pod?}

    SVCQ -->|não| LABELS[labels / selectors / endpoints]
    SVCQ -->|sim| ROUTEQ{Route chega no Service?}

    ROUTEQ -->|não| ROUTE[Route / TLS / target]
    ROUTEQ -->|sim| OK[Fluxo ponta a ponta OK]
```

Casos reais já encontrados nos labs:

- `BuildConfigInstantiateFailed` enquanto uma imagem-base ainda não estava resolvida.
- webhook chegando como `system:anonymous` e falhando por RBAC.
- `tasks:latest`/`vote:latest` atualizado enquanto o Pod continuava com digest antigo.
- `imagePullPolicy: Always` não provoca rollout sozinho.
- `contextDir` define contexto de build, não filtra eventos do webhook por caminho.
- `postCommit` com exit code diferente de zero faz o Build falhar.

---

## Próximo ramo: S2I

```mermaid
flowchart LR
    GIT[Git source] --> S2I[S2I Build]
    BUILDER[Builder Image] --> S2I
    S2I --> OUT[ImageStreamTag]
    OUT --> DEPLOY[Deployment]

    S2I -. estudar .-> ASSEMBLE[assemble]
    S2I -. estudar .-> RUN[run]
    S2I -. estudar .-> SCRIPTS[custom scripts]
```

Quando S2I começar, será criado o capítulo correspondente em `topics/` e este mapa será expandido.

---

## Regra de manutenção

Ao terminar um bloco de estudo:

```text
README raiz
→ atualizar progresso

mindmap/README.md
→ atualizar relações e fluxos

topics/XX-*/README.md
→ registrar comandos, exemplos e troubleshooting
```
