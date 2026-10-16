# 07 — Health Monitoring / Probes

[← Voltar para o README principal](../../README.md) · [🧭 Mindmap](../../mindmap/)

Bloco hands-on de health monitoring no OpenShift, cobrindo `readinessProbe`, `livenessProbe`, `startupProbe`, probes HTTP, exec e TCP, timings, thresholds e troubleshooting.

## Modelo mental

```text
startupProbe
→ a aplicação terminou de inicializar?

livenessProbe
→ o container continua saudável?

readinessProbe
→ o Pod já pode receber tráfego / trabalho?
```

Efeitos:

```text
startup falha até failureThreshold
→ reinicia o container
→ liveness/readiness ainda não são executadas

liveness falha até failureThreshold
→ reinicia o container

readiness falha até failureThreshold
→ NÃO reinicia o container
→ Pod fica NotReady
→ deixa de ser elegível para tráfego do Service
```

## Lab base

Deployment usado:

```bash
oc create deployment probes-lab \
  --image=image-registry.openshift-image-registry.svc:5000/monticelli-ex288/s2i-broken-run:latest

oc expose deployment probes-lab \
  --port=8080 \
  --target-port=8080
```

Inspeção inicial:

```bash
oc get deploy probes-lab
oc get pods -l app=probes-lab
oc get endpoints probes-lab
```

> O cluster avisou que `v1 Endpoints` está deprecated. O comando ainda foi útil no lab para visualizar rapidamente os backends elegíveis do Service.

## Readiness HTTP

Probe saudável:

```bash
oc set probe deployment/probes-lab \
  --readiness \
  --get-url=http://:8080/health \
  --initial-delay-seconds=2 \
  --period-seconds=5 \
  --failure-threshold=2
```

Probe quebrada propositalmente:

```bash
oc set probe deployment/probes-lab \
  --readiness \
  --get-url=http://:8080/nao-existe \
  --initial-delay-seconds=2 \
  --period-seconds=5 \
  --failure-threshold=2
```

Comportamento validado:

```text
STATUS=Running
READY=0/1
RESTARTS=0

Readiness probe failed:
HTTP probe failed with statuscode: 404
```

Conclusão:

```text
Running ≠ Ready
```

## Liveness HTTP

Probe saudável:

```bash
oc set probe deployment/probes-lab \
  --liveness \
  --get-url=http://:8080/health \
  --initial-delay-seconds=2 \
  --period-seconds=5 \
  --failure-threshold=2
```

Probe quebrada:

```bash
oc set probe deployment/probes-lab \
  --liveness \
  --get-url=http://:8080/nao-existe \
  --initial-delay-seconds=2 \
  --period-seconds=5 \
  --failure-threshold=2
```

Comportamento observado:

```text
mesmo Pod
→ container reinicia
→ RESTARTS aumenta
→ READY alterna durante os restarts
```

Events:

```text
Liveness probe failed: HTTP probe failed with statuscode: 404
Back-off restarting failed container
```

O exit code observado no lab foi 137, mas ele não deve ser tratado como regra universal de liveness. A regra é: falha de liveness até o threshold leva o kubelet a reiniciar o container.

## Startup probe

Probe quebrada propositalmente:

```bash
oc set probe deployment/probes-lab \
  --startup \
  --get-url=http://:8080/nao-existe \
  --period-seconds=5 \
  --failure-threshold=3
```

Comportamento validado:

```text
startup ainda não passou
→ liveness não roda
→ readiness não roda

3 falhas consecutivas
→ container reiniciado

repetição do ciclo
→ pode resultar em CrashLoopBackOff
```

Events:

```text
Startup probe failed: HTTP probe failed with statuscode: 404
Container ... failed startup probe, will be restarted
```

Correção:

```bash
oc set probe deployment/probes-lab \
  --startup \
  --get-url=http://:8080/health \
  --period-seconds=5 \
  --failure-threshold=3
```

Depois do sucesso da startup, liveness e readiness passam a ser executadas.

## Exec readinessProbe

A sintaxe foi reconstruída com:

```bash
oc set probe --help
```

Probe saudável:

```bash
oc set probe deploy/probes-lab \
  --readiness \
  -- test -f /opt/app-root/src/app.py
```

Resultado no PodTemplate:

```yaml
readinessProbe:
  exec:
    command:
      - test
      - -f
      - /opt/app-root/src/app.py
```

Probe quebrada:

