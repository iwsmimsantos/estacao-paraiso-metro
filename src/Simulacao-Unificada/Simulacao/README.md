# APIs Mockadas - Microsoft 365 & Ferramentas Colaborativas

Projeto de **5 APIs mockadas** desenvolvidas em **Python 3.11+** e **FastAPI** para simular serviços Microsoft 365 e ferramentas colaborativas, focado em testes de **requisitos não funcionais (RNF)** de segurança, rastreabilidade e escalabilidade.

---

## 🎯 Objetivo

Fornecer APIs simuladas que respondam com dados estruturados e realistas para permitir que um **middleware externo** teste:

- **Segurança**: Contexto de autenticação, MFA, escopos e permissões
- **Rastreabilidade**: Correlation IDs, trace IDs e spans distribuídos
- **Escalabilidade**: Paginação, volume de dados e métricas de performance

---

## 📦 APIs Disponíveis

### 1. SharePoint (`/sharepoint`)
- `GET /sharepoint/sites` - Lista sites do SharePoint
- `GET /sharepoint/sites/{site_id}/documents` - Lista documentos de um site
- `GET /sharepoint/audit-logs` - Logs de auditoria

### 2. Miro (`/miro`)
- `GET /miro/boards` - Lista boards do Miro
- `GET /miro/boards/{board_id}/activities` - Atividades em um board
- `GET /miro/audit-logs` - Logs de auditoria

### 3. Microsoft 365 Copilot (`/copilot`)
- `GET /copilot/sessions` - Lista sessões de uso do Copilot
- `GET /copilot/sessions/{session_id}/messages` - Mensagens de uma sessão
- `GET /copilot/audit-events` - Eventos de auditoria

### 4. Microsoft 365 Office (`/office`)
- `GET /office/documents` - Lista documentos (Word/Excel/PowerPoint)
- `GET /office/emails` - Lista e-mails (Outlook)
- `GET /office/calendar-events` - Lista eventos de calendário

### 5. Microsoft Sentinel (`/sentinel`)
- `GET /sentinel/incidents` - Lista incidentes de segurança
- `GET /sentinel/alerts` - Lista alertas agregados
- `GET /sentinel/events` - Lista eventos normalizados

---

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)

### Passo 1: Instalar dependências

```bash
pip install -r requirements.txt
```

### Passo 2: Executar a aplicação

```bash
# Método 1: Usando uvicorn diretamente
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Método 2: Executando o script main.py
python main.py
```

### Passo 3: Acessar a documentação

Abra seu navegador e acesse:

- **Swagger UI (documentação interativa)**: http://localhost:8000/docs
- **ReDoc (documentação alternativa)**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json
- **Health Check**: http://localhost:8000/health

---

## 📁 Estrutura do Projeto

```
Simulacao/
├── main.py                 # Aplicação principal FastAPI
├── requirements.txt        # Dependências Python
├── README.md              # Este arquivo
│
├── core/                  # Configurações e utilitários centrais
│   ├── __init__.py
│   ├── config.py          # Constantes e configurações
│   └── utils.py           # Funções utilitárias (CSV, geração de dados)
│
├── models/                # Modelos Pydantic para schemas
│   ├── __init__.py
│   ├── common.py          # Modelos compartilhados (envelope padrão)
│   ├── sharepoint.py      # Modelos do SharePoint
│   ├── miro.py            # Modelos do Miro
│   ├── copilot.py         # Modelos do Copilot
│   ├── office.py          # Modelos do Office
│   └── sentinel.py        # Modelos do Sentinel
│
├── routers/               # Rotas das APIs
│   ├── __init__.py
│   ├── sharepoint.py      # Endpoints do SharePoint
│   ├── miro.py            # Endpoints do Miro
│   ├── copilot.py         # Endpoints do Copilot
│   ├── office.py          # Endpoints do Office
│   └── sentinel.py        # Endpoints do Sentinel
│
└── data/                  # Dados mockados
    └── users.csv          # CSV com usuários compartilhados
```

---

## 📊 Dados Mockados

### CSV de Usuários

Todas as APIs usam **exclusivamente** os usuários definidos em `data/users.csv`:

```csv
user_id,display_name,email,department,role,risk_level,is_active,last_login_utc,mfa_enabled,tenant_id
u001,Ana Souza,ana.souza@empresa.com,TI,Administrador,high,true,2025-11-20T13:45:00Z,true,tenant-01
u002,Carlos Lima,carlos.lima@empresa.com,Finanças,Analista,medium,true,2025-11-21T09:12:00Z,true,tenant-01
...
```

