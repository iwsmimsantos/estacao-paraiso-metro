<Table>
  <tr>
    <td><a href= "https://www.metro.sp.gov.br/"><img src="img/logo-metrosp.png" alt="Metrô de São Paulo" border="0"></td>
    <td>
      <a href= "https://www.inteli.edu.br/"><img src="img/logo-Inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
    </td>
  </tr>
</table>

# Nome do Projeto: Estação Portuguesa Tietê Acesso ao Terminal Rodoviário

## Nome do Grupo: Estação Paraíso

## Integrantes:

- <a href="https://www.linkedin.com/in/gabriel-nascimento3/">Gabriel Santos do Nascimento</a>
- <a href="https://www.linkedin.com/in/iasmim-/">Iasmim Santos Silva de Jesus</a>
- <a href="https://www.linkedin.com/in/milena-castro-vieira/">Milena Aparecida Vieira Castro</a>
- <a href="https://www.linkedin.com/in/nicolasramons/">Nicolas Ramon da Silva</a>
- <a href="https://www.linkedin.com/in/pauloheribeiro/">Paulo Henrique Ribeiro</a>
- <a href="https://www.linkedin.com/in/thalyta-viana/">Thalyta da Silva Viana</a>
- <a href="https://www.linkedin.com/in/viniciussavian/">Vinicius dos Reis Savian</a>

# Sumário



# 1. Introdução

Este documento estabelece os padrões de codificação e práticas de desenvolvimento para o projeto **Estação Portuguesa Tietê Acesso ao Terminal Rodoviário**, desenvolvido em parceria com o Metrô de São Paulo. O projeto visa modernizar a arquitetura tecnológica do ambiente de gestão de portfólio, integrando agentes de Inteligência Artificial para automatizar processos, melhorar a rastreabilidade e garantir segurança e escalabilidade.

O sistema atual utiliza um ecossistema Microsoft composto por SharePoint, Power Automate, Power BI e Miro, e apresenta desafios relacionados à dependência de tarefas manuais, falhas de sincronização e baixa rastreabilidade. A nova arquitetura busca resolver esses problemas através da implementação de três Requisitos Não Funcionais (RNFs) principais:

- **RNF-01 - Escalabilidade**: Garantir que o sistema suporte crescimento de carga e novos agentes de IA
- **RNF-02 - Segurança**: Implementar mecanismos de autenticação, autorização e proteção de dados
- **RNF-03 - Rastreabilidade**: Registrar e correlacionar todas as ações realizadas no sistema para auditoria

Este guia serve como referência para toda a equipe de desenvolvimento, garantindo consistência, qualidade e manutenibilidade do código produzido.

## 1.1 Objetivo do Documento

Este documento estabelece padrões de codificação e práticas de desenvolvimento para garantir a qualidade e a consistência do código produzido no projeto.

A importância de seguir padrões de desenvolvimento está relacionada a diversos benefícios:

- **Facilita a manutenção**: Código padronizado é mais fácil de entender e modificar, reduzindo o tempo necessário para correções e melhorias
- **Melhora a legibilidade**: Padrões consistentes tornam o código mais legível para todos os membros da equipe, independentemente de quem o escreveu
- **Promove a colaboração**: Quando todos seguem os mesmos padrões, a colaboração entre desenvolvedores se torna mais eficiente e menos propensa a erros
- **Garante qualidade**: Padrões bem definidos ajudam a prevenir bugs e vulnerabilidades, especialmente em áreas críticas como segurança (RNF-02) e rastreabilidade (RNF-03)
- **Facilita onboarding**: Novos membros da equipe podem se integrar mais rapidamente quando há padrões claros e documentados

# 2. Padrões de Codificação

Os padrões de codificação definidos neste documento aplicam-se a todas as linguagens utilizadas no projeto: TypeScript (Node.js e Angular), Python (FastAPI) e JavaScript quando necessário. A consistência na nomenclatura e formatação facilita a leitura, manutenção e colaboração entre desenvolvedores.

## 2.1 Naming Conventions

### TypeScript/JavaScript

