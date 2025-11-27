# Audit Mock - Documentação

## Visão Geral
O **Audit Mock** simula o serviço de auditoria e logging estruturado do sistema Metro-SP. Ele registra eventos críticos para rastreabilidade, compliance e análise forense, suportando consultas por `trace_id`.

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

#### 1. POST /log
**Descrição:** Endpoint para ingestão de eventos de auditoria.

**Request Body:**
```json
{
  "trace_id": "uuid-v4",
  "event_type": "document_upload",
  "resource": "file-456",
  "action": "CREATE",
  "user_id": "user-123",
  "status": "success",
  "metadata": {
    "file_name": "project_plan.docx",
    "file_size": 245760
  }
}
```

**Response (200 OK):**
```json
{
  "status": "success",
  "message": "Audit log recorded",
  "data": {
    "log_id": "log-789",
    "timestamp": "2025-01-01T12:00:00.123456Z"
  }
}
```

**Comportamento Simulado:**
- **Latência:** 10-50ms (ingestão rápida, escrita em memória)
- **Taxa de erro:** 0.5% (serviço crítico, alta confiabilidade)
- **Armazenamento:** In-memory (para testes; produção usaria DB)

#### 2. GET /logs/{trace_id}
**Descrição:** Recupera todos os eventos de auditoria associados a um `trace_id`.

**Response (200 OK):**
```json
{
  "trace_id": "abc-123",
  "events": [
    {
      "log_id": "log-789",
      "timestamp": "2025-01-01T12:00:00.123456Z",
      "event_type": "authentication",
      "action": "LOGIN",
      "status": "success"
    },
    {
      "log_id": "log-790",
      "timestamp": "2025-01-01T12:00:05.456789Z",
      "event_type": "document_upload",
      "action": "CREATE",
      "status": "success"
    }
  ],
  "total_events": 2
}
```

#### 3. GET /health
**Descrição:** Health check do serviço.

#### 4. GET /metrics
**Descrição:** Métricas de observabilidade.

## Execução Local

### Comando Básico
```bash
python -m uvicorn src.mocks.audit_mock:app --host 0.0.0.0 --port 8004
```

### Teste Manual de Logging
```powershell
# PowerShell - Registrar evento de auditoria
$body = @{
    trace_id = "test-trace-001"
    event_type = "test_event"
    resource = "test-resource"
    action = "TEST"
    user_id = "user-test"
    status = "success"
    metadata = @{
        test_key = "test_value"
    }
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8004/log" `
    -Method Post `
    -Body $body `
    -ContentType "application/json"
```

### Consultar Logs por trace_id
```powershell
Invoke-RestMethod -Uri "http://localhost:8004/logs/test-trace-001" -Method Get
```

## Ajuste de Parâmetros de Teste

### 1. Latência de Ingestão
```python
# src/mocks/audit_mock.py - Linha ~20
processing_time = random.uniform(0.01, 0.05)  # 10-50ms (muito rápido)
time.sleep(processing_time)
```

Para simular logging distribuído (ex: Elasticsearch):
```python
processing_time = random.uniform(0.05, 0.15)  # 50-150ms
```

### 2. Taxa de Perda de Eventos
```python
# Linha ~23 - Simular perda de eventos (não recomendado para auditoria!)
EVENT_LOSS_RATE = 0.0001  # 0.01% (extremamente baixo)

if random.random() < EVENT_LOSS_RATE:
    logger.error(f"Simulated event loss for trace_id {request.trace_id}")
    raise HTTPException(status_code=500, detail="Event lost")
```

**CRÍTICO:** Para auditoria, taxa de perda deve ser 0% em produção!

### 3. Indexação de trace_id
```python
# Armazenamento em memória otimizado para busca
from collections import defaultdict

audit_logs_by_trace = defaultdict(list)

@app.post("/log")
async def log_event(request: AuditLog):
    # Indexar por trace_id para busca O(1)
    audit_logs_by_trace[request.trace_id].append(request.dict())
    return {"status": "success", "log_id": f"log-{uuid.uuid4()}"}

@app.get("/logs/{trace_id}")
async def get_logs(trace_id: str):
    events = audit_logs_by_trace.get(trace_id, [])
    return {"trace_id": trace_id, "events": events, "total_events": len(events)}
```

### 4. Retenção de Logs
```python
# Limpar logs antigos (em produção, usar TTL de DB)
import time
from datetime import datetime, timedelta

LOG_RETENTION_HOURS = 24

def cleanup_old_logs():
    cutoff_time = datetime.now() - timedelta(hours=LOG_RETENTION_HOURS)
    # Implementar lógica de limpeza
    ...
```

## Coleta de Artefatos

### Logs de Auditoria
```json
{
  "timestamp": "2025-01-01T12:00:00.123456Z",
  "level": "INFO",
  "trace_id": "abc-123",
  "component": "audit-mock",
  "event_type": "document_upload",
  "resource": "file-456",
  "action": "CREATE",
  "user_id": "user-123",
  "status": "success",
  "latency_ms": 23.4
}
```

### Exportar Logs para Análise
```bash
# Exportar todos os logs de um trace_id específico
curl http://localhost:8004/logs/abc-123 | jq . > audit_trace_abc-123.json

