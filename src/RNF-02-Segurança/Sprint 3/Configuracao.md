# RNF-02 Segurança

## Início Rápido em 3 Passos

### 1. Instalar Dependências

```bash
cd RNF-02-Segurança/Sprint\ 3
pip install -r requirements.txt
```

### 2. Executar o Sistema

**Opção A: Servidor Web com APIs**
```bash
python main.py
```
Acesse: http://localhost:8000/docs

**Opção B: Testes Automatizados**
```bash
python tests/test_scenarios.py
```

### 3. Testar os Cenários

#### Via Navegador (Swagger UI)

1. Abra http://localhost:8000/docs
2. Clique em "POST /middleware/access/check"
3. Clique em "Try it out"
4. Preencha os dados da requisição
5. Clique em "Execute"
6. Veja o resultado!

#### Via cURL

**Cenário 1 - Cadastro Incorreto:**
```bash
# 1. Registrar token
curl -X POST "http://localhost:8000/middleware/auth/token/register?user_email=teste@metrosp.com.br&user_id=USER-0001"

# 2. Registrar permissão em projeto A
curl -X POST "http://localhost:8000/middleware/permissions/register?user_email=teste@metrosp.com.br&user_id=USER-0001&project_id=PROJ-METRO-2024-0001&permission_level=Colaborador"

# 3. Tentar acessar projeto B (deve ser bloqueado)
curl -X POST "http://localhost:8000/middleware/access/check" \
  -H "Content-Type: application/json" \
  -d '{
    "user_email": "teste@metrosp.com.br",
    "user_id": "USER-0001",
    "token": "TOKEN-XXXXXXXX",
    "requested_project_id": "PROJ-METRO-2024-0002",
    "requested_resource": "documentos",
    "action": "read"
  }'
```

**Cenário 2 - Acesso Indevido ao Miro:**
```bash
# Tentar acessar Miro sem autenticação (deve ser bloqueado)
curl -X POST "http://localhost:8000/middleware/miro/access/check" \
  -H "Content-Type: application/json" \
  -d '{
    "miro_board_id": "MIRO-BOARD-0001",
    "miro_link": "https://miro.com/app/board/1234567890/",
    "project_id": "PROJ-METRO-2024-0001",
    "is_authenticated": false
  }'
```

**Cenário 3 - Inconsistência de Dados:**
```bash
# Validar integridade entre Miro e SharePoint
curl -X POST "http://localhost:8000/integrity/validate" \
  -H "Content-Type: application/json" \
  -d '{
    "project_id": "PROJ-METRO-2024-0001",
    "miro_data": "Cronograma\nTarefa 1: 01/01/2024",
    "sharepoint_data": "Cronograma\nTarefa 1: 15/01/2024",
    "data_type": "cronograma"
  }'
```

**Ver Incidentes:**
```bash
curl "http://localhost:8000/middleware/incidents"
```

**Ver Estatísticas:**
```bash
curl "http://localhost:8000/middleware/statistics"
```

---

## Verificar Dados

Os logs são salvos em `data/`:
- `security_incidents.json` - Incidentes de segurança
- `checksum_validations.json` - Validações de checksum
- `integrity_checks.json` - Verificações de integridade
- `access_logs.json` - Logs de acesso

Abra com qualquer editor de texto ou JSON viewer.

---

## Executar Todos os Cenários

```bash
python tests/test_scenarios.py
```

Resultado esperado:
```
✓ PASSOU Cenário 1: Acesso bloqueado automaticamente, incidente registrado
✓ PASSOU Cenário 2: Todos os acessos indevidos foram bloqueados
✓ PASSOU Cenário 3: Integridade de dados validada, inconsistências detectadas

Taxa de sucesso: 100.0%
```

---

## Principais Endpoints

| Endpoint | Descrição |
|----------|-----------|
| `GET /` | Informações do sistema |
| `GET /scenarios` | Lista os 3 cenários |
| `POST /middleware/access/check` | Verifica acesso a recursos |
| `POST /middleware/miro/access/check` | Verifica acesso ao Miro |
| `POST /middleware/auth/token/register` | Registra token de autenticação |
| `POST /middleware/permissions/register` | Registra permissão de projeto |
| `GET /middleware/incidents` | Lista incidentes de segurança |
| `POST /integrity/validate` | Valida integridade de dados |
| `GET /middleware/statistics` | Estatísticas de segurança |

---

## Componentes do Sistema

### 1. Serviço de Autenticação (`auth_service`)
- Validação de tokens
- Registro de tokens
- Revogação de tokens

### 2. Serviço de Controle de Acesso (`access_control_service`)
- Verificação de permissões por projeto
- Controle de acesso a recursos
- Controle de acesso ao Miro
- Registro de incidentes de acesso negado

### 3. Serviço de Integridade (`integrity_service`)
- Geração de checksum
- Normalização de whitespace
- Validação de integridade entre sistemas
- Detecção de inconsistências

### 4. Repositório de Incidentes (`incident_repository`)
- Armazenamento de incidentes de segurança
- Incident Queue (fila de incidentes)
- Validações de checksum
- Verificações de integridade

---

## Critérios de Aceitação

### Cenário 1: Cadastro Incorreto
- ✓ Acesso bloqueado em 100% dos casos de permissão incorreta
- ✓ Nenhum documento visualizável por usuários não cadastrados
- ✓ Incidente registrado na incident queue
- ✓ Log com data, hora, usuário e ação bloqueada

### Cenário 2: Acesso Indevido ao Miro
- ✓ Acesso permitido somente a usuários autenticados
- ✓ Tentativas anônimas bloqueadas e registradas
- ✓ Tentativas com token inválido bloqueadas
- ✓ Tentativas sem permissão bloqueadas

### Cenário 3: Inconsistência de Dados
- ✓ Diferenças detectadas automaticamente
- ✓ Sincronização bloqueada até correção
- ✓ Diferenças apenas de whitespace ignoradas
- ✓ Incidente registrado na incident queue


