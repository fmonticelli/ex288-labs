# 02 — Container Images

## Objetivo

Entender como construir imagens compatíveis com OpenShift e como um Dockerfile/Containerfile influencia posteriormente o BuildConfig.

## Conceitos estudados

- `FROM`
- `WORKDIR`
- `COPY`
- `RUN`
- `ENV`
- `EXPOSE`
- `ENTRYPOINT`
- `CMD`
- cache de layers
- multi-stage build
- execução non-root
- UID arbitrário
- permissões para grupo `0`
- Healthcheck de imagem
- diferenças práticas entre formato OCI e Docker

## Aplicação `hello`

```Dockerfile
FROM registry.access.redhat.com/ubi9/nodejs-20
WORKDIR /opt/app-root/src
COPY package.json ./
RUN npm install
COPY server.js ./
EXPOSE 8080
CMD ["node", "server.js"]
```

## Aplicação `vote`

```Dockerfile
FROM registry.access.redhat.com/ubi9/python-311
WORKDIR /opt/app-root/src
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py ./
EXPOSE 8080
CMD ["python", "app.py"]
```

## Cache de layers

```Dockerfile
COPY package.json ./
RUN npm install
COPY server.js ./
```

Alterar apenas `server.js` permite reaproveitar a layer do `npm install`.

## `npm install` x `npm ci`

Sem `package-lock.json`, foi utilizado:

```Dockerfile
RUN npm install
```

`npm ci` exige lockfile válido.

## UID arbitrário no OpenShift

Foi testada execução com UID arbitrário e `gid=0(root)`.

Padrão útil para diretórios graváveis:

```Dockerfile
RUN chgrp -R 0 /opt/app-root/src/data && \
    chmod -R g=u /opt/app-root/src/data
```

```text
chgrp -R 0
→ grupo root

chmod -R g=u
→ replica permissões do owner para o grupo
```

## Testes com Podman

```bash
podman exec ex288 id
podman healthcheck run ex288
podman build --format docker ...
```

## Healthcheck de imagem

```Dockerfile
HEALTHCHECK CMD curl -f http://localhost:8080/health || exit 1
```

Isso é diferente das probes do Kubernetes/OpenShift.

## Multi-stage builds

Faz sentido quando existe separação real entre ambiente de build e imagem final.

## Pegadinhas para a EX288

Não depender de UID fixo para permissões da aplicação.

Não confundir:

```Dockerfile
LABEL ...
```

com:

```yaml
metadata:
  labels:
    app: vote
```

## Exercícios realizados

- Build de aplicação Node.js
- Build de aplicação Python
- Testes com UID arbitrário
- Testes de escrita em diretórios
- Healthcheck de container
- Otimização básica de cache de layers
