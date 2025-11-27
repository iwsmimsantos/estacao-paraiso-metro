# 🚀 Quick Start - APIs Mockadas

Guia rápido para começar a usar as 5 APIs mockadas em **menos de 2 minutos**.

---

## ⚡ Início Rápido (3 comandos)

### Linux/Mac

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Iniciar servidor
./start.sh

# Ou alternativamente:
python main.py
```

### Windows

```powershell
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Iniciar servidor
.\start.ps1

# Ou alternativamente:
python main.py
```

---

## 📚 Acessar Documentação

Após iniciar o servidor, abra no navegador:

**http://localhost:8000/docs**

Você verá a interface Swagger com todas as APIs e poderá testar cada endpoint interativamente.

---

## 🧪 Testar com Script de Exemplo

Em outro terminal:

```bash
# Instalar requests (se ainda não tiver)
pip install requests

# Executar script de exemplo
python example_requests.py
```

O script fará requisições para todas as 5 APIs e mostrará os resultados formatados.

---

## 🎯 Endpoints Principais

| API | Endpoint Principal | Descrição |
|-----|-------------------|-----------|
| **SharePoint** | `GET /sharepoint/sites` | Lista sites |
| **Miro** | `GET /miro/boards` | Lista boards |
| **Copilot** | `GET /copilot/sessions` | Lista sessões |
| **Office** | `GET /office/documents` | Lista documentos |
| **Sentinel** | `GET /sentinel/incidents` | Lista incidentes |

---

## 📋 Exemplos cURL

### SharePoint - Listar sites
```bash
curl "http://localhost:8000/sharepoint/sites?page=1&page_size=5"
```

### Miro - Listar boards de um usuário
```bash
curl "http://localhost:8000/miro/boards?user_id=u001&page=1"
```

### Copilot - Listar sessões
```bash
curl "http://localhost:8000/copilot/sessions?tenant_id=tenant-01"
```

### Office - Listar e-mails
```bash
curl "http://localhost:8000/office/emails?page=1&page_size=10"
```

### Sentinel - Listar alertas por serviço
```bash
curl "http://localhost:8000/sentinel/alerts?source_service=sharepoint"
```

---

## 🔗 Testar Rastreabilidade

Use o header `X-Correlation-Id` para rastrear requisições relacionadas:

```bash
# Requisição 1
curl -H "X-Correlation-Id: trace-123" \
     "http://localhost:8000/sharepoint/sites"

# Requisição 2 (mesmo correlation_id)
curl -H "X-Correlation-Id: trace-123" \
     "http://localhost:8000/sentinel/alerts"
```

Ambas as respostas terão o mesmo `correlation_id` em `meta.traceability`.

---

## 🛑 Parar o Servidor

Pressione **Ctrl+C** no terminal onde o servidor está rodando.

---

## 📖 Mais Informações

- **README completo**: `README.md`
- **Documentação detalhada**: http://localhost:8000/docs
- **OpenAPI Schema**: http://localhost:8000/openapi.json
- **Health Check**: http://localhost:8000/health

---

## ❓ Problemas Comuns

### Porta 8000 já em uso

```bash
# Linux/Mac
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Módulo não encontrado

```bash
pip install -r requirements.txt
```

### CSV não encontrado

Certifique-se de estar no diretório correto:
```bash
cd src/Simulacao-Unificada/Simulacao
```

---

✅ **Pronto!** Suas APIs mockadas estão rodando e prontas para testes de RNF.