- Variáveis e Funções: Utilize camelCase
  - Exemplos:
    - ```typescript
      let projectName = "Estação Portuguesa";
      function calculateProjectProgress() { ... }
      ```

- Classes e Interfaces: Utilize PascalCase
  - Exemplos:
    - ```typescript
      class ProjectManager { ... }
      interface SharePointIntegration { ... }
      ```

- Constantes: Utilize UPPER_CASE com underscores
  - Exemplo:
    - ```typescript
      const MAX_PROJECTS = 100;
      const SHAREPOINT_API_URL = "https://metrosp.sharepoint.com";
      ```

### Python

- Variáveis e Funções: Utilize snake_case
  - Exemplos:
    - ```python
      project_name = "Estação Portuguesa"
      def calculate_project_progress():
          pass
      ```

- Classes: Utilize PascalCase
  - Exemplo:
    - ```python
      class ProjectManager:
          pass
      ```

- Constantes: Utilize UPPER_CASE com underscores
  - Exemplo:
    - ```python
      MAX_PROJECTS = 100
      SHAREPOINT_API_URL = "https://metrosp.sharepoint.com"
      ```

### Convenções Específicas do Projeto

- Arquivos de API: Utilize kebab-case para nomes de arquivos
  - Exemplos: `sharepoint-api.ts`, `sentinel-api.py`

- Componentes Angular: Utilize PascalCase para nomes de componentes
  - Exemplo: `ProjectListComponent`, `DashboardComponent`

- Serviços: Utilize camelCase com sufixo "Service" ou "Service" no final
  - Exemplos: `projectService`, `correlationService` 

## 2.2 Formatação de Código

### TypeScript/JavaScript

- Indentação: Utilize 2 espaços para indentação.
- Linhas: Mantenha o comprimento das linhas em até 100 caracteres (recomendado) ou 120 caracteres (máximo).
- Chaves: Coloque chaves de abertura na mesma linha.
  - Exemplo:
    ```typescript
    if (condition) {
      // código
    }
    
    class ProjectService {
      getProjects(): Observable<Project[]> {
        return this.http.get<Project[]>(this.apiUrl);
      }
    }
    ```

### Python

- Indentação: Utilize 4 espaços para indentação (seguindo PEP 8).
- Linhas: Mantenha o comprimento das linhas em até 88 caracteres (Black formatter) ou 100 caracteres (máximo).
- Imports: Organize imports em grupos (stdlib, third-party, local) com linha em branco entre grupos.
  - Exemplo:
    ```python
    from datetime import datetime
    from typing import List, Optional
    
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    
    from api.sharepoint_api import router as sharepoint_router
    from models.log_models import LogEntry
    ```

### Configuração de Formatação

- TypeScript/JavaScript: Utilize Prettier com configuração padronizada
- Python: Utilize Black formatter para formatação automática
- Ambos: Configure o editor para formatar ao salvar

## 2.3 Comentários e Documentação

### TypeScript/JavaScript

- Comentários de Linha: Use para explicar lógica complexa ou decisões de negócio importantes.
  - Exemplo: 
    ```typescript
    // Valida se o projeto possui TAP aprovado antes de permitir execução
    // RNF-02: Segurança - Previne execução sem autorização formal
    if (!project.hasApprovedTAP()) {
      throw new UnauthorizedException('TAP não aprovado');
    }
    ```

- Comentários de Bloco: Use para documentar funções e classes com JSDoc.
  - Exemplo: 
    ```typescript
    /**
     * Busca projetos do SharePoint e sincroniza com a base local.
     * Implementa RNF-03 (Rastreabilidade) registrando todas as operações.
     * 
     * @param {string} listId - ID da lista do SharePoint
     * @param {Date} lastSyncDate - Data da última sincronização
     * @returns {Promise<Project[]>} Lista de projetos sincronizados
     * @throws {SharePointError} Quando há falha na comunicação com SharePoint
     */
    async function syncProjectsFromSharePoint(
      listId: string, 
      lastSyncDate: Date
    ): Promise<Project[]> {
      // implementação
    }
    ```

### Python