# Exportar métricas agregadas
curl http://localhost:8004/metrics | jq . > audit_metrics.json
```

## Interpretação de Artefatos

### Análise de Rastreabilidade
```python
import json

with open('logs/audit.log', 'r') as f:
    logs = [json.loads(line) for line in f if line.strip()]

# Verificar cobertura de trace_id
total_events = len(logs)
events_with_trace_id = len([log for log in logs if 'trace_id' in log and log['trace_id']])

trace_id_coverage = events_with_trace_id / total_events * 100
print(f"Trace ID Coverage: {trace_id_coverage:.2f}%")
print(f"SLO: 100% (CRÍTICO para rastreabilidade)")

# Critério: 100% dos eventos devem ter trace_id
assert trace_id_coverage == 100, "FAILED: Missing trace_id in audit logs!"
```

### Análise de Perda de Eventos
```python
# Comparar eventos enviados vs eventos registrados
from collections import Counter

# Assumindo que temos logs de envio e recebimento
sent_trace_ids = set(...)  # trace_ids enviados
received_trace_ids = set([log['trace_id'] for log in logs])

lost_events = sent_trace_ids - received_trace_ids
loss_rate = len(lost_events) / len(sent_trace_ids) * 100

print(f"Event Loss Rate: {loss_rate:.3f}%")
print(f"SLO: 0% (ZERO perda permitida)")

if lost_events:
    print(f"Lost trace_ids: {list(lost_events)[:10]}")  # Primeiros 10
```

### Análise de Latência de Consulta
```python
import requests
import time

trace_ids = ["trace-1", "trace-2", "trace-3"]  # Amostra
query_latencies = []

for trace_id in trace_ids:
    start = time.time()
    response = requests.get(f"http://localhost:8004/logs/{trace_id}")
    latency = (time.time() - start) * 1000  # ms
    query_latencies.append(latency)

avg_query_latency = sum(query_latencies) / len(query_latencies)
p95_query_latency = sorted(query_latencies)[int(len(query_latencies) * 0.95)]

print(f"Avg Query Latency: {avg_query_latency:.2f} ms")
print(f"P95 Query Latency: {p95_query_latency:.2f} ms")
print(f"SLO: P95 < 150 ms")
```

## Testes de Carga

### Cenário: Burst de Eventos (10k eventos/s)
```bash
locust -f tests/locust/locustfile_audit.py \
    --headless \
    -u 1000 \
    -r 100 \
    -t 2m \
    --csv=results/audit_burst \
    --host=http://localhost:8004
```

**Análise de Resultados:**
```bash
# Verificar se sistema conseguiu processar 10k req/s
awk -F',' 'NR>1 {sum+=$10} END {print "Avg RPS:", sum/NR}' results/audit_burst_stats.csv
```

### Cenário: Consultas Concorrentes
```python
# Editar locustfile_audit.py - adicionar task de consulta
@task(5)  # 5x mais consultas que ingestão
def query_logs(self):
    trace_id = f"trace-{random.randint(1, 1000)}"
    self.client.get(f"/logs/{trace_id}")
```

```bash
locust -f tests/locust/locustfile_audit.py \
    --headless \
    -u 500 \
    -r 50 \
    -t 10m \
    --csv=results/audit_queries \
    --host=http://localhost:8004
```

### Cenário: Retenção de Longa Duração
```bash
# Ingestão contínua por 1 hora para testar memória
locust -f tests/locust/locustfile_audit.py \
    --headless \
    -u 100 \
    -r 10 \
    -t 1h \
    --csv=results/audit_retention \
    --host=http://localhost:8004
```

**Monitorar Uso de Memória:**
```powershell
# PowerShell - Monitorar processo uvicorn
while ($true) {
    $process = Get-Process | Where-Object {$_.ProcessName -like "*python*"}
    $memoryMB = [math]::Round($process.WorkingSet64 / 1MB, 2)
    Write-Host "$(Get-Date -Format 'HH:mm:ss') - Memory: $memoryMB MB"
    Start-Sleep -Seconds 10
}
```

## Troubleshooting

### Problema: Perda de eventos durante burst
**Diagnóstico:**
```bash
# Comparar total de requisições enviadas vs recebidas
sent=$(grep "POST /log" logs/access.log | wc -l)
received=$(curl http://localhost:8004/metrics | jq '.total_requests')
echo "Loss: $(($sent - $received)) events"
```

**Soluções:**
1. Aumentar workers do uvicorn:
   ```bash
   uvicorn src.mocks.audit_mock:app --workers 4 --port 8004
   ```

2. Implementar fila de buffer:
   ```python
   import asyncio
   from asyncio import Queue
   
   event_queue = Queue(maxsize=10000)
   
   @app.post("/log")
   async def log_event(request: AuditLog):
       await event_queue.put(request)
       return {"status": "queued"}
   
   # Background worker para processar fila
   async def process_queue():
       while True:
           event = await event_queue.get()
           # Processar evento
           ...
   ```

### Problema: Latência de consulta alta (> 200ms)
**Diagnóstico:**
```python
# Verificar tamanho do dataset
total_events = sum(len(events) for events in audit_logs_by_trace.values())
print(f"Total events in memory: {total_events}")
```

**Soluções:**
1. Implementar paginação:
   ```python
   @app.get("/logs/{trace_id}")
   async def get_logs(trace_id: str, page: int = 1, page_size: int = 100):
       events = audit_logs_by_trace.get(trace_id, [])
       start = (page - 1) * page_size
       end = start + page_size
       return {
           "trace_id": trace_id,
           "events": events[start:end],
           "total_events": len(events),
           "page": page,
           "page_size": page_size
       }
   ```

2. Usar indexação eficiente (produção: Elasticsearch)

### Problema: Uso excessivo de memória
**Causa:** Armazenamento in-memory sem limite

**Solução:**
```python
from collections import OrderedDict

class LRUCache(OrderedDict):
    def __init__(self, maxsize=10000):
        super().__init__()
        self.maxsize = maxsize
    
    def __setitem__(self, key, value):
        if key in self:
            self.move_to_end(key)
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]

