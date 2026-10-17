# 06 — ConfigMaps e Secrets

[← Voltar para o README principal](../../README.md)

Bloco prático de configuração de aplicações no OpenShift usando ConfigMaps e Secrets.

## Objetivos praticados

- criar ConfigMaps por literal, arquivo e env-file;
- injetar ConfigMaps como variáveis de ambiente;
- montar ConfigMaps como volumes;
- criar Secrets por literal e arquivo;
- injetar Secrets como variáveis de ambiente;
- montar Secrets como volumes;
- atualizar configuração e observar a diferença entre env e volume;
- validar rollouts e conteúdo dentro do container.

## ConfigMap por literal

```bash
oc create configmap app-config \
  --from-literal APP_MESSAGE=hello-from-configmap \
  --from-literal APP_MODE=study \
  --dry-run=server -o yaml

oc create configmap app-config \
  --from-literal APP_MESSAGE=hello-from-configmap \
  --from-literal APP_MODE=study

oc get cm app-config
oc get cm app-config -o yaml
```

Resultado conceitual:

```yaml
data:
  APP_MESSAGE: hello-from-configmap
  APP_MODE: study
```

## ConfigMap por arquivo

Arquivo local:

```text
APP_COLOR=blue
APP_FEATURE=enabled
```

Criação:

```bash
oc create cm app-config-file --from-file app.properties --dry-run=server -o yaml
oc create cm app-config-file --from-file app.properties
oc get cm app-config-file -o yaml
```

Estrutura:

```yaml
data:
  app.properties: |
    APP_COLOR=blue
    APP_FEATURE=enabled
```

Regra:

```text
--from-file
→ nome do arquivo vira uma key
→ conteúdo inteiro do arquivo vira o value
```

## ConfigMap por env-file

```bash
oc create cm app-config-env --from-env-file app.properties
oc get cm app-config-env -o yaml
```

Estrutura:

```yaml
data:
  APP_COLOR: blue
  APP_FEATURE: enabled
```

Regra:

```text
--from-env-file
→ cada linha KEY=VALUE vira uma key independente
```

## ConfigMap como volume

Deployment usado:

```bash
oc create deployment config-lab \
  --image=image-registry.openshift-image-registry.svc:5000/monticelli-ex288/s2i-broken-run:latest
```

Montagem correta:

```bash
oc set volumes deployment/config-lab \
  --add \
  --type configmap \
  --configmap-name app-config-file \
  --mount-path /etc/config
```

Validação:

```bash
oc exec deployment/config-lab -- ls -l /etc/config
oc exec deployment/config-lab -- cat /etc/config/app.properties
oc exec deployment/config-lab -- sh -c 'echo "APP_COLOR=$APP_COLOR"'
```

O arquivo existe no filesystem, mas montar um ConfigMap como volume não cria variáveis de ambiente.

Pegadinha encontrada no laboratório:

```text
--path
≠
--mount-path
```

Para montar no container, foi necessário usar `--mount-path`.

## ConfigMap como env

```bash
oc set env deploy/config-lab --from=configmap/app-config-env
oc rollout status deployment/config-lab
oc exec deployment/config-lab -- env | grep '^APP_'
```

Resultado observado:

```text
APP_COLOR=blue
APP_FEATURE=enabled
```

A alteração do PodTemplate provoca rollout.

### Uma key específica

A CLI permite selecionar keys ao importar:

```bash
oc set env deploy/config-lab \
  --from=configmap/app-config-env \
  --keys=APP_COLOR
```

Para renomear arbitrariamente a variável e apontar para uma key diferente, entra `configMapKeyRef` no manifest. Esse detalhe foi apenas reconhecido, não priorizado como habilidade principal neste bloco.

`envFrom` diretamente no manifest permanece como item de revisão.

## Atualização de ConfigMap: volume x env

Atualização declarativa praticada:

```bash
oc create cm app-config-file \
  --from-file app.properties \
  --dry-run=client -o yaml | oc apply -f-

oc create cm app-config-env \
  --from-env-file app.properties \
  --dry-run=client -o yaml | oc apply -f-
```

Com volume:

```bash
oc exec deploy/config-lab -- cat /etc/config/app.properties
```

O conteúdo atualizado apareceu sem rollout.

Com env:

```bash
oc exec deploy/config-lab -- env | grep '^APP_'
oc rollout restart deploy/config-lab
oc exec deploy/config-lab -- env | grep '^APP_'
```

O valor antigo permaneceu no container existente. Um novo Pod foi necessário para ler o valor novo.

Modelo:

```text
ConfigMap como env
→ valor é resolvido quando o Pod nasce
→ alteração exige novo Pod

ConfigMap como volume
→ arquivo projetado pode atualizar sem rollout
→ pode existir atraso de propagação
```

## Secret por literal

