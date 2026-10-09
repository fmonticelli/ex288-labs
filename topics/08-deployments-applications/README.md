# 08 — Deployments e aplicações

## Objetivo

Executar uma imagem já construída no OpenShift e expor a aplicação usando Deployment, Service e Route.

## Fluxo

```text
ImageStream / registry
 ↓
Deployment
 ↓
ReplicaSet
 ↓
Pod
 ↓
Service
 ↓
Route
```

## Criar Deployment

```bash
oc create deployment vote \
  --image=image-registry.openshift-image-registry.svc:5000/monticelli-ex288/vote:latest
```

## Dry-run

```bash
oc create deployment vote \
  --image=image-registry.openshift-image-registry.svc:5000/monticelli-ex288/vote:latest \
  --dry-run=server \
  -o yaml
```

Foi observado que o gerador cria `app: vote` no Deployment, selector e Pod template.

## Deployment → ReplicaSet → Pod

```bash
oc get deployment vote
oc get rs -l app=vote
oc get po -l app=vote
```

## Service

```bash
oc expose deployment vote \
  --port=8080 \
  --target-port=8080
```

Validação:

```bash
oc get svc vote
oc describe svc vote
oc get endpoints vote
```

## Route HTTP

```bash
oc expose service vote
```

## Route HTTPS com edge termination

```bash
oc create route edge vote \
  --service=vote \
  --insecure-policy=Redirect
```

```text
HTTP
 ↓
Redirect
 ↓
HTTPS
 ↓
OpenShift Router
 ↓
HTTP
 ↓
Service
 ↓
Pod
```

## ImageChange trigger no Deployment

```bash
oc set triggers deployment/vote \
  --from-image=vote:latest \
  -c vote
```

Consultar:

```bash
oc set triggers deployment/vote
```

Comportamento observado:

```text
vote:latest muda
 ↓
Deployment atualiza PodTemplate
 ↓
novo ReplicaSet
 ↓
novo Pod
```

Não foi necessário:

```bash
oc rollout restart deployment/vote
```

## Validar digest

```bash
oc get deployment vote \
  -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```

```bash
oc get istag vote:latest \
  -o jsonpath='{.image.dockerImageReference}{"\n"}'
```

## Rollout

```bash
oc get rs -l app=vote
oc get po -l app=vote
oc rollout history deployment/vote
```

## Pegadinhas para a EX288

```text
oc expose deployment
→ cria Service

oc expose service
→ cria Route
```

Uma mudança em `:latest` não implica rollout automático sem um trigger apropriado.

## Exercícios realizados

- criação manual de Deployment
- Service
- Route HTTP
- Route HTTPS edge/Redirect
- labels e selectors
- ReplicaSets
- rollout automático via ImageChange
