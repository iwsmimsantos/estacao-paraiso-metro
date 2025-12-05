# Orchestrator Mock - Documentação

## Visão Geral
O **Orchestrator Mock** simula o serviço de orquestração de agentes de IA do sistema Metro-SP. Ele processa workflows que envolvem múltiplas chamadas a modelos de IA, simulando latência de inferência e controle de concorrência.

## Dependências

### Instalação
```bash
pip install -r requirements.txt
```

### Dependências Principais
- `fastapi==0.109.0`
- `uvicorn[standard]==0.27.0`
- `pydantic==2.5.3`

## Arquitetura do Componente

### Endpoints Disponíveis

#### 1. POST /orchestrate
**Descrição:** Endpoint para orquestração de workflows de IA.

**Request Body:**
```json
{
  "trace_id": "uuid-v4",
  "user_id": "user-123",
  "action": "process_workflow",
  "payload": {
    "workflow_id": "wf-789",
    "model": "gpt-4",
    "prompt": "Analyze project data...",
    "parameters": {}
  }
}
```

**Response (200 OK):**
```json
{
  "status": "success",
  "message": "Workflow orchestrated successfully",
  "data": {
    "task_id": "task-456",
    "model_version": "gpt-4-0613",
    "timestamp": "2025-01-01T12:00:00Z",
    "estimated_completion": "2025-01-01T12:00:30Z"
  }
}
```

**Comportamento Simulado:**
- **Latência:** 100-500ms (simula processamento de IA mais complexo)
- **Taxa de erro:** 3% (maior que ingestor devido à complexidade)
- **Throttling:** 2% (controle de rate limiting de APIs de IA)
- **Versionamento:** Registra versão do modelo usado

#### 2. GET /health
**Descrição:** Health check do serviço.

#### 3. GET /metrics
**Descrição:** Métricas de observabilidade.

## Execução Local

### Comando Básico
```bash
python -m uvicorn src.mocks.orchestrator_mock:app --host 0.0.0.0 --port 8002
```

### Verificação de Health
```bash
# PowerShell
Invoke-RestMethod -Uri "http://localhost:8002/health" -Method Get

# Bash
curl http://localhost:8002/health
```

### Teste Manual de Orquestração
```powershell
# PowerShell
$body = @{
    trace_id = "test-trace-001"
    user_id = "user-test"
    action = "process_workflow"
    payload = @{
        workflow_id = "wf-123"
        model = "gpt-4"
        prompt = "Test prompt"
    }
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8002/orchestrate" `
    -Method Post `
    -Body $body `
    -ContentType "application/json"
```

## Ajuste de Parâmetros de Teste

### 1. Latência de Processamento IA
Edite `src/mocks/orchestrator_mock.py`:
```python
# Linha ~27 - Ajustar range de latência
processing_time = random.uniform(0.1, 0.5)  # 100-500ms
time.sleep(processing_time)
```

Para simular modelos mais rápidos (ex: Claude Haiku):
```python
processing_time = random.uniform(0.05, 0.15)  # 50-150ms
```

Para simular modelos mais lentos (ex: GPT-4 Vision):
```python
processing_time = random.uniform(0.5, 2.0)  # 500-2000ms
```

### 2. Taxa de Erro
```python
# Linha ~30
if random.random() < 0.03:  # Altere para 0.01 (1%) ou 0.05 (5%)
    raise HTTPException(status_code=500, detail="IA model error")
```

### 3. Controle de Concorrência
Para simular limite de workers de IA:
```python
# Adicionar semáforo (exemplo)
from asyncio import Semaphore

MAX_CONCURRENT_TASKS = 10
task_semaphore = Semaphore(MAX_CONCURRENT_TASKS)

@app.post("/orchestrate")
async def orchestrate(request: TransactionRequest):
    async with task_semaphore:
        # Processar workflow
        ...
```

### 4. Versão do Modelo
```python
# Linha ~40 - Simular diferentes versões
model_versions = {
    "gpt-4": "gpt-4-0613",
    "gpt-3.5": "gpt-3.5-turbo-0125",
    "claude": "claude-3-opus-20240229"
}
model_version = model_versions.get(request.payload.get("model"), "unknown")
```

## Coleta de Artefatos

### Logs de Workflow
Logs incluem metadados específicos de IA:

```json
{
  "timestamp": "2025-01-01T12:00:00.123Z",
  "level": "INFO",
  "trace_id": "abc-123",
  "component": "orchestrator-mock",
  "workflow_id": "wf-789",
  "model": "gpt-4",
  "model_version": "gpt-4-0613",
  "latency_ms": 325.7,
  "status": "success"
}
```

### Métricas de IA
```bash
# Coletar métricas específicas de IA
curl http://localhost:8002/metrics | jq '{
  total_workflows: .total_requests,
  avg_inference_time: .avg_latency_ms,
  model_errors: .failed_requests
}'
```

## Interpretação de Artefatos

### Análise de Performance por Modelo
```python
import json
from collections import defaultdict

with open('logs/orchestrator.log', 'r') as f:
    logs = [json.loads(line) for line in f if line.strip()]

# Agrupar por modelo
model_latencies = defaultdict(list)
for log in logs:
    if 'model' in log and 'latency_ms' in log:
        model_latencies[log['model']].append(log['latency_ms'])

