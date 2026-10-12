# Cenário 02 — Broken custom assemble

## Objetivo

Diagnosticar um build S2I que falha porque o source fornece um script `assemble` customizado incompatível com o usuário não-root da builder image.

## Estado inicial

A aplicação utiliza a builder `python-311:latest` e fornece um script customizado em:

```text
.s2i/bin/assemble
```

O script quebrado continha:

```bash
#!/bin/bash

set -e

echo "Running custom assemble..."

cp -a /tmp/src/. /opt/app-root/src/

echo "Creating build cache..."
mkdir -p /root/ex288-cache

pip install --no-cache-dir -r /opt/app-root/src/requirements.txt
```

A versão quebrada foi preservada em:

```text
versions/assemble.broken
```

## Sintoma

O primeiro build falhou:

```bash
oc get build -l app=s2i-broken-assemble
```

Resultado:

```text
s2i-broken-assemble-1   Failed (GenericBuildFailed)
```

## Diagnóstico

Logs do Build:

```bash
oc logs -f build/s2i-broken-assemble-1
```

Trecho relevante:

```text
STEP 8/10: USER 1001
STEP 9/10: RUN /tmp/scripts/assemble
Running custom assemble...
Creating build cache...
mkdir: cannot create directory '/root/ex288-cache': Permission denied
error: build error: building at STEP "RUN /tmp/scripts/assemble": while running runtime: exit status 1
```

Dois pontos foram importantes para o diagnóstico:

```text
USER 1001
```

mostra que o script é executado como usuário não-root.

E:

```text
RUN /tmp/scripts/assemble
```

mostra que o S2I está utilizando o `assemble` customizado fornecido pelo source, e não apenas o script padrão da builder image.

## Causa raiz

O custom `assemble` tentava criar:

```text
/root/ex288-cache
```

O usuário `1001` não possui permissão para criar diretórios dentro de `/root`.

## Correção

Como o diretório de cache não era utilizado pelo restante do script, a linha foi removida.

O script corrigido ficou equivalente a:

```bash
#!/bin/bash

set -e

echo "Running custom assemble..."

cp -a /tmp/src/. /opt/app-root/src/

echo "Creating build cache..."

pip install --no-cache-dir -r /opt/app-root/src/requirements.txt
```

Outra correção possível, caso um cache fosse realmente necessário, seria utilizar um caminho gravável pelo usuário da builder, por exemplo `/tmp/ex288-cache` ou outro diretório preparado com permissões adequadas.

## Publicação da correção

```bash
git add s2i-troubleshooting/02-broken-assemble/.s2i/bin/assemble
git commit -m "update s2i-troubleshooting/02-broken-assemble/.s2i/bin/assemble"
git push
```

## Novo build

```bash
oc start-build s2i-broken-assemble --follow
```

O segundo build utilizou o commit corrigido e concluiu com sucesso.

## Validação

```bash
oc get build -l app=s2i-broken-assemble
```

Resultado observado:

```text
s2i-broken-assemble-1   Source   Failed
s2i-broken-assemble-2   Source   Complete
```

Nos logs do build corrigido:

```text
STEP 8/10: USER 1001
STEP 9/10: RUN /tmp/scripts/assemble
Running custom assemble...
Creating build cache...
Successfully installed Flask-3.1.3 ...
STEP 10/10: CMD /usr/libexec/s2i/run
...
Push successful
```

## Preservar a versão corrigida

```bash
cp   s2i-troubleshooting/02-broken-assemble/.s2i/bin/assemble   s2i-troubleshooting/02-broken-assemble/versions/assemble.fixed
```

## Fluxo de troubleshooting

```text
Build Failed
    ↓
oc logs build/<build>
    ↓
RUN /tmp/scripts/assemble
    ↓
custom assemble do source
    ↓
Permission denied em /root
    ↓
builder executando como USER 1001
    ↓
corrigir caminho/operação incompatível com non-root
    ↓
git push
    ↓
oc start-build
    ↓
Build Complete
```

## Pegadinhas EX288

Um erro dentro de:

```text
RUN /tmp/scripts/assemble
```

indica que existe uma customização S2I fornecida pelo source.

Já:

```text
RUN /usr/libexec/s2i/assemble
```

normalmente indica o script `assemble` fornecido pela própria builder image.

Sempre observar também qual usuário está executando o script. Builder images OpenShift normalmente executam a aplicação e os scripts S2I como usuário não-root.