- Docstrings: Use docstrings no formato Google ou NumPy para documentar módulos, classes e funções.
  - Exemplo:
    ```python
    def correlate_logs(sharepoint_event_id: str, sentinel_log_id: str) -> dict:
        """
        Correlaciona eventos do SharePoint com logs do Sentinel.
        
        Implementa RNF-03 (Rastreabilidade) criando trilha de auditoria
        completa entre origem (SharePoint) e destino (Sentinel).
        
        Args:
            sharepoint_event_id: ID do evento no SharePoint
            sentinel_log_id: ID do log correspondente no Sentinel
            
        Returns:
            Dicionário com informações de correlação e status de integridade
            
        Raises:
            CorrelationError: Quando não é possível correlacionar os eventos
        """
        pass
    ```

- Comentários Inline: Use para explicar lógica complexa ou decisões arquiteturais.
  - Exemplo:
    ```python
    # RNF-01: Escalabilidade - Utiliza cache distribuído para reduzir carga
    # no SharePoint durante picos de acesso
    cached_data = redis_client.get(cache_key)
    ```

### Documentação da API

- **FastAPI (Python)**: Utilize anotações de tipo e docstrings. A documentação Swagger/OpenAPI é gerada automaticamente em `/docs` e `/redoc`.
  - Exemplo:
    ```python
    @app.post("/sharepoint/events/simulate-change")
    async def simulate_change(
        event: SharePointEvent,
        with_justification: bool = True
    ):
        """
        Simula evento de mudança no SharePoint.
        
        Valida se mudanças sem justificativa são bloqueadas (RNF-02).
        """
        pass
    ```

- **Node.js/TypeScript**: Utilize Swagger/OpenAPI com decoradores ou comentários JSDoc. Configure rota `/api-docs` para acesso à documentação.
  - Exemplo: Utilize `@nestjs/swagger` ou `swagger-jsdoc` para geração automática.

### Boas Práticas

- Documente sempre funções públicas, classes e interfaces
- Explique o "porquê" em comentários, não apenas o "o que"
- Mantenha comentários atualizados quando o código mudar
- Use comentários para referenciar RNFs específicos quando aplicável

# 3. Padrões de Projeto

Os padrões de projeto (design patterns) e a arquitetura definida neste documento garantem que o sistema atenda aos Requisitos Não Funcionais (RNFs) estabelecidos, promovendo escalabilidade, segurança e rastreabilidade. A arquitetura adotada permite a integração harmoniosa entre os componentes do ecossistema Microsoft (SharePoint, Power Automate, Power BI) e os novos agentes de IA.

## 3.1 Design Patterns

Os seguintes design patterns são adotados no projeto para resolver problemas recorrentes e garantir qualidade arquitetural:

### Repository Pattern
- **Objetivo**: Abstrair a camada de acesso a dados, facilitando testes e troca de implementação
- **Aplicação**: Utilizado para acesso a logs de rastreabilidade (RNF-03) e dados do SharePoint
- **Exemplo**: `LogRepository`, `ProjectRepository`
- **Benefício**: Facilita migração entre diferentes fontes de dados (SharePoint, banco de dados, APIs)

### Service Layer Pattern
- **Objetivo**: Centralizar lógica de negócios e regras de validação
- **Aplicação**: Serviços de correlação de logs, validação de segurança, sincronização de dados
- **Exemplo**: `CorrelationService`, `SecurityValidationService`
- **Benefício**: Separação de responsabilidades e reutilização de código

### Middleware Pattern
- **Objetivo**: Interceptar requisições para adicionar funcionalidades transversais (logging, autenticação, rastreabilidade)
- **Aplicação**: Middleware de correlação de eventos (RNF-03), middleware de autenticação (RNF-02)
- **Exemplo**: Middleware que registra todas as requisições para auditoria
- **Benefício**: Implementação centralizada de funcionalidades cross-cutting

### Observer Pattern
- **Objetivo**: Notificar componentes sobre mudanças de estado
- **Aplicação**: Notificações de eventos do SharePoint para o Sentinel, alertas de segurança
- **Exemplo**: Sistema de eventos que notifica mudanças em projetos
- **Benefício**: Desacoplamento entre componentes e reatividade do sistema

