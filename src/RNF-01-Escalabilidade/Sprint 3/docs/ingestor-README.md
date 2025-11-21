# Ingestor Mock - Documentação

## Visão Geral
O **Ingestor Mock** simula o serviço de ingestão de dados do Miro para o sistema Metro-SP. Ele recebe boards e artefatos, processa-os com latência realista e simula falhas controladas para testes de escalabilidade.

## Dependências

### Instalação
```bash
pip install -r requirements.txt
```

### Dependências Principais
- `fastapi==0.109.0` - Framework web assíncrono
- `uvicorn[standard]==0.27.0` - Servidor ASGI
- `pydantic==2.5.3` - Validação de dados

## Arquitetura do Componente

### Endpoints Disponíveis

#### 1. POST /ingest
**Descrição:** Endpoint principal para ingestão de dados do Miro.

**Request Body:**
```json
{
  "trace_id": "uuid-v4",
  "user_id": "user-123",
  "action": "ingest_board",
  "payload": {
    "board_id": "board-456",
    "content": "...",
    "metadata": {}
  }
}
```

**Response (200 OK):**
```json
{
  "status": "success",
  "message": "Data ingested successfully",
  "data": {
    "event_id": "evt-789",
    "timestamp": "2025-01-01T12:00:00Z"
  }
}
```

**Comportamento Simulado:**
- **Latência:** 50-200ms (simula processamento)
- **Taxa de erro:** 2% (simula falhas aleatórias)
- **Throttling:** 1% (simula limite de taxa)
- **Rastreabilidade:** Todos os eventos incluem `trace_id`

#### 2. GET /health
**Descrição:** Health check do serviço.

**Response (200 OK):**
```json
{
  "status": "healthy",
  "service": "ingestor-mock",
  "version": "1.0.0"
}
```

#### 3. GET /metrics
**Descrição:** Métricas de observabilidade.

**Response (200 OK):**
```json
{
  "total_requests": 1523,
  "successful_requests": 1492,
  "failed_requests": 31,
  "avg_latency_ms": 125.4
}
```

## Execução Local

### Comando Básico
```bash
# Ativar ambiente virtual
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Executar o mock
python -m uvicorn src.mocks.ingestor_mock:app --host 0.0.0.0 --port 8001
```

### Comando com Hot Reload (Desenvolvimento)
```bash
python -m uvicorn src.mocks.ingestor_mock:app --host 0.0.0.0 --port 8001 --reload
```

### Verificação de Health
```bash
# PowerShell
Invoke-RestMethod -Uri "http://localhost:8001/health" -Method Get

# Bash/curl
curl http://localhost:8001/health
```

## Ajuste de Parâmetros de Teste

### 1. Taxa de Erro
Edite `src/mocks/ingestor_mock.py`:
```python
# Linha ~30
if random.random() < 0.02:  # Altere 0.02 para ajustar (2%)
    raise HTTPException(status_code=500, detail="Simulated random error")
```

### 2. Latência
```python
# Linha ~27
processing_time = random.uniform(0.05, 0.2)  # Min: 50ms, Max: 200ms
time.sleep(processing_time)
```

### 3. Throttling
```python
# Linha ~33
if random.random() < 0.01:  # Altere 0.01 para ajustar (1%)
    raise HTTPException(status_code=429, detail="Rate limit exceeded")
```

### 4. Payload Size Máximo
Ajuste no FastAPI:
```python
app = FastAPI(
    title="Ingestor Mock",
    max_request_size=10 * 1024 * 1024  # 10 MB (padrão)
)
```

## Coleta de Artefatos

### Logs Estruturados
Logs são emitidos em formato JSON para facilitar análise:

**Localização:** Stdout do processo (redirecionável)

**Exemplo de Log:**
```json
{
  "timestamp": "2025-01-01T12:00:00.123Z",
  "level": "INFO",
  "trace_id": "abc-123",
  "component": "ingestor-mock",
  "message": "Request processed successfully",
  "latency_ms": 125.4,
  "status": "success"
}
```

**Redirecionar para Arquivo:**
```bash
python -m uvicorn src.mocks.ingestor_mock:app --port 8001 > logs/ingestor.log 2>&1
```

### Métricas (CSV/JSON)
As métricas podem ser coletadas via endpoint `/metrics`:

