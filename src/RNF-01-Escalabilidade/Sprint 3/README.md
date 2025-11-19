# Sprint 3 - Estrutura de Testes de Escalabilidade

Este diretório contém a implementação completa dos mocks de serviços e testes automatizados para validar o RNF de Escalabilidade.

## Estrutura

```
Sprint 3/
├── src/                    # Código-fonte
│   ├── common/            # Código compartilhado
│   ├── mocks/             # Implementação dos mocks
│   └── utils/             # Utilitários
├── tests/                 # Testes automatizados
│   ├── unit/             # Testes unitários
│   ├── integration/      # Testes de integração
│   └── locust/           # Testes de carga
└── scripts/              # Scripts auxiliares
    └── chaos/            # Simulação de falhas
```

## Instalação

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

## Executando os Mocks

Cada mock é um serviço FastAPI independente:

```bash
# Ingestor (porta 8001)
uvicorn src.mocks.ingestor_mock:app --host 0.0.0.0 --port 8001

# Orchestrator (porta 8002)
uvicorn src.mocks.orchestrator_mock:app --host 0.0.0.0 --port 8002

# SharePoint (porta 8003)
uvicorn src.mocks.sharepoint_mock:app --host 0.0.0.0 --port 8003

# Audit (porta 8004)
uvicorn src.mocks.audit_mock:app --host 0.0.0.0 --port 8004

# IAM (porta 8005)
uvicorn src.mocks.iam_mock:app --host 0.0.0.0 --port 8005
```

## Executando Testes

```bash
# Todos os testes
./scripts/run_tests.sh all

# Apenas testes unitários
./scripts/run_tests.sh unit

# Apenas testes de integração
./scripts/run_tests.sh integration

# Com relatório de cobertura
./scripts/run_tests.sh coverage
```

## Testes de Carga com Locust

```bash
# Teste de carga do Ingestor
locust -f tests/locust/locustfile_ingestor.py --host=http://localhost:8001

# Com interface web
locust -f tests/locust/locustfile_ingestor.py --web-port=8089
```

Acesse http://localhost:8089 para configurar e iniciar os testes.

## Chaos Engineering

Scripts para simular falhas:

```bash
# Parar um serviço
./scripts/chaos/stop_service.sh ingestor stop

# Iniciar um serviço
./scripts/chaos/stop_service.sh ingestor start

# Adicionar latência de rede (requer root)
sudo ./scripts/chaos/toggle_network_delay.sh add 200 eth0

# Remover latência
sudo ./scripts/chaos/toggle_network_delay.sh remove eth0
```

## Endpoints dos Mocks

Todos os mocks expõem:

- `POST /[action]` - Endpoint principal de ação
- `GET /health` - Health check
- `GET /metrics` - Métricas operacionais

## Características dos Mocks

### Ingestor Mock
- Simula processamento 50-200ms
- 2% de falha aleatória
- 1% de throttling

### Orchestrator Mock
- Simula processamento 100-500ms
- 3% de falha aleatória

### SharePoint Mock
- Simula processamento 100-300ms
- 5% de throttling (simula SharePoint real)
- 2% de falha aleatória

### Audit Mock
- Simula processamento 10-50ms
- 0.5% de falha aleatória
- Armazena logs em memória

### IAM Mock
- Simula autenticação 50-150ms
- Simula autorização 20-80ms
- 5% de falha de autenticação
- 10% de negação de autorização

## Métricas Coletadas

Cada mock coleta:
- Total de requisições
- Requisições bem-sucedidas
- Erros
- Throttling
- Duração das requisições

Acesse `/metrics` em cada serviço para visualizar.

## Desenvolvimento

Para adicionar novos mocks ou testes:

1. Novos mocks: `src/mocks/novo_mock.py`
2. Testes unitários: `tests/unit/test_novo.py`
3. Testes de carga: `tests/locust/locustfile_novo.py`

Siga os padrões existentes para manter consistência.
