## APIs Disponíveis

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

## Dados Mockados

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

## Resposta Padrão

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

## Parâmetros de Consulta Comuns

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

## Exemplos de Uso

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