Campos importantes:
- **user_id**: Identificador único do usuário
- **tenant_id**: ID do tenant (suporta múltiplos tenants)
- **mfa_enabled**: Se o usuário tem MFA habilitado
- **risk_level**: Nível de risco (low, medium, high)
- **department**: Departamento do usuário

---

## 🔗 Envelope de Resposta Padrão

**Todas as APIs** retornam respostas no seguinte formato:

```json
{
  "request_id": "uuid-aleatorio",
  "service": "sharepoint | miro | copilot | office | sentinel",
  "timestamp_utc": "2025-11-27T10:15:00Z",
  "correlation_id": "uuid-correlacao",
  "data": {
    // Dados específicos da resposta
  },
  "meta": {
    "page": 1,
    "page_size": 20,
    "total_items": 120,
    "security_context": {
      "user_id": "u001",
      "tenant_id": "tenant-01",
      "mfa_required": true,
      "mfa_enabled": true,
      "ip_address": "192.168.0.10",
      "device_id": "device-xyz-123",
      "auth_method": "OAuth2_Bearer",
      "scopes": ["Files.Read.All"]
    },
    "traceability": {
      "trace_id": "uuid-trace",
      "span_id": "uuid-span",
      "source_system": "mock-api",
      "ingested_at_utc": "2025-11-27T10:15:00Z"
    },
    "performance": {
      "processing_time_ms": 23,
      "items_in_response": 10
    }
  }
}
```

---

## 🔍 Parâmetros de Consulta Comuns

Todas as rotas de listagem suportam os seguintes parâmetros:

| Parâmetro | Tipo | Descrição |
|-----------|------|-----------|
| `page` | int | Número da página (padrão: 1) |
| `page_size` | int | Tamanho da página (padrão: 20, máx: 100) |
| `user_id` | str | Filtrar por usuário específico |
| `tenant_id` | str | Filtrar por tenant específico |

### Headers Opcionais

| Header | Descrição |
|--------|-----------|
| `X-Correlation-Id` | ID de correlação para rastreabilidade entre serviços |

---

## 📝 Exemplos de Uso

### Exemplo 1: Listar sites do SharePoint

```bash
curl -X GET "http://localhost:8000/sharepoint/sites?page=1&page_size=10&tenant_id=tenant-01" \
     -H "X-Correlation-Id: my-correlation-123"
```

### Exemplo 2: Listar sessões do Copilot de um usuário

```bash
curl -X GET "http://localhost:8000/copilot/sessions?user_id=u002&page=1&page_size=5"
```

### Exemplo 3: Listar alertas do Sentinel por serviço

```bash
curl -X GET "http://localhost:8000/sentinel/alerts?source_service=sharepoint&page=1"
```

### Exemplo 4: Listar e-mails com paginação

```bash
curl -X GET "http://localhost:8000/office/emails?page=2&page_size=20"
```

---

## 🧪 Testes

### Testar manualmente com Swagger UI

1. Acesse http://localhost:8000/docs
2. Escolha uma API (ex: SharePoint)
3. Clique em um endpoint (ex: `GET /sharepoint/sites`)
4. Clique em "Try it out"
5. Preencha os parâmetros desejados
6. Clique em "Execute"
7. Veja a resposta com o envelope padrão

### Testar rastreabilidade

Use o mesmo `X-Correlation-Id` em múltiplas requisições para simular rastreamento:

```bash
# Requisição 1: SharePoint
curl -X GET "http://localhost:8000/sharepoint/audit-logs" \
     -H "X-Correlation-Id: trace-123"

# Requisição 2: Sentinel (mesmo correlation_id)
curl -X GET "http://localhost:8000/sentinel/events" \
     -H "X-Correlation-Id: trace-123"
```

---

## 🛠️ Desenvolvimento

### Adicionar novos endpoints

1. Defina modelos Pydantic em `models/`
2. Implemente a rota em `routers/`
3. Use as funções utilitárias de `core/utils.py`
4. Mantenha o envelope de resposta padrão

### Modificar dados mockados

Edite `data/users.csv` para adicionar/modificar usuários. Todas as APIs carregam automaticamente os dados do CSV.

---

## 📚 Tecnologias Utilizadas

- **Python 3.11+**: Linguagem de programação
- **FastAPI**: Framework web moderno e rápido
- **Pydantic**: Validação de dados e serialização
- **Uvicorn**: Servidor ASGI de alta performance

---

## 📄 Licença

MIT License - Este é um projeto educacional para testes de RNF.

---

## 👥 Contato

Para dúvidas ou sugestões, entre em contato com a equipe de desenvolvimento.

