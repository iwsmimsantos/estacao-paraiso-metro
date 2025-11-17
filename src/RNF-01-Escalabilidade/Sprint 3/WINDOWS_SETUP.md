# Guia Rápido - Windows PowerShell

## Problema com ExecutionPolicy

Se você receber erro ao executar scripts PowerShell, execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Setup Inicial (Método Recomendado)

Execute o script de setup automatizado:

```powershell
.\setup_env.ps1
```

Este script irá:
1. Criar o ambiente virtual (se não existir)
2. Ativar o ambiente virtual
3. Instalar todas as dependências
4. Verificar a instalação

## Setup Manual (Alternativa)

Se preferir fazer manualmente:

### 1. Criar ambiente virtual
```powershell
python -m venv venv
```

### 2. Ativar ambiente virtual

**Opção A - PowerShell (recomendado):**
```powershell
venv\Scripts\Activate.ps1
```

**Opção B - Command Prompt:**
```cmd
venv\Scripts\activate.bat
```

**Opção C - Se der erro de política de execução:**
```powershell
# Temporariamente permite execução de scripts
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
venv\Scripts\Activate.ps1
```

### 3. Instalar dependências
```powershell
pip install -r requirements.txt
```

## Executando os Mocks

Cada mock em um terminal separado:

```powershell
# Terminal 1 - Ingestor (porta 8001)
python -m uvicorn src.mocks.ingestor_mock:app --host 0.0.0.0 --port 8001 --reload

# Terminal 2 - Orchestrator (porta 8002)
python -m uvicorn src.mocks.orchestrator_mock:app --host 0.0.0.0 --port 8002 --reload

# Terminal 3 - SharePoint (porta 8003)
python -m uvicorn src.mocks.sharepoint_mock:app --host 0.0.0.0 --port 8003 --reload

# Terminal 4 - Audit (porta 8004)
python -m uvicorn src.mocks.audit_mock:app --host 0.0.0.0 --port 8004 --reload

# Terminal 5 - IAM (porta 8005)
python -m uvicorn src.mocks.iam_mock:app --host 0.0.0.0 --port 8005 --reload
```

## Executando Testes

```powershell
# Todos os testes unitários
pytest tests/unit/ -v

# Teste específico
pytest tests/unit/test_ingestor.py -v

# Testes com cobertura
pytest tests/ --cov=src --cov-report=html

# Testes de integração
pytest tests/integration/ -v
```

## Testando os Endpoints

Abra o navegador e acesse:

- Ingestor: http://localhost:8001/docs
- Orchestrator: http://localhost:8002/docs
- SharePoint: http://localhost:8003/docs
- Audit: http://localhost:8004/docs
- IAM: http://localhost:8005/docs

Ou use curl/PowerShell:

```powershell
# Health check
Invoke-RestMethod -Uri "http://localhost:8001/health" -Method Get

# Métricas
Invoke-RestMethod -Uri "http://localhost:8001/metrics" -Method Get

# Ingestão de dados
$body = @{
    trace_id = "test-123"
    user_id = "user1"
    action = "ingest"
    payload = @{ data = "test" }
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8001/ingest" -Method Post -Body $body -ContentType "application/json"
```

## Testes de Carga com Locust

```powershell
# Instalar Locust (se não instalado)
pip install locust

# Executar teste de carga
locust -f tests/locust/locustfile_ingestor.py --host=http://localhost:8001

# Com interface web
locust -f tests/locust/locustfile_ingestor.py --web-port=8089
```

Depois acesse: http://localhost:8089

## Desativar Ambiente Virtual

```powershell
deactivate
```

## Troubleshooting

### Erro: "cannot be loaded because running scripts is disabled"

**Solução:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Erro: "python: command not found"

**Solução:** Certifique-se de que Python está instalado e no PATH.

Verifique:
```powershell
python --version
```

Se não funcionar, tente:
```powershell
py --version
```

E substitua `python` por `py` nos comandos.

### Erro: "Module not found"

**Solução:** Certifique-se de estar no diretório correto e com venv ativado:
```powershell
cd "c:\Users\Inteli\Documents\M8_Inteli_Metro\2025-2B-T13-ES08-G01\src\RNF-01-Escalabilidade\Sprint 3"
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Porta já em uso

**Solução:** Mate o processo na porta:
```powershell
# Encontrar processo na porta 8001
netstat -ano | findstr :8001

# Matar processo (substitua PID)
taskkill /PID <PID> /F
```

## Comandos Úteis

```powershell
# Ver pacotes instalados
pip list

# Atualizar pip
python -m pip install --upgrade pip

# Limpar cache do pip
pip cache purge

# Verificar versões
python --version
pip --version

# Criar requirements.txt atualizado
pip freeze > requirements-frozen.txt
```
