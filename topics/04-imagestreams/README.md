# 04 — ImageStreams

## Objetivo

Entender como OpenShift referencia, acompanha e publica imagens através de ImageStreams e ImageStreamTags.

## Modelo mental

```text
Registry
→ armazena a imagem

ImageStream
→ acompanha/referencia imagens e tags

ImageStreamTag
→ nome lógico como vote:latest

digest
→ imagem exata e imutável
```

## ImageStreams dos labs

```text
hello: nodejs-20, hello
vote:  python-311, vote
```

## Consultas

```bash
oc get is
oc get is vote
oc get istag vote:latest
```

## Repository do ImageStream

```bash
oc get is vote \
  -o jsonpath='{.status.dockerImageRepository}{"\n"}'
```

Formato interno:

```text
image-registry.openshift-image-registry.svc:5000/<namespace>/<image>:<tag>
```

Exemplo:

```text
image-registry.openshift-image-registry.svc:5000/monticelli-ex288/vote:latest
```

## Resolver imagem exata

```bash
oc get istag vote:latest \
  -o jsonpath='{.image.dockerImageReference}{"\n"}'
```

## Tag x digest

```text
vote:latest
→ mutável

vote@sha256:...
→ imagem exata
```

## Output do BuildConfig

```text
Output to: ImageStreamTag vote:latest
```

```text
Build/vote-N
 ↓
registry interno
 ↓
ImageStreamTag vote:latest
```

## Comparar ImageStream e Pod

```bash
oc get istag vote:latest \
  -o jsonpath='{.image.dockerImageReference}{"\n"}'
```

```bash
oc get pod -l app=vote \
  -o jsonpath='{.items[0].status.containerStatuses[0].imageID}{"\n"}'
```

## ImageChange

```text
BuildConfig ImageChange
→ imagem de entrada mudou
→ novo Build

Deployment ImageChange
→ imagem da aplicação mudou
→ novo rollout
```

## Pegadinhas para a EX288

`imagePullPolicy: Always` não monitora continuamente a tag e não reinicia um Pod existente sozinho.

## Exercícios realizados

- consulta de ImageStreams
- consulta de ImageStreamTags
- tag x digest
- output de BuildConfig
- registry interno
- comparação entre digest atual e digest executado pelo Pod
- ImageChange trigger no Deployment