### Strategy Pattern
- **Objetivo**: Permitir troca de algoritmos em tempo de execução
- **Aplicação**: Diferentes estratégias de escalabilidade (cache, load balancing, horizontal scaling)
- **Exemplo**: Estratégias de cache para diferentes tipos de dados
- **Benefício**: Flexibilidade para adaptar comportamento conforme necessidade (RNF-01)

### Factory Pattern
- **Objetivo**: Centralizar criação de objetos complexos
- **Aplicação**: Criação de agentes de IA, geração de logs padronizados
- **Exemplo**: `LogEntryFactory` para criar entradas de log com formato consistente
- **Benefício**: Garantia de consistência e facilidade de manutenção

**Referência**: Para mais detalhes sobre design patterns, consulte: https://refactoring.guru/

## 3.2 Arquitetura de Software

- Utilize a Arquitetura de Três Camadas: Separe a lógica de negócios (Camada de Negócios), a interface do usuário (Camada de Apresentção) e o acesso aos dados (Camada de Dados).
  - Exemplo: Em uma aplicação Angular, utilize serviços para lógica de negócios, componentes para a interface e controladores para gerenciar a interação.

# 4. Práticas de Desenvolvimento

As práticas de desenvolvimento definidas neste documento garantem qualidade, confiabilidade e manutenibilidade do código. Elas são essenciais para atender aos RNFs de Escalabilidade, Segurança e Rastreabilidade, assegurando que o sistema funcione corretamente em produção e possa evoluir de forma sustentável.

## 4.1 Testes Automatizados

### Testes Unitários

**TypeScript/JavaScript (Jest)**
- Utilize Jest para testes unitários de funções, classes e serviços
- Cobertura mínima recomendada: 70% para código crítico (segurança, rastreabilidade)
- Exemplo:
  ```typescript
  describe('ProjectService', () => {
    it('deve validar TAP aprovado antes de permitir execução', () => {
      const project = { hasApprovedTAP: () => false };
      expect(() => projectService.executeProject(project))
        .toThrow('TAP não aprovado');
    });
    
    it('deve registrar log de auditoria ao executar projeto', () => {
      const project = { id: '123', hasApprovedTAP: () => true };
      projectService.executeProject(project);
      expect(logRepository.save).toHaveBeenCalledWith(
        expect.objectContaining({ action: 'EXECUTE_PROJECT' })
      );
    });
  });
  ```

**Python (pytest)**
- Utilize pytest para testes unitários de funções, classes e serviços
- Cobertura mínima recomendada: 70% para código crítico
- Exemplo:
  ```python
  def test_correlate_logs_should_return_correlation_id():
      """Testa se correlação de logs retorna correlation_id válido"""
      sharepoint_event = {"id": "sp-123", "action": "update"}
      sentinel_log = {"id": "sent-456", "correlation_id": "corr-789"}
      
      result = correlation_service.correlate_logs(
          sharepoint_event, sentinel_log
      )
      
      assert result["correlation_id"] == "corr-789"
      assert result["status"] == "correlated"
  ```

### Testes de Integração

**Frontend (Cypress)**
- Teste interação entre componentes Angular e serviços
- Valide fluxos de autenticação e autorização (RNF-02)
- Exemplo:
  ```typescript
  describe('Integração: Listagem de Projetos', () => {
    it('deve carregar projetos do SharePoint e exibir na interface', () => {
      cy.visit('/projects');
      cy.get('[data-cy=project-list]').should('be.visible');
      cy.get('[data-cy=project-item]').should('have.length.greaterThan', 0);
    });
  });
  ```

**Backend (pytest com TestClient do FastAPI)**
- Teste integração entre APIs, serviços e repositórios
- Valide fluxos de rastreabilidade end-to-end (RNF-03)
- Exemplo:
  ```python
  def test_sharepoint_event_should_create_sentinel_log(client):
      """Testa se evento do SharePoint gera log no Sentinel"""
      response = client.post(
          "/sharepoint/events/simulate-change",
          json={"project_id": "123", "with_justification": True}
      )
      assert response.status_code == 200
      
      # Verifica se log foi criado no Sentinel
      logs = client.get("/sentinel/logs").json()
      assert any(log["project_id"] == "123" for log in logs)
  ```

