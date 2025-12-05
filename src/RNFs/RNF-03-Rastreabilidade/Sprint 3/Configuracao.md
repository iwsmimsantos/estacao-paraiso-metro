# RNF-03 Rastreabilidade

## Início Rápido em 3 Passos

### 1. Instalar Dependências

```bash
cd RNF-03-Rastreabilidade
pip install -r requirements.txt
```

### 2. Executar o Sistema

**Opção A: Servidor Web com APIs**
```bash
python main.py
```
Acesse: http://localhost:8000/docs

**Opção B: Demonstração Interativa**
```bash
python demo.py
```

**Opção C: Testes Automatizados**
```bash
python tests/test_scenarios.py
```

### 3. Testar os Cenários

#### Via Navegador (Swagger UI)

1. Abra http://localhost:8000/docs
2. Clique em "POST /sharepoint/events/simulate-change"
3. Clique em "Try it out"
4. Defina `with_justification` como `false` (para testar bloqueio)
5. Clique em "Execute"
6. Veja o resultado!

#### Via cURL

**Cenário 1 - Bloqueio:**
```bash
curl -X POST "http://localhost:8000/sharepoint/events/simulate-change?with_justification=false&scenario=cenario_1"
```

**Cenário 2 - Aprovação:**
```bash
curl -X POST "http://localhost:8000/sharepoint/events/simulate-change?with_justification=true&scenario=cenario_2"
```

**Ver Logs:**
```bash
curl "http://localhost:8000/sentinel/logs"
```

**Ver Alertas:**
```bash
curl "http://localhost:8000/sentinel/alerts"
```

**Ver Estatísticas:**
```bash
curl "http://localhost:8000/sentinel/dashboard/statistics"
```

---

## Verificar Dados

Os logs são salvos em `data/`:
- `sharepoint_events.json`
- `sentinel_logs.json`
- `correlated_logs.json`
- `historico_alteracoes.json`
- `alertas.json`
- `audit_trails.json`

Abra com qualquer editor de texto ou JSON viewer.

---

## Executar Todos os Cenários

```bash
python tests/test_scenarios.py
```

Resultado esperado:
```
✓ PASSOU Cenário 1: Mudança bloqueada com sucesso
✓ PASSOU Cenário 2: Mudança registrada automaticamente
✓ PASSOU Cenário 3: Integridade validada com sucesso
✓ PASSOU Cenário 4: Trilha de auditoria criada
✓ PASSOU Cenário 5: Alerta crítico gerado

Taxa de sucesso: 100.0%
```

---

## Principais Endpoints

| Endpoint | Descrição |
|----------|-----------|
| `GET /` | Informações do sistema |
| `GET /scenarios` | Lista os 5 cenários |
| `POST /sharepoint/events/simulate-change` | Simula mudança |
| `GET /sentinel/logs` | Ver logs do Sentinel |
| `GET /sentinel/alerts` | Ver alertas |
| `GET /sentinel/dashboard/statistics` | Estatísticas |

---
