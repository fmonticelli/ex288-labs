# EX288 — Mindmap navegável

[← Voltar para o README principal](../README.md)

Este mapa cresce junto com os estudos. O objetivo é mostrar **como os objetos do OpenShift se conectam** e fornecer atalhos para os capítulos técnicos e laboratórios do repositório.

## Navegação rápida

| Área | Status | Material |
|---|---|---|
| Fundamentos OpenShift e Git | ✅ | [Abrir](../topics/01-openshift-git/) |
| Container Images | ✅ / 🟡 multi-stage | [Abrir](../topics/02-container-images/) |
| BuildConfig e Builds | ✅ / 🟡 custom builder | [Abrir](../topics/03-buildconfig-builds/) |
| ImageStreams | ✅ / 🟡 troubleshooting | [Abrir](../topics/04-imagestreams/) |
| S2I | ✅ / 🟡 incremental + trigger habit | [Labs](../s2i-troubleshooting/) |
| Deployments e aplicações | ✅ base / 🟡 avançado | [Abrir](../topics/08-deployments-applications/) |
| Troubleshooting | 🟡 em evolução | [Abrir](../topics/09-troubleshooting/) |

## Visão geral do fluxo já praticado

```mermaid
flowchart LR
    GIT[Git / Source] --> BC[BuildConfig]

    BASE[ImageStreamTag<br/>imagem-base] -->|ImageChange| BC

    BC --> STRAT{Strategy}
    STRAT -->|Docker| DOCKER[Docker / Containerfile build]
    STRAT -->|Source| S2I[S2I build]

    DOCKER --> BUILD[Build]
    S2I --> BUILD

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

### Fluxo automático já validado

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
      Source strategy / S2I
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
    S2I ✅
      Builder image
      sourceStrategy
      Git source
      assemble
        build time
        requirements
        custom assemble
      run
        runtime
        custom run
      save-artifacts 🟡
      Troubleshooting
        dependency failure
        permission failure
        CrashLoopBackOff
    Deployments
      Deployment ✅
      ReplicaSet ✅
      Pod ✅
      Service ✅
      Route ✅
      ImageChange trigger 🟡 hábito
      Rollout history 🟡
      Rollback ⬜
      RollingUpdate ⬜
      Recreate ⬜
      Probes ⬜
    Troubleshooting 🟡
      get ✅
      describe ✅
      logs ✅
      logs --previous ✅
      exec ⬜
      Events 🟡
      Build failures ✅
      CrashLoopBackOff ✅
      ImagePullBackOff ⬜
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
    STRAT --> SOURCE[Source / S2I]
    STRAT --> CUSTOM[Custom Strategy 🟡]

    SOURCE --> BUILDER[Builder Image]
    SOURCE --> ASSEMBLE[assemble]

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

oc new-build \
  --name=<nome> \
  --strategy=source \
  --image-stream=<builder>:latest \
  --context-dir=<dir> \
  <git-url>

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

## S2I — modelo mental

```mermaid
flowchart TD
    GIT[Git source] --> BC[BuildConfig<br/>sourceStrategy]
    BUILDER[Builder Image] --> BC

    BC --> BUILD[Build]

    BUILD --> SCRIPTSEL{Scripts S2I}

    SCRIPTSEL -->|source customizado| CUSTOM[.s2i/bin/*]
    SCRIPTSEL -->|fallback| DEFAULT[/usr/libexec/s2i/*]

    CUSTOM --> ASSEMBLE[assemble]
    DEFAULT --> ASSEMBLE

    ASSEMBLE --> OUT[ImageStreamTag]
    OUT --> DEPLOY[Deployment]

    DEPLOY --> POD[Pod]
    POD --> RUN[run]
```

### Regra central

```text
assemble
→ executa durante o Build
→ exit != 0 normalmente resulta em Build Failed

run
→ executa no container
→ pode existir Build Complete + Pod quebrado
```

### Como identificar qual `assemble` foi usado

```text
RUN /usr/libexec/s2i/assemble
→ script padrão da builder

RUN /tmp/scripts/assemble
→ script customizado vindo do source
```

### Labs de troubleshooting realizados

```mermaid
flowchart LR
    A[01 requirements inválido] --> A1[assemble falha]
    A1 --> A2[Build Failed]

    B[02 custom assemble] --> B1[USER 1001]
    B1 --> B2[gravação em /root]
    B2 --> B3[Permission denied]
    B3 --> B4[Build Failed]

    C[03 custom run] --> C1[Build Complete]
    C1 --> C2[Pod inicia]
    C2 --> C3[missing.py]
    C3 --> C4[container reinicia]
```

Comandos usados no diagnóstico:

```bash
oc get build -l app=<nome>
oc logs build/<build>
oc get pods
oc logs pod/<pod>
oc logs --previous pod/<pod>
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
    IST[ImageStreamTag] -->|ImageChange trigger| DEP[Deployment]
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

oc set triggers deployment/<nome>
oc set triggers deployment/<nome> --from-image=<imagestream>:latest -c <container>

oc rollout restart deployment/<nome>
oc rollout history deployment/<nome>
```

### Trigger x restart

```text
oc rollout restart
→ força novos Pods agora

oc set triggers ... --from-image=...
→ configura rollout automático para futuras mudanças da ImageStreamTag
```

Se a sintaxe não vier de memória:

```bash
oc set --help
oc set triggers --help
```

Observação já validada: ao omitir o nome em `oc create route edge --service=<service>`, a Route pode usar o nome do Service.

---

## Troubleshooting — fluxo de decisão

```mermaid
flowchart TD
    START[Aplicação não funciona] --> BUILDQ{Build completou?}

    BUILDQ -->|não| BLOG[oc logs build/...]
    BLOG --> ASSEMBLEQ{Falha no assemble?}
    ASSEMBLEQ -->|sim| SOURCE[dependências / scripts S2I / permissões]
    ASSEMBLEQ -->|não| BOTHER[Git / builder / output / registry]

    BUILDQ -->|sim| PODQ{Pod fica Running?}

    PODQ -->|não| PLOG[oc logs pod/...]
    PLOG --> PREV[oc logs --previous pod/...]
    PREV --> RUNTIME[run / config / probes / imagem]

    PODQ -->|sim| SVCQ{Service seleciona o Pod?}
    SVCQ -->|não| LABELS[labels / selectors / endpoints]
    SVCQ -->|sim| ROUTEQ{Route chega no Service?}

    ROUTEQ -->|não| ROUTE[Route / TLS / target]
    ROUTEQ -->|sim| OK[Fluxo ponta a ponta OK]
```

Casos reais já encontrados nos labs:

- `BuildConfigInstantiateFailed` enquanto uma imagem-base ainda não estava resolvida.
- webhook chegando como `system:anonymous` e falhando por RBAC.
- `ImageStreamTag` atualizado enquanto o Pod continuava com imagem antiga.
- `imagePullPolicy: Always` não provoca rollout sozinho.
- `contextDir` define contexto de build, não filtra eventos do webhook por caminho.
- `postCommit` com exit code diferente de zero faz o Build falhar.
- `requirements.txt` inválido causando falha no `assemble`.
- custom `assemble` tentando gravar em `/root` como `USER 1001`.
- custom `run` apontando para arquivo inexistente e causando reinício do container.
- `oc logs --previous` para recuperar logs da execução anterior de um container.

---

## Próximo ramo: Deployments avançados

```mermaid
flowchart LR
    DEP[Deployment] --> STRAT[Deployment Strategy]
    STRAT --> ROLLING[RollingUpdate]
    STRAT --> RECREATE[Recreate]

    DEP --> HIST[rollout history]
    HIST --> ROLLBACK[rollback]

    DEP --> HEALTH[Health]
    HEALTH --> READY[readiness]
    HEALTH --> LIVE[liveness]
    HEALTH --> STARTUP[startup]

    DEP --> RES[Resources]
    RES --> REQUESTS[requests]
    RES --> LIMITS[limits]

    DEP --> STATE[Stateful]
    STATE --> PVC[PVC / persistência]
```

Próximo objetivo: controlar o comportamento do Deployment durante atualizações e falhas, em vez de apenas criar a aplicação.

---

## Regra de manutenção

Ao terminar um bloco de estudo:

```text
README raiz
→ atualizar progresso

mindmap/README.md
→ atualizar relações e fluxos

topics/XX-*/README.md ou lab equivalente
→ registrar comandos, exemplos e troubleshooting
```