### Testes End-to-End (E2E)

**Cypress para Fluxos Completos**
- Teste requisitos funcionais de ponta a ponta
- Valide integração com sistemas externos (SharePoint, Power Automate)
- Exemplo:
  ```typescript
  describe('E2E: Fluxo de Criação de Projeto', () => {
    it('deve criar projeto no SharePoint e gerar log de rastreabilidade', () => {
      cy.login('usuario@metrosp.com.br', 'senha');
      cy.visit('/projects/new');
      cy.get('[data-cy=project-name]').type('Novo Projeto');
      cy.get('[data-cy=save-button]').click();
      
      // Valida criação no SharePoint
      cy.get('[data-cy=success-message]').should('be.visible');
      
      // Valida log de rastreabilidade
      cy.request('GET', '/api/audit-logs').then((response) => {
        expect(response.body).to.have.property('logs');
        expect(response.body.logs[0].action).to.equal('CREATE_PROJECT');
      });
    });
  });
  ```

### Testes de Performance e Escalabilidade (RNF-01)

- Utilize ferramentas como Artillery ou k6 para testes de carga
- Valide comportamento sob diferentes níveis de carga
- Exemplo: Teste de carga simulando 300% de aumento de usuários simultâneos

### Estratégia de Testes

1. **Testes Unitários**: Base da pirâmide - maior quantidade, execução rápida
2. **Testes de Integração**: Camada intermediária - validação de componentes trabalhando juntos
3. **Testes E2E**: Topo da pirâmide - menor quantidade, validação de fluxos críticos
4. **Testes de Performance**: Executados periodicamente e antes de releases importantes

## 4.2 Controle de Qualidade

### Revisão de Código (Code Review)

- **Obrigatoriedade**: Todos os commits devem ser revisados por pelo menos um outro desenvolvedor antes de serem mergeados na branch principal
- **Processo**:
  1. Criar Pull Request (PR) para a branch de desenvolvimento
  2. Solicitar revisão de pelo menos um membro da equipe
  3. Resolver comentários e sugestões antes do merge
  4. Aprovação de pelo menos um revisor é obrigatória
- **Foco da Revisão**:
  - Conformidade com padrões de codificação
  - Qualidade e legibilidade do código
  - Cobertura de testes adequada
  - Impacto em RNFs (Escalabilidade, Segurança, Rastreabilidade)
  - Performance e otimizações

### Análise Estática de Código

**TypeScript/JavaScript (ESLint)**
- Utilize ESLint com regras configuradas para TypeScript e Angular
- Regras recomendadas:
  - `@typescript-eslint/recommended`
  - `@angular-eslint/recommended`
  - Regras customizadas para o projeto
- Integre ESLint no pipeline de CI/CD para bloquear commits com erros

**Python (pylint, flake8, mypy)**
- Utilize pylint ou flake8 para análise de código Python
- Utilize mypy para verificação estática de tipos
- Configure regras no `pyproject.toml` ou `.pylintrc`
- Exemplo de configuração:
  ```toml
  [tool.pylint.messages_control]
  disable = ["C0114", "C0115", "C0116"]  # Desabilita warnings de docstrings opcionais
  ```

### Formatação Automática

- **Prettier** (TypeScript/JavaScript): Formatação automática de código
- **Black** (Python): Formatação automática seguindo PEP 8
- Configure pre-commit hooks para formatar código automaticamente antes de commits

### Validação de Segurança (RNF-02)

- Utilize ferramentas de análise de vulnerabilidades:
  - **npm audit** para dependências Node.js
  - **safety** ou **pip-audit** para dependências Python
  - **Snyk** ou **Dependabot** para monitoramento contínuo
- Revise regularmente dependências e atualize quando necessário
- Valide inputs de usuário e sanitize dados antes de processamento

### Validação de Rastreabilidade (RNF-03)

