# IAM Mock - Documentação

## Visão Geral
O **IAM Mock** simula o serviço de Identity and Access Management (IAM) do sistema Metro-SP. Ele gerencia autenticação (AuthN), autorização (AuthZ), sessões de usuário e tokens, garantindo controle de acesso seguro a todos os recursos.

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

#### 1. POST /authenticate
**Descrição:** Autentica usuário e emite token de acesso.

**Request Body:**
```json
{
  "username": "user@metro.sp.gov.br",
  "password": "password123"
}
```

**Response (200 OK):**
```json
{
  "status": "success",
  "message": "Authentication successful",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user_id": "user-123",
    "roles": ["project_manager", "editor"],
    "expires_at": "2025-01-01T13:00:00Z"
  }
}
```

**Comportamento Simulado:**
- **Latência:** 50-150ms (validação de credenciais)
- **Taxa de falha:** 5% (credenciais inválidas)
- **Banco de Usuários:** Mock in-memory com 5 usuários pré-definidos

#### 2. POST /authorize
**Descrição:** Verifica se usuário tem permissão para ação em recurso.

**Request Body:**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "resource": "projects/123/documents",
  "action": "write"
}
```

**Response (200 OK):**
```json
{
  "status": "success",
  "message": "Authorization granted",
  "data": {
    "authorized": true,
    "user_id": "user-123",
    "roles": ["project_manager"],
    "resource": "projects/123/documents",
    "action": "write"
  }
}
```

**Response (403 Forbidden):**
```json
{
  "status": "error",
  "message": "Insufficient permissions",
  "data": {
    "authorized": false,
    "required_role": "admin",
    "user_roles": ["viewer"]
  }
}
```

**Comportamento Simulado:**
- **Latência:** 20-80ms (verificação de permissões)
- **Taxa de negação:** 10% (simulação de controle de acesso)
- **RBAC:** Role-Based Access Control com 4 roles

#### 3. GET /health
**Descrição:** Health check do serviço.

#### 4. GET /metrics
**Descrição:** Métricas de observabilidade.

## Execução Local

### Comando Básico
```bash
python -m uvicorn src.mocks.iam_mock:app --host 0.0.0.0 --port 8005
```

### Teste Manual de Autenticação
```powershell
# PowerShell - Autenticar usuário
$body = @{
    username = "admin@metro.sp"
    password = "admin123"
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri "http://localhost:8005/authenticate" `
    -Method Post `
    -Body $body `
    -ContentType "application/json"

$token = $response.data.token
Write-Host "Token: $token"
```

### Teste Manual de Autorização
```powershell
# Verificar permissão
$authBody = @{
    token = $token
    resource = "projects/123/documents"
    action = "write"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8005/authorize" `
    -Method Post `
    -Body $authBody `
    -ContentType "application/json"
```

## Banco de Usuários Mock

### Usuários Pré-definidos
```python
MOCK_USERS = {
    "admin@metro.sp": {
        "user_id": "user-001",
        "password": "admin123",
        "roles": ["admin", "project_manager", "editor", "viewer"]
    },
    "pm@metro.sp": {
        "user_id": "user-002",
        "password": "pm123",
        "roles": ["project_manager", "editor", "viewer"]
    },
    "editor@metro.sp": {
        "user_id": "user-003",
        "password": "editor123",
        "roles": ["editor", "viewer"]
    },
    "viewer@metro.sp": {
        "user_id": "user-004",
        "password": "viewer123",
        "roles": ["viewer"]
    },
    "test@metro.sp": {
        "user_id": "user-005",
        "password": "test123",
        "roles": ["viewer"]
    }
}
```

### Hierarquia de Roles
```
admin
  └─ project_manager
       └─ editor
            └─ viewer
```

**Permissões por Role:**
- `viewer`: read
- `editor`: read, write
- `project_manager`: read, write, delete
- `admin`: read, write, delete, admin

## Ajuste de Parâmetros de Teste

### 1. Taxa de Falha de Autenticação
```python
# src/mocks/iam_mock.py - Linha ~35
AUTH_FAILURE_RATE = 0.05  # 5% de falhas

if random.random() < AUTH_FAILURE_RATE:
    raise HTTPException(status_code=401, detail="Authentication failed")
```

### 2. Latência de Autenticação
```python
# Linha ~32
processing_time = random.uniform(0.05, 0.15)  # 50-150ms
time.sleep(processing_time)
```

Para simular MFA (Multi-Factor Authentication):
```python
processing_time = random.uniform(0.2, 0.5)  # 200-500ms (MFA mais lento)
```

### 3. Taxa de Negação de Autorização
```python
# Linha ~70
AUTHZ_DENIAL_RATE = 0.10  # 10% de negações

if random.random() < AUTHZ_DENIAL_RATE:
    raise HTTPException(status_code=403, detail="Access denied")
```

### 4. Expiração de Token
```python
from datetime import datetime, timedelta

TOKEN_LIFETIME_MINUTES = 60  # 1 hora

def generate_token(user_id: str) -> dict:
    expires_at = datetime.now() + timedelta(minutes=TOKEN_LIFETIME_MINUTES)
    token = jwt.encode(
        {"user_id": user_id, "exp": expires_at},
        SECRET_KEY,
        algorithm="HS256"
    )
    return {"token": token, "expires_at": expires_at.isoformat()}
```

### 5. Adicionar Novos Usuários
```python
# Adicionar ao MOCK_USERS
MOCK_USERS["newuser@metro.sp"] = {
    "user_id": "user-006",
    "password": "new123",
    "roles": ["editor", "viewer"]
}
```

## Coleta de Artefatos

### Logs de Autenticação
```json
{
  "timestamp": "2025-01-01T12:00:00.123Z",
  "level": "INFO",
  "component": "iam-mock",
  "event_type": "authentication",
  "user_id": "user-123",
  "username": "pm@metro.sp",
  "status": "success",
  "latency_ms": 87.3,
  "ip_address": "192.168.1.100"
}
```

### Logs de Autorização
```json
{
  "timestamp": "2025-01-01T12:00:05.456Z",
  "level": "INFO",
  "component": "iam-mock",
  "event_type": "authorization",
  "user_id": "user-123",
  "resource": "projects/123/documents",
  "action": "write",
  "authorized": true,
  "roles": ["project_manager", "editor"],
  "latency_ms": 34.2
}
```

### Logs de Segurança (Falhas)
```json
{
  "timestamp": "2025-01-01T12:01:00.789Z",
  "level": "WARNING",
  "component": "iam-mock",
  "event_type": "authentication_failure",
  "username": "attacker@external.com",
  "reason": "invalid_credentials",
  "ip_address": "203.0.113.42"
}
```

## Interpretação de Artefatos

### Análise de Taxa de Autenticação
```python
import json

with open('logs/iam.log', 'r') as f:
    logs = [json.loads(line) for line in f if line.strip()]

# Filtrar eventos de autenticação
auth_logs = [log for log in logs if log.get('event_type') == 'authentication']

total_auth = len(auth_logs)
successful_auth = len([log for log in auth_logs if log.get('status') == 'success'])
failed_auth = total_auth - successful_auth

auth_success_rate = (successful_auth / total_auth * 100) if total_auth > 0 else 0

print(f"Total Authentication Attempts: {total_auth}")
print(f"Successful: {successful_auth} ({auth_success_rate:.2f}%)")
print(f"Failed: {failed_auth} ({100 - auth_success_rate:.2f}%)")
print(f"SLO: ≥ 95% success rate (excluding invalid credentials)")
```

### Análise de Negações de Acesso
```python
# Filtrar eventos de autorização
authz_logs = [log for log in logs if log.get('event_type') == 'authorization']

total_authz = len(authz_logs)
granted = len([log for log in authz_logs if log.get('authorized') == True])
denied = total_authz - granted

denial_rate = (denied / total_authz * 100) if total_authz > 0 else 0

print(f"Total Authorization Checks: {total_authz}")
print(f"Granted: {granted} ({100 - denial_rate:.2f}%)")
print(f"Denied: {denied} ({denial_rate:.2f}%)")
print(f"Expected: ~10% denial (simulated RBAC)")
```

### Detecção de Ataques (Brute Force)
```python
from collections import Counter, defaultdict

# Contar falhas por usuário
auth_failures = defaultdict(int)
for log in auth_logs:
    if log.get('status') != 'success':
        username = log.get('username', 'unknown')
        auth_failures[username] += 1

# Detectar possíveis ataques (> 5 falhas)
suspicious_users = {user: count for user, count in auth_failures.items() if count > 5}

if suspicious_users:
    print("⚠️  Suspicious activity detected:")
    for user, count in sorted(suspicious_users.items(), key=lambda x: x[1], reverse=True):
        print(f"  - {user}: {count} failed attempts")
else:
    print("✓ No brute force attacks detected")
```

### Análise de Latência por Operação
```python
import numpy as np

auth_latencies = [log['latency_ms'] for log in auth_logs if 'latency_ms' in log]
authz_latencies = [log['latency_ms'] for log in authz_logs if 'latency_ms' in log]

print("Authentication Latencies:")
print(f"  P50: {np.percentile(auth_latencies, 50):.2f} ms")
print(f"  P95: {np.percentile(auth_latencies, 95):.2f} ms")
print(f"  P99: {np.percentile(auth_latencies, 99):.2f} ms")
print(f"  SLO: P95 < 100 ms")

print("\nAuthorization Latencies:")
print(f"  P50: {np.percentile(authz_latencies, 50):.2f} ms")
print(f"  P95: {np.percentile(authz_latencies, 95):.2f} ms")
print(f"  SLO: P95 < 80 ms")
```

## Testes de Carga

### Cenário: Sessões Ativas (50k Tokens)
```bash
locust -f tests/locust/locustfile_iam.py \
    --headless \
    -u 50000 \
    -r 1000 \
    -t 30m \
    --csv=results/iam_sessions \
    --host=http://localhost:8005
```

**Nota:** Este teste simula 50k usuários ativos com tokens válidos.

### Cenário: Pico de Autenticação (Login Storm)
```bash
# Simular horário de pico (início do expediente)
locust -f tests/locust/locustfile_iam.py \
    --headless \
    -u 5000 \
    -r 500 \
    -t 10m \
    --csv=results/iam_login_storm \
    --host=http://localhost:8005
```

### Cenário: Autorização de Alta Frequência
```python
# Editar locustfile_iam.py - priorizar autorização
@task(20)  # 20x mais autorização que autenticação
def authorize_action(self):
    if not self.token:
        self.authenticate()
    
    resource = f"projects/{random.randint(1, 100)}/documents"
    action = random.choice(["read", "write", "delete"])
    
    self.client.post("/authorize", json={
        "token": self.token,
        "resource": resource,
        "action": action
    })
```

```bash
locust -f tests/locust/locustfile_iam.py \
    --headless \
    -u 2000 \
    -r 200 \
    -t 15m \
    --csv=results/iam_authz_heavy \
    --host=http://localhost:8005
```

### Cenário: Token Replay Attack
```python
# Teste de segurança - detectar replay attacks
@task(1)
def replay_attack(self):
    # Usar token expirado ou de outro usuário
    old_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.expired.token"
    
    response = self.client.post("/authorize", json={
        "token": old_token,
        "resource": "admin/users",
        "action": "delete"
    }, catch_response=True)
    
    if response.status_code == 401:
        response.success()  # Esperado: rejeição de token inválido
    else:
        response.failure(f"Token replay not blocked! Status: {response.status_code}")
```

## Troubleshooting

### Problema: Alta taxa de falha de autenticação (> 10%)
**Diagnóstico:**
```bash
# Contar falhas de autenticação
grep '"event_type":"authentication"' logs/iam.log | grep '"status":"failed"' | wc -l
```

**Causa Provável:**
1. Taxa de falha simulada muito alta no código
2. Credenciais inválidas nos testes
3. Token expiration muito curto

**Solução:**
```python
# Reduzir AUTH_FAILURE_RATE
AUTH_FAILURE_RATE = 0.02  # 2% (mais realista)

# Ou garantir credenciais corretas nos testes
TEST_CREDENTIALS = {
    "username": "admin@metro.sp",
    "password": "admin123"  # Deve corresponder a MOCK_USERS
}
```

### Problema: Token expirado prematurely
**Diagnóstico:**
```powershell
# Verificar tempo de vida do token
$response = Invoke-RestMethod -Uri "http://localhost:8005/authenticate" -Method Post -Body (@{username="admin@metro.sp"; password="admin123"} | ConvertTo-Json) -ContentType "application/json"
$expiresAt = [datetime]::Parse($response.data.expires_at)
$now = Get-Date
$lifetime = ($expiresAt - $now).TotalMinutes
Write-Host "Token lifetime: $lifetime minutes"
```

**Solução:**
```python
# Aumentar TOKEN_LIFETIME_MINUTES
TOKEN_LIFETIME_MINUTES = 120  # 2 horas
```

### Problema: Latência P95 > 100ms
**Causa Provável:** Simulação de latência muito alta ou contenção de recursos

**Solução:**
```python
# Reduzir latência simulada
processing_time = random.uniform(0.02, 0.08)  # 20-80ms
```

## Critérios de Aceitação (SLOs)

| Métrica | Limite | Validação |
|---------|--------|-----------|
| Latência P95 Autenticação | < 100 ms | Percentil 95 |
| Latência P95 Autorização | < 80 ms | Percentil 95 |
| Taxa de Sucesso (AuthN) | ≥ 95% | Excluindo credenciais inválidas |
| Taxa de Rejeição Correta | 100% | Tokens inválidos DEVEM ser rejeitados |
| Logs de Segurança | 100% | Todas as falhas DEVEM ser logadas |
| Throughput Autenticação | ≥ 1000 req/s | Durante pico |
| Throughput Autorização | ≥ 5000 req/s | Durante operação normal |

### Validação de Segurança (CRÍTICO)
```python
def validate_security(log_file):
    """Validação obrigatória de segurança."""
    with open(log_file, 'r') as f:
        logs = [json.loads(line) for line in f if line.strip()]
    
    # 1. Verificar se tokens inválidos são rejeitados
    invalid_token_attempts = [log for log in logs if log.get('event_type') == 'authorization' and 'invalid_token' in log.get('reason', '')]
    accepted_invalid = [log for log in invalid_token_attempts if log.get('authorized') == True]
    
    if accepted_invalid:
        print(f"CRITICAL: {len(accepted_invalid)} invalid tokens were accepted!")
        return False
    
    # 2. Verificar se falhas de autenticação são logadas
    auth_failures = [log for log in logs if log.get('event_type') == 'authentication' and log.get('status') == 'failed']
    print(f"✓ {len(auth_failures)} authentication failures properly logged")
    
    # 3. Verificar ausência de credenciais em logs
    credentials_in_logs = [log for log in logs if 'password' in str(log).lower()]
    
    if credentials_in_logs:
        print(f"CRITICAL: {len(credentials_in_logs)} logs contain passwords!")
        return False
    
    print("✓ Security validation passed")
    return True

# Executar após testes
assert validate_security('logs/iam.log'), "Security validation FAILED"
```

## Implementação de Segurança Adicional

### Rate Limiting por IP
```python
from collections import defaultdict
from datetime import datetime, timedelta

class IPRateLimiter:
    def __init__(self, max_attempts=5, window_minutes=5):
        self.attempts = defaultdict(list)
        self.max_attempts = max_attempts
        self.window = timedelta(minutes=window_minutes)
    
    def check_rate_limit(self, ip_address: str) -> bool:
        now = datetime.now()
        # Limpar tentativas antigas
        self.attempts[ip_address] = [
            attempt for attempt in self.attempts[ip_address]
            if now - attempt < self.window
        ]
        
        if len(self.attempts[ip_address]) >= self.max_attempts:
            return True  # Rate limited
        
        self.attempts[ip_address].append(now)
        return False

rate_limiter = IPRateLimiter()

@app.post("/authenticate")
async def authenticate(request: Request, credentials: dict):
    ip = request.client.host
    
    if rate_limiter.check_rate_limit(ip):
        raise HTTPException(status_code=429, detail="Too many authentication attempts")
    
    # ... resto do código
```

### JWT Token Real (Produção)
```python
import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key-change-in-production"
ALGORITHM = "HS256"

def create_jwt_token(user_id: str, roles: list) -> str:
    payload = {
        "user_id": user_id,
        "roles": roles,
        "exp": datetime.utcnow() + timedelta(hours=1),
        "iat": datetime.utcnow()
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_jwt_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
```

## Referências
- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
- [JWT Best Practices](https://datatracker.ietf.org/doc/html/rfc8725)
- [Especificação RNF-01](../../documentos/Projeto.md#821-definição-do-cenário)