```bash
# Coletar métricas periodicamente
while true; do
  curl -s http://localhost:8001/metrics >> metrics/ingestor_metrics.json
  echo "" >> metrics/ingestor_metrics.json
  sleep 10
done
```

## Interpretação de Artefatos

### Análise de Logs
```python
import json

# Carregar logs
with open('logs/ingestor.log', 'r') as f:
    logs = [json.loads(line) for line in f if line.strip()]

# Calcular estatísticas
latencies = [log['latency_ms'] for log in logs if 'latency_ms' in log]
success_rate = sum(1 for log in logs if log.get('status') == 'success') / len(logs) * 100

print(f"P95 Latency: {sorted(latencies)[int(len(latencies) * 0.95)]:.2f} ms")
print(f"Success Rate: {success_rate:.2f}%")
```

### Análise de Métricas
```python
import json

with open('metrics/ingestor_metrics.json', 'r') as f:
    metrics = [json.loads(line) for line in f if line.strip()]

final_metrics = metrics[-1]
print(f"Total Requests: {final_metrics['total_requests']}")
print(f"Error Rate: {final_metrics['failed_requests'] / final_metrics['total_requests'] * 100:.2f}%")
```

## Testes de Carga

### Comando Locust Recomendado
```bash
# Teste básico (150 usuários, ramp-up 10/s, duração 10 min)
locust -f tests/locust/locustfile_ingestor.py \
    --headless \
    -u 150 \
    -r 10 \
    -t 10m \
    --csv=results/ingestor_run \
    --host=http://localhost:8001
```

### Parâmetros Ajustáveis
- `-u`: Número total de usuários simultâneos
- `-r`: Taxa de ramp-up (usuários/segundo)
- `-t`: Duração do teste (ex: 10m, 1h, 300s)
- `--csv`: Prefixo para arquivos CSV de resultado

### Cenários de Teste por Carga

#### Teste de Baseline (Carga Normal)
```bash
locust -f tests/locust/locustfile_ingestor.py --headless -u 50 -r 5 -t 5m --csv=results/baseline
```

#### Teste de Pico (1000 requisições)
```bash
locust -f tests/locust/locustfile_ingestor.py --headless -u 200 -r 20 -t 10m --csv=results/peak
```

#### Teste de Estresse (Sobrecarga)
```bash
locust -f tests/locust/locustfile_ingestor.py --headless -u 500 -r 50 -t 15m --csv=results/stress
```

## Troubleshooting

### Problema: Porta 8001 já em uso
```bash
# Windows - Encontrar processo
netstat -ano | findstr :8001
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:8001 | xargs kill -9
```

### Problema: Import errors
```bash
# Garantir que PYTHONPATH inclui o diretório raiz
export PYTHONPATH="${PYTHONPATH}:$(pwd)"  # Linux/Mac
$env:PYTHONPATH = "$(pwd)"  # PowerShell
```

### Problema: High error rate durante testes
- **Causa Provável:** Configuração de taxa de erro muito alta
- **Solução:** Ajustar parâmetro de erro em `ingestor_mock.py` (reduzir de 0.02 para 0.005)

### Problema: Latência muito alta (> 1s)
- **Causa Provável:** Recursos limitados (CPU/memória)
- **Solução:** Reduzir número de usuários simultâneos ou aumentar recursos da máquina

## Critérios de Aceitação (SLOs)

De acordo com a especificação RNF-01:

| Métrica | Limite | Como Medir |
|---------|--------|------------|
| Taxa de Sucesso | ≥ 99.5% | `(successful_requests / total_requests) * 100` |
| Latência P95 | < 800 ms | Percentil 95 dos tempos de resposta |
| Latência P99 | < 1.5 s | Percentil 99 dos tempos de resposta |
| Taxa de Erro | < 1% | `(failed_requests / total_requests) * 100` |
| Rastreabilidade | 100% | Todos os logs devem conter `trace_id` |

### Validação Automatizada
```bash
# Executar testes unitários
pytest tests/unit/test_ingestor.py -v

# Validar SLOs após teste de carga
python scripts/validate_slos.py --results results/ingestor_run_stats.csv
```

## Referências
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Locust Documentation](https://docs.locust.io/)
- [Especificação RNF-01](../../documentos/Projeto.md#81-rnf-02-escalabilidade)
