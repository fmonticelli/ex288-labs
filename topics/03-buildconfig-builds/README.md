# 03 — BuildConfig e Builds

## Objetivo

Construir imagens no OpenShift a partir de código Git utilizando BuildConfig e compreender o ciclo de vida dos Builds.

## Conceitos estudados

- BuildConfig
- Build
- Docker strategy
- Git source
- `contextDir`
- output do build
- ImageStream como destino
- rebuild manual
- logs de build
- labels
- triggers
- GitHub webhook
- Generic webhook
- ImageChange trigger da imagem-base (conceito; validação prática pendente)

## BuildConfig x Build

```text
BuildConfig
→ receita persistente de como construir

Build
→ uma execução específica dessa receita
```

## `oc new-build`

```bash
oc new-build \
  --name hello \
  -l app=hello \
  --strategy docker \
  https://github.com/fmonticelli/ex288-labs \
  --context-dir hello/
```

```bash
oc new-build \
  --name vote \
  -l app=vote \
  --strategy docker \
  https://github.com/fmonticelli/ex288-labs \
  --context-dir vote
```

```text
Git
 ↓
BuildConfig
 ↓
Build
 ↓
ImageStreamTag
 ↓
registry interno
```

Não cria automaticamente Deployment, Service ou Route.

## `oc new-build` x `oc new-app`

```text
oc new-build
→ foco no processo de build

oc new-app
→ cria uma aplicação a partir de source ou imagem
```

Quando `oc new-app` recebe source que exige build, pode criar BuildConfig, Build, ImageStream, Deployment e Service.

## Strategy

A strategy define COMO a imagem será construída.

```bash
--strategy=docker
```

## `contextDir`

```bash
--context-dir hello/
--context-dir vote
```

```text
contextDir
→ define o diretório usado como contexto do build
→ NÃO filtra quais commits podem disparar um webhook
```

## Validação

```bash
oc get bc
oc get builds
oc describe bc vote
oc get builds -l app=vote
```

## Rebuild manual

```bash
oc start-build vote
oc start-build vote --follow
```

## Logs

```bash
oc logs -f bc/vote
oc logs -f build/vote-2
```

## Imagem-base do Docker strategy

Dockerfile:

```Dockerfile
FROM registry.access.redhat.com/ubi9/python-311
```

BuildConfig:

```text
From Image: ImageStreamTag python-311:latest
```

Durante o build foi observado:

```text
Replaced Dockerfile FROM image registry.access.redhat.com/ubi9/python-311
```

## Triggers observados

```bash
oc set triggers bc/vote
oc describe bc vote
```

```text
ConfigChange
ImageChange
GitHub
Generic
```

## GitHub webhook

```text
git push
 ↓
GitHub webhook
 ↓
BuildConfig
 ↓
Build automático
```

O webhook externo foi removido depois do laboratório para evitar builds a cada alteração do repositório.

## RBAC do webhook

Erro observado:

```text
User "system:anonymous" cannot create resource "buildconfigs/webhooks"
```

Solução usada no laboratório:

```bash
oc create rolebinding webhook-access-unauthenticated \
  --clusterrole=system:webhook \
  --group=system:unauthenticated \
  -n monticelli-ex288
```

Remoção posterior:

```bash
oc delete rolebinding webhook-access-unauthenticated
```

## Git ref

O fluxo funcionou sem exigir obrigatoriamente `refs/heads/main` em `spec.source.git.ref`.

## ImageChange do BuildConfig

Entrada atual:

```text
ImageStreamTag/python-311:latest
```

Fluxo a finalizar:

```text
python-311:latest muda
 ↓
ImageChange trigger
 ↓
Build/vote-N
 ↓
vote:latest muda
```

## Pegadinhas para a EX288

```text
"configure a build"
→ pensar primeiro em oc new-build

"create/deploy an application"
→ oc new-app pode ser apropriado
```

## Exercícios realizados

- Build `hello`
- Build `vote`
- Docker strategy
- Git source
- `contextDir`
- labels
- rebuild manual
- acompanhamento de logs
- webhook
- troubleshooting de RBAC
- observação de triggers
