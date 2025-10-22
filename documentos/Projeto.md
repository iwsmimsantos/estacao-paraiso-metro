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
- **Volumes operacionais:**  
  _(Informe dados quantitativos como número de usuários, transações, registros, incidentes ou falhas relevantes.)_

### 2.1.5 Estratégias de Crescimento e Evolução
- **Estratégias de crescimento:**  
  _(Explique planos ou estratégias de evolução do sistema frente aos desafios identificados.)_


## 2.2 Riscos e Oportunidades
_(Identifique riscos e oportunidades associados ao sistema atual, considerando aspectos técnicos, de negócio e legais.)_

### 2.2.1 Matriz de Riscos
_(Insira aqui uma tabela com probabilidade × impacto dos riscos identificados.)_

### 2.2.2 Riscos ligados ao sistema
_(Liste vulnerabilidades técnicas, de negócio ou de conformidade legal observadas no sistema.)_

### 2.2.3 Oportunidades de melhoria dos SLAs
_(Descreva possibilidades de aprimorar níveis de serviço, incluindo segurança, disponibilidade, desempenho e tolerância a falhas.)_

---

# 3. Visão de Modelo Comportamental (Simulação do Sistema Atual)

Esta seção deve apresentar a **modelagem comportamental** do sistema atual e os **experimentos de simulação** realizados para observar seu comportamento frente a cenários críticos, especialmente aqueles relacionados a **Requisitos Não Funcionais (RNFs)**, como desempenho, segurança, privacidade e tolerância a falhas.

---

## 3.1 RNFs do Sistema Atual

Descrever RFNs que representam o funcionamento do sistema atual de gestão de projeto do metrô

---

## 3.2 Estrutura Estática do Modelo
_(Apresente os elementos e parâmetros da simulação, evidenciando como o modelo representa o comportamento do sistema atual.)_

- **Elementos do sistema envolvidos nos RNFs selecionados:**  
  _(Liste os componentes, módulos, serviços ou processos do sistema que serão considerados na simulação, e associe-os aos RNFs analisados.)_

- **Estrutura e conexões entre os elementos:**  
  _(Descreva as relações entre os componentes simulados e justifique a escolha dos parâmetros de simulação. Pode incluir diagramas, fluxos de dados, filas, threads e elementos paralelos de processamento.)_

---

## 3.3 Modelagem Comportamental e Simulação dos RNFs
_(Seção para inserir dados sobre testagem)_

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
_(Dados de simulação, evidenciando as melhorias - Sessões de simulações detalhadas pelos cenários, massa de dados utilizados, processamentos e resultados obtidos, com apresentação dos registros e também visualização de gráficos.)_

- **Cenários de simulação:** _(Liste os cenários e parâmetros simulados.)_  
- **Dados e evidências:** _(Apresente os registros de simulação e as métricas observadas.)_

---

## 3.4 Consolidação dos Resultados da Simulação
_(Apresente uma análise integrada dos resultados obtidos nas simulações, destacando os principais achados e implicações para a arquitetura do sistema.)_

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