```bash
oc create secret generic app-secret \
  --from-literal=DB_USER=admin \
  --from-literal=DB_PASSWORD=s3cr3t \
  --dry-run=server -o yaml

oc create secret generic app-secret \
  --from-literal=DB_USER=admin \
  --from-literal=DB_PASSWORD=s3cr3t

oc get secret app-secret
oc get secret app-secret -o yaml
```

Exemplo:

```yaml
data:
  DB_PASSWORD: czNjcjN0
  DB_USER: YWRtaW4=
type: Opaque
```

Base64 é encoding, não criptografia.

Decodificação:

```bash
echo 'YWRtaW4=' | base64 -d
echo 'czNjcjN0' | base64 -d
```

Também pode ser consultado diretamente:

```bash
oc get secret app-secret \
  -o jsonpath='{.data.DB_USER}' | base64 -d
```

## Secret por arquivo

Arquivo:

```text
username=felipe
password=lab123
```

Criação:

```bash
oc create secret generic app-secret-file \
  --from-file=credentials.txt \
  --dry-run=server -o yaml

oc create secret generic app-secret-file --from-file=credentials.txt
oc get secret app-secret-file -o yaml
```

Estrutura conceitual:

```text
key
→ credentials.txt

value
→ conteúdo inteiro do arquivo codificado em base64
```

Decodificação:

```bash
oc get secret app-secret-file \
  -o jsonpath='{.data.credentials\.txt}' | base64 -d
```

## Secret como env

```bash
oc set env deploy/config-lab --from=secret/app-secret
oc rollout status deployment/config-lab
oc exec deployment/config-lab -- env | grep '^DB_'
```

Dentro do container o valor aparece decodificado:

```text
DB_USER=admin
DB_PASSWORD=s3cr3t
```

## Secret como volume

```bash
oc set volumes deployment/config-lab \
  --add \
  --type secret \
  --secret-name app-secret-file \
  --mount-path /etc/secret

oc rollout status deployment/config-lab

oc exec deploy/config-lab -- ls -l /etc/secret
oc exec deploy/config-lab -- cat /etc/secret/credentials.txt
```

O arquivo apareceu em texto normal dentro do container.

O volume projetado usou symlink semelhante a:

```text
credentials.txt -> ..data/credentials.txt
```

## Atualização de Secret: volume x env

Atualização:

```bash
oc create secret generic app-secret-file \
  --from-file=credentials.txt \
  --dry-run=client -o yaml | oc apply -f-

oc create secret generic app-secret \
  --from-literal=DB_USER=blue \
  --from-literal=DB_PASSWORD=gr33n \
  --dry-run=client -o yaml | oc apply -f-
```

Secret usado como env:

```text
alteração do Secret
→ container existente continua com valor antigo
→ rollout restart
→ novo Pod recebe novo valor
```

Secret montado como volume:

```text
alteração do Secret
→ arquivo pode continuar antigo por algum tempo
→ kubelet atualiza o volume projetado
→ novo conteúdo aparece sem rollout
```

No laboratório o Secret teve um delay de propagação perceptivelmente maior que o ConfigMap. O comportamento importante é não assumir atualização instantânea.

`subPath` é uma exceção: não deve ser tratado como volume projetado que recebe atualização automática.

## Aviso do oc apply

Ao aplicar sobre recursos originalmente criados de forma imperativa, apareceu:

```text
missing the kubectl.kubernetes.io/last-applied-configuration annotation
```

O próprio `oc apply` adicionou a annotation automaticamente. O warning não impediu a atualização.

## Mini-simulado

Sem solução prévia, foram criados:

```text
ConfigMap exam-config
APP_ENV=production
APP_COLOR=red

Secret exam-secret
API_USER=developer
API_PASSWORD=openshift123
```

Comandos:

```bash
oc create secret generic exam-secret \
  --from-literal=API_USER=developer \
  --from-literal=API_PASSWORD=openshift123

oc create cm exam-config \
  --from-literal=APP_ENV=production \
  --from-literal=APP_COLOR=red

oc set env deploy/config-lab --from=secret/exam-secret
oc set env deploy/config-lab --from=configmap/exam-config

oc exec deploy/config-lab -- env | grep -E '^(APP_|API_)'
```

Depois:

```bash
oc create cm exam-file --from-file message.txt

oc set volumes deploy/config-lab \
  --add \
  --type configmap \
  --configmap-name exam-file \
  --mount-path /opt/exam

oc exec deploy/config-lab -- cat /opt/exam/message.txt
```

Resultado:

```text
hello-from-exam
```

## Modelo mental para prova

```text
preciso de configuração não sensível
→ ConfigMap

preciso de credencial / dado sensível
→ Secret

preciso expor como variável
→ oc set env --from=...

preciso expor como arquivo
→ oc set volumes --add ...

recurso mudou e uso env
→ novo Pod

recurso mudou e uso volume
→ aguardar propagação e validar arquivo
```

Comandos de descoberta úteis:

```bash
oc create configmap --help
oc create secret --help
oc set env --help
oc set volumes --help
oc explain deployment.spec.template.spec.containers.envFrom
```