- Garanta que todas as operações críticas registrem logs de auditoria
- Valide que logs contenham informações necessárias (timestamp, usuário, ação, resultado)
- Verifique correlação entre eventos de diferentes sistemas (SharePoint ↔ Sentinel)

### Métricas de Qualidade

- **Cobertura de Testes**: Mínimo de 70% para código crítico
- **Complexidade Ciclomática**: Máximo de 10 por função/método
- **Duplicação de Código**: Máximo de 3% (detectado por ferramentas como SonarQube)
- **Debt Técnico**: Monitorar e reduzir continuamente

### Pipeline de CI/CD

Configure pipeline que execute automaticamente:
1. Linting (ESLint, pylint)
2. Formatação (Prettier, Black)
3. Testes unitários
4. Testes de integração
5. Análise de segurança
6. Cobertura de testes
7. Build da aplicação

Apenas código que passe em todas as etapas pode ser mergeado.

# 5. Ferramentas e Tecnologias

## 5.1 Ferramentas de Desenvolvimento

- Editor de Código: Utilize Visual Studio Code como editor padrão.

- Plugins recomendados: ESLint, Prettier, GitLens.

## 5.2 Tecnologias e Frameworks

### Backend

**Node.js com TypeScript**
- Runtime: Node.js (versão LTS recomendada)
- Linguagem: TypeScript para type safety e melhor manutenibilidade
- Framework: Express.js ou NestJS para APIs REST
- Gerenciamento de pacotes: npm ou yarn
- Uso: APIs principais, serviços de integração, lógica de negócios

**Python com FastAPI**
- Runtime: Python 3.10+
- Framework: FastAPI para APIs REST de alta performance
- Gerenciamento de pacotes: pip com requirements.txt ou poetry
- Uso: Middleware de rastreabilidade (RNF-03), serviços de correlação de logs, integração com Sentinel
- Exemplo de uso no projeto: Sistema de rastreabilidade em `src/RNF-03-Rastreabilidade/Sprint 3/`

### Frontend

**Angular com TypeScript**
- Framework: Angular (versão mais recente estável)
- Linguagem: TypeScript
- Gerenciamento de pacotes: npm
- Uso: Interface do usuário, dashboards, visualização de projetos e relatórios
- Componentes principais:
  - Componentes de listagem e detalhamento de projetos
  - Dashboards com Power BI embarcado
  - Formulários de criação e edição de projetos

### Integrações e Serviços Externos

**Microsoft 365 Ecosystem**
- **SharePoint**: API REST para acesso a listas e documentos
- **Power Automate**: Webhooks e APIs para automação de fluxos
- **Power BI**: APIs para embedding de relatórios e dashboards
- **Microsoft Sentinel**: API para envio e consulta de logs de segurança

**Ferramentas de Desenvolvimento**
- **Git**: Controle de versão
- **GitHub/GitLab**: Repositório e gerenciamento de código
- **Docker**: Containerização de serviços (opcional, para ambientes de desenvolvimento/teste)

### Bibliotecas e Dependências Principais

**Backend Node.js/TypeScript**
- Express.js ou NestJS: Framework web
- Axios: Cliente HTTP para integrações
- JWT: Autenticação e autorização (RNF-02)
- Winston ou Pino: Logging estruturado (RNF-03)

**Backend Python/FastAPI**
- FastAPI: Framework web assíncrono
- Pydantic: Validação de dados e modelos
- Uvicorn: Servidor ASGI
- Requests ou httpx: Cliente HTTP para integrações

**Frontend Angular**
- Angular Material ou PrimeNG: Componentes de UI
- RxJS: Programação reativa
- Angular HTTP Client: Comunicação com APIs
- NgRx (opcional): Gerenciamento de estado

### Ferramentas de Testes

- **Jest**: Testes unitários e de integração (TypeScript/JavaScript)
- **pytest**: Testes unitários e de integração (Python)
- **Cypress**: Testes end-to-end (Frontend)
- **TestClient (FastAPI)**: Testes de API (Python)

### Monitoramento e Observabilidade

- **Winston/Pino**: Logging estruturado
- **Prometheus + Grafana** (opcional): Métricas e monitoramento
- **Sentry** (opcional): Rastreamento de erros em produção

