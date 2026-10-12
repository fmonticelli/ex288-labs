# Cenário 03 — Broken custom run

## Objetivo

Diagnosticar uma aplicação construída com S2I cujo Build termina com sucesso, mas cujo container falha em runtime por causa de um script `run` customizado incorreto.

## Estado inicial

A aplicação fornece um script S2I customizado em:

```text
.s2i/bin/run
```

Versão quebrada:

```bash
#!/bin/bash

set -e

echo "Starting application with custom S2I run script..."

exec python /opt/app-root/src/missing.py
```

A versão quebrada foi preservada em:

```text
versions/run.broken
```

## 1. Validando o Build

```bash
oc get build -l app=s2i-broken-run
```

Resultado inicial:

```text
s2i-broken-run-1   Source   Git@bbc50b4   Complete
```

O Build estava `Complete`, indicando que o problema não estava no processo de build S2I.

## 2. Localizando a imagem produzida

```bash
oc describe is s2i-broken-run
```

Foi identificado o repositório interno:

```text
image-registry.openshift-image-registry.svc:5000/monticelli-ex288/s2i-broken-run:latest
```

## 3. Criando o Deployment

```bash
oc create deployment s2i-broken-run   --image=image-registry.openshift-image-registry.svc:5000/monticelli-ex288/s2i-broken-run:latest
```

O Deployment foi criado, porém o Pod entrou em erro/restart.

## 4. Diagnóstico do runtime

Como o container reiniciava, foram consultados os logs da execução anterior:

```bash
oc logs --previous pod/<pod>
```

Erro observado:

```text
Starting application with custom S2I run script...
python: can't open file '/opt/app-root/src/missing.py': [Errno 2] No such file or directory
```

Isso mostrou que a falha ocorria somente quando o container iniciava.

## 5. Causa raiz

O `.s2i/bin/run` executava:

```bash
exec python /opt/app-root/src/missing.py
```

mas a aplicação possuía:

```text
/opt/app-root/src/app.py
```

## 6. Correção

O script foi alterado para:

```bash
#!/bin/bash

set -e

echo "Starting application with custom S2I run script..."

exec python /opt/app-root/src/app.py
```

Preserve também a versão corrigida:

```bash
cp   s2i-troubleshooting/03-broken-run/.s2i/bin/run   s2i-troubleshooting/03-broken-run/versions/run.fixed
```

## 7. Publicação da correção

```bash
git add s2i-troubleshooting/03-broken-run/.s2i/bin/run
git commit -m "udpate s2i-troubleshooting/03-broken-run/.s2i/bin/run"
git push
```

## 8. Novo Build

```bash
oc start-build s2i-broken-run --follow
```

Validação:

```bash
oc get build -l app=s2i-broken-run
```

Resultado:

```text
s2i-broken-run-1   Source   Git@bbc50b4   Complete
s2i-broken-run-2   Source   Git@30d7b8b   Complete
```

## 9. Atualizando os Pods

Foi forçado um novo rollout:

```bash
oc rollout restart deployment/s2i-broken-run
```

Como o Deployment usava `s2i-broken-run:latest`, o novo Pod passou a usar a imagem atualizada.

Em um fluxo OpenShift automatizado, pode-se configurar um ImageChange trigger:

```bash
oc set triggers deployment/s2i-broken-run   --from-image=s2i-broken-run:latest   -c s2i-broken-run
```

## 10. Validação final

```bash
oc logs -f deployment/s2i-broken-run
```

Resultado:

```text
Starting application with custom S2I run script...
 * Serving Flask app 'app'
 * Running on all addresses (0.0.0.0)
```

A aplicação permaneceu executando corretamente.

## Fluxo de troubleshooting

```text
Build Complete
    ↓
imagem produzida
    ↓
Deployment criado
    ↓
Pod falha/reinicia
    ↓
oc logs --previous pod/<pod>
    ↓
erro no custom run
    ↓
missing.py não existe
    ↓
corrigir .s2i/bin/run
    ↓
git push
    ↓
novo Build Complete
    ↓
novo rollout
    ↓
Pod Running
```

## Pegadinhas EX288

### `assemble` vs `run`

```text
assemble
→ executado durante o Build
→ erro normalmente deixa Build Failed

run
→ executado quando o container inicia
→ Build pode ficar Complete e o Pod falhar depois
```

### Logs corretos para cada camada

Falha durante o Build:

```bash
oc logs build/<build>
```

Falha depois que o container inicia:

```bash
oc logs pod/<pod>
```

Se o container já reiniciou:

```bash
oc logs --previous pod/<pod>
```

Também é possível consultar logs pelo Deployment:

```bash
oc logs deployment/<deployment>
```

### Atualização da imagem

Criar uma nova imagem no ImageStream não implica automaticamente um novo rollout de qualquer Deployment.

Para automação baseada em ImageStreamTag, configure um ImageChange trigger no Deployment.
