# RNF-02 Segurança - Implementação dos Mecanismos Arquiteturais

## Visão Geral

Este projeto implementa os mecanismos de segurança (RNF-02) para o sistema de gerenciamento de projetos do Metrô de São Paulo. O sistema garante controle de acesso granular, autenticação robusta e verificação de integridade de dados entre as ferramentas Miro e SharePoint.

## Estrutura do Projeto

```
RNF-02-Segurança/Sprint 3/
├── api/                    # APIs REST simuladas
│   ├── __init__.py
│   ├── middleware_api.py   # API do middleware de segurança
│   └── integrity_api.py    # API de verificação de integridade
├── models/                 # Modelos de dados
│   ├── __init__.py
│   └── security_models.py  # Modelos de segurança (tokens, permissões, incidentes)
├── services/              # Serviços de negócio
│   ├── __init__.py
│   ├── auth_service.py           # Serviço de autenticação
│   ├── access_control_service.py # Serviço de controle de acesso
│   ├── integrity_service.py       # Serviço de verificação de integridade
│   └── mock_data_generator.py     # Gerador de dados mockados
├── storage/               # Camada de persistência
│   ├── __init__.py
│   └── incident_repository.py     # Repositório de incidentes e logs
├── tests/                 # Testes automatizados (TDD)
│   ├── __init__.py
│   └── test_scenarios.py  # Testes dos 3 cenários de segurança
├── data/                  # Dados persistidos (gerado automaticamente)
│   ├── security_incidents.json
│   ├── checksum_validations.json
│   ├── integrity_checks.json
│   └── access_logs.json
├── main.py                # Aplicação principal FastAPI
├── Configuracao.md        # Guia de configuração e uso
├── requirements.txt      # Dependências do projeto
└── README.md             # Este arquivo
```

## Componentes Utilizados

### 1. Framework Web - FastAPI

**Descrição:** Framework moderno e rápido para construção de APIs REST em Python.

**Instalação:**
```bash
pip install fastapi==0.104.1
```

**Uso no Projeto:**
- `main.py`: Aplicação principal FastAPI
- `api/middleware_api.py`: Endpoints do middleware de segurança
- `api/integrity_api.py`: Endpoints de verificação de integridade

**Documentação:** https://fastapi.tiangolo.com/

---

### 2. Servidor ASGI - Uvicorn

**Descrição:** Servidor ASGI de alto desempenho para aplicações FastAPI.

**Instalação:**
```bash
pip install uvicorn==0.24.0
```

**Uso no Projeto:**
- Servidor HTTP para a aplicação FastAPI
- Suporte a hot-reload durante desenvolvimento

**Documentação:** https://www.uvicorn.org/

---

### 3. Validação de Dados - Pydantic

**Descrição:** Biblioteca para validação de dados usando anotações de tipo Python.

**Instalação:**
```bash
pip install pydantic==2.5.0
```

**Uso no Projeto:**
- `models/security_models.py`: Modelos de dados com validação automática
- Validação de requisições e respostas das APIs
- Serialização JSON automática

**Documentação:** https://docs.pydantic.dev/

---

### 4. Geração de Dados Mockados - Faker

**Descrição:** Biblioteca para geração de dados falsos realistas para testes.

**Instalação:**
```bash
pip install faker==20.1.0
```

**Uso no Projeto:**
- `services/mock_data_generator.py`: Geração de usuários, projetos e dados de teste
- Suporte a localização em português brasileiro (pt_BR)

**Documentação:** https://faker.readthedocs.io/

---

### 5. Manipulação de Datas - python-dateutil

**Descrição:** Extensões para o módulo datetime padrão do Python.

**Instalação:**
```bash
pip install python-dateutil==2.8.2
```

**Uso no Projeto:**
- Manipulação de timestamps e expiração de tokens
- Cálculo de datas e intervalos

**Documentação:** https://dateutil.readthedocs.io/

---

### 6. Biblioteca Padrão Python

