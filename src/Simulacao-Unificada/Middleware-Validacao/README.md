# Middleware de Validação

Servidor FastAPI para validação dos requisitos não funcionais (RNF-01 Segurança, RNF-02 Escalabilidade, RNF-03 Rastreabilidade) do projeto Metrô SP.

## Função

O middleware atua como camada intermediária entre os serviços do sistema (Miro, SharePoint, Copilot, Sentinel) validando três aspectos principais:

**Segurança (RNF-01)**

- Controle de acesso: verifica se usuários têm permissão para acessar projetos e recursos
- Integridade de dados: valida checksums entre Miro e SharePoint para detectar inconsistências
- Guardrails de IA: bloqueia prompts maliciosos ou fora do escopo permitido para o Copilot

**Escalabilidade (RNF-02)**

- Gerenciamento de carga: processa múltiplas requisições simultâneas (ingestão de dados, workflows, uploads)
- Enfileiramento: armazena requisições temporariamente quando serviços externos estão ocupados
- Retry automático: reprocessa operações que falharam por problemas de rede

**Rastreabilidade (RNF-03)**

- Auditoria completa: registra todas as operações realizadas (quem, quando, o quê)
- Correlação de eventos: vincula ações entre diferentes serviços usando trace_id
- Detecção de anomalias: identifica padrões suspeitos (mudanças sem justificativa, tentativas de acesso não autorizadas)

Todos os logs e incidentes são armazenados em arquivos JSON no diretório `storage/` para análise posterior.

## Instalação

```powershell
pip install -r requirements.txt
```

## Execução

```powershell
python main.py
```

O servidor inicia em `http://localhost:8001`

## Acesso

- **Dashboard**: http://localhost:8001/dashboard
- **Logs**: http://localhost:8001/logs
- **API Docs**: http://localhost:8001/docs
- **Health**: http://localhost:8001/health

## Testes

Os testes estão em `../Testes-Automatizados/` e devem ser executados deste diretório:

```bash
# Execução recomendada (output limpo e formatado)
python executar_testes.py

# Execução padrão pytest
pytest

# Por requisito específico
pytest unit/test_rnf01_seguranca.py        # 13/13 (100%)
pytest unit/test_rnf02_escalabilidade.py   # 10/12 (83%)
pytest unit/test_rnf03_rastreabilidade.py  # 16/17 (94%)

# Com cobertura
pytest --cov=src --cov-report=html
```

**Nota:** O script `executar_testes.py` fornece output resumido e profissional, mostrando apenas estatísticas e testes falhados.

Documentação completa: `../Testes-Automatizados/README.md`

## Estrutura

```
Middleware-Validacao/
├── main.py                 # Servidor FastAPI
├── requirements.txt        # Dependências
├── src/
│   ├── api/               # Endpoints (test_support.py)
│   ├── core/              # Autenticação
│   ├── monitoring/        # Logger e métricas
│   └── services/          # Integração com API mockada
└── storage/               # Logs e incidentes (JSON)

Testes-Automatizados/
├── unit/                  # Testes pytest
│   ├── test_rnf01_seguranca.py
│   ├── test_rnf02_escalabilidade.py
│   └── test_rnf03_rastreabilidade.py
├── conftest.py            # Fixtures
└── README.md              # Documentação dos testes
```

## Integração

O middleware se comunica com a API mockada (porta 8000) para simular integrações com Miro, SharePoint, Sentinel e Copilot durante os testes.
