# Testes Automatizados - Middleware de Validação

## Visão Geral

Suite de testes unitários para validação dos Requisitos Não Funcionais (RNFs) do Middleware de Validação do projeto Metrô-SP.

### RNFs Cobertos

- **RNF-01: Segurança** - Autenticação, autorização, integridade e guardrails de IA
- **RNF-02: Escalabilidade** - Performance, throughput, latência e carga
- **RNF-03: Rastreabilidade** - Auditoria, logs, correlação e integridade de dados

## Estrutura dos Testes

```
tests/
├── __init__.py
├── conftest.py                          # Fixtures compartilhadas
├── unit/
│   ├── test_rnf01_seguranca.py         # 13 testes de segurança
│   ├── test_rnf02_escalabilidade.py    # 12 testes de escalabilidade
│   └── test_rnf03_rastreabilidade.py   # 17 testes de rastreabilidade
└── integration/
    └── (testes de integração futuros)
```

Total: 42 testes unitários

## Execução dos Testes

**IMPORTANTE:** Os testes devem ser executados do diretório `Middleware-Validacao` pois o `conftest.py` importa o módulo `main`.

### Pré-requisitos

```bash
pip install -r requirements.txt
```

### Executar Todos os Testes

```bash
# Certifique-se de estar em Middleware-Validacao
cd ../Middleware-Validacao

# Execução completa
pytest ../Testes-Automatizados/unit/ -v --no-cov

# Com relatório de cobertura
pytest ../Testes-Automatizados/unit/ -v --cov=src --cov-report=html

# Sem captura de output (mostra prints)
pytest ../Testes-Automatizados/unit/ -v -s --no-cov
```

### Executar por RNF

```bash
# RNF-01: Segurança (13 testes)
pytest ../Testes-Automatizados/unit/test_rnf01_seguranca.py -v --no-cov

# RNF-02: Escalabilidade (12 testes)
pytest ../Testes-Automatizados/unit/test_rnf02_escalabilidade.py -v --no-cov

# RNF-03: Rastreabilidade (17 testes)
pytest ../Testes-Automatizados/unit/test_rnf03_rastreabilidade.py -v --no-cov
```

### Executar por Cenário

```bash
# RNF-01 - Cenário 1: Cadastro incorreto
pytest -k "cenario1" tests/unit/test_rnf01_seguranca.py -v

# RNF-02 - Cenário 4: Burst de eventos
pytest -k "cenario4" tests/unit/test_rnf02_escalabilidade.py -v

# RNF-03 - Cenário 3: Validação de integridade
pytest -k "cenario3" tests/unit/test_rnf03_rastreabilidade.py -v
```

## Cenários de Teste

### RNF-01: Segurança (4 Cenários, 13 testes)

1. **Cadastro Incorreto** (3 testes): Bloquear acesso de usuários não vinculados
2. **Acesso Indevido ao Miro** (3 testes): Garantir autenticação antes do acesso
3. **Inconsistências de Dados** (3 testes): Detectar diferenças entre Miro/SharePoint
4. **Guardrails de IA** (4 testes): Impedir ações fora do escopo

### RNF-02: Escalabilidade (5 Cenários, 12 testes)

1. **Ingestor Miro - Pico** (3 testes): Avaliar throughput e latência (p95 < 800ms)
2. **Workflows Concorrentes** (2 testes): Medir performance de workflows (p95 < 600ms)
3. **Upload Concomitante** (2 testes): Validar integridade de uploads (p95 < 2s)
4. **Burst de Eventos** (2 testes): Ingestão massiva de logs (p95 < 150ms)
5. **Sessões Ativas IAM** (3 testes): Performance de autenticação (p95 < 100ms)

### RNF-03: Rastreabilidade (5 Cenários, 17 testes)

1. **Bloqueio Sem Justificativa** (3 testes): Impedir mudanças sem justificativa
2. **Registro Automático** (3 testes): Validar criação de histórico
3. **Validação de Integridade** (3 testes): Garantir consistência de logs
4. **Consulta e Auditoria** (3 testes): Rastrear mudanças ponta a ponta
5. **Alertas Inválidos** (5 testes): Detectar tentativas suspeitas

## Resultados Atuais

- **Total**: 39/42 testes passando (93%)
- **RNF-01**: 13/13 (100%)
- **RNF-02**: 10/12 (83%) - 2 falhas conhecidas em perda de eventos
- **RNF-03**: 16/17 (94%) - 1 falha em frequência de alertas
- **Tempo de execução**: ~5s

