# 09 — Troubleshooting

## Objetivo

Registrar problemas reais encontrados durante os laboratórios e o processo utilizado para diagnosticá-los.

## Comandos básicos

```bash
oc get all
oc get all -l app=vote
oc describe bc vote
oc describe deployment vote
oc describe svc vote
oc describe route vote
oc logs -f bc/vote
oc logs -f build/vote-2
```

## Caso 1 — BuildConfigInstantiateFailed

```text
Error resolving ImageStreamTag python-311:latest:
unable to find latest tagged image
```

Também ocorreu com `nodejs-20:latest`.

Causa observada: o BuildConfig tentou iniciar antes de o ImageStreamTag da imagem-base estar resolvido/importado.

Diagnóstico:

```bash
oc describe bc vote
oc get is
oc get istag python-311:latest
oc get builds
```

## Caso 2 — `git push` não criou Build

O BuildConfig não faz polling no Git.

```text
git push
 ↓
GitHub
 ↓
webhook HTTP
 ↓
BuildConfig
 ↓
Build
```

## Caso 3 — Webhook retornando 403

```text
User "system:anonymous" cannot create resource "buildconfigs/webhooks"
```

O request chegava ao cluster; o problema era autorização/RBAC.

```bash
oc create rolebinding webhook-access-unauthenticated \
  --clusterrole=system:webhook \
  --group=system:unauthenticated \
  -n monticelli-ex288
```

Depois:

```bash
oc delete rolebinding webhook-access-unauthenticated
```

## Caso 4 — Imagem nova, Pod antigo

```bash
oc get istag vote:latest \
  -o jsonpath='{.image.dockerImageReference}{"\n"}'
```

```bash
oc get pod -l app=vote \
  -o jsonpath='{.items[0].status.containerStatuses[0].imageID}{"\n"}'
```

Causa: Deployment sem ImageChange trigger.

Solução:

```bash
oc set triggers deployment/vote \
  --from-image=vote:latest \
  -c vote
```

## Caso 5 — `imagePullPolicy: Always` não fez rollout

`Always` atua quando um Pod é criado; não monitora continuamente a tag.

## Caso 6 — Route HTTP x HTTPS

Primeira forma:

```bash
oc expose service vote
```

Com TLS edge:

```bash
oc create route edge vote \
  --service=vote \
  --insecure-policy=Redirect
```

## Caso 7 — `redirect` x `Redirect`

Valor correto utilizado:

```text
Redirect
```

O `--dry-run=server` foi útil para validar o recurso no API server.

## Caso 8 — Commit só no README gerou Build

`contextDir: vote` controla o contexto do Build, não filtra eventos do webhook por path.

```text
push em main
 ↓
webhook
 ↓
BuildConfig
 ↓
novo Build
```

## Caso 9 — Build sem mudança da aplicação pode gerar digest novo

O OpenShift injeta metadados de build/commit na imagem, por exemplo:

```text
OPENSHIFT_BUILD_COMMIT
io.openshift.build.commit.id
io.openshift.build.commit.message
```

## Estratégia de troubleshooting

```text
oc get
 ↓
oc describe
 ↓
Events
 ↓
oc logs
 ↓
comparar configuração desejada x estado atual
```

```text
imagem-base mudou?
 ↓
Build aconteceu?
 ↓
ImageStreamTag mudou?
 ↓
Deployment foi atualizado?
 ↓
ReplicaSet novo apareceu?
 ↓
Pod ficou Ready?
 ↓
Service seleciona o Pod?
 ↓
Route alcança o Service?
```