**Componentes utilizados:**
- `hashlib`: Geração de checksums SHA-256 para verificação de integridade
- `json`: Serialização e deserialização de dados
- `uuid`: Geração de identificadores únicos
- `datetime`: Manipulação de datas e timestamps
- `pathlib`: Manipulação de caminhos de arquivos
- `re`: Expressões regulares para normalização de whitespace
- `typing`: Anotações de tipo para type hints

## Instalação do Projeto

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Navegue até o diretório do projeto:**
```bash
cd src/RNF-02-Segurança/Sprint\ 3
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

## Executando o Sistema

### Opção 1: Servidor Web com APIs

```bash
python main.py
```

Acesse a documentação interativa:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Opção 2: Testes Automatizados

```bash
python tests/test_scenarios.py
```

Executa os 3 cenários de teste e exibe relatório completo.

## Cenários de Teste Implementados

### Cenário 1: Cadastro Incorreto de Usuário
- **Objetivo:** Verificar bloqueio de acesso de usuários não vinculados ao projeto
- **Validações:**
  - Acesso negado automaticamente
  - Incidente registrado na incident queue
  - Log completo com data, hora, usuário e ação bloqueada

### Cenário 2: Acesso Indevido ao Miro
- **Objetivo:** Garantir que apenas usuários autenticados acessem o Miro
- **Validações:**
  - Bloqueio de links públicos
  - Bloqueio de tokens inválidos
  - Bloqueio de usuários sem permissão
  - Registro de todas as tentativas

### Cenário 3: Inconsistência de Dados Miro/SharePoint
- **Objetivo:** Detectar diferenças entre dados do Miro e SharePoint
- **Validações:**
  - Detecção automática de inconsistências
  - Bloqueio de sincronização até correção
  - Ignorar diferenças apenas de whitespace
  - Registro de incidentes de inconsistência

## Arquitetura dos Componentes

### Serviço de Autenticação (`auth_service`)
- Validação de tokens de autenticação
- Registro e revogação de tokens
- Integração simulada com Microsoft Entra ID

### Serviço de Controle de Acesso (`access_control_service`)
- Verificação de permissões por projeto
- Controle de acesso a recursos (documentos, cronogramas)
- Controle de acesso ao Miro
- Registro automático de incidentes

### Serviço de Integridade (`integrity_service`)
- Geração de checksums SHA-256
- Normalização de whitespace
- Comparação de dados entre sistemas
- Detecção de inconsistências

### Repositório de Incidentes (`incident_repository`)
- Armazenamento em JSON (simulado)
- Incident Queue (fila de incidentes)
- Estatísticas de segurança
- Consultas e filtros

## Dados Persistidos

Os dados são armazenados em arquivos JSON no diretório `data/`:

- `security_incidents.json`: Incidentes de segurança registrados
- `checksum_validations.json`: Validações de checksum realizadas
- `integrity_checks.json`: Verificações de integridade
- `access_logs.json`: Logs de acesso ao sistema

## Critérios de Aceitação

✓ **Cenário 1:** Acesso bloqueado em 100% dos casos de permissão incorreta  
✓ **Cenário 2:** Acesso permitido somente a usuários autenticados com permissões válidas  
✓ **Cenário 3:** Inconsistências detectadas automaticamente, sincronização bloqueada

## Alinhamento com Cenários de Simulação

Os testes automatizados foram alinhados diretamente com os cenários de simulação prática:

- **Cadastro incorreto** → Teste de autenticação e controle de acesso
- **Acesso público ao Miro** → Teste de bloqueio e controle de links
- **Inconsistência de dados** → Teste de verificação de consistência e validação automática

## Próximos Passos

1. Integração com Microsoft Entra ID real
2. Integração com APIs reais do Miro e SharePoint
3. Implementação de fila de mensagens (Service Bus) para incident queue
4. Dashboard de monitoramento de segurança
5. Alertas automáticos via Microsoft Teams

## Contato

**Companhia do Metrô - PMO**  
Email: pmo@metrosp.com.br

---

**Versão:** 1.0.0  
**Última atualização:** 2024


