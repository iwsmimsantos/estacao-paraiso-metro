# SharePoint Mock - Documentação

## Visão Geral
O **SharePoint Mock** simula o serviço de upload e sincronização de artefatos para SharePoint Online do Metro-SP. Implementa verificação de integridade via hash, throttling realista e simulação de falhas de rede.

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

#### 1. POST /upload
**Descrição:** Endpoint para upload de artefatos.

**Request Body:**
```json
{
  "trace_id": "uuid-v4",
  "user_id": "user-123",
  "action": "upload_document",
  "payload": {
    "file_name": "project_plan.docx",
    "file_content": "base64_encoded_content",
    "file_hash": "sha256_hash",
    "metadata": {
      "project_id": "proj-789",
      "version": "1.2"
    }
  }
}
```

**Response (200 OK):**
```json
{
  "status": "success",
  "message": "File uploaded successfully",
  "data": {
    "file_id": "file-456",
    "url": "https://sharepoint.com/sites/metro/file-456",
    "hash_verified": true,
    "timestamp": "2025-01-01T12:00:00Z"
  }
}
```

**Comportamento Simulado:**
- **Latência:** 100-300ms (upload de rede)
- **Taxa de erro:** 2% (falhas de rede/permissão)
- **Throttling:** 5% (SharePoint tem limites agressivos)
- **Verificação de Hash:** Compara hash recebido com hash calculado

#### 2. GET /health
**Descrição:** Health check do serviço.

#### 3. GET /metrics
**Descrição:** Métricas de observabilidade.

## Execução Local

### Comando Básico
```bash
python -m uvicorn src.mocks.sharepoint_mock:app --host 0.0.0.0 --port 8003
```

### Verificação de Upload
```powershell
# PowerShell - Upload de teste
$content = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes("Test file content"))
$hash = (Get-FileHash -InputStream ([System.IO.MemoryStream]::new([System.Text.Encoding]::UTF8.GetBytes("Test file content"))) -Algorithm SHA256).Hash

$body = @{
    trace_id = "test-trace-001"
    user_id = "user-test"
    action = "upload_document"
    payload = @{
        file_name = "test.txt"
        file_content = $content
        file_hash = $hash
    }
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8003/upload" `
    -Method Post `
    -Body $body `
    -ContentType "application/json"
```

## Ajuste de Parâmetros de Teste

### 1. Throttling (Limites de Taxa)
SharePoint Online tem limites agressivos. Ajuste a simulação:

```python
# src/mocks/sharepoint_mock.py - Linha ~30
if random.random() < 0.05:  # 5% de throttling (realista)
    raise HTTPException(status_code=429, detail="SharePoint throttling")
```

Para testes mais agressivos:
```python
if random.random() < 0.15:  # 15% (sobrecarga extrema)
```

### 2. Latência de Upload
```python
# Linha ~27
processing_time = random.uniform(0.1, 0.3)  # 100-300ms

# Para arquivos grandes, aumentar latência
file_size_mb = len(request.payload.get("file_content", "")) / (1024 * 1024)
processing_time = 0.1 + (file_size_mb * 0.05)  # +50ms por MB
```

### 3. Verificação de Hash
```python
# Linha ~35 - Controlar taxa de falha de integridade
HASH_MISMATCH_RATE = 0.001  # 0.1% de corrupção

if random.random() < HASH_MISMATCH_RATE:
    # Simular corrupção de dados
    calculated_hash = "corrupted_hash"
```

### 4. Permissões Negadas
```python
# Simular falha de autorização
PERMISSION_DENIED_RATE = 0.02  # 2%

if random.random() < PERMISSION_DENIED_RATE:
    raise HTTPException(status_code=403, detail="Insufficient permissions")
```

## Coleta de Artefatos

### Logs de Upload
```json
{
  "timestamp": "2025-01-01T12:00:00.123Z",
  "level": "INFO",
  "trace_id": "abc-123",
  "component": "sharepoint-mock",
  "file_name": "project_plan.docx",
  "file_size_bytes": 245760,
  "hash_verified": true,
  "latency_ms": 287.3,
  "status": "success"
}
```

### Verificação de Integridade
Todos os uploads registram verificação de hash:

```bash
# Extrair eventos de verificação de hash
grep '"hash_verified"' logs/sharepoint.log | jq '{
  file_name: .file_name,
  hash_verified: .hash_verified,
  file_size: .file_size_bytes
}'
```

## Interpretação de Artefatos

### Análise de Integridade de Dados
```python
import json

with open('logs/sharepoint.log', 'r') as f:
    logs = [json.loads(line) for line in f if line.strip()]

# Verificar corrupções
total_uploads = len([log for log in logs if 'hash_verified' in log])
corrupted = len([log for log in logs if log.get('hash_verified') == False])

corruption_rate = (corrupted / total_uploads * 100) if total_uploads > 0 else 0
print(f"Total Uploads: {total_uploads}")
print(f"Corrupted Files: {corrupted}")
print(f"Corruption Rate: {corruption_rate:.3f}% (SLO: 0%)")

# Critério: ZERO corrupções permitidas
assert corruption_rate == 0, "FAILED: Data corruption detected!"
```

### Análise de Throttling
```python
# Extrair eventos de throttling
throttled = len([log for log in logs if log.get('status_code') == 429])
throttle_rate = throttled / len(logs) * 100

print(f"Throttle Rate: {throttle_rate:.2f}%")
print(f"Expected: ~5% (simulated SharePoint behavior)")
```

### Análise de Retry Bem-Sucedidos
```python
# Verificar se retries funcionaram
retry_logs = [log for log in logs if 'retry_attempt' in log]
successful_retries = [log for log in retry_logs if log.get('status') == 'success']

