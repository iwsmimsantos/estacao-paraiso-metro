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

- [Nome do Projeto: ](#nome-do-projeto-)
  - [Nome do Grupo: ](#nome-do-grupo-)
  - [Integrantes:](#integrantes)
- [Sumário](#sumário)
- [Projeto · Módulo 08 – Arquitetura Digital Segura e Tolerante a Falhas](#projeto--módulo-08--arquitetura-digital-segura-e-tolerante-a-falhas)
- [1. Introdução](#1-introdução)
  - [1.1 Termos e Abreviações](#11-termos-e-abreviações)
  - [1.2 Contexto e Motivação](#12-contexto-e-motivação)
  - [1.3 Objetivo](#13-objetivo)
    - [Objetivo Geral](#objetivo-geral)
    - [Objetivos Específicos](#objetivos-específicos)
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
      - [Principais diretrizes e metas:](#principais-diretrizes-e-metas)
  - [2.2 Riscos e Oportunidades](#22-riscos-e-oportunidades)
    - [2.2.1 Matriz de Riscos](#221-matriz-de-riscos)
    - [2.2.2 Riscos ligados ao sistema](#222-riscos-ligados-ao-sistema)
    - [2.2.3 Oportunidades de melhoria dos SLAs](#223-oportunidades-de-melhoria-dos-slas)
- [3. Visão de Modelo Comportamental (Simulação do Sistema Atual)](#3-visão-de-modelo-comportamental-simulação-do-sistema-atual)
  - [3.1 RNFs do Sistema Atual](#31-rnfs-do-sistema-atual)
    - [**Principais Lacunas Identificadas no Sistema Atual:**](#principais-lacunas-identificadas-no-sistema-atual)
    - [**Justificativa para Nova Arquitetura:**](#justificativa-para-nova-arquitetura)
  - [3.2 Estrutura Estática do Modelo](#32-estrutura-estática-do-modelo)
    - [A. Elementos do Sistema Envolvidos nos RNFs Selecionados](#a-elementos-do-sistema-envolvidos-nos-rnfs-selecionados)
    - [B. Estrutura e Conexão entre os Elementos (Modelo de Simulação)](#b-estrutura-e-conexão-entre-os-elementos-modelo-de-simulação)
      - [Detalhamento do Modelo de Simulação de Cada RNF](#detalhamento-do-modelo-de-simulação-de-cada-rnf)
  - [3.3 Modelagem Comportamental e Simulação dos RNFs](#33-modelagem-comportamental-e-simulação-dos-rnfs)
    - [3.3.1 Modelagem Comportamental](#331-modelagem-comportamental)
      - [**Cenário 1 – Escalabilidade e Acessos Simultâneos**](#cenário-1--escalabilidade-e-acessos-simultâneos)
      - [**Cenário 2 – Disponibilidade e Recuperação de Falhas**](#cenário-2--disponibilidade-e-recuperação-de-falhas)
      - [**Cenário 3 – Segurança e Controle de Acessos**](#cenário-3--segurança-e-controle-de-acessos)
      - [**Cenário 4 – Rastreabilidade e Auditoria de Interações**](#cenário-4--rastreabilidade-e-auditoria-de-interações)
      - [**Consolidação dos Cenários e Foco nas Melhorias de RNFs**](#consolidação-dos-cenários-e-foco-nas-melhorias-de-rnfs)
    - [3.3.2 Cenários Simulados](#332-cenários-simulados)
      - [**Cenário 1 – Escalabilidade e Acessos Simultâneos (Hipotético)**](#cenário-1--escalabilidade-e-acessos-simultâneos-hipotético)
      - [**Cenário 2 – Disponibilidade e Recuperação de Falhas (Hipotético)**](#cenário-2--disponibilidade-e-recuperação-de-falhas-hipotético)
      - [**Cenário 3 – Segurança e Controle de Acessos (Hipotético)**](#cenário-3--segurança-e-controle-de-acessos-hipotético)
      - [**Cenário 4 – Rastreabilidade e Auditoria (Hipotético)**](#cenário-4--rastreabilidade-e-auditoria-hipotético)
  - [3.4 Consolidação dos Resultados da Simulação](#34-consolidação-dos-resultados-da-simulação)
    - [**Tabela de Resultados Esperados**](#tabela-de-resultados-esperados)
    - [**Principais Falhas Esperadas**](#principais-falhas-esperadas)
      - [**1. Degradação Crítica de Performance**](#1-degradação-crítica-de-performance)
      - [**2. Vulnerabilidades de Segurança Críticas**](#2-vulnerabilidades-de-segurança-críticas)
      - [**3. Indisponibilidade Operacional**](#3-indisponibilidade-operacional)
      - [**4. Falhas de Compliance e Auditoria**](#4-falhas-de-compliance-e-auditoria)
    - [**Recomendações Arquiteturais**](#recomendações-arquiteturais)
      - [**1. Implementação de Nova Arquitetura**](#1-implementação-de-nova-arquitetura)
      - [**2. Mecanismos de Tolerância a Falhas**](#2-mecanismos-de-tolerância-a-falhas)
      - [**3. Segurança e Compliance**](#3-segurança-e-compliance)
      - [**4. Escalabilidade e Performance**](#4-escalabilidade-e-performance)
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

&emsp;Esta seção apresenta o **contexto do projeto** desenvolvido em parceria com o Metrô de São Paulo, descrevendo os **principais conceitos, motivações e objetivos** que orientam a proposta de uma nova arquitetura para o sistema de gestão de portfólio. O foco está em estabelecer uma base técnica sólida para a integração de agentes de Inteligência Artificial, garantindo disponibilidade, rastreabilidade e segurança nas operações e dados corporativos.

## 1.1 Termos e Abreviações

| Sigla / Termo       | Definição                                                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Metrô-SP**        | Companhia do Metropolitano de São Paulo – empresa pública responsável pela operação e expansão da rede metroviária da cidade de São Paulo. |
| **PMO**             | _Project Management Office_ – Escritório de Projetos responsável pela governança e gestão do portfólio estratégico do Metrô-SP.            |
| **IA**              | Inteligência Artificial – conjunto de tecnologias que permitem a automação inteligente de processos, análise de dados e suporte à decisão. |
| **RNF**             | Requisitos Não Funcionais – características que definem o desempenho, segurança, rastreabilidade e disponibilidade da solução.             |
| **SharePoint**      | Plataforma da Microsoft utilizada para armazenamento, gestão e colaboração em documentos corporativos.                                     |
| **Power Automate**  | Ferramenta da Microsoft utilizada para automação de fluxos de trabalho e integração entre sistemas.                                        |
| **Power BI**        | Plataforma de análise e visualização de dados da Microsoft, utilizada para geração de relatórios e indicadores.                            |
| **Miro**            | Ferramenta de colaboração visual usada para brainstorming e mapeamento de projetos.                                                        |
| **Failover**        | Mecanismo que permite a continuidade dos serviços em caso de falha de um componente do sistema.                                            |
| **MTTR**            | _Mean Time to Recovery_ – tempo médio necessário para restaurar o funcionamento do sistema após uma falha.                                 |
| **Guardiões de IA** | Módulos de controle responsáveis por monitorar, restringir e validar as ações dos agentes de IA, garantindo segurança e conformidade.      |

## 1.2 Contexto e Motivação

&emsp;O **Metrô de São Paulo** é uma das principais empresas públicas de transporte urbano do país, responsável pela operação e expansão da rede metroviária que transporta milhões de passageiros diariamente [[1]](#referências) [[3]](#referências). Dentro da companhia, o **PMO Corporativo** desempenha papel estratégico na gestão do portfólio de projetos, garantindo que as iniciativas estejam alinhadas às metas organizacionais e aos planos de governo [[2]](#referências).

&emsp;Atualmente, o processo de gerenciamento de projetos é apoiado por diversas ferramentas do ecossistema Microsoft — como Miro, SharePoint, Power Automate e Power BI — utilizadas para o registro, acompanhamento e validação das informações dos projetos [[2]](#referências). Apesar de funcional, **o sistema apresenta alta dependência de tarefas manuais, falhas ocasionais de sincronização e baixa rastreabilidade das ações realizadas**, dificultando a escalabilidade e a eficiência operacional do processo [[2]](#referências).

&emsp;Diante desse cenário, surge a necessidade de modernizar a arquitetura tecnológica do ambiente de gestão de portfólio, tornando-a **mais inteligente, segura e escalável**. A **adoção de agentes de IA** representa uma oportunidade concreta para automatizar atividades repetitivas, oferecer suporte inteligente às equipes e fortalecer a governança digital do Metrô-SP, assegurando **disponibilidade, rastreabilidade e segurança dos dados**.

## 1.3 Objetivo

### Objetivo Geral

&emsp;Desenvolver uma arquitetura de software escalável, resiliente e segura para o sistema de gestão de portfólio de projetos do Metrô de São Paulo, que possibilite a integração controlada de agentes de Inteligência Artificial, promovendo a automação de processos e a padronização das informações, garantindo a disponibilidade contínua dos serviços, a rastreabilidade completa das ações realizadas e a segurança integral dos dados corporativos, em conformidade com as políticas de governança e compliance da companhia.

### Objetivos Específicos

1. **Diagnosticar o ambiente tecnológico atual** de gestão de portfólio do Metrô-SP — baseado em ferramentas como Miro, SharePoint, Power Automate e Power BI — identificando vulnerabilidades, gargalos e limitações de integração entre plataformas.

2. **Modelar uma arquitetura modular e flexível**, capaz de evoluir de forma sustentável, garantindo interoperabilidade com os sistemas existentes e suporte à futura incorporação de agentes de IA.

3. **Assegurar a disponibilidade dos serviços críticos** de gestão de portfólio, projetando mecanismos de tolerância a falhas, recuperação automática e balanceamento de carga que mantenham o sistema operacional e estável, mesmo sob alta demanda.

4. **Garantir a rastreabilidade de todas as ações** realizadas no ambiente de portfólio, implementando logs detalhados, trilhas de auditoria e mecanismos de versionamento que permitam reconstruir o histórico de alterações e assegurar o não repúdio das operações.

5. **Reforçar a segurança da informação**, especificando políticas e camadas de controle de acesso baseadas em perfis de usuário (PMO, diretoria, equipe técnica), criptografia de dados sensíveis e mecanismos de prevenção contra vazamentos e acessos indevidos.

6. **Definir mecanismos de integração de agentes de IA**, permitindo automação de tarefas repetitivas, validação inteligente de dados e geração proativa de relatórios e insights para apoio à tomada de decisão.

7. **Propor um modelo de consolidação de dados**, permitindo a extração automática de informações do Miro e sua integração estruturada com o SharePoint, reduzindo o retrabalho manual e aumentando a consistência dos registros.

8. **Projetar componentes de controle e governança de IA** ("guardiões de IA"), responsáveis por supervisionar o comportamento dos agentes automatizados e garantir que operem dentro dos limites éticos, técnicos e de compliance definidos pelo Metrô.

9. **Desenvolver cenários de simulação e testes**, avaliando a escalabilidade, desempenho e confiabilidade da arquitetura, com foco em Requisitos Não Funcionais (RNFs) relacionados à disponibilidade, rastreabilidade e segurança.

10. **Evidenciar os ganhos de eficiência e governança digital**, por meio de métricas quantitativas que demonstrem a melhoria na qualidade dos dados, na automação dos processos e na transparência das operações do PMO.

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

&emsp;O sistema de gestão de portfólio do Metrô de São Paulo é utilizado por **aproximadamente 150 usuários cadastrados**, entre analistas, gerentes e membros das equipes de projeto. Desses, estima-se que **entre 30 e 50 usuários possam operar simultaneamente em períodos de pico**, chegando a até 75 usuários simultâneos em momentos de alta demanda, como etapas de consolidação de relatórios ou fechamento de ciclos mensais.

&emsp;Cada projeto em andamento gera cerca de **10.000 documentos**, incluindo relatórios, cronogramas, registros de risco e atas, resultando em um volume expressivo de dados processados e armazenados. A plataforma, composta por ferramentas como SharePoint, Power Automate, Power BI e Miro, **realiza em média de 500 a 1.000 transações mensais**, considerando operações de leitura, atualização, automação de fluxos e geração de relatórios.

&emsp;As estimativas de desempenho indicam uma **taxa de 1 a 2 requisições por segundo (RPS) em períodos normais de operação**, podendo atingir até 2,5 RPS em cenários de pico. Para garantir estabilidade e disponibilidade, recomenda-se o dimensionamento da arquitetura para **100 usuários simultâneos**, permitindo margens de segurança e escalabilidade futura.

&emsp;Os principais pontos de vulnerabilidade observados estão relacionados à dependência de processos manuais, falhas ocasionais de sincronização entre SharePoint e Power BI, e limitações de rastreabilidade de ações entre usuários. Tais fatores impactam a confiabilidade dos dados e reforçam a necessidade de uma arquitetura com mecanismos de tolerância a falhas, registro de auditoria e monitoramento proativo de desempenho.

**Tabela 1 - Resumo dos Volumes Operacionais**

| **Métrica**                       | **Valor**         | **Observações**                                    |
| --------------------------------- | ----------------- | -------------------------------------------------- |
| **Usuários Cadastrados**          | 150 usuários      | Analistas, gerentes e membros das equipes          |
| **Usuários Simultâneos (Normal)** | 30-50 usuários    | Períodos de operação padrão                        |
| **Usuários Simultâneos (Pico)**   | 75 usuários       | Consolidação de relatórios e fechamentos           |
| **Capacidade Recomendada**        | 100 usuários      | Margem de segurança e escalabilidade               |
| **Documentos por Projeto**        | 10.000 documentos | Relatórios, cronogramas, registros de risco e atas |
| **Transações Mensais**            | 500-1.000         | Operações de leitura, atualização e automação      |
| **Taxa de Requisições (Normal)**  | 1-2 RPS           | Períodos normais de operação                       |
| **Taxa de Requisições (Pico)**    | 2,5 RPS           | Cenários de alta demanda                           |

### 2.1.5 Estratégias de Crescimento e Evolução

&emsp;A proposta de evolução do sistema de gestão de portfólio do Metrô de São Paulo tem como foco estabelecer uma **arquitetura escalável e segura**, capaz de **integrar agentes de Inteligência Artificial** para apoiar a automação e o gerenciamento inteligente dos projetos corporativos.

&emsp;A estratégia de crescimento busca fortalecer três pilares: **escalabilidade técnica, inteligência operacional e confiabilidade das informações**, garantindo que o ambiente atual (baseado em Miro, SharePoint, Power Automate e Power BI) possa evoluir sem comprometer a integridade e rastreabilidade dos dados.

#### Principais diretrizes e metas:

&emsp;As ações estratégicas estão estruturadas em cinco eixos principais, diretamente relacionados aos RNFs:

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

### 2.2.1 Matriz de Riscos

&emsp;O sistema atual de gestão de portfólio do Metrô de São Paulo utiliza majoritariamente ferramentas do ecossistema Microsoft (_SharePoint_, _Power Automate_, _Power BI_) e o _Miro_ como apoio colaborativo. Apesar de atender às demandas básicas, essa estrutura apresenta riscos operacionais e técnicos relacionados à integração, à dependência de processos manuais e à governança dos dados.


<div align="center">
  <sub>Figura X - Matriz de Risco</sub>
  <img src="../documentos/img/section2/risk_matrix.png">
  <sup>Fonte: material produzido pelos autores (2025).</sup>
</div>

### 2.2.2 Riscos ligados ao sistema

| Código | Nome do Risco | Tipo | Descrição | Aspectos Afetados | Probabilidade | Impacto |
|:--:|:--|:--|:--|:--|:--:|:--:|
| **R1** | **Inconsistência de Dados** | Técnico / Negócio | O preenchimento manual de informações em diferentes plataformas (Miro, SharePoint, Excel) pode gerar divergências e falta de padronização. | **Precisão**, **Integridade de Dados** | 70% | Alto |
| **R2** | **Dependência de Processos Manuais** | Técnico / Operacional | A ausência de automação completa para entrada, validação e atualização de dados aumenta a chance de erros humanos. | **Desempenho**, **Disponibilidade**, **Confiabilidade** | 80% | Moderado | 
| **R3** | **Falha de Integração entre Ferramentas** | Técnico | Problemas de sincronização entre _Power Automate_, _Power BI_ e _SharePoint_ podem comprometer relatórios e atualizações de status. | **Disponibilidade**, **Tolerância a Falhas**, **Desempenho** | 60% | Alto | 
| **R4** | **Acesso Indevido a Informações** | Compliance / Segurança | Falhas nas permissões de acesso no _SharePoint_ ou _Power BI_ podem permitir a visualização de dados sensíveis por usuários não autorizados. | **Segurança**, **Governança**, **Confidencialidade** | 40% | Muito Alto | 
| **R5** | **Baixa Rastreabilidade das Ações** | Técnico / Governança | As plataformas atuais não possuem logs integrados e centralizados de auditoria das ações dos usuários e fluxos do _Power Automate_. | **Rastreabilidade**, **Auditoria**, **Transparência** | 50% | Moderado | 
| **R6** | **Dependência de Conectividade e Licenciamento Microsoft** | Negócio / Técnico | A indisponibilidade de serviços Microsoft ou falhas de licenciamento podem interromper o funcionamento das automações e relatórios. | **Disponibilidade**, **Continuidade Operacional** | 30% | Alto | 


### 2.2.3 Oportunidades de melhoria dos SLAs

&emsp;Apesar de funcional, o ecossistema apresenta oportunidades de melhoria voltadas à disponibilidade, desempenho, segurança, rastreabilidade e governança dos dados, com foco em elevar os níveis de serviço (SLA) e reduzir riscos operacionais.

| Código | Oportunidade | Descrição | SLA Impactado | Benefício Esperado |
|:--:|:--|:--|:--|:--|
| **O1** | **Automatização de Monitoramento de Serviços** | Criação de fluxos no Power Automate para monitorar a disponibilidade das integrações entre SharePoint, Power BI e Miro, com alertas automáticos em caso de falhas. | **Disponibilidade**, **Tolerância a Falhas** | Redução do tempo de detecção e resposta a incidentes, garantindo continuidade dos serviços. |
| **O2** | **Padronização de Logs e Auditorias** | Implementação de uma política de versionamento e armazenamento centralizado de logs das ações realizadas nas plataformas. | **Rastreabilidade**, **Segurança** | Melhoria na rastreabilidade e suporte a auditorias internas e externas. |
| **O3** | **Otimização de Processos no Power Automate** | Revisão e otimização dos fluxos de automação existentes para eliminar redundâncias e gargalos de execução. | **Desempenho**, **Disponibilidade** | Redução do tempo de processamento e aumento da eficiência operacional. |
| **O4** | **Melhoria na Integração entre Ferramentas** | Criação de conectores otimizados entre SharePoint, Power BI e Miro, minimizando falhas de sincronização e perda de dados. | **Disponibilidade**, **Rastreabilidade** | Garantia de consistência dos dados e maior confiabilidade nas informações compartilhadas. |
| **O5** | **Fortalecimento das Políticas de Segurança e Compliance** | Revisão dos controles de acesso, autenticação e permissões no SharePoint e Miro, alinhando-se às diretrizes da LGPD. | **Segurança**, **Compliance** | Diminuição do risco de acesso indevido e exposição de informações sensíveis. |
| **O6** | **Criação de Painéis de Acompanhamento de SLA** | Desenvolvimento de dashboards no Power BI para consolidar métricas de disponibilidade, desempenho e incidentes. | **Governança**, **Transparência** | Visibilidade contínua sobre o cumprimento dos SLAs e suporte à tomada de decisão gerencial. |

As oportunidades identificadas visam fortalecer o sistema de gestão de projetos atual por meio de:
- **Automatização e otimização de fluxos**, reduzindo falhas e atrasos operacionais.  
- **Aprimoramento da rastreabilidade e governança**, com maior controle sobre logs e dados.  
- **Reforço da segurança e conformidade**, garantindo aderência à LGPD e políticas internas.  
- **Melhoria da integração entre ferramentas**, assegurando consistência e confiabilidade das informações.  

Essas iniciativas contribuem para a consolidação de um **ecossistema mais estável, seguro e eficiente**, promovendo a evolução contínua da gestão de portfólio do Metrô de São Paulo.

# 3. Visão de Modelo Comportamental (Simulação do Sistema Atual)

Esta seção apresenta a **modelagem comportamental** do sistema atual de gestão de projetos do Metrô de São Paulo e os **experimentos de simulação** realizados para observar seu comportamento frente a cenários críticos, especialmente aqueles relacionados a **Requisitos Não Funcionais (RNFs)**, como desempenho, segurança, privacidade e tolerância a falhas.

A análise comportamental do sistema atual baseia-se na arquitetura existente que utiliza aplicações como Miro para brainstorming de projetos e SharePoint para armazenamento e validação de informações. O foco está em identificar limitações e vulnerabilidades que justifiquem a implementação de uma nova arquitetura escalável com integração de agentes de IA.

---

## 3.1 RNFs do Sistema Atual

A análise do sistema atual de gestão de projetos do Metrô de São Paulo revela uma **ausência crítica de requisitos não funcionais adequados**. O sistema atual baseado em Miro e SharePoint **não possui implementação adequada** dos RNFs essenciais para uma gestão de projetos escalável.

A tabela abaixo compara o **estado atual (deficiente)** versus os **requisitos que a nova arquitetura deveria ter**, incluindo o **status de implementação** para tracking do progresso:

| **Requisito Não Funcional** | **Estado Atual do Metrô (Deficiente)**                                                                                                                                       | **Arquitetura Reformada (Desejada)**                                                                                                                               | **Checklist de Implementação** |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ |
| **Escalabilidade**          | • Dependência total de ferramentas externas sem controle<br>• Ausência de balanceamento de carga<br>• Processamento sequencial manual<br>• Limitação de usuários simultâneos | • Arquitetura escalável com auto-scaling<br>• Balanceamento de carga automático<br>• Processamento paralelo com IA<br>• Suporte a milhares de usuários simultâneos | **☐ Implementar auto-scaling horizontal**<br>**☐ Configurar load balancer (HAProxy/Nginx)**<br>**☐ Implementar processamento paralelo com IA**<br>**☐ Otimizar para milhares de usuários simultâneos**<br>**☐ Configurar métricas de escalabilidade** |
| **Disponibilidade**         | • Dependência de SLA de terceiros (Miro/SharePoint)<br>• Ausência de redundância<br>• Sem monitoramento proativo<br>• Downtime não controlado                                | • SLA de 99.9% garantido<br>• Redundância e failover automático<br>• Monitoramento 24/7<br>• Recuperação automática em <5s                                         | Não Trabalharemos|
| **Segurança**               | • Controle de acesso limitado<br>• Ausência de auditoria<br>• Dependência de políticas externas<br>• Dados expostos em ferramentas de terceiros                              | • Controle de acesso granular<br>• Auditoria completa de todas as ações<br>• Criptografia end-to-end<br>• Conformidade com LGPD                                    | **☐ Implementar controle de acesso granular (RBAC)**<br>**☐ Configurar auditoria completa de ações**<br>**☐ Implementar criptografia end-to-end**<br>**☐ Garantir conformidade com LGPD**<br>**☐ Implementar autenticação multi-fator** |
| **Rastreabilidade**         | • Logs limitados das ferramentas<br>• Ausência de trilha integrada<br>• Dificuldade de correlação<br>• Sem compliance automático                                             | • Logs detalhados de todas as ações<br>• Trilha de auditoria integrada<br>• Correlação automática de eventos<br>• Compliance e relatórios automáticos              | **☐ Implementar logs detalhados de todas as ações**<br>**☐ Configurar trilha de auditoria integrada**<br>**☐ Implementar correlação automática de eventos**<br>**☐ Configurar compliance e relatórios automáticos**<br>**☐ Implementar sistema de alertas** |
| **Performance**             | • Dependência de conectividade externa<br>• Processamento manual<br>• Ausência de cache<br>• Tempos de resposta imprevisíveis                                                | • Processamento local otimizado<br>• Cache inteligente<br>• Tempo de resposta <1s<br>• Otimização com IA                                                           | Não Trabalharemos |
| **Tolerância a Falhas**     | • Sem mecanismos de recuperação<br>• Falha única pode parar todo o sistema<br>• Perda de dados em caso de falha<br>• Recuperação manual                                      | • Recuperação automática<br>• Redundância em múltiplas camadas<br>• Zero perda de dados<br>• Failover transparente                                                 | Não Trabalharemos |

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

### A. Elementos do Sistema Envolvidos nos RNFs Selecionados

&emsp;A simulação foca nos quatro RNFs críticos identificados no sistema atual, que é baseado em ferramentas de terceiros (Miro e SharePoint). Os elementos do sistema envolvidos na simulação são modelados em dois níveis: o **Nível de Aplicação** (as ferramentas de front-end e colaboração) e o **Nível de Infraestrutura** (os componentes que suportam o processamento e o armazenamento).

| RNF Selecionado     | Elementos do Sistema (Nível de Aplicação)                              | Elementos do Sistema (Nível de Infraestrutura)                                                                                                    | Foco da Simulação                                                |
| :------------------ | :--------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------- |
| **Escalabilidade**  | Agentes de IA (requisições simultâneas), Usuários (acessos)            | **Serviço de Processamento Sequencial** (simulando a dependência de um único ponto de processamento), **Fila de Requisições** (limitada).         | Capacidade de suportar carga e processamento paralelo.           |
| **Disponibilidade** | SharePoint (Base de Dados Principal)                                   | **Serviço de Armazenamento Único** (simulando a ausência de redundância), **Monitoramento Manual** (simulando a falta de monitoramento proativo). | Tempo de recuperação (MTTR) e perda de dados em falha.           |
| **Segurança**       | Usuários (tentativas de acesso), Agentes de IA (envio de comandos)     | **Módulo de Controle de Acesso Básico** (simulando políticas externas limitadas), **Base de Dados Exposta**.                                      | Resistência a acessos indevidos e exposição de dados sensíveis.  |
| **Rastreabilidade** | Usuários (ações de modificação), Agentes de IA (tarefas automatizadas) | **Módulo de Logs Limitados** (simulando a ausência de trilha integrada), **Módulo de Correlação Manual**.                                         | Percentual de ações registradas e tempo de recuperação dos logs. |

### B. Estrutura e Conexão entre os Elementos (Modelo de Simulação)

&emsp;O modelo de simulação é estruturado para demonstrar as limitações do sistema atual (AS-IS) ao tentar atender aos requisitos da arquitetura reformada (TO-BE), como a necessidade de suportar milhares de usuários e processamento paralelo com IA.

#### Detalhamento do Modelo de Simulação de Cada RNF

| RNF                 | Estrutura e Conexão                                                                                                                                                                                                                                                                                                                   | Parametrização para Simulação                                                                                                                                                                                                                                                                                                                      |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Escalabilidade**  | **Estrutura:** O modelo é composto por um **Gerador de Requisições** (simulando usuários e Agentes de IA) que direciona o tráfego para uma **Fila de Requisições** de tamanho limitado. A fila alimenta um único **Serviço de Processamento Sequencial** (simulando a dependência de um único servidor ou a limitação do SharePoint). | **Entrada:** Taxa de chegada de requisições (λ) variando de 500 a 5.000 requisições/minuto. **Processamento:** Tempo de execução da transação (μ) fixo e alto. **Saída:** Taxa de rejeição de requisições (devido à fila cheia), Tempo de espera na fila e Taxa de Sucesso.                                                                        |
| **Disponibilidade** | **Estrutura:** O modelo simula o **Serviço de Armazenamento Único** (SharePoint) sem réplicas. Um evento de **Falha Crítica** é injetado no sistema. A recuperação é tratada por um **Processo de Recuperação Manual** (simulando a intervenção humana).                                                                              | **Entrada:** Injeção de falha no tempo T. **Processamento:** Tempo de Recuperação Manual (alto, 30-60 minutos). **Saída:** Tempo Médio de Recuperação (MTTR) e Quantidade de Transações Perdidas (modelada como alta, devido à ausência de _failover_).                                                                                            |
| **Segurança**       | **Estrutura:** O modelo simula o fluxo de consultas a projetos. O **Módulo de Controle de Acesso Básico** permite que um percentual de **Consultas Indevidas** (simulando ataques) atinja a **Base de Dados Exposta**.                                                                                                                | **Entrada:** Taxa de Consultas Seguras vs. Taxa de Consultas Sob Ataque (simuladas). **Processamento:** O Módulo de Controle de Acesso Básico falha em bloquear 5% das consultas sob ataque. **Saída:** Taxa de Consultas Seguras, Taxa de Consultas Sob Ataque, e o registro do **Acesso Indevido** à Base de Dados.                              |
| **Rastreabilidade** | **Estrutura:** O modelo simula as ações dos usuários e Agentes de IA que são registradas pelo **Módulo de Logs Limitados**. O **Módulo de Correlação Manual** é acionado para tentar correlacionar eventos em caso de falha.                                                                                                          | **Entrada:** Número de Ações de Modificação e Automatizadas. **Processamento:** O Módulo de Logs Limitados registra apenas 30-40% das ações (simulando a perda de logs). O tempo de correlação é alto (simulando a dificuldade de auditoria). **Saída:** Percentual de Ações Registradas Corretamente e Tempo Médio de Recuperação de Logs (alto). |

&emsp;A simulação desses cenários no modelo estático visa quantificar as vulnerabilidades do sistema AS-IS, fornecendo a base técnica para justificar a implementação da nova arquitetura, que deverá substituir esses elementos limitados por componentes escaláveis, redundantes e seguros.

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

| **Métrica**              | **Sistema Atual (Sem RNFs)** | **Cenário Hipotético (Com RNFs)** | **Resultado Esperado**       |
| ------------------------ | ---------------------------- | --------------------------------- | ---------------------------- |
| **Usuários Simultâneos** | 30-50 usuários (limitado)    | 100+ usuários                     | ❌ **Degradação Severa**     |
| **Tempo de Resposta**    | 2-5 segundos (imprevisível)  | <1 segundo                        | ❌ **Falhas Frequentes**     |
| **Taxa de Sucesso**      | 70-80% (dependência externa) | 95%+                              | ❌ **Sobrecarga do Sistema** |
| **Escalabilidade**       | Manual e limitada            | Automática                        | ❌ **Colapso do Sistema**    |

**Resultados Hipotéticos Esperados:**

- **Degradação Severa do Desempenho:** Com 100+ usuários simultâneos, o sistema atual entraria em colapso
- **Falhas de Conectividade:** Dependência de ferramentas externas (Miro/SharePoint) causaria timeouts
- **Perda de Dados:** Ausência de mecanismos de recuperação resultaria em perda de informações
- **Indisponibilidade Total:** Sistema ficaria inoperante durante picos de demanda

#### **Cenário 2 – Disponibilidade e Recuperação de Falhas (Hipotético)**

**Situação Atual vs. Cenário com RNFs Implementados:**

| **Métrica**         | **Sistema Atual (Sem RNFs)** | **Cenário Hipotético (Com RNFs)** | **Resultado Esperado**        |
| ------------------- | ---------------------------- | --------------------------------- | ----------------------------- |
| **MTTR**            | 30-60 minutos (manual)       | <5 segundos                       | ❌ **Recuperação Impossível** |
| **Disponibilidade** | 85-90% (dependência externa) | 99.9%                             | ❌ **Downtime Prolongado**    |
| **Perda de Dados**  | Alta (sem backup)            | Zero                              | ❌ **Perda Total de Dados**   |
| **Failover**        | Não existe                   | Automático                        | ❌ **Sistema Indisponível**   |

**Resultados Hipotéticos Esperados:**

- **Falha Total do Sistema:** Ausência de redundância causaria indisponibilidade completa
- **Perda Massiva de Dados:** Sem mecanismos de backup, todos os dados seriam perdidos
- **Recuperação Manual Prolongada:** Dependência de intervenção humana para restabelecer serviços
- **Impacto Operacional Crítico:** Projetos paralisados por horas ou dias

#### **Cenário 3 – Segurança e Controle de Acessos (Hipotético)**

**Situação Atual vs. Cenário com RNFs Implementados:**

| **Métrica**             | **Sistema Atual (Sem RNFs)**  | **Cenário Hipotético (Com RNFs)** | **Resultado Esperado**              |
| ----------------------- | ----------------------------- | --------------------------------- | ----------------------------------- |
| **Controle de Acesso**  | Limitado (políticas externas) | Granular                          | ❌ **Vulnerabilidades Críticas**    |
| **Auditoria**           | Parcial (logs limitados)      | Completa                          | ❌ **Acessos Não Autorizados**      |
| **Criptografia**        | Básica (ferramentas externas) | End-to-end                        | ❌ **Exposição de Dados Sensíveis** |
| **Detecção de Ataques** | Não existe                    | Automática                        | ❌ **Invasões Não Detectadas**      |

**Resultados Hipotéticos Esperados:**

- **Vulnerabilidades Críticas:** Dados sensíveis dos projetos expostos a acessos não autorizados
- **Falta de Rastreabilidade:** Impossibilidade de identificar quem acessou ou modificou informações
- **Compliance Violado:** Violação de regulamentações de segurança e privacidade
- **Riscos Legais:** Exposição de informações confidenciais do Metrô

#### **Cenário 4 – Rastreabilidade e Auditoria (Hipotético)**

**Situação Atual vs. Cenário com RNFs Implementados:**

| **Métrica**              | **Sistema Atual (Sem RNFs)** | **Cenário Hipotético (Com RNFs)** | **Resultado Esperado**             |
| ------------------------ | ---------------------------- | --------------------------------- | ---------------------------------- |
| **Registro de Ações**    | 30-40% (logs limitados)      | 100%                              | ❌ **Perda de Rastreabilidade**    |
| **Tempo de Recuperação** | 5-10 minutos                 | <2 segundos                       | ❌ **Logs Inacessíveis**           |
| **Integridade**          | Não verificada               | Hash verification                 | ❌ **Dados Corrompidos**           |
| **Compliance**           | Manual e incompleto          | Automático                        | ❌ **Violação de Regulamentações** |

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

| **RNF Analisado**   | **Cenário Atual** | **Resultado Hipotético**        | **Impacto Crítico**           | **Justificativa**                  |
| ------------------- | ----------------- | ------------------------------- | ----------------------------- | ---------------------------------- |
| **Escalabilidade**  | 30-50 usuários    | Colapso total com 100+ usuários | ❌ **Sistema Inoperante**     | Ausência de balanceamento de carga |
| **Disponibilidade** | 85-90%            | Downtime prolongado             | ❌ **Perda Total de Dados**   | Sem redundância ou failover        |
| **Segurança**       | Controle limitado | Vulnerabilidades críticas       | ❌ **Exposição de Dados**     | Dependência de políticas externas  |
| **Rastreabilidade** | 30-40% de logs    | Perda total de auditoria        | ❌ **Violação de Compliance** | Sistema de logs inadequado         |

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

Com base na análise da Seção 3.1, o sistema atual apresenta **ausência crítica de RNFs adequados**. A tabela abaixo consolida os RNFs vulneráveis identificados:

| **RNF** | **Estado Atual (Deficiente)** | **Vulnerabilidades Críticas** | **Impacto no Negócio** |
|---------|------------------------------|-------------------------------|------------------------|
| **Escalabilidade** | • Dependência de ferramentas externas sem controle<br>• Ausência de balanceamento de carga, sem previsibilidade e controle de demanda<br>• Processamento sequencial manual<br>• Limitação de usuários simultâneos | • Sistema colapsa com muitos usuários simultâneos<br>• Impossibilidade de crescimento proporcional à demanda<br>• Gargalos de processamento | • Operações paralisadas em picos de demanda<br>• Limitação de uso<br>• Inviabilidade de expansão futura |
| **Disponibilidade** | • Dependência de SLA de terceiros (Miro/SharePoint)<br>• Ausência de redundância<br>• Sem monitoramento proativo<br>• Downtime não controlado | • Risco de indisponibilidade em software de terceiros<br>• Qualquer reparo nas ferramentas depende de uma equipe externa<br>• Perda de dados em falhas | • Paralisação de projetos de R$ 1,5 bi/ano<br>• +6.000 colaboradores impactados<br>• Perda de informações para decisões estratégicas |
| **Segurança** | • Controle de acesso limitado<br>• Ausência de auditoria<br>• Dependência de políticas externas<br>• Dados expostos em ferramentas de terceiros | • Dados sensíveis expostos a políticas externas<br>• 0% de tentativas de ataque detectadas<br>• Criptografia básica | • Risco de vazamento de informações estratégicas<br>• Violação de LGPD<br>• Danos à imagem institucional |
| **Rastreabilidade** | • Logs limitados das ferramentas<br>• Ausência de trilha integrada<br>• Dificuldade de correlação<br>• Sem compliance automático | • Ações não auditáveis<br>• Falta de recuperação de logs<br>• Sem verificação de integridade | • Violação de compliance para empresa pública<br>• Impossibilidade de investigação de incidentes<br>• Riscos legais de multas |
| **Performance** | • Dependência de conectividade externa<br>• Processamento manual<br>• Ausência de cache<br>• Tempos de resposta imprevisíveis | • Tempo de resposta muito lento<br>• Degradação severa em picos<br>• Baixa eficiência operacional | • Perda de produtividade de equipes<br>• Frustração de usuários<br>• Retrabalho por timeouts |
| **Tolerância a Falhas** | • Sem mecanismos de recuperação<br>• Falha única pode parar todo o sistema<br>• Perda de dados em caso de falha<br>• Recuperação manual | • Sistema colapsado em qualquer falha<br>• Recuperação manual prolongada<br>• Alta perda de dados | • Downtime prolongado (60-120 min)<br>• Perda de informações críticas<br>• Impacto operacional severo |

**Seleção dos RNFs Críticos (Priorizados)**

Com base nos **business drivers** (Seção 2.1.5) e na análise de riscos, foram selecionados **3 RNFs críticos**:

#### **RNF-01: Rastreabilidade** ⭐ **PRIORIDADE ALTA**

**Justificativa:**
- **Business Driver:** "Rastreabilidade completa das tentativas de acesso"
- **Compliance:** Empresa pública sob fiscalização do TCE
- **Risco:** Multas e violação de governança

**Métricas:**

| **Métrica** | **Atual** | **Meta** | **Ganho** |
|------------|----------|---------|-----------|
| **Cobertura logs** | Limitada | 100% | Auditabilidade total |
| **Recuperação** | Demorada | <2s | Investigação ágil |
| **Integridade** | 0% | 100% (hash) | Não repúdio |
| **Compliance** | Violado | Atendido | Requisito legal |

#### **RNF-02: Segurança** ⭐ **PRIORIDADE ALTA**

**Justificativa:**
- **Business Driver:** "Segurança com controle de acesso baseado em perfis"
- **LGPD:** Proteção de dados de R$ 10 bilhões em projetos
- **Risco:** Vazamento de informações estratégicas

**Métricas:**

| **Métrica** | **Atual** | **Meta** | **Ganho** |
|------------|----------|---------|-----------|
| **Controle acesso** | Limitado | Granular (RBAC) | Segmentação |
| **Detecção ataques** | 0% | 100% | Proteção proativa |
| **Criptografia** | Básica | End-to-end | Proteção integral |
| **LGPD** | Não atendida | Atendida | Conformidade |

#### **RNF-03: Escalabilidade** ⭐ **PRIORIDADE ALTA**

**Justificativa:**
- **Business Driver:** "Preparar sistema para crescimento futuro e integração de agentes de IA"
- **Contexto:** Expansão da rede metroviária + aumento de projetos + automação com IA
- **Risco:** Limitação atual impede expansão operacional

**Métricas:**

| **Métrica** | **Atual** | **Meta** | **Ganho** |
|------------|----------|---------|-----------|
| **Usuários simultâneos** | Limitado | 100+ | Suporte crescimento |
| **Balanceamento** | Ausente | Automático | Distribuição carga |
| **Processamento** | Sequencial | Paralelo com IA | Automação |
| **Previsibilidade** | Zero | Total | Planejamento |

---

## 4.2 Justificativas para RNFs

### 4.2.1 Controle de Riscos e Mitigação

| **RNF** | **Risco** | **Impacto** | **Mitigação** |
|---------|-----------|-------------|---------------|
| **Rastreabilidade** | Logs limitados impedem auditoria | Violação compliance TCE + multas | Logs 100% + trilha integrada + hash SHA-256 |
| **Segurança** | Dados expostos a políticas externas | Vazamento estratégico + LGPD | RBAC + detecção 100% + AES-256 |
| **Escalabilidade** | Gargalos impedem crescimento | Operações paralisadas + expansão inviável | Auto-scaling + balanceamento + IA |

### 4.2.2 Argumentação por RNF

#### **Rastreabilidade**
- **Problema:** Ações não auditáveis violam compliance público
- **Solução:** 100% registrado + recuperação <2s + hash verification
- **Ganho:** Conformidade TCE + investigação ágil

#### **Segurança**
- **Problema:** 0% ataques detectados + criptografia básica
- **Solução:** RBAC + WAF/IDS/IPS + criptografia end-to-end
- **Ganho:** Proteção R$ 10 bi + LGPD atendida

#### **Escalabilidade**
- **Problema:** Sistema colapsa com muitos usuários + sem previsibilidade
- **Solução:** Auto-scaling + balanceamento automático + processamento paralelo
- **Ganho:** Suporte expansão + preparação para IA

---

## 4.3 Melhorias Esperadas com Implementação de RNFs

### 4.3.1 Melhorias por RNF

| **RNF** | **Atual** | **Novo** | **Ganhos** |
|---------|----------|---------|------------|
| **Rastreabilidade** | Logs limitados<br>Sem trilha<br>Compliance violado | 100% logs<br>Trilha integrada<br>Compliance total | Auditabilidade<br>Recuperação <2s<br>Conformidade TCE |
| **Segurança** | Controle limitado<br>0% detecção<br>LGPD não atendida | RBAC<br>100% detecção<br>LGPD atendida | Segmentação<br>Proteção proativa<br>Conformidade legal |
| **Escalabilidade** | Usuários limitados<br>Sem balanceamento<br>Sequencial | 100+ usuários<br>Auto-scaling<br>Paralelo IA | Suporte crescimento<br>Distribuição carga<br>Automação |

### 4.3.2 Indicadores Consolidados

| **Indicador** | **Atual** | **Meta** | **Impacto** |
|--------------|----------|---------|-------------|
| **Autonomia operacional** | Dependência externa | Controle total | Decisões ágeis |
| **Auditabilidade** | Limitada | 100% | Compliance TCE |
| **Detecção ameaças** | 0% | 100% | Proteção integral |
| **Usuários simultâneos** | Limitado | 100+ | Expansão viável |
| **Conformidade legal** | Violada | Atendida | LGPD + TCE |

### 4.3.3 Benefícios Transversais

- **Autonomia:** Fim da dependência de SLA externo
- **Governança:** Auditabilidade total para TCE
- **Proteção:** R$ 10 bi em projetos seguros
- **Crescimento:** Preparação para expansão + IA

---

## 4.4 Consolidação dos Requisitos e Diretrizes para a Nova Arquitetura

### 4.4.1 Requisitos Não Funcionais (Priorizados)

| **ID** | **RNF** | **Critérios** | **Prioridade** |
|--------|---------|---------------|----------------|
| **RNF-01** | **Rastreabilidade** | 100% logs + recuperação <2s + hash |ALTA |
| **RNF-02** | **Segurança** | RBAC + 100% detecção + AES-256 |ALTA |
| **RNF-03** | **Escalabilidade** | 100+ usuários + auto-scaling + IA |ALTA |

### 4.4.2 Requisitos Funcionais (Suporte)

| **RF** | **Descrição** | **RNFs** |
|--------|---------------|----------|
| **RF-01** | Logs centralizado (100% + hash SHA-256) | RNF-02, RNF-03 |
| **RF-02** | Autenticação RBAC + MFA | RNF-03 |
| **RF-03** | Failover automático <5s | RNF-01 |
| **RF-04** | Backup contínuo + replicação | RNF-01 |
| **RF-05** | Painel auditoria <2s | RNF-02 |
| **RF-06** | Detecção ameaças (WAF + IDS/IPS) | RNF-03 |
| **RF-07** | Balanceador carga automático | RNF-04 |
| **RF-08** | Auto-scaling elástico | RNF-04 |

### 4.4.3 Diretrizes Arquiteturais

1. **Infraestrutura Própria:** Controle total eliminando dependência externa
2. **Redundância Automática:** Failover <5s + replicação ativa
3. **Segurança em Camadas:** RBAC + WAF + IDS/IPS + AES-256
4. **Auditabilidade Total:** Event sourcing + logs 100% + hash
5. **Escalabilidade Elástica:** Auto-scaling + balanceamento automático

### 4.4.4 Mapa de Rastreabilidade

| **Business Driver** | **RNF** | **RF** | **Benefício** |
|---------------------|---------|--------|---------------|
| "Rastreabilidade total" | RNF-01 | RF-01, RF-05 | 100% auditável |
| "Segurança com controle" | RNF-02 | RF-02, RF-06 | RBAC + proteção |
| "Escalabilidade futura" | RNF-03 | RF-07, RF-08 | Crescimento + IA |

---

# 5. Avaliação dos Mecanismos Utilizados no Sistema Atual (Diagnóstico ATAM)

Esta seção detalha os **mecanismos e componentes arquiteturais** do sistema atual que justificam as **limitações e vulnerabilidades** observadas nos RNFs.  
O objetivo é compreender **as causas dos defeitos** e construir a base para propor **táticas e soluções evolutivas**.

---
## 5.1 Mapa de RNFs

_(Definir o mapa da de RNFs e definir se será realmente o decidido na última sprint)_

## 5.2 Revisão do Mapa de RNFs e Vulnerabilidades

_(Esta seção deve consolidar os 3 RNFs selecionados e suas vulnerabilidades. Para cada RNF, detalhe entradas, saídas e como o controle é feito.)_

### 5.2.1 RNF-01 — <Escalabilidade>

#### A. Entrada
_Esta seção deve descrever os dados e transações de entrada relevantes a este RNF (volumetria, tipos, frequência, origem), incluindo casos normais e tentativas indevidas._

#### B. Saída
_Esta seção deve listar os registros de transações realizadas corretamente e as realizadas de maneira inadequada (ex.: fraudulentas), indicando como são diferenciadas e armazenadas._

#### C. Controle do RNF
_Esta seção deve indicar como as transações corretas e inadequadas são controladas (sistemicamente ou manualmente), incluindo limites, regras, validações e responsáveis._

---

### 5.2.2 RNF-02 — <Segurança>

#### A. Entrada
_Esta seção deve descrever os dados e transações de entrada relevantes a este RNF (volumetria, tipos, frequência, origem), incluindo casos normais e tentativas indevidas._

#### B. Saída
_Esta seção deve listar os registros de transações realizadas corretamente e as realizadas de maneira inadequada (ex.: fraudulentas), indicando como são diferenciadas e armazenadas._

#### C. Controle do RNF
_Esta seção deve indicar como as transações corretas e inadequadas são controladas (sistemicamente ou manualmente), incluindo limites, regras, validações e responsáveis._

---

### 5.2.3 RNF-03 — <Rastreabilidade>

#### A. Entrada
_Esta seção deve descrever os dados e transações de entrada relevantes a este RNF (volumetria, tipos, frequência, origem), incluindo casos normais e tentativas indevidas._

#### B. Saída
_Esta seção deve listar os registros de transações realizadas corretamente e as realizadas de maneira inadequada (ex.: fraudulentas), indicando como são diferenciadas e armazenadas._

#### C. Controle do RNF
_Esta seção deve indicar como as transações corretas e inadequadas são controladas (sistemicamente ou manualmente), incluindo limites, regras, validações e responsáveis._

---

## 5.3 Táticas Arquiteturais e Componentes Adotados

_(Esta seção deve descrever as táticas/componentes que suportam a execução e o controle dos 3 RNFs do sistema atual.)_

### 5.3.1 RNF-01 — <Escalabilidade>

#### A. Como monitorar o RNF
_Esta seção deve indicar como o nível de atendimento deste RNF é monitorado (componentes, métricas, SLIs/SLOs), e se o monitoramento é manual e/ou sistêmico, considerando limitações/vulnerabilidades._

#### B. Como resolver o RNF (Preventivo e Reativo)
_Esta seção deve listar os componentes e táticas presentes para atendimento preventivo (ex.: limites, validações, políticas) e reativo (ex.: alertas, contenção, correção) deste RNF._

#### C. Como recuperar/subsidiar o tratamento de impactos
_Esta seção deve descrever os componentes e procedimentos usados para subsidiar o atendimento a falhas que causem quebras de níveis de serviço, incluindo justificativas, detalhamento e passos de recuperação._

---

### 5.3.2 RNF-02 — <Segurança>

#### A. Como monitorar o RNF
_Esta seção deve indicar como o nível de atendimento deste RNF é monitorado (componentes, métricas, SLIs/SLOs), e se o monitoramento é manual e/ou sistêmico, considerando limitações/vulnerabilidades._

#### B. Como resolver o RNF (Preventivo e Reativo)
_Esta seção deve listar os componentes e táticas presentes para atendimento preventivo (ex.: limites, validações, políticas) e reativo (ex.: alertas, contenção, correção) deste RNF._

#### C. Como recuperar/subsidiar o tratamento de impactos
_Esta seção deve descrever os componentes e procedimentos usados para subsidiar o atendimento a falhas que causem quebras de níveis de serviço, incluindo justificativas, detalhamento e passos de recuperação._

---

### 5.3.3 RNF-03 — <Rastreabilidade>

#### A. Como monitorar o RNF
_Esta seção deve indicar como o nível de atendimento deste RNF é monitorado (componentes, métricas, SLIs/SLOs), e se o monitoramento é manual e/ou sistêmico, considerando limitações/vulnerabilidades._

#### B. Como resolver o RNF (Preventivo e Reativo)
_Esta seção deve listar os componentes e táticas presentes para atendimento preventivo (ex.: limites, validações, políticas) e reativo (ex.: alertas, contenção, correção) deste RNF._

#### C. Como recuperar/subsidiar o tratamento de impactos
_Esta seção deve descrever os componentes e procedimentos usados para subsidiar o atendimento a falhas que causem quebras de níveis de serviço, incluindo justificativas, detalhamento e passos de recuperação._

---

## 5.4 Análise de Causas e Impactos

### 5.4.1 RNF-01 — <Escalabilidade>

#### C. Como recuperar/subsidiar o tratamento de impactos
_Esta seção deve descrever os componentes e procedimentos usados para subsidiar o atendimento a falhas que causem quebras de níveis de serviço, incluindo justificativas, detalhamento e passos de recuperação._

---

### 5.4.2 RNF-02 — <Segurança>

#### C. Como recuperar/subsidiar o tratamento de impactos
_Esta seção deve descrever os componentes e procedimentos usados para subsidiar o atendimento a falhas que causem quebras de níveis de serviço, incluindo justificativas, detalhamento e passos de recuperação._

---

### 5.4.3 RNF-03 — <Rastreabilidade>

#### C. Como recuperar/subsidiar o tratamento de impactos
_Esta seção deve descrever os componentes e procedimentos usados para subsidiar o atendimento a falhas que causem quebras de níveis de serviço, incluindo justificativas, detalhamento e passos de recuperação._

---

# 6. Especificação da Solução Técnica do Sistema Novo

_(Descreva como a nova arquitetura elimina as vulnerabilidades e implementa melhorias técnicas e de negócio.)_

---

## 6.1 Revisão do Mapa de RNFs do Sistema Novo

_(Definir e destacar os 3 RNFs priorizados para o sistema novo, alinhados aos defeitos do atual. Evidenciar, de forma objetiva, as melhorias esperadas em relação ao estado atual.)_

---

## 6.2 Revisão do Mapa de RNFs do Sistema Novo e Vulnerabilidades Eliminadas

_(Para cada RNF priorizado do sistema novo, detalhar entradas, saídas e controles, evidenciando como suplantam as vulnerabilidades do sistema atual.)_

### 6.2.1 RNF-01 — <Escalabilidade>

#### A. Entrada
_Esta seção deve descrever os dados e transações de entrada esperados para o sistema novo (volumetria, tipos, frequência, origem), incluindo o patamar aceitável em cenários de pico._

#### B. Saída
_Esta seção deve listar os registros de transações realizadas corretamente e as inadequadas (ex.: rejeitadas por limite), destacando como esses registros evidenciam a melhoria frente ao sistema atual._

#### C. Controle do RNF
_Esta seção deve indicar como as transações corretas e inadequadas são controladas no novo sistema (sistemicamente e/ou manualmente), relacionando as táticas e componentes que eliminam as vulnerabilidades anteriores._

---

### 6.2.2 RNF-02 — <Segurança>

#### A. Entrada
_Esta seção deve descrever os dados e transações de entrada sob a ótica de segurança/privacidade (ex.: tentativas de login, chamadas autenticadas, volume de queries), com limites aceitáveis para o sistema novo._

#### B. Saída
_Esta seção deve listar os registros de transações corretas e fraudulentas/bloqueadas, mostrando como a nova arquitetura evidencia a melhoria de bloqueio, detecção e rastreabilidade em relação ao atual._

#### C. Controle do RNF
_Esta seção deve indicar como o requisito é controlado no novo sistema (políticas, mecanismos sistêmicos e procedimentos), considerando as táticas e componentes que suplantam as vulnerabilidades._

---

### 6.2.3 RNF-03 — <Rastreabilidade>

#### A. Entrada
_Esta seção deve descrever as entradas que geram eventos auditáveis (ações de usuários e agentes), com a cobertura mínima aceitável para o sistema novo._

#### B. Saída
_Esta seção deve listar os registros de auditoria esperados (ações corretas e tentativas indevidas), destacando como a saída evidencia a melhoria de rastreabilidade e consulta em relação ao atual._

#### C. Controle do RNF
_Esta seção deve indicar como o requisito é controlado (event sourcing, políticas de retenção, integridade por hash), relacionando componentes que eliminam as falhas do sistema atual._

---

## 6.3 Táticas Arquiteturais e Componentes Adotados (Sistema Novo)

_(Descrever táticas e componentes que viabilizam a execução e o controle dos RNFs do sistema novo, demonstrando a eliminação das vulnerabilidades.)_

### 6.3.1 RNF-01 — <Escalabilidade>

#### A. Como monitorar o RNF
_Esta seção deve indicar como o nível de atendimento deste RNF será monitorado (componentes, métricas, SLIs/SLOs), justificando como a monitoração aprimorada suplantará limitações do atual._

#### B. Como resolver o RNF (Preventivo e Reativo)
_Esta seção deve listar os componentes e táticas preventivas (ex.: auto-scaling, rate limiting, cache) e reativas (ex.: circuit breaker, shedding) que eliminam as limitações._

#### C. Como recuperar/subsidiar o tratamento de impactos
_Esta seção deve descrever os componentes e procedimentos para recuperar níveis de serviço (ex.: fila de prioridade, reprocessamento, rollback), com justificativas e passos._

---

### 6.3.2 RNF-02 — <Segurança>

#### A. Como monitorar o RNF
_Esta seção deve indicar como o requisito será monitorado (ex.: SIEM, alertas de IAM, WAF), e como essa monitoração elimina as vulnerabilidades do atual._

#### B. Como resolver o RNF (Preventivo e Reativo)
_Esta seção deve listar componentes preventivos (ex.: login/senha, MFA, RBAC/ABAC, criptografia de dados em trânsito e em repouso) e reativos (ex.: detecção de anomalias, contenção, revogação de sessões)._ 

#### C. Como recuperar/subsidiar o tratamento de impactos
_Esta seção deve descrever procedimentos para recuperação pós-incidente (ex.: identificação de transações fraudulentas, recomposição de dados, comunicação e evidências)._ 

_Exemplo de táticas para requisito de privacidade:_
- _Resistência à invasão: autenticação forte (MFA), RBAC/ABAC, criptografia end-to-end._
- _Detecção da invasão: rastreabilidade de transações, monitoramento de acessos, análise de padrões/sazonalidade._
- _Recuperação da invasão: identificação e reversão de transações fraudulentas, recomposição de impactos._

---

### 6.3.3 RNF-03 — <Rastreabilidade>

#### A. Como monitorar o RNF
_Esta seção deve indicar como a cobertura de auditoria será verificada (ex.: amostragem contínua, SLIs de cobertura, tempo de consulta), mostrando a superação do atual._

#### B. Como resolver o RNF (Preventivo e Reativo)
_Esta seção deve listar táticas preventivas (ex.: event sourcing, correlação automática, políticas de retenção) e reativas (ex.: reconstrução de trilhas, enriquecimento de logs)._ 

#### C. Como recuperar/subsidiar o tratamento de impactos
_Esta seção deve descrever como subsidiar investigações (ex.: integridade por hash, cadeia de custódia, export de evidências) e procedimentos de recuperação._

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

[1] COMPANHIA DO METROPOLITANO DE SÃO PAULO – METRÔ. Sobre o Metrô de São Paulo. Disponível em: https://www.metro.sp.gov.br. Acesso em: 22 out. 2025.

[2] INTELI; COMPANHIA DO METROPOLITANO DE SÃO PAULO – METRÔ. TAPI – Módulo 8: Arquitetura de Software Flexível e Sustentável – Projeto: Arquitetura para Agente de IA Portfólio de Projetos do Metrô. São Paulo: Inteli, 2025.

[3] SÃO PAULO (Município). Lei Municipal nº 6.988, de 26 de dezembro de 1966: Cria a Companhia do Metropolitano de São Paulo – Metrô. Disponível em: https://transparencia.metrosp.com.br/dataset/lei-municipal-6988. Acesso em: 22 out. 2025.
