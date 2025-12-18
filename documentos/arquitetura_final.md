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

- [Storytelling de Dados da Arquitetura do Sistema Novo](#storytelling-de-dados-da-arquitetura-do-sistema-novo)
- [1. Business Drivers](#1-business-drivers)
  - [1.1 Contexto e Motivação](#11-contexto-e-motivação)
  - [1.2 Cenário do Sistema Atual](#12-cenário-do-sistema-atual)
  - [1.3 Desafios de Crescimento e Evolução](#13-desafios-de-crescimento-e-evolução)
  - [1.4 Volumes Operacionais e Capacidade](#14-volumes-operacionais-e-capacidade)
- [2. Riscos e Oportunidades como Requisitos Não Funcionais](#2-riscos-e-oportunidades-como-requisitos-não-funcionais)
  - [2.1 Mapeamento de Riscos e Oportunidades para RNFs](#21-mapeamento-de-riscos-e-oportunidades-para-rnfs)
  - [2.2 Evidências e Resultados das Estratégias](#22-evidências-e-resultados-das-estratégias)
- [3. Seleção e Foco dos RNFs](#3-seleção-e-foco-dos-rnfs)
  - [3.1 RNFs Selecionados](#31-rnfs-selecionados)
  - [3.2 Critérios de Seleção](#32-critérios-de-seleção)
  - [3.3 Justificativa e Evidências](#33-justificativa-e-evidências)
- [4. Simulação do Sistema Atual](#4-simulação-do-sistema-atual)
- [5. Decisões Arquiteturais e Simulação do Novo Sistema](#5-decisões-arquiteturais-e-simulação-do-novo-sistema)
- [6. Medições Finais](#6-medições-finais)
- [7. Conclusão – Avaliação dos Resultados](#7-conclusão--avaliação-dos-resultados)

---

# Storytelling de Dados da Arquitetura do Sistema Novo

Este documento consolida a **evolução arquitetural do sistema de gestão de portfólio do Metrô de São Paulo**, narrando como o projeto evoluiu ao longo das sprints — desde a identificação dos **business drivers** e diagnóstico do sistema atual até a implementação de uma arquitetura escalável, segura e rastreável com integração de **agentes de Inteligência Artificial**.

O foco é evidenciar o **racional de decisões arquiteturais**, os **Requisitos Não Funcionais (RNFs)** priorizados e controlados, e os **impactos mensuráveis** observados com a nova arquitetura.

### Evolução do Projeto por Sprints

**Sprint 1 - Diagnóstico e Fundamentos**
- Análise do sistema atual (Miro, SharePoint, Power Automate, Power BI)
- Identificação dos business drivers e desafios operacionais
- Mapeamento inicial de riscos e oportunidades
- Definição do escopo arquitetural e objetivos do projeto

**Sprint 2 - Simulação e Seleção de RNFs**
- Simulação do sistema atual com JMT (Java Modelling Tools)
- Identificação de gargalos: sincronização Miro/SharePoint com 97% de utilização
- Seleção dos 3 RNFs críticos: Rastreabilidade, Segurança e Escalabilidade
- Especificação técnica dos requisitos não funcionais

**Sprint 3 - Implementação e Validação**
- Desenvolvimento do Middleware de Validação (FastAPI)
- Implementação de táticas arquiteturais para cada RNF
- Simulação do sistema novo com Locust
- Testes automatizados de compliance, escalabilidade e segurança

**Sprint 4 - Medição e Consolidação**
- Medições estruturais e comportamentais do sistema novo
- Validação de métricas de desempenho, segurança e rastreabilidade
- Análise de tradeoffs arquiteturais
- Consolidação da documentação técnica e resultados

**Sprint 5 - Finalização e Documentação**
- Realização de ajustes necessários na documentação e na arquitetura
- Realização de novos testes da arquitetura
- Finalização do plano de implementação e do orçamento
- Consolidação da documentação e dos resultados

---

## 1. Business Drivers

### 1.1 Contexto e Motivação

&emsp;O **Metrô de São Paulo** é uma das principais empresas públicas de transporte urbano do país, responsável pela operação e expansão da rede metroviária que transporta milhões de passageiros diariamente. Dentro da companhia, o **PMO Corporativo** desempenha papel estratégico na gestão do portfólio de projetos, garantindo que as iniciativas estejam alinhadas às metas organizacionais e aos planos de governo.

&emsp;O sistema de gestão de projetos atual é apoiado por diversas ferramentas do ecossistema Microsoft — como **Miro, SharePoint, Power Automate e Power BI** — utilizadas para o registro, acompanhamento e validação das informações dos projetos. Apesar de funcional, o sistema apresenta **desafios críticos**:

- **Alta dependência de tarefas manuais**: Transferência manual de dados entre Miro e SharePoint
- **Falhas ocasionais de sincronização**: Problemas de integração entre Power Automate, Power BI e SharePoint
- **Baixa rastreabilidade das ações**: Ausência de logs integrados e centralizados de auditoria
- **Riscos de inconsistência de dados**: Divergências entre fontes devido ao preenchimento manual
- **Limitações de escalabilidade**: Gargalo identificado na sincronização Miro/SharePoint (97% de utilização)

&emsp;Diante desse cenário, surge a necessidade de **modernizar a arquitetura tecnológica** do ambiente de gestão de portfólio, tornando-a **mais inteligente, segura e escalável**. A **adoção de agentes de IA** representa uma oportunidade concreta para automatizar atividades repetitivas, oferecer suporte inteligente às equipes e fortalecer a governança digital do Metrô-SP.

### 1.2 Cenário do Sistema Atual

#### 1.2.1 Visão Geral e Fluxo de Trabalho

&emsp;O principal objetivo é transformar a gestão de projetos do Metrô, que atualmente depende de ferramentas semi-estruturadas (Miro para brainstorming) e repositórios passivos (SharePoint para validação/armazenamento), em um ecossistema inteligente e proativo.

**Fluxo de Negócio Atual (AS-IS):**

1. **Planejamento Inicial** (Líder/Equipe do Projeto)
   - Elaboração do Termo de Abertura do Projeto (TAP), Mapa de Benefícios, Entregas e Cronograma
   - Utilização de Miro para brainstorming e documentos MS Office (Word/Excel)

2. **Transferência Manual de Dados**
   - O Líder/Equipe **transporta manualmente** as informações do Miro para as **Listas do SharePoint**
   - Processo suscetível a inconsistências e perda de dados

3. **Reporte Mensal de Status**
   - Atualização mensal do status do projeto, percentual de avanço e riscos no SharePoint
   - Processo manual sem validação automática

4. **Geração de Relatórios**
   - O PMO consolida informações do Power BI e documentos de escritório
   - Criação de **Relatório Mensal** e **Balanço Semestral** usando MS Word, Excel e PowerPoint

**Pontos Fortes:**
- Flexibilidade e agilidade visual do Miro na fase inicial
- Centralização e governança documental no SharePoint
- Integração com ferramentas do ecossistema Microsoft

**Oportunidades de Melhoria:**
- **Maior ineficiência**: Transição manual dos dados entre Miro e SharePoint
- Perda de rastreabilidade durante a transferência de informações
- Consumo significativo de tempo da equipe (overhead)
- Risco elevado de inconsistências entre planejamento inicial e registro final

#### 1.2.2 Evidências Técnicas do Sistema Atual

<div align="center">
<sub>Figura 1.2.2.1 - Diagrama do Fluxo de Negócio AS-IS</sub><br>
<img src="img/section2/as-is.png" width="100%"><br>
<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

**Simulação do Sistema Atual (Sprint 2 - JMT):**

| **Componente**               | **Utilização** | **Latência Média** | **Status**        |
|------------------------------|----------------|--------------------|-------------------|
| Miro (Planejamento)          | 45%            | 10s                | Estável           |
| Sincronização Miro/SharePoint| **97%**        | **45s (em fila)**  | **Gargalo crítico**|
| SharePoint (Armazenamento)   | 60%            | 8s                 | Operacional       |
| Power Automate (Automação)   | 50%            | 15s                | Operacional       |
| Power BI (Relatórios)        | 40%            | 12s                | Estável           |

**Conclusão da Simulação:**
- **Gargalo principal**: Componente de sincronização Miro/SharePoint com **97% de utilização**
- **Latência crítica**: 45 segundos em filas durante picos de carga
- **Processo manual**: Validação e transferência de dados entre ferramentas

### 1.3 Desafios de Crescimento e Evolução

&emsp;A proposta de evolução do sistema de gestão de portfólio do Metrô de São Paulo tem como foco estabelecer uma **arquitetura escalável e segura**, capaz de **integrar agentes de Inteligência Artificial** para apoiar a automação e o gerenciamento inteligente dos projetos corporativos.

#### 1.3.1 Estratégias de Crescimento

**1. Escalabilidade e Desempenho**
- Reestruturação da arquitetura para suportar até **100 usuários simultâneos** e **300 projetos ativos**
- Capacidade elástica para escalar horizontalmente de acordo com a carga de requisições
- Implementação de balanceamento de carga e monitoramento dinâmico
- Tempo médio de resposta abaixo de **1 segundo** mesmo em picos de 5.000 requisições

**2. Disponibilidade e Recuperação de Falhas**
- Modelo de arquitetura distribuída e tolerante a falhas
- Failover automático entre instâncias críticas
- Políticas de backup contínuo e replicação ativa
- Tempo médio de recuperação (MTTR) reduzido para menos de **5 segundos**
- Disponibilidade mínima de **99,5%**

**3. Segurança e Governança de Dados**
- Camadas de defesa contra injeções de comandos e acessos indevidos
- Detecção e bloqueio automático de tentativas maliciosas
- Rastreabilidade completa das tentativas de acesso
- Integração de logs e auditorias a sistemas de alerta

**4. Rastreabilidade e Auditoria de Interações**
- Sistema centralizado de logs registrando **100% das ações**
- Verificação por hash (SHA-256) para garantir integridade
- Recuperação de registros em menos de **2 segundos**
- Conformidade com LGPD e políticas de compliance

**5. Evolução e Integração Inteligente**
- Preparação para futuras integrações com IA generativa
- Automação cognitiva e relatórios preditivos
- Priorização de controle e auditabilidade das informações
- Compatibilidade com Microsoft Power Platform, SharePoint e Copilot

### 1.4 Volumes Operacionais e Capacidade

&emsp;O sistema de gestão de portfólio do Metrô de São Paulo opera com os seguintes volumes:

| **Métrica**                       | **Valor**         | **Observações**                                    |
|-----------------------------------|-------------------|----------------------------------------------------||
| **Usuários Cadastrados**          | 150 usuários      | Analistas, gerentes e membros das equipes          |
| **Usuários Simultâneos (Normal)** | 30-50 usuários    | Períodos de operação padrão                        |
| **Usuários Simultâneos (Pico)**   | 75 usuários       | Consolidação de relatórios e fechamentos           |
| **Capacidade Recomendada**        | 100 usuários      | Margem de segurança e escalabilidade               |
| **Documentos por Projeto**        | 10.000 documentos | Relatórios, cronogramas, registros de risco e atas |
| **Transações Mensais**            | 500-1.000         | Operações de leitura, atualização e automação      |
| **Taxa de Requisições (Normal)**  | 1-2 RPS           | Períodos normais de operação                       |
| **Taxa de Requisições (Pico)**    | 2,5 RPS           | Cenários de alta demanda                           |

**Pontos de Vulnerabilidade:**
- Dependência de processos manuais
- Falhas ocasionais de sincronização entre SharePoint e Power BI
- Limitações de rastreabilidade de ações entre usuários
- Impacto na confiabilidade dos dados e necessidade de tolerância a falhas

### Resumo

&emsp;Os **business drivers** do Metrô de São Paulo, **eficiência operacional, governança de projetos e modernização tecnológica**, justificam a necessidade de evolução arquitetural. O sistema atual, apesar de funcional, apresenta **gargalos críticos de sincronização (97% de utilização), dependência de processos manuais e baixa rastreabilidade**, limitando a escalabilidade e a confiabilidade dos dados.

&emsp;A arquitetura proposta, com **integração de agentes de IA, middleware unificado e processamento assíncrono**, visa resolver esses desafios, garantindo **disponibilidade de 99,5%, rastreabilidade completa (100% de logs auditáveis) e segurança robusta** com verificação de integridade SHA-256. A evolução representa um salto qualitativo na gestão de portfólio, alinhada às metas estratégicas da companhia.

---

## 2. Riscos e Oportunidades como Requisitos Não Funcionais

### 2.1 Mapeamento de Riscos e Oportunidades para RNFs

&emsp;Mapeamento dos riscos e oportunidades identificados para os **3 RNFs** implementados:

| **Risco/Oportunidade**                                 | **Código** | **RNF**         | **Estratégia Implementada**                                         |
| :----------------------------------------------------- | :--------: | :-------------- | :------------------------------------------------------------------ |
| **Riscos Mitigados:**                                  |            |                 |                                                                     |
| Inconsistência de Dados                                |     R1     | Rastreabilidade | Hash SHA-256 + validação de integridade                             |
| Baixa Rastreabilidade das Ações                        |     R5     | Rastreabilidade | Audit Trail 100% + correlação automática                            |
| Acesso Indevido a Informações                          |     R4     | Segurança       | Middleware de segurança + bloqueio automático                       |
| Dependência de Processos Manuais                       |     R2     | Escalabilidade  | Middleware unificado + processamento assíncrono                     |
| Falha de Integração entre Ferramentas                  |     R3     | Escalabilidade  | Middleware com simulação de integrações (SharePoint, Miro, Copilot) |
| **Oportunidades Realizadas:**                          |            |                 |                                                                     |
| Padronização de Logs e Auditorias                      |     O2     | Rastreabilidade | Logs centralizados + recuperação <2s                                |
| Otimização de Processos no Power Automate              |     O3     | Escalabilidade  | Middleware unificado + processamento assíncrono                     |
| Fortalecimento das Políticas de Segurança e Compliance |     O5     | Segurança       | Verificação de integridade + registro de incidentes                 |

### 2.2 Evidências e Resultados das Estratégias

#### 2.2.1 RNF-01: Rastreabilidade

| **Métrica**            | **AS-IS** | **TO-BE**      | **Evidência**                               |
| :--------------------- | :-------- | :------------- | :------------------------------------------ |
| Cobertura de Logs      | 30-40%    | 100%           | Audit Trail completo em todos os cenários   |
| Integridade Verificada | 0%        | 100% (SHA-256) | Hash comparison = True em 100% dos logs     |
| Correlação de Eventos  | Manual    | 75% automática | Correlation ID presente em todas as trilhas |

**Estratégia:** Sistema de Audit Trail com hash SHA-256 e correlação automática.
**Resultado:** Trilha completa de ponta a ponta (SharePoint → Sentinel → Power BI) com 6 eventos correlacionados.

#### 2.2.2 RNF-02: Segurança

| **Métrica**                   | **AS-IS**  | **TO-BE**  | **Evidência**                            |
| :---------------------------- | :--------- | :--------- | :--------------------------------------- |
| Bloqueio de Acessos Indevidos | Limitado   | 100%       | 3/3 tentativas bloqueadas                |
| Verificação de Integridade    | Não existe | SHA-256    | 100% de detecção de inconsistências      |
| Registro de Incidentes        | Manual     | Automático | 3 incidentes registrados automaticamente |

**Estratégia:** Middleware FastAPI com controle de acesso e verificação de integridade.
**Resultado:** 100% de bloqueio de acessos indevidos e detecção de inconsistências entre Miro e SharePoint.

#### 2.2.3 RNF-03: Escalabilidade

| **Métrica**              | **AS-IS**  | **TO-BE**                           | **Evidência**                                                                                    |
| :----------------------- | :--------- | :---------------------------------- | :----------------------------------------------------------------------------------------------- |
| Arquitetura              | Monolítica | Middleware unificado                | Middleware FastAPI consolidando 8 endpoints principais (+ endpoints auxiliares de monitoramento) |
| Processamento            | Síncrono   | Assíncrono                          | FastAPI assíncrono implementado                                                                  |
| Simulação de Integrações | Não existe | SharePoint, Miro, Copilot, Sentinel | APIs mockadas integradas no middleware                                                           |
| Throughput               | Limitado   | Validado em testes                  | Testes Locust validaram capacidade de processamento                                              |

**Estratégia:** Middleware unificado com processamento assíncrono que simula integrações externas (SharePoint, Miro, Copilot, Sentinel).
**Resultado:** Arquitetura consolidada com 8 endpoints unificados, reduzindo complexidade e permitindo escalabilidade através de processamento assíncrono.

#### 2.2.4 Consolidação

| **Risco/Oportunidade**      | **RNF**         | **Status**   | **Evidência**                                     |
| :-------------------------- | :-------------- | :----------- | :------------------------------------------------ |
| R1: Inconsistência de Dados | Rastreabilidade | ✅ Mitigado  | 100% de integridade verificada                    |
| R4: Acesso Indevido         | Segurança       | ✅ Mitigado  | 100% de bloqueio (3/3 tentativas)                 |
| R5: Baixa Rastreabilidade   | Rastreabilidade | ✅ Mitigado  | Trilha completa em 100% dos eventos               |
| R2: Processos Manuais       | Escalabilidade  | ✅ Mitigado  | Middleware unificado com processamento assíncrono |
| O2: Logs Padronizados       | Rastreabilidade | ✅ Realizada | 100% de ações auditáveis                          |
| O5: Segurança Fortalecida   | Segurança       | ✅ Realizada | Verificação SHA-256 + registro automático         |
| O3: Otimização de Processos | Escalabilidade  | ✅ Realizada | Middleware consolidado com 8 endpoints unificados |

---

## 3. Seleção e Foco dos RNFs

### 3.1 RNFs Selecionados

&emsp;Com base no diagnóstico do sistema atual e nos business drivers identificados, foram selecionados **três Requisitos Não Funcionais (RNFs) críticos** para a evolução da arquitetura do sistema de gestão de portfólio do Metrô-SP:

| **RNF** | **Nome** | **Justificativa de Priorização** |
|:-------:|:---------|:--------------------------------|
| **RNF-01** | **Escalabilidade** | Resolver o gargalo crítico de sincronização Miro/SharePoint (97% de utilização) e suportar crescimento de 150 para 300 projetos ativos |
| **RNF-02** | **Segurança** | Mitigar riscos de acesso indevido a informações sensíveis (R4) e garantir conformidade com LGPD e políticas de compliance |
| **RNF-03** | **Rastreabilidade** | Eliminar a baixa rastreabilidade de ações (R5) e garantir auditoria completa de todas as operações (100% de cobertura) |

### 3.2 Critérios de Seleção

&emsp;A seleção dos RNFs seguiu uma metodologia baseada em **análise de riscos, impacto no negócio e viabilidade técnica**, considerando os seguintes critérios:

#### 3.2.1 Análise de Impacto e Probabilidade

**Critério 1: Probabilidade × Impacto do Risco**

| **Risco** | **Nome** | **Probabilidade** | **Impacto** | **Prioridade** | **RNF Associado** |
|:---------:|:---------|:-----------------:|:-----------:|:--------------:|:------------------|
| **R1** | Inconsistência de Dados | 70% | Alto | **Crítica** | Rastreabilidade |
| **R2** | Dependência de Processos Manuais | 80% | Moderado | **Alta** | Escalabilidade |
| **R3** | Falha de Integração entre Ferramentas | 60% | Alto | **Alta** | Escalabilidade |
| **R4** | Acesso Indevido a Informações | 40% | Muito Alto | **Crítica** | Segurança |
| **R5** | Baixa Rastreabilidade das Ações | 50% | Moderado | **Alta** | Rastreabilidade |
| **R6** | Dependência de Licenciamento Microsoft | 30% | Alto | Média | (Fora do escopo) |

**Critério 2: Alinhamento com Business Drivers**

- **Escalabilidade**: Suportar crescimento de projetos (150 → 300) e usuários simultâneos (50 → 100)
- **Segurança**: Conformidade com LGPD e proteção de dados sensíveis de projetos estratégicos
- **Rastreabilidade**: Governança e transparência para auditorias e tomada de decisão

**Critério 3: Evidências da Simulação (Sprint 2)**

- **Gargalo de 97% de utilização** no componente de sincronização → **Escalabilidade**
- **Latência de 45 segundos em filas** durante picos → **Escalabilidade**
- **Ausência de logs centralizados** e auditoria → **Rastreabilidade**
- **Falhas de validação de acesso** em ferramentas distintas → **Segurança**

#### 3.2.2 Matriz de Priorização de RNFs

<div align="center">
<sub>Figura 3.2.2.1 - Matriz de Priorização de RNFs</sub><br>

| **RNF** | **Impacto no Negócio** | **Complexidade Técnica** | **Viabilidade (Sprints)** | **Prioridade Final** |
|:-------:|:----------------------:|:------------------------:|:-------------------------:|:--------------------:|
| Escalabilidade | Crítico | Moderada | Alta | **1º** |
| Segurança | Crítico | Alta |  Moderada | **2º** |
| Rastreabilidade | Alto | Moderada |  Muito Alta | **3º** |

<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

### 3.3 Justificativa e Evidências

#### 3.3.1 RNF-01: Escalabilidade

**Por que foi selecionado?**
- **Evidência crítica**: Simulação JMT (Sprint 2) identificou gargalo de **97% de utilização** no componente de sincronização Miro/SharePoint
- **Impacto no negócio**: Latência de **45 segundos** durante picos compromete a produtividade e experiência do usuário
- **Projeção de crescimento**: Sistema precisa suportar **100 usuários simultâneos** e **300 projetos ativos** (dobro da capacidade atual)

**Táticas implementadas:**
- Enfileiramento de requisições (Queue-Based Load Leveling)
- Processamento assíncrono com FastAPI (Async/Await Pattern)
- Retry automático com backoff exponencial

**Resultados esperados:**
- Throughput de **100 requisições/segundo**
- Latência p95 < **800ms** para operações críticas
- Redução de **150%** no tempo de resposta comparado ao sistema atual

#### 3.3.2 RNF-02: Segurança

**Por que foi selecionado?**
- **Evidência crítica**: Risco R4 (Acesso Indevido) com **Impacto Muito Alto** e probabilidade de 40%
- **Conformidade regulatória**: Necessidade de atender LGPD e políticas de segurança da informação do Metrô-SP
- **Dados sensíveis**: Sistema gerencia informações estratégicas de projetos de infraestrutura pública

**Táticas implementadas:**
- Controle de acesso baseado em projetos (Multi-Tenancy)
- Validação de integridade com checksum SHA-256
- Guardrails de IA para prevenção de prompt injection

**Resultados esperados:**
- **100% de bloqueio** de acessos não autorizados
- Detecção de **100%** de inconsistências de dados
- Registro automático de **todos os incidentes** de segurança

#### 3.3.3 RNF-03: Rastreabilidade

**Por que foi selecionado?**
- **Evidência crítica**: Risco R5 (Baixa Rastreabilidade) com probabilidade de 50% e impacto moderado
- **Cobertura atual**: Apenas **30-40%** das ações são auditadas no sistema AS-IS
- **Conformidade**: Necessário para auditorias, análises forenses e conformidade com LGPD

**Táticas implementadas:**
- Rastreamento distribuído com Correlation ID
- Auditoria completa (Event Sourcing + Logs estruturados)
- Detecção de anomalias com análise estatística

**Resultados esperados:**
- **100% de cobertura** de logs para todas as operações
- Recuperação de registros em < **2 segundos**
- Correlação automática de **75%** dos eventos relacionados

### 3.4 RNFs Não Selecionados (Justificativa)

| **RNF Candidato** | **Por que não foi priorizado?** |
|:------------------|:-------------------------------|
| **Disponibilidade** | Sistema atual já possui disponibilidade aceitável (95%+) via infraestrutura Microsoft Azure; não é gargalo crítico |
| **Performance** | Coberto indiretamente pela **Escalabilidade**; métricas de latência e throughput já contempladas |
| **Usabilidade** | Não é prioridade técnica; interface atual (SharePoint/Miro) já consolidada e aceita pelos usuários |
| **Manutenibilidade** | Importante, mas não crítico; arquitetura modular já garante manutenibilidade básica |

### Resumo

&emsp;A seleção dos **três RNFs críticos** — **Escalabilidade, Segurança e Rastreabilidade** — foi guiada por **evidências técnicas concretas** (simulação JMT com gargalo de 97%), **análise de riscos quantificada** (matriz de probabilidade × impacto) e **alinhamento com business drivers** (crescimento operacional, conformidade regulatória e governança de dados).

&emsp;Cada RNF foi escolhido para resolver um problema específico e mensurável do sistema atual, com **táticas arquiteturais comprovadas** e **metas quantitativas claras**. A priorização balanceou **impacto no negócio** (crítico para operação), **complexidade técnica** (viável em 4 sprints) e **viabilidade de implementação** (recursos e cronograma disponíveis).

---

## 4. Simulação do Sistema Atual

Nesta seção são apresentadas as evidências de como o sistema atual de gestão de projetos do Metrô-SP se comporta frente aos principais **Requisitos Não Funcionais (RNFs)** selecionados — em especial **escalabilidade** e **rastreabilidade** — com base na modelagem do Seção 3 e nas simulações detalhadas no Seção 7 do `Projeto.md`.

- **Cenários simulados:**  
  - **Fluxo de negócio AS-IS (processo manual e fragmentado)**  
    O ponto de partida da simulação é o fluxo de negócio atual descrito na Seção 2.1.3.1, em que a gestão do portfólio depende de múltiplas ferramentas (Miro, SharePoint, Power Automate, Power BI) e de forte intervenção manual para transporte de informações e consolidação de relatórios. Esse fluxo foi utilizado como base conceitual para modelar o comportamento do sistema sob carga e para identificar os elementos críticos (acessos a projetos e relatórios, armazenamento único, logs limitados etc.).  
  - **RNF – Escalabilidade (Rede de Filas / JMT – Simulação AS-IS)**  
    A arquitetura atual foi modelada como uma **rede de filas com um único serviço de processamento sequencial** e uma fila limitada de requisições, representando a dependência de um ponto central (SharePoint/serviço de back-end) sem paralelismo. Foram simulados cenários de carga crescente (100%, 200% e 300% da carga base). Os resultados mostram que, entre **100% e 200% da carga**, os componentes de **Acesso a Projeto** e **Acesso a Relatório** atingem **100% de utilização**, caracterizando-os como gargalos críticos. No cenário de **300% da carga**, o **tempo de fila** cresce para a ordem de **12 milhões de segundos (≈138 dias)**, evidenciando que a taxa de chegada supera permanentemente a capacidade de processamento — situação incompatível com qualquer operação real.  
  - **RNF – Rastreabilidade (Cenários AS-IS de perda de trilha)**  
    Para o RNF de rastreabilidade, foram simulados cenários do sistema atual (Seção 7.3.1), como:  
    - **Cenário 10 – Encerramento manual de projeto (AS-IS)**: o fechamento de projetos depende de ações inteiramente manuais (inativação de elementos, remoção de acessos, arquivamento), o que aumenta o risco de registros órfãos e acessos residuais.  
    - **Cenário 11 – Alterações sem controle de cronograma (AS-IS)** e **Cenário 14 – Registro de mudança manual (AS-IS)**: alterações em cronograma e registros de mudança são feitos sem um mecanismo central de controle, o que leva a estados de **Orphan** e **Compromised** no modelo, representando perda definitiva da trilha de auditoria.  
    Em todos os cenários, o modelo evidencia que uma parcela significativa das ações não é registrada ou correlacionada adequadamente, reforçando a fragilidade do sistema atual em termos de compliance e auditoria.

- **Evidências:**  
  - **Diagrama do Fluxo de Negócio AS-IS**  
    O fluxo de negócio atual que fundamenta as simulações está documentado na Figura 2.1.3.1.1, que ilustra a jornada completa desde o planejamento (Miro, documentos Office) até o armazenamento e consolidação de relatórios no SharePoint/Power BI, destacando os diversos pontos de intervenção manual e a ausência de uma camada arquitetural central de controle.  

    <div align="center">
      <sub>Figura 4.1 – Diagrama do Fluxo de Negócio AS-IS (adaptado da Figura 2.1.3.1.1)</sub><br>
      <img src="img/section2/as-is.png" width="80%"><br>
      <sup>Fonte: Material produzido pelos autores (2025).</sup>
    </div>  

  - **Gráficos de Simulação de Escalabilidade (Sistema Atual)**  
    As simulações de rede de filas realizadas no JMT para o sistema AS-IS geraram gráficos de **utilização dos recursos**, **tempo de fila** e **número de clientes no sistema**, evidenciando o comportamento de saturação sob aumento de carga. Um dos principais gráficos utilizados como evidência é o de **Number of Customers (Navegacao)**, que mostra o crescimento explosivo do número de requisições em espera à medida que a carga se aproxima e ultrapassa o ponto de saturação.  

    <div align="center">
      <sub>Figura 4.2 – Gráfico de Number of Customers – Sistema Atual (AS-IS)</sub><br>
      <img src="img/section7/sistemaAtual/number_of_customers.png" width="80%"><br>
      <sup>Fonte: Material produzido pelos autores (2025).</sup>
    </div>  

  - **Tabelas e modelos dos RNFs do sistema atual**  
    A Tabela de RNFs do sistema atual (Seção 3.1) e as estruturas estáticas de simulação (Seção 3.2) servem como evidência complementar de que o ambiente baseado em Miro/SharePoint **não implementa adequadamente escalabilidade, disponibilidade, segurança, rastreabilidade e tolerância a falhas**, reforçando a leitura dos resultados empíricos da simulação.


  A simulação do sistema atual demonstra, de forma quantitativa e qualitativa, que a arquitetura AS-IS **não é capaz de escalar** para cargas mais altas e **não oferece rastreabilidade confiável** para suportar um ambiente crítico como o do Metrô-SP. Sob aumento moderado de carga, o sistema entra rapidamente em saturação, com tempos de fila impraticáveis e gargalos concentrados em poucos serviços; do ponto de vista de rastreabilidade, processos manuais de encerramento, alteração de cronograma e registro de mudanças levam com frequência a registros órfãos e estados comprometidos, inviabilizando auditoria robusta. Esses resultados consolidam o diagnóstico de que a manutenção do modelo atual representa um risco direto para **desempenho, confiabilidade e compliance**, justificando a necessidade urgente de uma nova arquitetura com mecanismos estruturados de escalabilidade, automação e controle de trilha de auditoria.

---

## 5. Decisões Arquiteturais e Simulação do Novo Sistema

### 5.1 Visão Geral da Arquitetura

A arquitetura proposta para o sistema de gerenciamento de projetos do Metrô-SP foi projetada com foco em três pilares fundamentais: **escalabilidade horizontal**, **rastreabilidade completa** e **segurança em profundidade**. A solução integra agentes de IA ao fluxo de trabalho existente (Miro → SharePoint), automatizando validações, análises e sincronizações que atualmente são manuais.

#### 5.1.1 Contexto e Motivação

O sistema atual apresenta gargalos críticos identificados na Sprint 2 através de simulação com JMT (_Java Modelling Tools_):
- **Gargalo principal:** Componente de sincronização Miro/SharePoint com 97% de utilização
- **Latência média:** 45 segundos em filas durante picos de carga
- **Processo manual:** Validação e transferência de dados entre ferramentas

A arquitetura proposta visa resolver esses problemas através de **automação inteligente**, **processamento assíncrono** e **resiliência a falhas**.

---

### 5.2 Táticas de Arquitetura

#### 5.2.1 Táticas de Escalabilidade (RNF-01)

##### 5.2.1.1 Enfileiramento de Requisições
**Tática:** _Queue-Based Load Leveling Pattern_

**Implementação:**
- Sistema de filas FIFO (_First-In-First-Out_) para requisições não urgentes
- Priorização baseada em níveis de acesso (Admin > Manager > Analyst > Viewer)
- Capacidade de buffer: 10.000 requisições simultâneas

**Benefícios:**
- Absorve picos de carga sem degradação de serviço
- Processamento ordenado evita condições de corrida
- Redução de 150% no tempo de resposta comparado ao sistema atual

**Evidência técnica:**
```python
# Middleware de Validação - Sistema de Enfileiramento
class RequestQueue:
    def __init__(self, max_size=10000):
        self.queue = asyncio.Queue(maxsize=max_size)
        self.priority_weights = {
            "Admin": 4, "Manager": 3, "Analyst": 2, "Viewer": 1
        }
    
    async def enqueue(self, request, priority="Viewer"):
        await self.queue.put((priority, time.time(), request))
```

##### 5.2.1.2 Processamento Assíncrono
**Tática:** _Async/Await Pattern_ com _FastAPI_

**Implementação:**
- Framework FastAPI (baseado em Starlette/ASGI) para concorrência nativa
- Servidor Uvicorn com suporte a HTTP/2 e WebSockets
- Event Loop Python para gerenciar I/O não bloqueante

**Benefícios:**
- _Throughput_ de até 100 requisições/segundo validado em testes
- Latência p95 < 800ms para operações de ingestão
- Redução de uso de CPU em 40% comparado a abordagens síncronas

**Evidência de performance:**
```
Teste de Carga (Locust - 100 usuários concorrentes):
- Requisições/segundo: 98.7
- Latência média: 542ms
- Latência p95: 783ms
- Taxa de erro: 0.3%
```

##### 5.2.1.3 Retry Automático com Backoff Exponencial
**Tática:** _Retry Pattern com Circuit Breaker_

**Implementação:**
- Tentativas automáticas: 3x com intervalo exponencial (1s, 2s, 4s)
- _Circuit breaker_ após 5 falhas consecutivas (timeout 30s)
- Fallback para cache local quando serviços externos estão indisponíveis

**Benefícios:**
- Resiliência a falhas transitórias (rede instável, timeouts momentâneos)
- Taxa de sucesso de 93% mesmo sob condições adversas
- Redução de 60% em erros de timeout

**Código implementado:**
```python
async def retry_with_backoff(func, max_retries=3):
    for attempt in range(max_retries):
        try:
            return await func()
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            await asyncio.sleep(2 ** attempt)  # 1s, 2s, 4s
```

---

#### 5.2.2 Táticas de Segurança (RNF-02)

##### 5.2.2.1 Controle de Acesso Baseado em Projetos
**Tática:** _Multi-Tenancy_ com Isolamento de Dados

**Implementação:**
- Validação de acesso por projeto_id + user_id em cada requisição
- Segregação de dados por tenant (cada projeto é um tenant isolado)
- Níveis de acesso hierárquicos: Admin → Manager → Analyst → Viewer

**Benefícios:**
- Isolamento completo entre projetos distintos
- Prevenção de acesso não autorizado a dados sensíveis
- Compatibilidade futura com Azure AD (OAuth 2.0)

**Matriz de permissões:**
| Nível       | Leitura | Escrita | Exclusão | Admin |
|-------------|---------|---------|----------|-------|
| Admin       | ✓       | ✓       | ✓        | ✓     |
| Manager     | ✓       | ✓       | ✓        | ✗     |
| Analyst     | ✓       | ✓       | ✗        | ✗     |
| Viewer      | ✓       | ✗       | ✗        | ✗     |

##### 5.2.2.2 Validação de Integridade (Checksum SHA-256)
**Tática:** _Data Integrity Verification_

**Implementação:**
- Cálculo de hash SHA-256 para todos os payloads críticos
- Validação de checksum no middleware antes de processar requisições
- Rejeição automática de payloads adulterados

**Benefícios:**
- Detecção de manipulação de dados (man-in-the-middle, corrupção)
- Garantia de integridade fim-a-fim
- Conformidade com LGPD (rastreabilidade de alterações)

**Exemplo de validação:**
```python
import hashlib

def verify_checksum(payload: dict, expected_checksum: str) -> bool:
    data = json.dumps(payload, sort_keys=True).encode()
    calculated = hashlib.sha256(data).hexdigest()
    return calculated == expected_checksum
```

##### 5.2.2.3 Guardrails de IA
**Tática:** _Content Filtering and Validation_

**Implementação:**
- Detecção de prompts maliciosos (injection, bypass attempts)
- Validação semântica de saídas de agentes de IA
- Blacklist de tokens perigosos (ex: "ignore previous instructions")

**Benefícios:**
- Prevenção de prompt injection e jailbreak
- Conformidade com políticas de uso ético de IA
- Proteção contra geração de conteúdo inadequado

**Padrões bloqueados:**
- "Ignore instruções anteriores"
- "DELETE FROM", "DROP TABLE" (SQL injection)
- Requisições com > 5000 tokens (prevenção de DoS)

---

#### 5.2.3 Táticas de Rastreabilidade (RNF-03)

##### 5.2.3.1 Rastreamento Distribuído
**Tática:** _Correlation ID Pattern_

**Implementação:**
- Geração de IDs únicos para cada transação:
  - `request_id`: Identificador único por requisição
  - `correlation_id`: Agrupa requisições relacionadas (ex: workflow completo)
  - `trace_id`: Rastreamento distribuído entre microserviços
- Propagação de IDs em todos os headers HTTP

**Benefícios:**
- Rastreamento fim-a-fim de operações complexas
- Depuração facilitada em ambientes distribuídos
- Compatibilidade com OpenTelemetry e Azure Application Insights

**Estrutura de resposta:**
```json
{
  "request_id": "req_7f3a9b2c",
  "correlation_id": "corr_1a2b3c4d",
  "trace_id": "trace_xyz789",
  "timestamp": "2025-12-16T14:32:01.234Z",
  "data": { ... }
}
```

##### 5.2.3.2 Auditoria Completa
**Tática:** _Event Sourcing_ com Log Estruturado

**Implementação:**
- Logs estruturados em JSON com campos padronizados
- Armazenamento de eventos de auditoria: criação, modificação, exclusão, acesso
- Timestamp UTC em todas as operações

**Benefícios:**
- Conformidade com LGPD (registro de consentimento e acesso a dados)
- Análise forense de incidentes de segurança
- Relatórios de compliance automatizados

**Formato de log:**
```json
{
  "timestamp": "2025-12-16T14:32:01.234Z",
  "level": "INFO",
  "event": "data_access",
  "user_id": "user_123",
  "project_id": "proj_456",
  "action": "read",
  "resource": "/api/projects/456/documents",
  "correlation_id": "corr_1a2b3c4d"
}
```

##### 5.2.3.3 Detecção de Anomalias
**Tática:** _Statistical Anomaly Detection_

**Implementação:**
- Análise de padrões: requisições por minuto, tamanho de payload, latência
- Alertas automáticos para desvios > 3 desvios-padrão
- Dashboard em tempo real para visualização de métricas

**Benefícios:**
- Detecção precoce de ataques DDoS ou acessos suspeitos
- Identificação de degradação de performance
- Resposta proativa a incidentes

**Métricas monitoradas:**
- Taxa de requisições (normal: 10-50/min, alerta: >100/min)
- Latência p95 (normal: <800ms, alerta: >1500ms)
- Taxa de erro (normal: <1%, alerta: >5%)

---

## 6. Medições Finais
_(Apresente os resultados obtidos com o sistema novo, tanto na estrutura quanto no comportamento.)_

- **Medição estrutural (estática):** _(Mostre a organização e desempenho da nova arquitetura.)_  
- **Medição comportamental (dinâmica):** _(Apresente evidências de desempenho, confiabilidade, escalabilidade, etc.)_  
- **Evidências e pitch:** _(Use gráficos e tabelas para evidenciar ganhos concretos.)_

---

## 7. Conclusão – Avaliação dos Resultados
_(Reflita sobre os resultados alcançados e o impacto geral da evolução arquitetural.)_

- **Síntese dos resultados:** _(Resumo dos ganhos e aprendizados obtidos ao longo das sprints.)_  
- **Tradeoffs e lições aprendidas:** _(Descreva as principais concessões e como elas foram gerenciadas.)_  
- **Pitch final:** _(Mensagem de encerramento destacando o valor do sistema evoluído e os próximos passos sugeridos.)_
