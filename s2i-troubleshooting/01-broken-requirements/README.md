# Cenário 01 — Broken requirements

## Objetivo

Diagnosticar um build S2I que falha durante o script `assemble` por causa de uma dependência inválida.

## Sintoma

O primeiro build falhou:

```bash
oc get build s2i-broken-deps-1
```

Resultado:

```text
Failed (GenericBuildFailed)
```

## Diagnóstico

Logs do Build:

```bash
oc logs build/s2i-broken-deps-1
```

Também foi possível consultar diretamente o Pod do build:

```bash
oc logs pods/s2i-broken-deps-1-build
```

Erro relevante:

```text
ERROR: Could not find a version that satisfies the requirement Flask==99.99.99
ERROR: No matching distribution found for Flask==99.99.99
error: build error: building at STEP "RUN /usr/libexec/s2i/assemble": while running runtime: exit status 1
```

O erro ocorreu durante:

```text
/usr/libexec/s2i/assemble
```

Portanto, a falha ocorreu em build time.

## Causa raiz

O arquivo `requirements.txt` continha uma versão inexistente:

```text
Flask==99.99.99
```

A versão quebrada foi preservada em:

```text
versions/requirements.broken.txt
```

## Correção

O arquivo foi alterado para uma versão válida:

```text
Flask==3.1.3
```

Comando utilizado:

```bash
sed -i 's/99.99.99/3.1.3/g' s2i-troubleshooting/01-broken-requirements/requirements.txt
```

A versão corrigida deve ser preservada em:

```text
versions/requirements.fixed.txt
```

Exemplo:

```bash
cp   s2i-troubleshooting/01-broken-requirements/requirements.txt   s2i-troubleshooting/01-broken-requirements/versions/requirements.fixed.txt
```

## Publicação da correção

```bash
git add s2i-troubleshooting/01-broken-requirements/requirements.txt
git commit -m "update requirements.txt"
git push
```

## Novo build

```bash
oc start-build s2i-broken-deps --follow
```

Resultado:

```text
s2i-broken-deps-2   Complete
```

## Validação

```bash
oc get build -l app=s2i-broken-deps
```

Resultado observado:

```text
s2i-broken-deps-1   Source   Git@98d9e10   Failed (GenericBuildFailed)
s2i-broken-deps-2   Source   Git@850ebd1   Complete
```

## Fluxo de troubleshooting

```text
Build Failed
    ↓
oc logs build/<build>
    ↓
erro dentro de assemble
    ↓
identificar arquivo/dependência
    ↓
corrigir source
    ↓
git push
    ↓
oc start-build
    ↓
Build Complete
```

## Pegadinha EX288

Se o erro aparece durante:

```text
RUN /usr/libexec/s2i/assemble
```

o problema está acontecendo durante o build.

Primeiro investigar:

```bash
oc logs build/<build>
```

Não confundir com problemas do script `run`, que aparecem somente quando o container é iniciado.
