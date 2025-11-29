# Middleware de Validação - Metrô SP

Middleware responsável por validação, controle de acesso e rastreabilidade no sistema de gestão de projetos do Metrô de São Paulo.

## 🎯 Objetivos

Este middleware implementa os 3 requisitos não funcionais principais:

### RNF-01: Segurança

- ✅ Autenticação e autorização de usuários
- ✅ Controle de acesso por projeto
- ✅ Validação de integridade de dados (checksum)
- ✅ Guardrails para agentes de IA

### RNF-02: Escalabilidade

- ✅ Rate limiting
- ✅ Circuit breaker para integrações
- ✅ Monitoramento de performance
- ✅ Cache de permissões

### RNF-03: Rastreabilidade

- ✅ Sistema de logs estruturado
- ✅ Incident queue
- ✅ Auditoria completa de ações
- ✅ Correlação de eventos (trace_id)

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

- **Página Inicial**: http://localhost:8001
- **Documentação da API**: http://localhost:8001/docs
- **Dashboard de Monitoramento**: http://localhost:8001/dashboard
- **Health Check**: http://localhost:8001/health

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
