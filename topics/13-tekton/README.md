# 13 — OpenShift Pipelines / Tekton

[← Voltar para o README principal](../../README.md)

Status atual: **🟡 em andamento**.

## Modelo mental

```text
Task
→ definição/receita

TaskRun
→ execução concreta da Task
→ cria um Pod

Step
→ container dentro do Pod do TaskRun
```

Analogia usada durante o estudo:

```text
Task / Pipeline
→ tipo uma definição de trabalho

TaskRun / PipelineRun
→ tipo uma instância concreta de execução
```

## API descoberta no cluster

```bash
oc api-resources | grep -Ei 'task|pipeline'
oc get crd | grep -Ei 'tekton|pipeline'
```

Recursos principais disponíveis:

```text
Task         tekton.dev/v1
TaskRun      tekton.dev/v1
Pipeline     tekton.dev/v1
PipelineRun  tekton.dev/v1
```

Regra prática: não assumir que todo recurso do ecossistema Tekton usa o mesmo API group; confirmar com `oc api-resources` e `oc explain`.

## 01 — Task single-step

Fluxo comprovado:

```text
Task
→ TaskRun
→ Pod
→ step-hello
→ exit code 0
→ TaskRun Succeeded=True
```

Comandos:

```bash
oc apply --dry-run=server -f task-hello-single.yaml
oc apply -f task-hello-single.yaml
oc apply --dry-run=server -f taskrun-hello-single.yaml
oc apply -f taskrun-hello-single.yaml

oc get task
oc get taskrun
oc describe task <nome>
oc describe taskrun <nome>
oc get pods
oc logs <pod>
```

## 02 — Task multi-step

Com dois Steps:

```text
1 TaskRun
→ 1 Pod
→ step-first
→ step-second
```

Logs por Step:

```bash
oc logs <pod> -c step-first
oc logs <pod> -c step-second
```

Regra prática:

```text
Task.spec.steps[].name = first
→ container criado pelo Tekton = step-first
```

Os Steps são orquestrados pelo Tekton e executados em sequência.

## 03 — Params

Sintaxe principal:

```text
Task.spec.params
→ declara parâmetros

TaskRun.spec.params
→ fornece os valores

$(params.NAME)
→ consome o parâmetro dentro da Task
```

Foram praticados:

```text
param obrigatório
param com default
TaskRun sobrescrevendo default
TaskRun omitindo valor e usando default
```

Exemplo conceitual:

```text
APP_NAME
→ obrigatório

ENVIRONMENT
→ default: dev

TaskRun:
APP_NAME=inventory-api
ENVIRONMENT omitido

resultado:
Application: inventory-api
Environment: dev
```

## 04 — Workspaces

### emptyDir básico

```text
Task
→ declara workspace shared-data

TaskRun
→ fornece emptyDir

step-write
→ grava arquivo

step-read
→ lê o mesmo arquivo
```

Como os Steps pertencem ao mesmo Pod, o `emptyDir` pode ser compartilhado entre eles.

### Caminho do workspace

Preferir:

```text
$(workspaces.shared-data.path)
```

em vez de hardcodar:

```text
/workspace/shared-data
```

Exemplo praticado:

```bash
echo 'inventory-api' > $(workspaces.shared-data.path)/app.txt
cat $(workspaces.shared-data.path)/app.txt
```

Substituições em camadas:

```text
$(workspaces.shared-data.path)
→ resolvido pelo Tekton

$(cat arquivo)
→ command substitution resolvido pelo Bash
```

## Limite do emptyDir

```text
Task A
→ TaskRun A
→ Pod A
→ emptyDir A

Task B
→ TaskRun B
→ Pod B
→ emptyDir B
```

`emptyDir A` e `emptyDir B` não são o mesmo filesystem.

Para compartilhar código/artefatos entre Tasks diferentes em uma Pipeline, o próximo passo é usar workspace com storage compartilhado, tipicamente PVC.

## Troubleshooting / inspeção já praticada

```bash
oc get taskrun
oc describe taskrun <nome>
oc get pods --sort-by=.metadata.creationTimestamp
oc describe pod <pod>
oc logs <pod> -c step-<nome>
```

Fluxo mental:

```text
TaskRun falhou
→ describe TaskRun
→ identificar Pod / Step
→ describe Pod
→ logs do step específico
```

## Próximo bloco

```text
Pipeline
→ PipelineRun
→ várias Tasks
→ vários TaskRuns
→ vários Pods
```

Depois:

```text
Pipeline params
→ workspace compartilhado
→ PVC
→ troubleshooting
```
