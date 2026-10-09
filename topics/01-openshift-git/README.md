# 01 — Fundamentos OpenShift e Git

## Objetivo

Praticar o uso básico do OpenShift pela CLI e estabelecer o fluxo de trabalho utilizado nos laboratórios da EX288.

## Conceitos estudados

- Project / Namespace
- Pods
- Deployments
- ReplicaSets
- Services
- Routes
- Labels
- Selectors
- Git como origem do código
- Uso da CLI `oc`
- Uso de `--dry-run=client` e `--dry-run=server`

## Fluxo

```text
Git
 ↓
OpenShift
 ↓
recursos da aplicação
```

O projeto utilizado nos laboratórios é:

```text
monticelli-ex288
```

## Comandos utilizados

```bash
oc project monticelli-ex288
oc get po
oc get deployment
oc get svc
oc get route
oc get all
oc get all -l app=vote
oc get po -l app=vote
oc get bc -l app=vote
oc get is -l app=vote
oc get po --show-labels
oc get deployment --show-labels
oc get bc --show-labels
```

## Git

```bash
git status
git add .
git commit -m "mensagem"
git push
```

Repositório:

```text
https://github.com/fmonticelli/ex288-labs
```

## Dry-run

```bash
oc create deployment vote \
  --image=image-registry.openshift-image-registry.svc:5000/monticelli-ex288/vote:latest \
  --dry-run=client \
  -o yaml
```

```bash
oc create deployment vote \
  --image=image-registry.openshift-image-registry.svc:5000/monticelli-ex288/vote:latest \
  --dry-run=server \
  -o yaml
```

```text
--dry-run=client
→ geração local
→ bom para produzir YAML rapidamente

--dry-run=server
→ passa pela validação/defaulting do API server
→ melhor para verificar o objeto como o cluster o interpretará
```

## Labels

```bash
-l app=vote
```

```yaml
metadata:
  labels:
    app: vote
```

```bash
oc get all -l app=vote
```

## Pegadinhas para a EX288

Depois de:

```bash
oc project namespace
```

é possível trabalhar sem repetir `-n`:

```bash
oc get po
```

Não trate nome de Pod como estático:

```text
Deployment/vote
 ↓
ReplicaSet/vote-588cb459cd
 ↓
Pod/vote-588cb459cd-9f8cx
```

Prefira selectors quando possível:

```bash
oc get po -l app=vote
```

## Exercícios realizados

- Seleção de projeto
- Consulta de Pods
- Consulta de recursos por label
- Uso de Git no fluxo de build
- Geração de YAML via `dry-run`
- Validação via API server