## Métricas de Sucesso

### Cobertura de Código

- Meta: 80% de cobertura
- Comando: `pytest --cov=src --cov-report=html`
- Relatório: `htmlcov/index.html`
- Atual: 32% (test_support.py: 31%)

### Performance

- RNF-01: Todos os bloqueios < 200ms
- RNF-02: Latências p95 dentro dos SLOs
- RNF-03: Consultas de auditoria < 500ms

## Fixtures Disponíveis

### Clientes de Teste

- `client`: TestClient FastAPI
- `mock_api_client`: Mock do cliente API
- `mock_validation_service`: Mock do serviço de validação
- `mock_sentinel_client`: Mock do cliente Sentinel

### Headers de Autenticação

- `valid_user_headers`: Usuário admin (u001)
- `invalid_user_headers`: Usuário não cadastrado (u999)
- `viewer_user_headers`: Usuário viewer (u050)

### Dados de Teste

- `sample_miro_data`: Dados do Miro
- `sample_sharepoint_data`: Dados do SharePoint
- `sample_copilot_request`: Requisição válida de IA
- `malicious_copilot_request`: Requisição maliciosa
- `sample_change_request`: Mudança com justificativa
- `change_request_without_justification`: Mudança sem justificativa
- `load_test_users`: 100 usuários para testes de carga

### Utilidades

- `generate_trace_id()`: Gera trace_id único
- `generate_checksum(data)`: Gera hash SHA-256
- `clear_storage`: Limpa storage entre testes

## Relatórios

### HTML Coverage Report

```bash
pytest --cov=src --cov-report=html
# Abrir htmlcov/index.html
```

### JUnit XML

```bash
pytest --junitxml=test-results.xml
```

### Relatório Detalhado

```bash
pytest -v --tb=long --cov=src --cov-report=term-missing
```

## Debugging

### Executar Teste Específico

```bash
# Por nome exato
pytest tests/unit/test_rnf01_seguranca.py::TestRNF01Seguranca::test_cenario1_bloqueio_usuario_nao_cadastrado -v

# Com output completo
pytest -v -s tests/unit/test_rnf01_seguranca.py::TestRNF01Seguranca::test_cenario1_bloqueio_usuario_nao_cadastrado
```

### Modo Verbose com Traceback

```bash
pytest -vv --tb=long
```

### Parar no Primeiro Erro

```bash
pytest -x
```

### Modo Interactive Debug

```bash
pytest --pdb
```

## Documentação dos Testes

Cada teste está documentado com:

- **Docstring** descrevendo o cenário
- **Objetivo** do teste
- **Critério de aceitação** esperado
- **Assertions** claras e específicas

### Exemplo

```python
def test_cenario1_bloqueio_usuario_nao_cadastrado(self, client, invalid_user_headers):
    """
    Cenário 1: Cadastro incorreto de usuário no projeto ou portfólio

    Objetivo: Verificar se o sistema impede o acesso de usuários não vinculados
    Critério: Acesso bloqueado em 100% dos casos de permissão incorreta
    """
    # ... código do teste
```

## Manutenção

### Adicionar Novo Teste

1. Criar função `test_*` na classe apropriada
2. Documentar com docstring completa
3. Usar fixtures existentes quando possível
4. Validar critérios de aceitação
5. Executar e verificar cobertura

### Atualizar Fixtures

- Editar `tests/conftest.py`
- Manter compatibilidade com testes existentes
- Documentar novos fixtures

### Revisar Cobertura

```bash
pytest --cov=src --cov-report=term-missing
pytest --cov=src --cov-report=html
```

## Problemas Conhecidos

### RNF-02: Perda de Eventos

- `test_cenario1_perda_eventos_ingestor`: 100% perda
- `test_cenario4_burst_eventos_auditoria`: 100 eventos perdidos
- Causa: Falta de buffer/queue real para eventos sob carga

### RNF-03: Frequência de Alertas

- `test_cenario5_frequencia_alertas`: Incidentes não persistem entre chamadas
- Causa: Storage em memória não mantém estado entre requests

## Suporte

Para dúvidas sobre os testes:

1. Consultar documentação inline (docstrings)
2. Verificar `conftest.py` para fixtures disponíveis
3. Executar com `-v` para output detalhado
4. Usar `--pdb` para debug interativo