audit_logs_by_trace = LRUCache(maxsize=10000)
```

## Critérios de Aceitação (SLOs)

| Métrica | Limite | Validação |
|---------|--------|-----------|
| **Rastreabilidade** | **100%** | **Todos os eventos DEVEM ter trace_id válido** |
| Taxa de Perda de Eventos | **0%** | **ZERO perdas permitidas** |
| Latência P95 Ingest | < 150 ms | Percentil 95 de ingestão |
| Latência P95 Query | < 200 ms | Percentil 95 de consulta por trace_id |
| Throughput Mínimo | ≥ 10k eventos/s | Durante burst de 2 minutos |
| Integridade de Dados | 100% | Eventos devem ser imutáveis |

### Validação de Rastreabilidade (CRÍTICO)
```python
def validate_traceability(log_file):
    """Validação obrigatória de rastreabilidade."""
    with open(log_file, 'r') as f:
        logs = [json.loads(line) for line in f if line.strip()]
    
    # Verificar presença de trace_id
    missing_trace_id = [log for log in logs if not log.get('trace_id')]
    
    if missing_trace_id:
        print(f"CRITICAL: {len(missing_trace_id)} events without trace_id!")
        for log in missing_trace_id[:10]:
            print(f"  - {log.get('log_id', 'unknown')} at {log.get('timestamp')}")
        return False
    
    # Verificar formato de trace_id (UUID v4)
    import re
    uuid_pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$', re.I)
    invalid_trace_ids = [log for log in logs if not uuid_pattern.match(log['trace_id'])]
    
    if invalid_trace_ids:
        print(f"WARNING: {len(invalid_trace_ids)} invalid trace_id formats")
        return False
    
    print(f"✓ Traceability validated: {len(logs)} events, all with valid trace_id")
    return True

# Executar após cada teste
assert validate_traceability('logs/audit.log'), "Traceability check FAILED"
```

### Validação de Perda de Eventos
```python
def validate_no_loss(sent_events, received_metrics):
    """Validação de ZERO perda de eventos."""
    loss = sent_events - received_metrics['total_requests']
    
    if loss > 0:
        print(f"CRITICAL: {loss} events lost!")
        loss_rate = loss / sent_events * 100
        print(f"Loss rate: {loss_rate:.3f}%")
        return False
    
    print(f"✓ No event loss: {sent_events} sent, {received_metrics['total_requests']} received")
    return True
```

## Compliance e Auditoria

### Requerimentos de Compliance
Para ambientes regulados (LGPD, SOC2, etc.):

1. **Imutabilidade:** Eventos de auditoria não podem ser modificados/deletados
2. **Integridade:** Usar assinaturas digitais para provar não-repúdio
3. **Retenção:** Manter logs por período mínimo (ex: 7 anos)
4. **Acesso Controlado:** Logs de auditoria são sensíveis (RBAC rigoroso)

### Implementação de Assinatura Digital
```python
import hmac
import hashlib

SECRET_KEY = "audit-secret-key-change-in-production"

def sign_event(event_data: dict) -> str:
    """Assina evento de auditoria para garantir integridade."""
    message = json.dumps(event_data, sort_keys=True).encode()
    signature = hmac.new(SECRET_KEY.encode(), message, hashlib.sha256).hexdigest()
    return signature

@app.post("/log")
async def log_event(request: AuditLog):
    event_dict = request.dict()
    event_dict['signature'] = sign_event(event_dict)
    audit_logs.append(event_dict)
    return {"status": "success", "log_id": event_dict['log_id']}
```

## Referências
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- [LGPD - Lei Geral de Proteção de Dados](https://www.gov.br/esporte/pt-br/acesso-a-informacao/lgpd)
- [Especificação RNF-01](../../documentos/Projeto.md#821-definição-do-cenário)
