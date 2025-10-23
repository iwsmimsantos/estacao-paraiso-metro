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

- [Nome do Projeto: ](#nome-do-projeto-)
  - [Nome do Grupo: ](#nome-do-grupo-)
  - [Integrantes:](#integrantes)
- [Sumário](#sumário)
- [Projeto · Módulo 08 – Arquitetura Digital Segura e Tolerante a Falhas](#projeto--módulo-08--arquitetura-digital-segura-e-tolerante-a-falhas)
- [1. Introdução](#1-introdução)
  - [1.1 Termos e Abreviações](#11-termos-e-abreviações)
  - [1.2 Contexto e Motivação](#12-contexto-e-motivação)
  - [1.3 Objetivo](#13-objetivo)
- [2. Descrição do Sistema Atual](#2-descrição-do-sistema-atual)
  - [2.1 Visão Geral e Contexto de Negócio](#21-visão-geral-e-contexto-de-negócio)
    - [2.1.1 Setor de Aplicação e Domínio](#211-setor-de-aplicação-e-domínio)
    - [2.1.2 Adição de Valor e Propósito](#212-adição-de-valor-e-propósito)
    - [2.1.3 Processos de Negócio e Fluxos Críticos](#213-processos-de-negócio-e-fluxos-críticos)
      - [2.1.3.1 Fluxo de Negócio Atual (AS-IS)](#2131-fluxo-de-negócio-atual-as-is)
    - [Fluxo do Processo AS-IS:](#fluxo-do-processo-as-is)
      - [Raia "Líder/Equipe do Projeto"](#raia-líderequipe-do-projeto)
      - [Raia "Sistema PMO (SharePoint/Power BI)"](#raia-sistema-pmo-sharepointpower-bi)
      - [2.1.3.1 Fluxo de Negócio Futuro (TO-BE)](#2131-fluxo-de-negócio-futuro-to-be)
    - [Fluxo do Processo TO-BE:](#fluxo-do-processo-to-be)
      - [Raia "Líder/Equipe do Projeto"](#raia-líderequipe-do-projeto-1)
      - [Raia "Agente de IA / Camada de Arquitetura"](#raia-agente-de-ia--camada-de-arquitetura)
      - [Raia "Sistema PMO (Base Estruturada/Power BI)"](#raia-sistema-pmo-base-estruturadapower-bi)
      - [2.1.3.3 Requisitos Arquiteturais Chave](#2133-requisitos-arquiteturais-chave)
    - [2.1.4 Volumes Operacionais e Capacidade](#214-volumes-operacionais-e-capacidade)
    - [2.1.5 Estratégias de Crescimento e Evolução](#215-estratégias-de-crescimento-e-evolução)
  - [2.2 Riscos e Oportunidades](#22-riscos-e-oportunidades)
    - [2.2.1 Matriz de Riscos](#221-matriz-de-riscos)
    - [2.2.2 Riscos ligados ao sistema](#222-riscos-ligados-ao-sistema)
    - [2.2.3 Oportunidades de melhoria dos SLAs](#223-oportunidades-de-melhoria-dos-slas)
- [3. Visão de Modelo Comportamental (Simulação do Sistema Atual)](#3-visão-de-modelo-comportamental-simulação-do-sistema-atual)
  - [3.1 RNFs do Sistema Atual](#31-rnfs-do-sistema-atual)
  - [3.2 Estrutura Estática do Modelo](#32-estrutura-estática-do-modelo)
  - [3.3 Modelagem Comportamental e Simulação dos RNFs](#33-modelagem-comportamental-e-simulação-dos-rnfs)
    - [3.3.1 Modelagem Comportamental](#331-modelagem-comportamental)
    - [3.3.2 Cenários Simulados](#332-cenários-simulados)
  - [3.4 Consolidação dos Resultados da Simulação](#34-consolidação-dos-resultados-da-simulação)
- [4. Arquitetura do Sistema Novo – Especificação de Requisitos](#4-arquitetura-do-sistema-novo--especificação-de-requisitos)
  - [4.1 Requisitos Não Funcionais do Sistema Novo](#41-requisitos-não-funcionais-do-sistema-novo)
  - [4.2 Justificativas para RNFs](#42-justificativas-para-rnfs)
  - [4.3 Melhorias Esperadas com Implementação de RNFs](#43-melhorias-esperadas-com-implementação-de-rnfs)
  - [4.4 Consolidação dos Requisitos e Diretrizes para a Nova Arquitetura](#44-consolidação-dos-requisitos-e-diretrizes-para-a-nova-arquitetura)
- [5. Avaliação dos Mecanismos Utilizados no Sistema Atual (Diagnóstico ATAM)](#5-avaliação-dos-mecanismos-utilizados-no-sistema-atual-diagnóstico-atam)
  - [5.1 Revisão do Mapa de RNFs e Vulnerabilidades](#51-revisão-do-mapa-de-rnfs-e-vulnerabilidades)
  - [5.2 Táticas Arquiteturais e Componentes Adotados](#52-táticas-arquiteturais-e-componentes-adotados)
  - [5.3 Análise de Causas e Impactos](#53-análise-de-causas-e-impactos)
- [6. Especificação da Solução Técnica do Sistema Novo](#6-especificação-da-solução-técnica-do-sistema-novo)
  - [6.1 Revisão do Mapa de RNFs do Sistema Novo](#61-revisão-do-mapa-de-rnfs-do-sistema-novo)
  - [6.2 Táticas Arquiteturais e Componentes Adotados](#62-táticas-arquiteturais-e-componentes-adotados)
  - [6.3 Justificativas Arquiteturais e Racional das Decisões](#63-justificativas-arquiteturais-e-racional-das-decisões)
  - [6.4 Consolidação Técnica da Solução](#64-consolidação-técnica-da-solução)
- [7. Simulação do Sistema Novo](#7-simulação-do-sistema-novo)
- [8. Implementação dos Mecanismos Arquiteturais](#8-implementação-dos-mecanismos-arquiteturais)
  - [8.1 Testes e Validação dos Mecanismos](#81-testes-e-validação-dos-mecanismos)
- [9. Revisão do Modelo de Simulação do Sistema Novo](#9-revisão-do-modelo-de-simulação-do-sistema-novo)
- [10. Ajustes na Implementação](#10-ajustes-na-implementação)
- [11. Evidências de Testes Não Funcionais](#11-evidências-de-testes-não-funcionais)
- [12. Medição e Avaliação do Sistema Novo](#12-medição-e-avaliação-do-sistema-novo)
- [13. Tradeoffs Arquiteturais](#13-tradeoffs-arquiteturais)
- [14. \[A construir\]](#14-a-construir)
- [Referências](#referências)

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

_(Descreva o sistema atual sob a ótica arquitetural e de negócio, destacando seus pontos fortes e oportunidades de melhoria.)_

### 2.1.1 Setor de Aplicação e Domínio

- **Setor de aplicação:** _(Informe o(s) setor(es) ou domínio(s) de atuação do sistema.)_

### 2.1.2 Adição de Valor e Propósito

- **Adição de valor:** _(Explique como o sistema agrega valor ao negócio ou aos usuários.)_

### 2.1.3 Processos de Negócio e Fluxos Críticos

#### 2.1.3.1 Fluxo de Negócio Atual (AS-IS)

O fluxo atual de gestão e monitoramento do portfólio de projetos é predominantemente **manual** e distribuído entre diversas ferramentas do ecossistema Microsoft e o Miro.

&emsp; A seguir, a descrição do fluxo de negócio atual (AS-IS) para o monitoramento e gestão do portfólio de projetos no Metrô-SP.

<div align="center">
<sub>Figura 2.1.3.1.1 - Diagrama do Fluxo de Negócio AS-IS (Representação Conceitual)</sub><br>
<img src="img/section2/as-is.png" width="250%"><br>
<sup>Fonte: Material produzido pelos autores (2025) </sup>
</div>

&emsp; Este diagrama representa o processo atual, que se inicia com o planejamento do projeto e se estende ao monitoramento mensal e semestral, com destaque para a dependência de ações manuais para a estruturação e consolidação dos dados.

### Fluxo do Processo AS-IS:

#### Raia "Líder/Equipe do Projeto"

- **Início: Planejamento Inicial**

  - O processo se inicia com o planejamento do projeto e a criação do **Mapa de Benefícios** em uma ferramenta de colaboração visual (Miro).
  - O Líder do Projeto, junto com a equipe, elabora o Termo de Abertura do Projeto (TAP), Entregas, Marcos e Cronograma, utilizando documentos de escritório (MS Word/Excel).

- **Transferência Manual de Dados (Miro -> SharePoint)**

  - O Líder/Equipe **transporta manualmente** as informações do Mapa de Benefícios e outros documentos para as **Listas do SharePoint** (a base de dados estruturada do PMO).

- **Reporte Mensal de Status**
  - Mensalmente, o Líder/Equipe informa o status do projeto (qualitativo), percentual de avanço e riscos nas Listas do SharePoint.

#### Raia "Sistema PMO (SharePoint/Power BI)"

- **Armazenamento de Dados**

  - O SharePoint armazena os dados estruturados do projeto e o status mensal reportado.

- **Processamento e Automação (Power Automate)**

  - O Power Automate executa fluxos de trabalho básicos para automação de processos, como notificações ou movimentação de itens nas listas.

- **Geração de Relatórios (Power BI/Documentos)**

  - O Power BI gera relatórios de indicadores do portfólio com base nos dados do SharePoint.
  - O PMO consolida as informações do Power BI e dos documentos de escritório para gerar o **Relatório Mensal** e o **Balanço Semestral** (utilizando MS Word, Excel, PowerPoint).

- **Processo Concluído**
  - O processo de monitoramento mensal/semestral é concluído com a geração e distribuição dos relatórios.

#### 2.1.3.1 Fluxo de Negócio Futuro (TO-BE)

O fluxo futuro (TO-BE) incorpora um **Agente de IA** e uma **Camada de Arquitetura** que centraliza a informação e automatiza tarefas de alto valor, focando em integridade, rastreabilidade e suporte proativo.

&emsp; A seguir, a descrição do fluxo de negócio **TO-BE** utilizando a nova arquitetura proposta, com o objetivo de reduzir a dependência de processos manuais e maximizar a qualidade e a precisão dos dados.

<div align="center">
<sub>Figura 2.1.3.1.1 - Diagrama do Fluxo de Negócio TO-BE (Representação Conceitual)</sub><br>
<img src="img/section2/to-be.png" width="150%"><br>
<sup>Fonte: Material produzido pelos autores (2025) </sup>
</div>

&emsp; Este diagrama representa um processo automatizado e inteligente, onde o Agente de IA atua como um assistente proativo e um validador de qualidade, garantindo que os dados inseridos sejam estruturados e consistentes desde o início.

### Fluxo do Processo TO-BE:

#### Raia "Líder/Equipe do Projeto"

- **Início: Planejamento Inicial**

  - O Líder/Equipe inicia o planejamento. O **Agente de IA** é acionado para auxiliar no preenchimento do Mapa de Benefícios e do Termo de Abertura (TAP), orientando e esclarecendo dúvidas sobre normativos.

- **Inserção de Dados na Base Estruturada**

  - Os dados de planejamento (TAP, Entregas, Cronograma) são inseridos diretamente na **Base Estruturada** (ex: Listas de SharePoint ou nova plataforma), com o auxílio do Agente de IA.

- **Reporte Mensal de Status**
  - O Líder/Equipe reporta o status do projeto. O **Agente de IA** envia lembretes proativos sobre pendências e oferece apoio para o preenchimento.

#### Raia "Agente de IA / Camada de Arquitetura"

- **Validação e Análise de Qualidade (IA)**

  - O **Agente de IA** avalia a qualidade dos dados inseridos (ex: verifica se há poucos marcos, se o cronograma concentra entregas no final do ano).
  - O Agente de IA define uma **nota de avaliação** e sugere melhorias para o Líder/Equipe.

- **Monitoramento e Previsão (IA)**

  - O Agente de IA monitora o avanço do projeto e realiza a **previsão de obtenção do objetivo** em determinado prazo.

- **Geração Automatizada de Conteúdo (IA)**
  - O Agente de IA gera automaticamente prévias de:
    - Apresentação da partida do portfólio.
    - Apresentação mensal para a diretoria (destacando status e indicadores).
    - Relatório final de fechamento do portfólio e de cada projeto.

#### Raia "Sistema PMO (Base Estruturada/Power BI)"

- **Armazenamento Centralizado e Rastreável**

  - A **Base Estruturada** armazena todos os dados de planejamento e status.
  - A **Camada de Arquitetura** garante a rastreabilidade e o não repúdio de todas as ações e consultas.

- **Geração de Relatórios Finais**

  - O Power BI ou a nova plataforma utiliza os dados validados e analisados pela IA para gerar os relatórios finais.

- **Processo Concluído**
  - O processo de monitoramento é concluído com a distribuição dos relatórios automatizados e de alta precisão.

#### 2.1.3.3 Requisitos Arquiteturais Chave

A nova arquitetura deve suportar a transição entre os fluxos, garantindo os seguintes requisitos:

| Requisito                               | Descrição                                                                                                                                                                                 |
| :-------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Integridade e Consistência de Dados** | A arquitetura deve garantir que a Base Estruturada receba dados validados e consistentes, eliminando a dispersão de informações (Miro, SharePoint, documentos).                           |
| **Rastreabilidade e Não Repúdio**       | Implementação de mecanismos arquiteturais que registrem todas as ações do Agente de IA e dos usuários, atendendo a restrições de _compliance_.                                            |
| **Flexibilidade e Interoperabilidade**  | A arquitetura deve ser modular o suficiente para permitir a troca da plataforma de gestão (SharePoint para Project, Business Map, etc.) sem comprometer a funcionalidade do Agente de IA. |
| **Segurança e Confidencialidade**       | Garantir que o Agente de IA atue dentro dos limites de permissão e acesso, e que o processamento de dados confidenciais ocorra em um ambiente homologado (ecossistema Microsoft).         |
| **Escalabilidade para IA**              | A camada de arquitetura deve ser projetada para acomodar a evolução do Agente de IA (ex: processamento de linguagem natural, reconhecimento de áudio).                                    |

---

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

_(A. Cenários de simulação, focando as melhorias dos RNFs - Lista de cenários de simulação - caracterizando as condições de simulações planejadas;)_

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