print(f"Total Retries: {len(retry_logs)}")
print(f"Successful Retries: {len(successful_retries)}")
print(f"Retry Success Rate: {len(successful_retries) / len(retry_logs) * 100:.2f}%")
```

## Testes de Carga

### Cenário: Upload Concomitante (500 Simultâneos)
```bash
locust -f tests/locust/locustfile_sharepoint.py \
    --headless \
    -u 500 \
    -r 50 \
    -t 15m \
    --csv=results/sharepoint_concurrent \
    --host=http://localhost:8003
```

### Cenário: Arquivos Grandes
Para testar uploads de arquivos de 1-10 MB:

```python
# Editar tests/locust/locustfile_sharepoint.py
def generate_file_content(size_mb=5):
    """Gera conteúdo de arquivo com tamanho especificado."""
    size_bytes = size_mb * 1024 * 1024
    return "A" * size_bytes  # Conteúdo simples

# No task do Locust
file_content = generate_file_content(size_mb=random.randint(1, 10))
```

```bash
locust -f tests/locust/locustfile_sharepoint.py \
    --headless \
    -u 100 \
    -r 10 \
    -t 20m \
    --csv=results/sharepoint_large_files \
    --host=http://localhost:8003
```

### Cenário: Rede Degradada
Simular latência de rede com `tc` (Linux) ou script de delay:

```bash
# Linux - Adicionar delay de 100ms
sudo tc qdisc add dev lo root netem delay 100ms

# Executar teste
locust -f tests/locust/locustfile_sharepoint.py \
    --headless -u 200 -r 20 -t 10m \
    --csv=results/sharepoint_degraded_network

# Remover delay após teste
sudo tc qdisc del dev lo root
```

Windows (via script):
```bash
# Usar scripts/chaos/toggle_network_delay.sh adaptado para Windows
./scripts/chaos/toggle_network_delay.sh enable 8003 100ms
```

## Troubleshooting

### Problema: Alta taxa de throttling (> 10%)
**Diagnóstico:**
```bash
grep '"status_code":429' logs/sharepoint.log | wc -l
```

**Solução:**
- Reduzir taxa de usuários simultâneos
- Implementar backoff exponencial nos clientes
- Ajustar THROTTLING_RATE no código do mock

### Problema: Verificação de hash falhando
**Diagnóstico:**
```bash
grep '"hash_verified":false' logs/sharepoint.log
```

**Causa Provável:**
1. Hash calculado incorretamente no cliente
2. Encoding de Base64 inconsistente
3. Corrupção simulada muito alta

**Solução:**
```python
# Validar hash no cliente antes de enviar
import hashlib
import base64

content = b"Test file content"
file_hash = hashlib.sha256(content).hexdigest()
file_content_b64 = base64.b64encode(content).decode()

# Enviar ambos para verificação
payload = {
    "file_content": file_content_b64,
    "file_hash": file_hash
}
```

### Problema: Timeout em uploads grandes
**Solução:**
```bash
# Aumentar timeout do uvicorn
uvicorn src.mocks.sharepoint_mock:app --timeout-keep-alive 300 --port 8003
```

## Critérios de Aceitação (SLOs)

| Métrica | Limite | Validação |
|---------|--------|-----------|
| Taxa de Sucesso (upload) | ≥ 99.5% | Excluindo 429 (throttling) |
| Latência P95 (≤ 5 MB) | < 2 s | Percentil 95 |
| Taxa de Erro | < 1% | Erros 4xx/5xx exceto 429 |
| **Integridade (Hash)** | **100%** | **ZERO corrupções permitidas** |
| Retries Bem-Sucedidos | ≥ 95% | Dentro de 5 minutos |

### Validação de Integridade (Crítico)
```python
# Script de validação obrigatório
def validate_integrity(log_file):
    with open(log_file, 'r') as f:
        logs = [json.loads(line) for line in f if 'hash_verified' in line]
    
    corrupted = [log for log in logs if not log['hash_verified']]
    
    if corrupted:
        print(f"CRITICAL: {len(corrupted)} corrupted files detected!")
        for log in corrupted:
            print(f"  - {log['file_name']} at {log['timestamp']}")
        return False
    
    print(f"✓ Integrity validated: {len(logs)} uploads, 0 corruptions")
    return True

# Executar após testes
assert validate_integrity('logs/sharepoint.log'), "Integrity check FAILED"
```

## Simulação de Comportamento Real do SharePoint

### Throttling Adaptativo
SharePoint ajusta limites dinamicamente. Simular:

```python
class AdaptiveThrottler:
    def __init__(self):
        self.requests_per_minute = []
        self.current_limit = 600  # Limite base
    
    def check_throttle(self):
        now = time.time()
        # Contar requisições no último minuto
        self.requests_per_minute = [t for t in self.requests_per_minute if t > now - 60]
        self.requests_per_minute.append(now)
        
        # Throttle se exceder limite atual
        if len(self.requests_per_minute) > self.current_limit:
            return True
        return False
    
    def adjust_limit(self, error_rate):
        # Reduzir limite se taxa de erro alta
        if error_rate > 0.05:
            self.current_limit = max(300, self.current_limit - 50)
        else:
            self.current_limit = min(600, self.current_limit + 10)
```

### Retries com Exponential Backoff
```python
from src.utils.retry import retry_with_backoff

@retry_with_backoff(max_retries=3, base_delay=1.0)
async def upload_with_retry(file_data):
    response = await client.post("/upload", json=file_data)
    if response.status_code == 429:
        raise ThrottlingError("Rate limited")
    return response
```

## Referências
- [SharePoint Online Throttling](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online)
- [Hash Verification Best Practices](https://docs.python.org/3/library/hashlib.html)
- [Especificação RNF-01](../../documentos/Projeto.md#821-definição-do-cenário)