# Estatísticas por modelo
for model, latencies in model_latencies.items():
    p95 = sorted(latencies)[int(len(latencies) * 0.95)]
    avg = sum(latencies) / len(latencies)
    print(f"{model}: P95={p95:.2f}ms, Avg={avg:.2f}ms")
```

### Análise de Taxa de Erro por Workflow
```python
from collections import Counter

workflow_status = Counter()
for log in logs:
    if 'workflow_id' in log:
        workflow_status[log['status']] += 1

error_rate = workflow_status['error'] / sum(workflow_status.values()) * 100
print(f"Workflow Error Rate: {error_rate:.2f}%")
```

## Testes de Carga

### Cenário: Concorrência de Workflows (200 Paralelos)
```bash
locust -f tests/locust/locustfile_orchestrator.py \
    --headless \
    -u 200 \
    -r 20 \
    -t 15m \
    --csv=results/orchestrator_concurrency \
    --host=http://localhost:8002
```

### Cenário: Stress Test de Modelos IA
```bash
# 500 workflows simultâneos (acima da capacidade)
locust -f tests/locust/locustfile_orchestrator.py \
    --headless \
    -u 500 \
    -r 50 \
    -t 10m \
    --csv=results/orchestrator_stress \
    --host=http://localhost:8002
```

### Cenário: Soak Test (Estabilidade)
```bash
# Carga moderada por período prolongado (2 horas)
locust -f tests/locust/locustfile_orchestrator.py \
    --headless \
    -u 100 \
    -r 10 \
    -t 2h \
    --csv=results/orchestrator_soak \
    --host=http://localhost:8002
```

## Troubleshooting

### Problema: Alta taxa de falha (> 5%)
**Diagnóstico:**
```bash
# Verificar logs de erro
grep '"level":"ERROR"' logs/orchestrator.log | tail -20
```

**Soluções:**
1. Reduzir taxa de erro simulada no código
2. Aumentar timeout de requisições no Locust
3. Verificar recursos do sistema (CPU/memória)

### Problema: Latência P95 > 600ms
**Diagnóstico:**
```python
# Analisar distribuição de latências
import json
import matplotlib.pyplot as plt

with open('logs/orchestrator.log', 'r') as f:
    latencies = [json.loads(line)['latency_ms'] for line in f if 'latency_ms' in line]

plt.hist(latencies, bins=50)
plt.xlabel('Latency (ms)')
plt.ylabel('Frequency')
plt.title('Orchestrator Latency Distribution')
plt.show()
```

**Soluções:**
1. Ajustar range de latência no mock (reduzir máximo)
2. Verificar se há contenção de recursos
3. Implementar caching de resultados de IA (se aplicável)

### Problema: Deadlock ou travamento
**Causa Provável:** Limite de concorrência muito restritivo

**Solução:**
```python
# Aumentar limite de workers uvicorn
uvicorn src.mocks.orchestrator_mock:app --workers 4 --port 8002
```

## Critérios de Aceitação (SLOs)

| Métrica | Limite | Validação |
|---------|--------|-----------|
| Taxa de Sucesso | ≥ 99.0% | Tolerância menor devido à complexidade de IA |
| Latência P95 (chamada IA) | < 600 ms | Percentil 95 |
| Latência P99 (chamada IA) | < 1.2 s | Percentil 99 |
| Taxa de Erro por Sessão | < 2% | Erros por workflow completo |
| Versionamento | 100% | Todos os logs devem incluir `model_version` |

### Validação de Versionamento
```bash
# Verificar se todos os logs têm model_version
grep -c '"model_version"' logs/orchestrator.log
# Deve ser igual ao total de requisições bem-sucedidas
```

## Simulação de Comportamento Real

### Rate Limiting de API Externa
Para simular throttling de APIs como OpenAI:

```python
import time
from collections import deque

class RateLimiter:
    def __init__(self, max_requests_per_minute=60):
        self.max_requests = max_requests_per_minute
        self.requests = deque()
    
    async def acquire(self):
        now = time.time()
        # Remove requisições antigas (> 1 minuto)
        while self.requests and self.requests[0] < now - 60:
            self.requests.popleft()
        
        if len(self.requests) >= self.max_requests:
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        
        self.requests.append(now)

rate_limiter = RateLimiter(max_requests_per_minute=100)

@app.post("/orchestrate")
async def orchestrate(request: TransactionRequest):
    await rate_limiter.acquire()
    # ... resto do código
```

### Determinismo em Modelos
Para testes que exigem resultados reproduzíveis:

```python
import hashlib

def deterministic_response(prompt: str, seed: int = 42):
    """Gera resposta determinística baseada no prompt."""
    hash_input = f"{prompt}{seed}".encode()
    hash_hex = hashlib.sha256(hash_input).hexdigest()
    return f"Generated response (hash: {hash_hex[:8]})"
```

## Referências
- [FastAPI Concurrency](https://fastapi.tiangolo.com/async/)
- [OpenAI Rate Limits](https://platform.openai.com/docs/guides/rate-limits)
- [Especificação RNF-01](../../documentos/Projeto.md#821-definição-do-cenário)
