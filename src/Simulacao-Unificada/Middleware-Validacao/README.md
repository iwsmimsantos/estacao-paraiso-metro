# Middleware de Validação - Metrô SP

Middleware responsável por validação, controle de acesso e rastreabilidade no sistema de gestão de projetos do Metrô de São Paulo.

## 🎯 Objetivos

Este middleware implementa os 3 requisitos não funcionais principais:

### RNF-01: Segurança

- ✅ Autenticação e autorização de usuários
- ✅ Controle de acesso por projeto
- ✅ Validação de integridade de dados (checksum)
- ✅ Guardrails para agentes de IA
- ✅ **12 testes unitários automatizados**

### RNF-02: Escalabilidade

- ✅ Rate limiting
- ✅ Circuit breaker para integrações
- ✅ Monitoramento de performance
- ✅ Cache de permissões
- ✅ **15 testes de performance automatizados**

### RNF-03: Rastreabilidade

- ✅ Sistema de logs estruturado
- ✅ Incident queue
- ✅ Auditoria completa de ações
- ✅ Correlação de eventos (trace_id)
- ✅ **18 testes de auditoria automatizados**

---

## 🚀 Como Executar

### 1. Instalar dependências

```powershell
pip install -r requirements.txt
```

### 2. Iniciar o middleware

```powershell
python main.py
```

O servidor estará disponível em: `http://localhost:8001`

### 3. Acessar a interface

- **Página Inicial**: http://localhost:8001 (Interface redesenhada)
- **Dashboard de Monitoramento**: http://localhost:8001/dashboard ⭐ **NOVO DESIGN!**
- **Todos os Logs**: http://localhost:8001/logs ⭐ **NOVA PÁGINA!**
- **Documentação da API**: http://localhost:8001/docs

---

## 🧪 Testes Automatizados

### Executar Todos os Testes

```bash
# Execução simples
pytest -v

# Com relatório de cobertura
pytest --cov=src --cov-report=html

# Scripts interativos
python run_tests.py
# ou
.\run_tests.ps1
```

### Executar por RNF

```bash
# RNF-01: Segurança (12 testes)
pytest tests/unit/test_rnf01_seguranca.py -v

# RNF-02: Escalabilidade (15 testes)
pytest tests/unit/test_rnf02_escalabilidade.py -v

# RNF-03: Rastreabilidade (18 testes)
pytest tests/unit/test_rnf03_rastreabilidade.py -v
```

### Documentação dos Testes

- **Guia Completo**: `tests/README.md`
- **Guia de Integração**: `tests/INTEGRATION_GUIDE.md`
- **Exemplos de Implementação**: `tests/IMPLEMENTATION_EXAMPLES.md`
- **Resumo Executivo**: `tests/SUMMARY.md`

**Total: 45 testes unitários** cobrindo todos os cenários dos RNFs.

---

- **Health Check**: http://localhost:8001/health

## 📊 Dashboard Melhorado

O dashboard foi completamente redesenhado com interface moderna e profissional:

### ✨ Novos Recursos:

- 🎨 **Design moderno** com gradientes e glassmorphism
- 📊 **Gráficos interativos** (Chart.js) - Eventos por tipo e Status das operações
- 🔍 **Filtros dinâmicos** para logs e incidentes
- 📱 **Responsivo** - Funciona em desktop, tablet e mobile
- ⚡ **Auto-refresh** a cada 15 segundos
- 🎯 **Animações suaves** e transições elegantes
- 🎨 **Cards interativos** com hover effects
- 📈 **Estatísticas em tempo real** com métricas visuais

> 📄 Veja detalhes completos em [DASHBOARD.md](./DASHBOARD.md) e preview visual em [DASHBOARD_PREVIEW.md](./DASHBOARD_PREVIEW.md)

## 📁 Estrutura do Projeto

```
Middleware-Validacao/
├── main.py                 # Servidor principal FastAPI
├── requirements.txt        # Dependências do projeto
├── README.md              # Este arquivo
├── src/
│   ├── api/               # Endpoints REST
│   ├── core/              # Autenticação e autorização
│   ├── monitoring/        # Sistema de logs e métricas
│   └── services/          # Integração com API mockada
└── storage/               # Persistência de dados (logs, incidents)
```

## 🔗 Integração com API Mockada

O middleware se comunica com a API mockada (porta 8000) para:

- Validar acessos ao Miro
- Sincronizar dados com SharePoint
- Enviar eventos para o Sentinel
- Processar requisições do Copilot

## 📊 Endpoints Disponíveis

### Health Check

```
GET /health
```

### Dashboard

```
GET /dashboard
```

Mais endpoints serão adicionados conforme a implementação avança.

## 🛠️ Desenvolvimento

Este é um projeto em desenvolvimento progressivo. Os próximos passos incluem:

1. ✅ Estrutura básica
2. ⏳ Sistema de autenticação
3. ⏳ Sistema de logs
4. ⏳ Validação Miro→SharePoint
5. ⏳ Interface web completa

## 📝 Licença

Projeto desenvolvido para o Metrô de São Paulo - Módulo 08
