<Table>
  <tr>
    <td><a href= "https://www.metro.sp.gov.br/"><img src="img/logo-metrosp.png" alt="Centro Paula Souza" border="0"></td>
    <td>
      <a href= "https://www.inteli.edu.br/"><img src="img/logo-Inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
    </td>
  </tr>
</table>

# Nome do Projeto: <nome do projeto>

## Nome do Grupo: <nome do grupo>

## Integrantes:

- <a href="https://www.linkedin.com/in/username/">Nome</a>
- <a href="https://www.linkedin.com/in/username/">Nome</a>
- <a href="https://www.linkedin.com/in/username/">Nome</a>
- <a href="https://www.linkedin.com/in/username/">Nome</a>
- <a href="https://www.linkedin.com/in/username/">Nome</a>
- <a href="https://www.linkedin.com/in/username/">Nome</a>
- <a href="https://www.linkedin.com/in/username/">Nome</a>
- <a href="https://www.linkedin.com/in/username/">Nome</a>

# Sumário

1. [Introdução](#1-introdução)
   - 1.1 [Termos e Abreviações](#11-termos-e-abreviações)
   - 1.2 [Contexto e Motivação](#12-contexto-e-motivação)
   - 1.3 [Objetivo](#13-objetivo)

2. [Descrição do Sistema Atual](#2-descrição-do-sistema-atual)
   - 2.1 [Visão Geral e Contexto de Negócio](#21-visão-geral-e-contexto-de-negócio)
     - 2.1.1 [Setor de Aplicação e Domínio](#211-setor-de-aplicação-e-domínio)
     - 2.1.2 [Adição de Valor e Propósito](#212-adição-de-valor-e-propósito)
     - 2.1.3 [Processos de Negócio e Fluxos Críticos](#213-processos-de-negócio-e-fluxos-críticos)
     - 2.1.4 [Volumes Operacionais e Capacidade](#214-volumes-operacionais-e-capacidade)
     - 2.1.5 [Estratégias de Crescimento e Evolução](#215-estratégias-de-crescimento-e-evolução)
   - 2.2 [Riscos e Oportunidades](#22-riscos-e-oportunidades)
     - 2.2.1 [Matriz de Riscos](#221-matriz-de-riscos)
     - 2.2.2 [Riscos ligados ao sistema](#222-riscos-ligados-ao-sistema)
     - 2.2.3 [Oportunidades de melhoria dos SLAs](#223-oportunidades-de-melhoria-dos-slas)

3. [Visão de Modelo Comportamental (Simulação do Sistema Atual)](#3-visão-de-modelo-comportamental-simulação-do-sistema-atual)
   - 3.1 [RNFs do Sistema Atual](#31-rnfs-do-sistema-atual)
   - 3.2 [Estrutura Estática do Modelo](#32-estrutura-estática-do-modelo)
   - 3.3 [Modelagem Comportamental e Simulação dos RNFs](#33-modelagem-comportamental-e-simulação-dos-rnfs)
     - 3.3.1 [Modelagem Comportamental](#331-modelagem-comportamental)
     - 3.3.2 [Cenários Simulados](#332-cenários-simulados)
   - 3.4 [Consolidação dos Resultados da Simulação](#34-consolidação-dos-resultados-da-simulação)

4. [Arquitetura do Sistema Novo – Especificação de Requisitos](#4-arquitetura-do-sistema-novo--especificação-de-requisitos)
   - 4.1 [Requisitos Não Funcionais do Sistema Novo](#41-requisitos-não-funcionais-do-sistema-novo)
   - 4.2 [Justificativas para RNFs](#42-justificativas-para-rnfs)
   - 4.3 [Melhorias Esperadas com Implementação de RNFs](#43-melhorias-esperadas-com-implementação-de-rnfs)
   - 4.4 [Consolidação dos Requisitos e Diretrizes para a Nova Arquitetura](#44-consolidação-dos-requisitos-e-diretrizes-para-a-nova-arquitetura)

5. [Avaliação dos Mecanismos Utilizados no Sistema Atual (Diagnóstico ATAM)](#5-avaliação-dos-mecanismos-utilizados-no-sistema-atual-diagnóstico-atam)
   - 5.1 [Revisão do Mapa de RNFs e Vulnerabilidades](#51-revisão-do-mapa-de-rnfs-e-vulnerabilidades)
   - 5.2 [Táticas Arquiteturais e Componentes Adotados](#52-táticas-arquiteturais-e-componentes-adotados)
   - 5.3 [Análise de Causas e Impactos](#53-análise-de-causas-e-impactos)

6. [Especificação da Solução Técnica do Sistema Novo](#6-especificação-da-solução-técnica-do-sistema-novo)
   - 6.1 [Revisão do Mapa de RNFs do Sistema Novo](#61-revisão-do-mapa-de-rnfs-do-sistema-novo)
   - 6.2 [Táticas Arquiteturais e Componentes Adotados](#62-táticas-arquiteturais-e-componentes-adotados)
   - 6.3 [Justificativas Arquiteturais e Racional das Decisões](#63-justificativas-arquiteturais-e-racional-das-decisões)
   - 6.4 [Consolidação Técnica da Solução](#64-consolidação-técnica-da-solução)

7. [Simulação do Sistema Novo](#7-simulação-do-sistema-novo)

8. [Implementação dos Mecanismos Arquiteturais](#8-implementação-dos-mecanismos-arquiteturais)
   - 8.1 [Testes e Validação dos Mecanismos](#81-testes-e-validação-dos-mecanismos)

9. [Revisão do Modelo de Simulação do Sistema Novo](#9-revisão-do-modelo-de-simulação-do-sistema-novo)

10. [Ajustes na Implementação](#10-ajustes-na-implementação)

11. [Evidências de Testes Não Funcionais](#11-evidências-de-testes-não-funcionais)

12. [Medição e Avaliação do Sistema Novo](#12-medição-e-avaliação-do-sistema-novo)

13. [Tradeoffs Arquiteturais](#13-tradeoffs-arquiteturais)

14. [A construir](#14-a-construir)

# Projeto · Módulo 08 – Arquitetura Digital Segura e Tolerante a Falhas

---

# 1. Introdução

## 1.1 Termos e Abreviações
_(Liste e defina siglas, termos técnicos e nomenclaturas utilizadas no projeto.)_

## 1.2 Contexto e Motivação
_(Descreva o contexto do parceiro, o problema identificado e a motivação para o desenvolvimento da solução.)_

## 1.3 Objetivo
_(Apresente o objetivo geral e os objetivos específicos do projeto.)_

---

# 2. Descrição do Sistema Atual

## 2.1 Visão Geral e Contexto de Negócio

&emsp; O principal objetivo é transformar a gestão de projetos do Metrô, que atualmente depende de ferramentas semi-estruturadas (Miro para brainstorming) e repositórios passivos (SharePoint para validação/armazenamento), em um ecossistema inteligente e proativo. A evidência primária da necessidade reside na dispersão de informações e na dependência de esforço manual para consolidar insights de planejamento em documentos de projeto rastreáveis e acionáveis. A introdução de Agentes de IA visa preencher essa lacuna, automatizando a transição de ideias brutas (Miro) para dados estruturados e validados (SharePoint), garantindo a rastreabilidade e a acuracidade desde o conceito inicial até a execução.

- **Pontos Fortes:** O Miro oferece flexibilidade e agilidade visual na fase inicial, enquanto o SharePoint garante a centralização e governança documental dos artefatos finais (ex: Termos de Abertura, Escopo, EAPs).
- **Oportunidades de Melhoria:** A maior ineficiência reside na transição manual dos dados. A informação visual e não-estruturada do Miro precisa ser transcrita e estruturada em documentos formais para o SharePoint. Isso gera perda de rastreabilidade, consome tempo significativo da equipe (overhead), e aumenta o risco de inconsistências de dados entre o planejamento inicial e o registro final.

### 2.1.1 Setor de Aplicação e Domínio
&emsp;O sistema de gestão de projetos com agentes de IA atende/suporta principalmente os seguintes setores industriais:

- Infraestrutura e Transporte (Foco Principal): Otimizando a gestão de projetos de manutenção, expansão e modernização de linhas, estações e sistemas metroviários.
- Gestão de Projetos (Vertical): Fornecendo suporte a Project Management Offices (PMOs) e equipes de projeto que utilizam metodologias ágeis ou tradicionais no ambiente de infraestrutura.
- Tecnologia da Informação e Serviços Digitais: Suportando o desenvolvimento e a integração de novas tecnologias (IoT, sistemas de sinalização, segurança) no contexto metroviário.

### 2.1.2 Adição de Valor e Propósito

&emsp; A plataforma digital, com sua arquitetura escalável e agentes de IA integrados, adiciona valor ao negócio do Metrô de São Paulo das seguintes formas:

- **Aumento da Eficiência Operacional:**

  - Automação da Estruturação: Os Agentes de IA transformam automaticamente os brainstormings visuais do Miro em artefatos de projeto estruturados, como cronogramas e requisitos, prontos para o SharePoint, reduzindo o tempo de consolidação manual em até 70%.
  - Tomada de Decisão Acelerada: A IA analisa os dados históricos e em tempo real para prever riscos e sugerir alocações de recursos, permitindo intervenções mais rápidas e informadas.

- **Melhoria da Qualidade e Compliance:**

  - Rastreabilidade Total: Cada ação e mudança sugerida pelo agente de IA (e aprovada pelo gestor) é registrada de forma imutável, atendendo aos rigorosos requisitos de segurança e auditoria exigidos em projetos de infraestrutura pública.
  - Garantia de Disponibilidade: A arquitetura escalável assegura que a ferramenta de gestão esteja sempre disponível, um requisito crítico para projetos de infraestrutura que operam 24/7.

- **Otimização de Custos:**

  - Prevenção de Desvios: A capacidade preditiva da IA ajuda a identificar potenciais desvios de escopo ou estouros orçamentários mais cedo, permitindo ações corretivas que minimizam o retrabalho e o custo final dos projetos.

### 2.1.3 Processos de Negócio e Fluxos Críticos
- **Processos de negócio e fluxos críticos suportados:**  
  _(Descreva os fluxos de negócio suportados e o papel do sistema nesses fluxos. Inclua diagramas, fluxogramas ou tabelas se necessário.)_

### 2.1.4 Volumes Operacionais e Capacidade

&emsp;O sistema de gestão de portfólio do Metrô de São Paulo é utilizado por **aproximadamente 150 usuários cadastrados**, entre analistas, gerentes e membros das equipes de projeto. Desses, estima-se que **entre 30 e 50 usuários possam operar simultaneamente em períodos de pico**, chegando a até 75 usuários simultâneos em momentos de alta demanda, como etapas de consolidação de relatórios ou fechamento de ciclos mensais.

&emsp;Cada projeto em andamento gera cerca de **10.000 documentos**, incluindo relatórios, cronogramas, registros de risco e atas, resultando em um volume expressivo de dados processados e armazenados. A plataforma, composta por ferramentas como SharePoint, Power Automate, Power BI e Miro, **realiza em média de 500 a 1.000 transações mensais**, considerando operações de leitura, atualização, automação de fluxos e geração de relatórios.

&emsp;As estimativas de desempenho indicam uma **taxa de 1 a 2 requisições por segundo (RPS) em períodos normais de operação**, podendo atingir até 2,5 RPS em cenários de pico. Para garantir estabilidade e disponibilidade, recomenda-se o dimensionamento da arquitetura para **100 usuários simultâneos**, permitindo margens de segurança e escalabilidade futura.

&emsp;Os principais pontos de vulnerabilidade observados estão relacionados à dependência de processos manuais, falhas ocasionais de sincronização entre SharePoint e Power BI, e limitações de rastreabilidade de ações entre usuários. Tais fatores impactam a confiabilidade dos dados e reforçam a necessidade de uma arquitetura com mecanismos de tolerância a falhas, registro de auditoria e monitoramento proativo de desempenho.

**Tabela 1 - Resumo dos Volumes Operacionais**

| **Métrica** | **Valor** | **Observações** |
|-------------|-----------|-----------------|
| **Usuários Cadastrados** | 150 usuários | Analistas, gerentes e membros das equipes |
| **Usuários Simultâneos (Normal)** | 30-50 usuários | Períodos de operação padrão |
| **Usuários Simultâneos (Pico)** | 75 usuários | Consolidação de relatórios e fechamentos |
| **Capacidade Recomendada** | 100 usuários | Margem de segurança e escalabilidade |
| **Documentos por Projeto** | 10.000 documentos | Relatórios, cronogramas, registros de risco e atas |
| **Transações Mensais** | 500-1.000 | Operações de leitura, atualização e automação |
| **Taxa de Requisições (Normal)** | 1-2 RPS | Períodos normais de operação |
| **Taxa de Requisições (Pico)** | 2,5 RPS | Cenários de alta demanda |

### 2.1.5 Estratégias de Crescimento e Evolução

&emsp;A proposta de evolução do sistema de gestão de portfólio do Metrô de São Paulo tem como foco estabelecer uma **arquitetura escalável e segura**, capaz de **integrar agentes de Inteligência Artificial** para apoiar a automação e o gerenciamento inteligente dos projetos corporativos.

&emsp;A estratégia de crescimento busca fortalecer três pilares: **escalabilidade técnica, inteligência operacional e confiabilidade das informações**, garantindo que o ambiente atual (baseado em Miro, SharePoint, Power Automate e Power BI) possa evoluir sem comprometer a integridade e rastreabilidade dos dados.

#### Principais diretrizes e metas:

&emsp;As ações estratégicas estão estruturadas em quatro eixos principais, diretamente relacionados aos RNFs:

  1. Escalabilidade e Desempenho
  - Reestruturação da arquitetura para suportar até 100 usuários simultâneos e 300 projetos ativos, com capacidade elástica para escalar horizontalmente de acordo com a carga de requisições. 
  - Implementação de balanceamento de carga e monitoramento dinâmico de desempenho, garantindo tempo médio de resposta abaixo de 1 segundo mesmo em picos de 5.000 requisições.
  - Adoção de técnicas de cache e indexação inteligente para acelerar consultas e minimizar sobrecarga nos módulos de IA.


  2. Disponibilidade e Recuperação de Falhas
  - Criação de um modelo de arquitetura distribuída e tolerante a falhas, com failover automático entre instâncias críticas (ex.: banco de dados e camada de aplicação).
  - Implementação de políticas de backup contínuo e replicação ativa, reduzindo o tempo médio de recuperação (MTTR) para menos de 5 segundos em casos de falha.
  - Monitoramento em tempo real e alertas automáticos para incidentes, garantindo disponibilidade mínima de 99,5%.


  3. Segurança e Governança de Dados
  - Implementação de camadas de defesa contra injeções de comandos e acessos indevidos, com detecção e bloqueio automático de tentativas maliciosas.
  - Garantia de rastreabilidade completa das tentativas de acesso, integrando logs e auditorias a sistemas de alerta e análise de segurança.


  4. Rastreabilidade e Auditoria de Interações
  - Criação de um sistema centralizado de logs que registre 100% das ações executadas por usuários e agentes de IA, garantindo integridade e não repúdio.
  - Utilização de verificação por hash e consultas otimizadas para recuperação de registros em menos de 2 segundos.


  5. Evolução e Integração Inteligente
  - Preparar a arquitetura para futuras integrações com IA generativa, automação cognitiva e relatórios preditivos, priorizando sempre o controle e a auditabilidade das informações processadas.
  - Expandir gradualmente o ecossistema tecnológico do Metrô, mantendo compatibilidade com o Microsoft Power Platform, SharePoint e Copilot, promovendo uma evolução segura e sustentável.


&emsp;Essas estratégias consolidam uma base técnica e ética para o uso de Inteligência Artificial no Metrô-SP, garantindo que o sistema evolua com eficiência, rastreabilidade e conformidade, sem comprometer a segurança ou a privacidade institucional.

## 2.2 Riscos e Oportunidades
_(Identifique riscos e oportunidades associados ao sistema atual, considerando aspectos técnicos, de negócio e legais.)_

### 2.2.1 Matriz de Riscos
_(Insira aqui uma tabela com probabilidade × impacto dos riscos identificados.)_

### 2.2.2 Riscos ligados ao sistema
_(Liste vulnerabilidades técnicas, de negócio ou de conformidade legal observadas no sistema.)_

### 2.2.3 Oportunidades de melhoria dos SLAs
_(Descreva possibilidades de aprimorar níveis de serviço, incluindo segurança, disponibilidade, desempenho e tolerância a falhas.)_

# 3. Visão de Modelo Comportamental (Simulação do Sistema Atual)

Esta seção apresenta a **modelagem comportamental** do sistema atual de gestão de projetos do Metrô de São Paulo e os **experimentos de simulação** realizados para observar seu comportamento frente a cenários críticos, especialmente aqueles relacionados a **Requisitos Não Funcionais (RNFs)**, como desempenho, segurança, privacidade e tolerância a falhas.

A análise comportamental do sistema atual baseia-se na arquitetura existente que utiliza aplicações como Miro para brainstorming de projetos e SharePoint para armazenamento e validação de informações. O foco está em identificar limitações e vulnerabilidades que justifiquem a implementação de uma nova arquitetura escalável com integração de agentes de IA.

---

## 3.1 RNFs do Sistema Atual

A análise do sistema atual de gestão de projetos do Metrô de São Paulo revela uma **ausência crítica de requisitos não funcionais adequados**. O sistema atual baseado em Miro e SharePoint **não possui implementação adequada** dos RNFs essenciais para uma gestão de projetos escalável.

A tabela abaixo compara o **estado atual (deficiente)** versus os **requisitos que a nova arquitetura deveria ter**:

| **Requisito Não Funcional** | **Estado Atual do Metrô (Deficiente)** | **Arquitetura Reformada (Desejada)** |
|------------------------------|----------------------------------------|--------------------------------------|
| **Escalabilidade** | • Dependência total de ferramentas externas sem controle<br>• Ausência de balanceamento de carga<br>• Processamento sequencial manual<br>• Limitação de usuários simultâneos | • Arquitetura escalável com auto-scaling<br>• Balanceamento de carga automático<br>• Processamento paralelo com IA<br>• Suporte a milhares de usuários simultâneos |
| **Disponibilidade** | • Dependência de SLA de terceiros (Miro/SharePoint)<br>• Ausência de redundância<br>• Sem monitoramento proativo<br>• Downtime não controlado | • SLA de 99.9% garantido<br>• Redundância e failover automático<br>• Monitoramento 24/7<br>• Recuperação automática em <5s |
| **Segurança** | • Controle de acesso limitado<br>• Ausência de auditoria<br>• Dependência de políticas externas<br>• Dados expostos em ferramentas de terceiros | • Controle de acesso granular<br>• Auditoria completa de todas as ações<br>• Criptografia end-to-end<br>• Conformidade com LGPD |
| **Rastreabilidade** | • Logs limitados das ferramentas<br>• Ausência de trilha integrada<br>• Dificuldade de correlação<br>• Sem compliance automático | • Logs detalhados de todas as ações<br>• Trilha de auditoria integrada<br>• Correlação automática de eventos<br>• Compliance e relatórios automáticos |
| **Performance** | • Dependência de conectividade externa<br>• Processamento manual<br>• Ausência de cache<br>• Tempos de resposta imprevisíveis | • Processamento local otimizado<br>• Cache inteligente<br>• Tempo de resposta <1s<br>• Otimização com IA |
| **Tolerância a Falhas** | • Sem mecanismos de recuperação<br>• Falha única pode parar todo o sistema<br>• Perda de dados em caso de falha<br>• Recuperação manual | • Recuperação automática<br>• Redundância em múltiplas camadas<br>• Zero perda de dados<br>• Failover transparente |

### **Principais Lacunas Identificadas no Sistema Atual:**

1. **Ausência de Controle Arquitetural:** O Metrô não possui controle sobre a infraestrutura das ferramentas externas
2. **Dependência Crítica:** Falha em qualquer ferramenta externa impacta todo o processo
3. **Segurança Comprometida:** Dados sensíveis dos projetos expostos a políticas de terceiros
4. **Escalabilidade Limitada:** Impossibilidade de crescer conforme demanda
5. **Auditoria Inadequada:** Dificuldade de compliance e rastreamento de ações

### **Justificativa para Nova Arquitetura:**

A **ausência desses RNFs no sistema atual** justifica completamente a necessidade de uma arquitetura reformada que implemente adequadamente todos esses requisitos, garantindo:
- **Controle total** sobre a infraestrutura
- **Segurança robusta** para dados sensíveis
- **Escalabilidade** para crescimento futuro
- **Disponibilidade** garantida para operações críticas
- **Rastreabilidade** completa para compliance

---

## 3.2 Estrutura Estática do Modelo
_(Apresente os elementos e parâmetros da simulação, evidenciando como o modelo representa o comportamento do sistema atual.)_

- **Elementos do sistema envolvidos nos RNFs selecionados:**  
  _(Liste os componentes, módulos, serviços ou processos do sistema que serão considerados na simulação, e associe-os aos RNFs analisados.)_

- **Estrutura e conexões entre os elementos:**  
  _(Descreva as relações entre os componentes simulados e justifique a escolha dos parâmetros de simulação. Pode incluir diagramas, fluxos de dados, filas, threads e elementos paralelos de processamento.)_

---

## 3.3 Modelagem Comportamental e Simulação dos RNFs

&nbsp; Esta seção apresenta a **modelagem comportamental** e os **experimentos de simulação** do sistema atual de gestão de projetos do Metrô de São Paulo, com foco na análise dos **Requisitos Não Funcionais (RNFs)** e suas limitações. O objetivo é demonstrar, através de **análise hipotética**, como o sistema atual se comportaria caso os RNFs fossem implementados, evidenciando as **limitações críticas** e **vulnerabilidades** que justificam a necessidade de uma nova arquitetura. A análise está organizada em três componentes: **3.3.1 Modelagem Comportamental** (cenários de simulação planejados), **3.3.2 Cenários Simulados** (resultados hipotéticos demonstrando falhas críticas) e **3.4 Consolidação dos Resultados** (integração dos achados e implicações arquiteturais).

### 3.3.1 Modelagem Comportamental

&nbsp; Esta seção descreve os cenários de simulação planejados, com foco nas melhorias dos Requisitos Não Funcionais (RNFs) da arquitetura proposta para integrar agentes de IA ao sistema de gestão de projetos do Metrô.  

&nbsp; Os cenários foram definidos de forma a avaliar o comportamento da solução em condições críticas e demonstrar melhorias de escalabilidade, disponibilidade, segurança e rastreabilidade, conforme as necessidades identificadas no projeto.  


#### **Cenário 1 – Escalabilidade e Acessos Simultâneos**  
**RNF relacionado:** Escalabilidade.  
**Objetivo:** Avaliar a capacidade do sistema de suportar múltiplos acessos simultâneos de agentes de IA e usuários humanos sem degradação do desempenho.  

**Condições de Simulação Planejadas:**  
- Execução de testes de carga com 500, 1.000 e 5.000 requisições simultâneas aos módulos de gestão de projetos.  
- Cada requisição envolve consultas de dados, geração de relatórios e interações com os agentes de IA.  

**Métricas Avaliadas:**  
- Tempo médio de resposta (ms).  
- Taxa de sucesso de requisições (%).  
- Uso de CPU e memória do servidor.  
- Número de instâncias escaladas automaticamente pela arquitetura.  

**Indicadores de Melhoria Esperados:**  
- Escalonamento automático proporcional à carga.  
- Manutenção do tempo médio de resposta abaixo de 1 segundo.  


#### **Cenário 2 – Disponibilidade e Recuperação de Falhas**  
**RNF relacionado:** Disponibilidade.  
**Objetivo:** Validar a continuidade de operação do sistema diante de falhas e interrupções de rede.  

**Condições de Simulação Planejadas:**  
- Desligamento forçado de um nó de processamento durante operações ativas.  
- Indisponibilidade temporária do banco de dados principal, acionando o failover para a réplica.  

**Métricas Avaliadas:**  
- Tempo médio de recuperação (MTTR).  
- Percentual de indisponibilidade (%).  
- Número de transações perdidas.  

**Indicadores de Melhoria Esperados:**  
- Recuperação automática do serviço em até 5 segundos.  
- Zero perda de dados durante a falha.  


#### **Cenário 3 – Segurança e Controle de Acessos**  
**RNF relacionado:** Segurança.  
**Objetivo:** Avaliar a resistência do sistema frente a tentativas de acesso indevido e injeções de comandos maliciosos via agentes de IA.  

**Condições de Simulação Planejadas:**  
- Execução de 1.000 requisições autenticadas e 200 tentativas de acesso não autorizado.  
- Envio de comandos maliciosos e consultas diretas simuladas ao banco de dados.  

**Métricas Avaliadas:**  
- Taxa de acessos bem-sucedidos (%).  
- Taxa de acessos bloqueados (%).  
- Tempo médio de resposta a alertas de segurança.  

**Indicadores de Melhoria Esperados:**  
- 100% de bloqueio de acessos indevidos.  
- Registro e rastreabilidade completa das tentativas de ataque.  


#### **Cenário 4 – Rastreabilidade e Auditoria de Interações**  
**RNF relacionado:** Rastreabilidade.  
**Objetivo:** Garantir que todas as ações dos agentes de IA e usuários sejam registradas e consultáveis de forma íntegra e auditável.  

**Condições de Simulação Planejadas:**  
- Execução de 500 tarefas automatizadas (ex.: geração de relatórios, atualização de cronogramas).  
- Consultas de verificação às trilhas de auditoria e logs do sistema.  

**Métricas Avaliadas:**  
- Percentual de ações registradas corretamente (%).  
- Tempo médio de recuperação de registros (ms).  
- Verificação de integridade por hash.  

**Indicadores de Melhoria Esperados:**  
- 100% das ações registradas e auditáveis.  
- Recuperação de logs em menos de 2 segundos.  


#### **Consolidação dos Cenários e Foco nas Melhorias de RNFs**

&nbsp; Cada cenário proposto visa evidenciar a evolução dos RNFs em relação à arquitetura anterior, por meio de medições quantitativas e análises qualitativas.  

&nbsp; Os resultados das simulações serão apresentados em tabelas e gráficos contendo:  
- Registros totais de requisições processadas.  
- Registros de falhas e execuções corretas.  
- Tempos de resposta médios e máximos.  
- Taxas de segurança e rastreabilidade.  

&nbsp; Essas simulações permitirão demonstrar, de forma mensurável, as melhorias de desempenho, confiabilidade e segurança obtidas com a nova arquitetura escalável implementada no contexto do Metrô.

### 3.3.2 Cenários Simulados

**Análise Hipotética dos Cenários Simulados com RNFs Implementados**

Considerando que o sistema atual do Metrô de São Paulo **não possui implementação adequada dos RNFs**, esta seção apresenta uma **análise hipotética** dos possíveis cenários simulados caso os RNFs fossem implementados, baseada nas limitações identificadas e nos cenários planejados na seção 3.3.1.

#### **Cenário 1 – Escalabilidade e Acessos Simultâneos (Hipotético)**

**Situação Atual vs. Cenário com RNFs Implementados:**

| **Métrica** | **Sistema Atual (Sem RNFs)** | **Cenário Hipotético (Com RNFs)** | **Resultado Esperado** |
|-------------|------------------------------|-----------------------------------|------------------------|
| **Usuários Simultâneos** | 30-50 usuários (limitado) | 100+ usuários | ❌ **Degradação Severa** |
| **Tempo de Resposta** | 2-5 segundos (imprevisível) | <1 segundo | ❌ **Falhas Frequentes** |
| **Taxa de Sucesso** | 70-80% (dependência externa) | 95%+ | ❌ **Sobrecarga do Sistema** |
| **Escalabilidade** | Manual e limitada | Automática | ❌ **Colapso do Sistema** |

**Resultados Hipotéticos Esperados:**
- **Degradação Severa do Desempenho:** Com 100+ usuários simultâneos, o sistema atual entraria em colapso
- **Falhas de Conectividade:** Dependência de ferramentas externas (Miro/SharePoint) causaria timeouts
- **Perda de Dados:** Ausência de mecanismos de recuperação resultaria em perda de informações
- **Indisponibilidade Total:** Sistema ficaria inoperante durante picos de demanda

#### **Cenário 2 – Disponibilidade e Recuperação de Falhas (Hipotético)**

**Situação Atual vs. Cenário com RNFs Implementados:**

| **Métrica** | **Sistema Atual (Sem RNFs)** | **Cenário Hipotético (Com RNFs)** | **Resultado Esperado** |
|-------------|------------------------------|-----------------------------------|------------------------|
| **MTTR** | 30-60 minutos (manual) | <5 segundos | ❌ **Recuperação Impossível** |
| **Disponibilidade** | 85-90% (dependência externa) | 99.9% | ❌ **Downtime Prolongado** |
| **Perda de Dados** | Alta (sem backup) | Zero | ❌ **Perda Total de Dados** |
| **Failover** | Não existe | Automático | ❌ **Sistema Indisponível** |

**Resultados Hipotéticos Esperados:**
- **Falha Total do Sistema:** Ausência de redundância causaria indisponibilidade completa
- **Perda Massiva de Dados:** Sem mecanismos de backup, todos os dados seriam perdidos
- **Recuperação Manual Prolongada:** Dependência de intervenção humana para restabelecer serviços
- **Impacto Operacional Crítico:** Projetos paralisados por horas ou dias

#### **Cenário 3 – Segurança e Controle de Acessos (Hipotético)**

**Situação Atual vs. Cenário com RNFs Implementados:**

| **Métrica** | **Sistema Atual (Sem RNFs)** | **Cenário Hipotético (Com RNFs)** | **Resultado Esperado** |
|-------------|------------------------------|-----------------------------------|------------------------|
| **Controle de Acesso** | Limitado (políticas externas) | Granular | ❌ **Vulnerabilidades Críticas** |
| **Auditoria** | Parcial (logs limitados) | Completa | ❌ **Acessos Não Autorizados** |
| **Criptografia** | Básica (ferramentas externas) | End-to-end | ❌ **Exposição de Dados Sensíveis** |
| **Detecção de Ataques** | Não existe | Automática | ❌ **Invasões Não Detectadas** |

**Resultados Hipotéticos Esperados:**
- **Vulnerabilidades Críticas:** Dados sensíveis dos projetos expostos a acessos não autorizados
- **Falta de Rastreabilidade:** Impossibilidade de identificar quem acessou ou modificou informações
- **Compliance Violado:** Violação de regulamentações de segurança e privacidade
- **Riscos Legais:** Exposição de informações confidenciais do Metrô

#### **Cenário 4 – Rastreabilidade e Auditoria (Hipotético)**

**Situação Atual vs. Cenário com RNFs Implementados:**

| **Métrica** | **Sistema Atual (Sem RNFs)** | **Cenário Hipotético (Com RNFs)** | **Resultado Esperado** |
|-------------|------------------------------|-----------------------------------|------------------------|
| **Registro de Ações** | 30-40% (logs limitados) | 100% | ❌ **Perda de Rastreabilidade** |
| **Tempo de Recuperação** | 5-10 minutos | <2 segundos | ❌ **Logs Inacessíveis** |
| **Integridade** | Não verificada | Hash verification | ❌ **Dados Corrompidos** |
| **Compliance** | Manual e incompleto | Automático | ❌ **Violação de Regulamentações** |

**Resultados Hipotéticos Esperados:**
- **Perda Total de Rastreabilidade:** Impossibilidade de auditar ações e mudanças
- **Logs Inacessíveis:** Sistema de logs não funcional ou corrompido
- **Violação de Compliance:** Não atendimento a regulamentações de auditoria
- **Responsabilidade Legal:** Impossibilidade de identificar responsáveis por ações

---

## 3.4 Consolidação dos Resultados da Simulação

**Análise Integrada dos Resultados Hipotéticos das Simulações**

Esta seção consolida os resultados esperados pela análise hipotética realizada nos cenários simulados, destacando os principais achados e suas implicações para a arquitetura do sistema de gestão de projetos do Metrô de São Paulo.

#### **Tabela de Resultados Esperados**

| **RNF Analisado** | **Cenário Atual** | **Resultado Hipotético** | **Impacto Crítico** | **Justificativa** |
|-------------------|-------------------|---------------------------|---------------------|-------------------|
| **Escalabilidade** | 30-50 usuários | Colapso total com 100+ usuários | ❌ **Sistema Inoperante** | Ausência de balanceamento de carga |
| **Disponibilidade** | 85-90% | Downtime prolongado | ❌ **Perda Total de Dados** | Sem redundância ou failover |
| **Segurança** | Controle limitado | Vulnerabilidades críticas | ❌ **Exposição de Dados** | Dependência de políticas externas |
| **Rastreabilidade** | 30-40% de logs | Perda total de auditoria | ❌ **Violação de Compliance** | Sistema de logs inadequado |

### **Principais Falhas Esperadas**

#### **1. Degradação Crítica de Performance**
- **Taxa de Falhas:** 80-90% em cenários de alta demanda
- **Tempo de Resposta:** Aumento de 300-500% em situações de pico
- **Capacidade:** Limitação crítica a 50 usuários simultâneos
- **Consequência:** Sistema inoperante durante períodos de alta demanda

#### **2. Vulnerabilidades de Segurança Críticas**
- **Exposição de Dados:** 100% dos dados sensíveis vulneráveis
- **Controle de Acesso:** Ausência de mecanismos de autenticação robustos
- **Auditoria:** Impossibilidade de rastrear acessos e modificações
- **Consequência:** Violação de regulamentações e riscos legais

#### **3. Indisponibilidade Operacional**
- **Downtime:** 15-20% de indisponibilidade em situações normais
- **Recuperação:** 30-60 minutos para restabelecer serviços
- **Perda de Dados:** Ausência de mecanismos de backup
- **Consequência:** Paralisação de projetos críticos

#### **4. Falhas de Compliance e Auditoria**
- **Rastreabilidade:** 60-70% das ações não auditáveis
- **Logs:** Sistema de registro inadequado e corrompido
- **Integridade:** Ausência de verificação de integridade
- **Consequência:** Violação de regulamentações de auditoria

### **Recomendações Arquiteturais**

#### **1. Implementação de Nova Arquitetura**
- **Reestruturação completa** do sistema atual
- **Migração controlada** dos dados existentes
- **Implementação gradual** dos RNFs
- **Validação rigorosa** antes da produção

#### **2. Mecanismos de Tolerância a Falhas**
- **Redundância** em múltiplas camadas
- **Failover automático** entre instâncias
- **Backup contínuo** e recuperação automática
- **Monitoramento 24/7** com alertas proativos

#### **3. Segurança e Compliance**
- **Controle de acesso granular** e autenticação robusta
- **Criptografia end-to-end** para dados sensíveis
- **Auditoria completa** de todas as ações
- **Conformidade** com regulamentações (LGPD, etc.)

#### **4. Escalabilidade e Performance**
- **Arquitetura elástica** com auto-scaling
- **Balanceamento de carga** automático
- **Cache inteligente** para otimização
- **Processamento paralelo** com IA

---

# 4. Arquitetura do Sistema Novo – Especificação de Requisitos

Esta seção descreve a **evolução do sistema** a partir da análise do estado atual, detalhando os **requisitos funcionais e não funcionais** (com base nas normas ISO/IEC 25010 e ISO/IEC 10746).  
O objetivo é evidenciar as melhorias esperadas no sistema novo, considerando **usabilidade, desempenho, segurança, confiabilidade e tolerância a falhas**.

---

## 4.1 Requisitos Não Funcionais do Sistema Novo
_(Mapeie os requisitos não funcionais priorizados para orientar o desenvolvimento do novo sistema.)_

- **Requisitos vulneráveis no sistema atual:** _(Liste e descreva sucintamente os RNFs com fragilidades observadas.)_  
- **Seleção dos RNFs críticos (2 a 4):** _(Justifique a escolha dos RNFs que terão foco no projeto, relacionando-os às estratégias do negócio e aos riscos identificados.)_

---

## 4.2 Justificativas para RNFs
_(Apresente a argumentação técnica e de negócio para os RNFs selecionados, evidenciando os ganhos projetados para o novo sistema.)_

- **Controle de riscos e mitigação:** _(Explique como o novo sistema corrige os problemas identificados no atual.)_  

---

## 4.3 Melhorias Esperadas com Implementação de RNFs

- **Melhorias em usabilidade e experiência:** _(Descreva ganhos esperados de eficiência e confiabilidade.)_  
- **Indicadores e evidências de melhoria:** _(Liste métricas que poderão comprovar os resultados esperados.)_

---

## 4.4 Consolidação dos Requisitos e Diretrizes para a Nova Arquitetura
_(Sintetize os requisitos funcionais e não funcionais que nortearão o projeto da nova arquitetura.)_

---

# 5. Avaliação dos Mecanismos Utilizados no Sistema Atual (Diagnóstico ATAM)

Esta seção detalha os **mecanismos e componentes arquiteturais** do sistema atual que justificam as **limitações e vulnerabilidades** observadas nos RNFs.  
O objetivo é compreender **as causas dos defeitos** e construir a base para propor **táticas e soluções evolutivas**.

---

## 5.1 Revisão do Mapa de RNFs e Vulnerabilidades
_(Apresente a consolidação dos RNFs analisados no sistema atual, destacando vulnerabilidades e controles existentes.)_

---

## 5.2 Táticas Arquiteturais e Componentes Adotados
_(Descreva os componentes e táticas arquiteturais implementadas para monitorar, atender e recuperar os RNFs.)_

---

## 5.3 Análise de Causas e Impactos
_(Apresente uma análise integrada das causas das vulnerabilidades encontradas e seus impactos sobre o negócio e o desempenho do sistema.)_

---

# 6. Especificação da Solução Técnica do Sistema Novo

_(Descreva como a nova arquitetura elimina as vulnerabilidades e implementa melhorias técnicas e de negócio.)_

---

## 6.1 Revisão do Mapa de RNFs do Sistema Novo
_(Consolide os RNFs aprimorados, detalhando entradas, saídas e controles planejados.)_

---

## 6.2 Táticas Arquiteturais e Componentes Adotados
_(Apresente as táticas e os componentes técnicos que garantem o atendimento dos RNFs.)_

---

## 6.3 Justificativas Arquiteturais e Racional das Decisões
_(Relacione decisões arquiteturais às vulnerabilidades anteriores e às metas de negócio.)_

---

## 6.4 Consolidação Técnica da Solução
_(Sintetize as decisões e seus impactos sobre a qualidade do sistema.)_

---

# 7. Simulação do Sistema Novo
_(Apresente a simulação comparativa entre o sistema atual e o sistema novo, evidenciando as melhorias obtidas nos RNFs selecionados.)_

---

# 8. Implementação dos Mecanismos Arquiteturais
_(Descreva brevemente a implementação prática das táticas e componentes arquiteturais definidos.)_

---

## 8.1 Testes e Validação dos Mecanismos
_(Resuma os testes automatizados criados para validar os mecanismos implementados e indique onde estão localizados no repositório.)_

---

# 9. Revisão do Modelo de Simulação do Sistema Novo
_(Apresente a revisão do modelo de simulação e a comparação entre os resultados do sistema atual e do novo, incluindo condições normais, de exceção e de limite.)_

---

# 10. Ajustes na Implementação
_(Liste os ajustes realizados após os testes, indicando melhorias, critérios de aceitação e evidências no repositório.)_

---

# 11. Evidências de Testes Não Funcionais
_(Apresente os resultados e análises dos testes automatizados não funcionais realizados após os ajustes de implementação.)_

---

# 12. Medição e Avaliação do Sistema Novo
_(Descreva como as medições estruturais e comportamentais comprovam o aprimoramento arquitetural obtido.)_

---

# 13. Tradeoffs Arquiteturais
_(Analise os ganhos e perdas resultantes das decisões arquiteturais e o impacto sobre os requisitos não funcionais e o negócio.)_

---

# 14. [A construir]
_(As próximas seções serão adicionadas conforme os artefatos da Sprint 5 forem definidos.)_

# Referências
_conteúdo_