```bash
oc set probe deploy/probes-lab \
  --readiness \
  -- test -f /opt/app-root/src/arquivo-que-nao-existe
```

Regra prática:

```text
exit code 0
→ sucesso

exit code diferente de 0
→ falha
```

Como `test -f` não imprime mensagem por padrão, o Event apareceu apenas como:

```text
Readiness probe failed:
```

## TCP readinessProbe

Probe saudável:

```bash
oc set probe deploy/probes-lab \
  --readiness \
  --open-tcp 8080
```

Inspeção:

```bash
oc get deploy probes-lab \
  -o jsonpath='{.spec.template.spec.containers[0].readinessProbe}' | jq
```

Resultado:

```json
{
  "tcpSocket": {
    "port": 8080
  }
}
```

Probe quebrada:

```bash
oc set probe deploy/probes-lab \
  --readiness \
  --open-tcp 9999
```

Event observado:

```text
Readiness probe failed:
dial tcp <pod-ip>:9999: connect: connection refused
```

Modelo mental:

```text
HTTP probe
→ verifica uma resposta HTTP

exec probe
→ executa comando dentro do container e avalia exit code

TCP probe
→ tenta abrir uma conexão TCP na porta
```

Uma TCP probe prova que a porta aceita conexão; ela não valida semântica da aplicação como uma probe HTTP pode fazer.

## Readiness + RollingUpdate

Ao quebrar a readiness do novo Pod:

```text
Pod antigo → 1/1 Running
Pod novo   → 0/1 Running
```

O Deployment preservou o Pod antigo saudável.

No lab TCP, a porta `9999` nunca ficou Ready e o rollout terminou com:

```text
deployment "probes-lab" exceeded its progress deadline
```

Isso conectou na prática:

```text
readiness
→ disponibilidade do novo Pod
→ progresso do RollingUpdate
→ progressDeadlineSeconds
```

## Timings e thresholds

Campos estudados:

```text
initialDelaySeconds
→ espera antes da primeira tentativa

periodSeconds
→ intervalo entre tentativas

timeoutSeconds
→ prazo máximo de cada tentativa individual

failureThreshold
→ falhas consecutivas necessárias para considerar falha

successThreshold
→ sucessos consecutivos necessários para considerar sucesso
```

Exemplo:

```yaml
readinessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 4
  periodSeconds: 5
  timeoutSeconds: 2
  failureThreshold: 3
  successThreshold: 2
```

Linha do tempo conceitual, assumindo respostas imediatas:

```text
t=4   primeira tentativa
t=9   segunda tentativa
t=14  terceira tentativa
t=19  quarta tentativa
t=24  quinta tentativa
```

Com três falhas consecutivas em `t=4`, `t=9` e `t=14`, a readiness é considerada falha em `t=14`.

Se depois houver dois sucessos consecutivos em `t=19` e `t=24`, com `successThreshold: 2`, volta a ficar saudável em `t=24`.

Para liveness:

```yaml
livenessProbe:
  initialDelaySeconds: 3
  periodSeconds: 4
  timeoutSeconds: 2
  failureThreshold: 3
```

Tentativas conceituais:

```text
t=3
t=7
t=11
t=15
t=19
```

Um SUCCESS no meio das falhas reinicia a contagem de falhas consecutivas.

### Estado de domínio

```text
✅ readinessProbe
✅ livenessProbe
✅ startupProbe
✅ HTTP
✅ exec
✅ TCP
✅ troubleshooting
✅ relação com RollingUpdate
🟡 cálculo rápido de timings / thresholds sem consulta
```

O ponto 🟡 é intencional: os conceitos estão entendidos, mas ainda vale repetir cálculos rápidos antes dos simulados.

## Troubleshooting

Comandos usados:

```bash
oc get pods -l app=probes-lab
oc get pods -l app=probes-lab -w
oc rollout status deployment/probes-lab
oc get deploy probes-lab -o yaml
oc describe pod <pod>
oc logs <pod>
oc logs --previous <pod>
oc events --for pod/<pod>
```

Atalho de inspeção recomendado:

```bash
oc get deploy probes-lab \
  -o jsonpath='{.spec.template.spec.containers[0].readinessProbe}' | jq
```

Para reconstruir sintaxe e confirmar semântica durante a prova:

```bash
oc set probe --help
oc explain deployment.spec.template.spec.containers.readinessProbe
oc explain deployment.spec.template.spec.containers.readinessProbe.periodSeconds
oc explain deployment.spec.template.spec.containers.readinessProbe.failureThreshold
```
