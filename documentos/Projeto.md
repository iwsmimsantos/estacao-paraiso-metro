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

- [Nome do Projeto: Estação Portuguesa Tietê Acesso ao Terminal Rodoviário](#nome-do-projeto-estação-portuguesa-tietê-acesso-ao-terminal-rodoviário)
  - [Nome do Grupo: Estação Paraíso](#nome-do-grupo-estação-paraíso)
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
    - [**RNF-01: Rastreabilidade** ⭐ **PRIORIDADE ALTA**](#rnf-01-rastreabilidade--prioridade-alta)
    - [**RNF-02: Segurança** ⭐ **PRIORIDADE ALTA**](#rnf-02-segurança--prioridade-alta)
    - [**RNF-03: Escalabilidade** ⭐ **PRIORIDADE ALTA**](#rnf-03-escalabilidade--prioridade-alta)
  - [4.2 Justificativas para RNFs](#42-justificativas-para-rnfs)
    - [4.2.1 Controle de Riscos e Mitigação](#421-controle-de-riscos-e-mitigação)
    - [4.2.2 Argumentação por RNF](#422-argumentação-por-rnf)
      - [**Rastreabilidade**](#rastreabilidade)
      - [**Segurança**](#segurança)
      - [**Escalabilidade**](#escalabilidade)
  - [4.3 Melhorias Esperadas com Implementação de RNFs](#43-melhorias-esperadas-com-implementação-de-rnfs)
    - [4.3.1 Melhorias por RNF](#431-melhorias-por-rnf)
    - [4.3.2 Indicadores Consolidados](#432-indicadores-consolidados)
    - [4.3.3 Benefícios Transversais](#433-benefícios-transversais)
  - [4.4 Consolidação dos Requisitos e Diretrizes para a Nova Arquitetura](#44-consolidação-dos-requisitos-e-diretrizes-para-a-nova-arquitetura)
    - [4.4.1 Requisitos Não Funcionais (Priorizados)](#441-requisitos-não-funcionais-priorizados)
    - [4.4.2 Requisitos Funcionais (Suporte)](#442-requisitos-funcionais-suporte)
    - [4.4.3 Diretrizes Arquiteturais](#443-diretrizes-arquiteturais)
    - [4.4.4 Mapa de Rastreabilidade](#444-mapa-de-rastreabilidade)
- [5. Avaliação dos Mecanismos Utilizados no Sistema Atual (Diagnóstico ATAM)](#5-avaliação-dos-mecanismos-utilizados-no-sistema-atual-diagnóstico-atam)
  - [5.1 Mapa de RNFs](#51-mapa-de-rnfs)
  - [5.2 Revisão do Mapa de RNFs e Vulnerabilidades](#52-revisão-do-mapa-de-rnfs-e-vulnerabilidades)
    - [**Fluxo de Trabalho do Sistema Atual (AS-IS)**](#fluxo-de-trabalho-do-sistema-atual-as-is)
    - [**Consolidação dos RNFs e Vulnerabilidades Mapeadas**](#consolidação-dos-rnfs-e-vulnerabilidades-mapeadas)
    - [5.2.1 RNF-01 — Escalabilidade](#521-rnf-01--escalabilidade)
      - [A. Entrada - Dados e Transações de Entrada](#a-entrada---dados-e-transações-de-entrada)
      - [B. Saída – Registros de Transações Corretas e Inadequadas](#b-saída--registros-de-transações-corretas-e-inadequadas)
      - [C. Controle do RNF – Indicação de Controle](#c-controle-do-rnf--indicação-de-controle)
    - [5.2.2 RNF-02 — \<Segurança\>](#522-rnf-02--segurança)
      - [A. Entrada - Dados e Transações de Entrada](#a-entrada---dados-e-transações-de-entrada-1)
      - [B. Saída - Registros de Transações Corretas e Inadequadas](#b-saída---registros-de-transações-corretas-e-inadequadas)
      - [C. Controle do RNF - Indicação de Controle](#c-controle-do-rnf---indicação-de-controle)
      - [1ª Etapa (Elaboração de Cronograma) - Controle de Acesso ao SharePoint:](#1ª-etapa-elaboração-de-cronograma---controle-de-acesso-ao-sharepoint)
      - [2ª Etapa (Documentação Miro/TAP) - Duplo Controle:](#2ª-etapa-documentação-mirotap---duplo-controle)
      - [3ª Etapa (Reporte Mensal) - Controle de Atualização:](#3ª-etapa-reporte-mensal---controle-de-atualização)
      - [4ª Etapa (Armazenamento de Dados) - Controle de Inserção/Alteração:](#4ª-etapa-armazenamento-de-dados---controle-de-inserçãoalteração)
      - [5ª Etapa (Geração de Relatórios) - Controle de Acesso e Exportação:](#5ª-etapa-geração-de-relatórios---controle-de-acesso-e-exportação)
    - [5.2.3 RNF-03 — Rastreabilidade](#523-rnf-03--rastreabilidade)
      - [A. Entrada](#a-entrada)
      - [B. Saída](#b-saída)
      - [C. Controle do RNF](#c-controle-do-rnf)
  - [5.3 Táticas Arquiteturais e Componentes Adotados](#53-táticas-arquiteturais-e-componentes-adotados)
    - [5.3.1 RNF-01 — Escalabilidade](#531-rnf-01--escalabilidade)
      - [A. Como monitorar o RNF](#a-como-monitorar-o-rnf)
      - [B. Como resolver o RNF (Preventivo e Reativo)](#b-como-resolver-o-rnf-preventivo-e-reativo)
      - [C. Como recuperar/subsidiar o tratamento de impactos](#c-como-recuperarsubsidiar-o-tratamento-de-impactos)
    - [5.3.2 RNF-02 — \<Segurança\>](#532-rnf-02--segurança)
      - [A. Como monitorar o RNF](#a-como-monitorar-o-rnf-1)
        - [1ª Etapa (Elaboração de Cronograma) - SharePoint Audit Logs:](#1ª-etapa-elaboração-de-cronograma---sharepoint-audit-logs)
        - [2ª Etapa (Documentação Miro/TAP):](#2ª-etapa-documentação-mirotap)
        - [3ª Etapa (Reporte Mensal) - SharePoint Audit Logs:](#3ª-etapa-reporte-mensal---sharepoint-audit-logs)
        - [4ª Etapa (Armazenamento de Dados) - SharePoint Audit Logs:](#4ª-etapa-armazenamento-de-dados---sharepoint-audit-logs)
        - [5ª Etapa (Geração de Relatórios):](#5ª-etapa-geração-de-relatórios)
        - [Componentes Transversais de Monitoramento de Segurança:](#componentes-transversais-de-monitoramento-de-segurança)
        - [Indicadores de Nível de Serviço de Segurança (SLIs/SLOs):](#indicadores-de-nível-de-serviço-de-segurança-slisslos)
        - [Tipo de Monitoramento:](#tipo-de-monitoramento)
      - [B. Como resolver o RNF (Preventivo e Reativo)](#b-como-resolver-o-rnf-preventivo-e-reativo-1)
        - [Táticas Preventivas:](#táticas-preventivas)
          - [1ª Etapa (Elaboração de Cronograma) - Controle de Acesso:](#1ª-etapa-elaboração-de-cronograma---controle-de-acesso)
          - [2ª Etapa (Documentação Miro/TAP) - Rastreabilidade e Controle de Integridade:](#2ª-etapa-documentação-mirotap---rastreabilidade-e-controle-de-integridade)
          - [3ª Etapa (Reporte Mensal) - Validação de Status:](#3ª-etapa-reporte-mensal---validação-de-status)
          - [4ª Etapa (Armazenamento de Dados) - Controle de Alterações Críticas:](#4ª-etapa-armazenamento-de-dados---controle-de-alterações-críticas)
          - [5ª Etapa (Geração de Relatórios) - Controle de Exportação:](#5ª-etapa-geração-de-relatórios---controle-de-exportação)
          - [Táticas Preventivas Transversais (Microsoft 365):](#táticas-preventivas-transversais-microsoft-365)
        - [Táticas Reativas:](#táticas-reativas)
          - [Detecção de Violações:](#detecção-de-violações)
          - [Contenção de Incidentes:](#contenção-de-incidentes)
          - [Correção e Recuperação:](#correção-e-recuperação)
      - [C. Como recuperar/subsidiar o tratamento de impactos](#c-como-recuperarsubsidiar-o-tratamento-de-impactos-1)
        - [Componentes de Recuperação por Tipo de Incidente:](#componentes-de-recuperação-por-tipo-de-incidente)
          - [1. Acesso Inadequado a Cronogramas/TAPs/Documentos (Violação de Segregação por Projeto):](#1-acesso-inadequado-a-cronogramastapsdocumentos-violação-de-segregação-por-projeto)
          - [2. Manipulação de Dados em Transferência Manual (Miro → TAP no SharePoint):](#2-manipulação-de-dados-em-transferência-manual-miro--tap-no-sharepoint)
          - [3. Alteração Não Autorizada de Documentos Críticos (TAP Aprovado, Cronograma Baseline):](#3-alteração-não-autorizada-de-documentos-críticos-tap-aprovado-cronograma-baseline)
          - [4. Exclusão Acidental ou Maliciosa de Documentos:](#4-exclusão-acidental-ou-maliciosa-de-documentos)
          - [5. Exportação Não Autorizada e Vazamento de Informações:](#5-exportação-não-autorizada-e-vazamento-de-informações)
          - [6. Indisponibilidade por Falha da Microsoft 365:](#6-indisponibilidade-por-falha-da-microsoft-365)
    - [5.3.3 RNF-03 — Rastreabilidade](#533-rnf-03--rastreabilidade)
      - [A. Como monitorar o RNF](#a-como-monitorar-o-rnf-2)
      - [B. Como resolver o RNF (Preventivo e Reativo)](#b-como-resolver-o-rnf-preventivo-e-reativo-2)
      - [C. Como recuperar/subsidiar o tratamento de impactos](#c-como-recuperarsubsidiar-o-tratamento-de-impactos-2)
  - [5.4 Análise de Causas e Impactos](#54-análise-de-causas-e-impactos)
    - [5.4.1 RNF-01 — Escalabilidade](#541-rnf-01--escalabilidade)
      - [Causas e Impactos da Quebra de Escalabilidade](#causas-e-impactos-da-quebra-de-escalabilidade)
      - [Detalhamento da Quebra de Nível de Serviço](#detalhamento-da-quebra-de-nível-de-serviço)
      - [Como recuperar/subsidiar o tratamento de impactos](#como-recuperarsubsidiar-o-tratamento-de-impactos)
    - [5.4.2 RNF-02 — \<Segurança\>](#542-rnf-02--segurança)
      - [C. Como recuperar/subsidiar o tratamento de impactos](#c-como-recuperarsubsidiar-o-tratamento-de-impactos-3)
        - [Matriz Consolidada de Recuperação por Tipo de Incidente:](#matriz-consolidada-de-recuperação-por-tipo-de-incidente)
        - [Template de Relatório de Incidente para Gestão:](#template-de-relatório-de-incidente-para-gestão)
        - [Documentação de Suporte para Justificativas (Anexos-Padrão):](#documentação-de-suporte-para-justificativas-anexos-padrão)
        - [Critérios para Escalonamento de Incidentes:](#critérios-para-escalonamento-de-incidentes)
        - [Exemplo de Justificativa Consolidada para Alta Gestão:](#exemplo-de-justificativa-consolidada-para-alta-gestão)
        - [Vulnerabilidade Final de Recuperação:](#vulnerabilidade-final-de-recuperação)
    - [5.4.3 RNF-03 — Rastreabilidade](#543-rnf-03--rastreabilidade)
      - [Causas e Impactos da Quebra de Rastreabilidade](#causas-e-impactos-da-quebra-de-rastreabilidade)
      - [Detalhamento da Quebra de Nível de Serviço](#detalhamento-da-quebra-de-nível-de-serviço-1)
      - [Como recuperar/subsidiar o tratamento de impactos](#como-recuperarsubsidiar-o-tratamento-de-impactos-1)
- [6. Especificação da Solução Técnica do Sistema Novo](#6-especificação-da-solução-técnica-do-sistema-novo)
  - [6.1 Revisão do Mapa de RNFs do Sistema Novo](#61-revisão-do-mapa-de-rnfs-do-sistema-novo)
  - [6.2 Revisão do Mapa de RNFs do Sistema Novo e Vulnerabilidades Eliminadas](#62-revisão-do-mapa-de-rnfs-do-sistema-novo-e-vulnerabilidades-eliminadas)
    - [6.2.1 RNF-01 — ](#621-rnf-01--)
      - [A. Entrada](#a-entrada-1)
      - [B. Saída](#b-saída-1)
      - [C. Controle do RNF](#c-controle-do-rnf-1)
    - [6.2.2 RNF-02 — \<Segurança\>](#622-rnf-02--segurança)
      - [A. Entrada](#a-entrada-2)
      - [B. Saída](#b-saída-2)
      - [C. Controle do RNF](#c-controle-do-rnf-2)
    - [6.2.3 RNF-03 — ](#623-rnf-03--)
      - [A. Entrada](#a-entrada-3)
      - [B. Saída](#b-saída-3)
      - [C. Controle do RNF](#c-controle-do-rnf-3)
  - [6.3 Táticas Arquiteturais e Componentes Adotados (Sistema Novo)](#63-táticas-arquiteturais-e-componentes-adotados-sistema-novo)
    - [6.3.1 RNF-01 — ](#631-rnf-01--)
      - [A. Como monitorar o RNF](#a-como-monitorar-o-rnf-3)
      - [B. Como resolver o RNF (Preventivo e Reativo)](#b-como-resolver-o-rnf-preventivo-e-reativo-3)
      - [C. Como recuperar/subsidiar o tratamento de impactos](#c-como-recuperarsubsidiar-o-tratamento-de-impactos-4)
    - [6.3.2 RNF-02 — \<Segurança\>](#632-rnf-02--segurança)
      - [A. Como monitorar o RNF](#a-como-monitorar-o-rnf-4)
      - [B. Como resolver o RNF (Preventivo e Reativo)](#b-como-resolver-o-rnf-preventivo-e-reativo-4)
      - [C. Como recuperar/subsidiar o tratamento de impactos](#c-como-recuperarsubsidiar-o-tratamento-de-impactos-5)
    - [6.3.3 RNF-03 — ](#633-rnf-03--)
      - [A. Como monitorar o RNF](#a-como-monitorar-o-rnf-5)
      - [B. Como resolver o RNF (Preventivo e Reativo)](#b-como-resolver-o-rnf-preventivo-e-reativo-5)
      - [C. Como recuperar/subsidiar o tratamento de impactos](#c-como-recuperarsubsidiar-o-tratamento-de-impactos-6)
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

| Código | Nome do Risco                                              | Tipo                   | Descrição                                                                                                                                    | Aspectos Afetados                                            | Probabilidade |  Impacto   |
| :----: | :--------------------------------------------------------- | :--------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- | :-----------: | :--------: |
| **R1** | **Inconsistência de Dados**                                | Técnico / Negócio      | O preenchimento manual de informações em diferentes plataformas (Miro, SharePoint, Excel) pode gerar divergências e falta de padronização.   | **Precisão**, **Integridade de Dados**                       |      70%      |    Alto    |
| **R2** | **Dependência de Processos Manuais**                       | Técnico / Operacional  | A ausência de automação completa para entrada, validação e atualização de dados aumenta a chance de erros humanos.                           | **Desempenho**, **Disponibilidade**, **Confiabilidade**      |      80%      |  Moderado  |
| **R3** | **Falha de Integração entre Ferramentas**                  | Técnico                | Problemas de sincronização entre _Power Automate_, _Power BI_ e _SharePoint_ podem comprometer relatórios e atualizações de status.          | **Disponibilidade**, **Tolerância a Falhas**, **Desempenho** |      60%      |    Alto    |
| **R4** | **Acesso Indevido a Informações**                          | Compliance / Segurança | Falhas nas permissões de acesso no _SharePoint_ ou _Power BI_ podem permitir a visualização de dados sensíveis por usuários não autorizados. | **Segurança**, **Governança**, **Confidencialidade**         |      40%      | Muito Alto |
| **R5** | **Baixa Rastreabilidade das Ações**                        | Técnico / Governança   | As plataformas atuais não possuem logs integrados e centralizados de auditoria das ações dos usuários e fluxos do _Power Automate_.          | **Rastreabilidade**, **Auditoria**, **Transparência**        |      50%      |  Moderado  |
| **R6** | **Dependência de Conectividade e Licenciamento Microsoft** | Negócio / Técnico      | A indisponibilidade de serviços Microsoft ou falhas de licenciamento podem interromper o funcionamento das automações e relatórios.          | **Disponibilidade**, **Continuidade Operacional**            |      30%      |    Alto    |

### 2.2.3 Oportunidades de melhoria dos SLAs

&emsp;Apesar de funcional, o ecossistema apresenta oportunidades de melhoria voltadas à disponibilidade, desempenho, segurança, rastreabilidade e governança dos dados, com foco em elevar os níveis de serviço (SLA) e reduzir riscos operacionais.

| Código | Oportunidade                                               | Descrição                                                                                                                                                          | SLA Impactado                                | Benefício Esperado                                                                          |
| :----: | :--------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------- | :------------------------------------------------------------------------------------------ |
| **O1** | **Automatização de Monitoramento de Serviços**             | Criação de fluxos no Power Automate para monitorar a disponibilidade das integrações entre SharePoint, Power BI e Miro, com alertas automáticos em caso de falhas. | **Disponibilidade**, **Tolerância a Falhas** | Redução do tempo de detecção e resposta a incidentes, garantindo continuidade dos serviços. |
| **O2** | **Padronização de Logs e Auditorias**                      | Implementação de uma política de versionamento e armazenamento centralizado de logs das ações realizadas nas plataformas.                                          | **Rastreabilidade**, **Segurança**           | Melhoria na rastreabilidade e suporte a auditorias internas e externas.                     |
| **O3** | **Otimização de Processos no Power Automate**              | Revisão e otimização dos fluxos de automação existentes para eliminar redundâncias e gargalos de execução.                                                         | **Desempenho**, **Disponibilidade**          | Redução do tempo de processamento e aumento da eficiência operacional.                      |
| **O4** | **Melhoria na Integração entre Ferramentas**               | Criação de conectores otimizados entre SharePoint, Power BI e Miro, minimizando falhas de sincronização e perda de dados.                                          | **Disponibilidade**, **Rastreabilidade**     | Garantia de consistência dos dados e maior confiabilidade nas informações compartilhadas.   |
| **O5** | **Fortalecimento das Políticas de Segurança e Compliance** | Revisão dos controles de acesso, autenticação e permissões no SharePoint e Miro, alinhando-se às diretrizes da LGPD.                                               | **Segurança**, **Compliance**                | Diminuição do risco de acesso indevido e exposição de informações sensíveis.                |
| **O6** | **Criação de Painéis de Acompanhamento de SLA**            | Desenvolvimento de dashboards no Power BI para consolidar métricas de disponibilidade, desempenho e incidentes.                                                    | **Governança**, **Transparência**            | Visibilidade contínua sobre o cumprimento dos SLAs e suporte à tomada de decisão gerencial. |

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

| **Requisito Não Funcional** | **Estado Atual do Metrô (Deficiente)**                                                                                                                                       | **Arquitetura Reformada (Desejada)**                                                                                                                               | **Checklist de Implementação**                                                                                                                                                                                                                              |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Escalabilidade**          | • Dependência total de ferramentas externas sem controle<br>• Ausência de balanceamento de carga<br>• Processamento sequencial manual<br>• Limitação de usuários simultâneos | • Arquitetura escalável com auto-scaling<br>• Balanceamento de carga automático<br>• Processamento paralelo com IA<br>• Suporte a milhares de usuários simultâneos | **☐ Implementar auto-scaling horizontal**<br>**☐ Configurar load balancer (HAProxy/Nginx)**<br>**☐ Implementar processamento paralelo com IA**<br>**☐ Otimizar para milhares de usuários simultâneos**<br>**☐ Configurar métricas de escalabilidade**       |
| **Disponibilidade**         | • Dependência de SLA de terceiros (Miro/SharePoint)<br>• Ausência de redundância<br>• Sem monitoramento proativo<br>• Downtime não controlado                                | • SLA de 99.9% garantido<br>• Redundância e failover automático<br>• Monitoramento 24/7<br>• Recuperação automática em <5s                                         | Não Trabalharemos                                                                                                                                                                                                                                           |
| **Segurança**               | • Controle de acesso limitado<br>• Ausência de auditoria<br>• Dependência de políticas externas<br>• Dados expostos em ferramentas de terceiros                              | • Controle de acesso granular<br>• Auditoria completa de todas as ações<br>• Criptografia end-to-end<br>• Conformidade com LGPD                                    | **☐ Implementar controle de acesso granular (RBAC)**<br>**☐ Configurar auditoria completa de ações**<br>**☐ Implementar criptografia end-to-end**<br>**☐ Garantir conformidade com LGPD**<br>**☐ Implementar autenticação multi-fator**                     |
| **Rastreabilidade**         | • Logs limitados das ferramentas<br>• Ausência de trilha integrada<br>• Dificuldade de correlação<br>• Sem compliance automático                                             | • Logs detalhados de todas as ações<br>• Trilha de auditoria integrada<br>• Correlação automática de eventos<br>• Compliance e relatórios automáticos              | **☐ Implementar logs detalhados de todas as ações**<br>**☐ Configurar trilha de auditoria integrada**<br>**☐ Implementar correlação automática de eventos**<br>**☐ Configurar compliance e relatórios automáticos**<br>**☐ Implementar sistema de alertas** |
| **Performance**             | • Dependência de conectividade externa<br>• Processamento manual<br>• Ausência de cache<br>• Tempos de resposta imprevisíveis                                                | • Processamento local otimizado<br>• Cache inteligente<br>• Tempo de resposta <1s<br>• Otimização com IA                                                           | Não Trabalharemos                                                                                                                                                                                                                                           |
| **Tolerância a Falhas**     | • Sem mecanismos de recuperação<br>• Falha única pode parar todo o sistema<br>• Perda de dados em caso de falha<br>• Recuperação manual                                      | • Recuperação automática<br>• Redundância em múltiplas camadas<br>• Zero perda de dados<br>• Failover transparente                                                 | Não Trabalharemos                                                                                                                                                                                                                                           |

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

| **RNF**                 | **Estado Atual (Deficiente)**                                                                                                                                                                                     | **Vulnerabilidades Críticas**                                                                                                                          | **Impacto no Negócio**                                                                                                               |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Escalabilidade**      | • Dependência de ferramentas externas sem controle<br>• Ausência de balanceamento de carga, sem previsibilidade e controle de demanda<br>• Processamento sequencial manual<br>• Limitação de usuários simultâneos | • Sistema colapsa com muitos usuários simultâneos<br>• Impossibilidade de crescimento proporcional à demanda<br>• Gargalos de processamento            | • Operações paralisadas em picos de demanda<br>• Limitação de uso<br>• Inviabilidade de expansão futura                              |
| **Disponibilidade**     | • Dependência de SLA de terceiros (Miro/SharePoint)<br>• Ausência de redundância<br>• Sem monitoramento proativo<br>• Downtime não controlado                                                                     | • Risco de indisponibilidade em software de terceiros<br>• Qualquer reparo nas ferramentas depende de uma equipe externa<br>• Perda de dados em falhas | • Paralisação de projetos de R$ 1,5 bi/ano<br>• +6.000 colaboradores impactados<br>• Perda de informações para decisões estratégicas |
| **Segurança**           | • Controle de acesso limitado<br>• Ausência de auditoria<br>• Dependência de políticas externas<br>• Dados expostos em ferramentas de terceiros                                                                   | • Dados sensíveis expostos a políticas externas<br>• 0% de tentativas de ataque detectadas<br>• Criptografia básica                                    | • Risco de vazamento de informações estratégicas<br>• Violação de LGPD<br>• Danos à imagem institucional                             |
| **Rastreabilidade**     | • Logs limitados das ferramentas<br>• Ausência de trilha integrada<br>• Dificuldade de correlação<br>• Sem compliance automático                                                                                  | • Ações não auditáveis<br>• Falta de recuperação de logs<br>• Sem verificação de integridade                                                           | • Violação de compliance para empresa pública<br>• Impossibilidade de investigação de incidentes<br>• Riscos legais de multas        |
| **Performance**         | • Dependência de conectividade externa<br>• Processamento manual<br>• Ausência de cache<br>• Tempos de resposta imprevisíveis                                                                                     | • Tempo de resposta muito lento<br>• Degradação severa em picos<br>• Baixa eficiência operacional                                                      | • Perda de produtividade de equipes<br>• Frustração de usuários<br>• Retrabalho por timeouts                                         |
| **Tolerância a Falhas** | • Sem mecanismos de recuperação<br>• Falha única pode parar todo o sistema<br>• Perda de dados em caso de falha<br>• Recuperação manual                                                                           | • Sistema colapsado em qualquer falha<br>• Recuperação manual prolongada<br>• Alta perda de dados                                                      | • Downtime prolongado (60-120 min)<br>• Perda de informações críticas<br>• Impacto operacional severo                                |

**Seleção dos RNFs Críticos (Priorizados)**

Com base nos **business drivers** (Seção 2.1.5) e na análise de riscos, foram selecionados **3 RNFs críticos**:

#### **RNF-01: Rastreabilidade** ⭐ **PRIORIDADE ALTA**

**Justificativa:**

- **Business Driver:** "Rastreabilidade completa das tentativas de acesso"
- **Compliance:** Empresa pública sob fiscalização do TCE
- **Risco:** Multas e violação de governança

**Métricas:**

| **Métrica**        | **Atual** | **Meta**    | **Ganho**            |
| ------------------ | --------- | ----------- | -------------------- |
| **Cobertura logs** | Limitada  | 100%        | Auditabilidade total |
| **Recuperação**    | Demorada  | <2s         | Investigação ágil    |
| **Integridade**    | 0%        | 100% (hash) | Não repúdio          |
| **Compliance**     | Violado   | Atendido    | Requisito legal      |

#### **RNF-02: Segurança** ⭐ **PRIORIDADE ALTA**

**Justificativa:**

- **Business Driver:** "Segurança com controle de acesso baseado em perfis"
- **LGPD:** Proteção de dados de R$ 10 bilhões em projetos
- **Risco:** Vazamento de informações estratégicas

**Métricas:**

| **Métrica**          | **Atual**    | **Meta**        | **Ganho**         |
| -------------------- | ------------ | --------------- | ----------------- |
| **Controle acesso**  | Limitado     | Granular (RBAC) | Segmentação       |
| **Detecção ataques** | 0%           | 100%            | Proteção proativa |
| **Criptografia**     | Básica       | End-to-end      | Proteção integral |
| **LGPD**             | Não atendida | Atendida        | Conformidade      |

#### **RNF-03: Escalabilidade** ⭐ **PRIORIDADE ALTA**

**Justificativa:**

- **Business Driver:** "Preparar sistema para crescimento futuro e integração de agentes de IA"
- **Contexto:** Expansão da rede metroviária + aumento de projetos + automação com IA
- **Risco:** Limitação atual impede expansão operacional

**Métricas:**

| **Métrica**              | **Atual**  | **Meta**        | **Ganho**           |
| ------------------------ | ---------- | --------------- | ------------------- |
| **Usuários simultâneos** | Limitado   | 100+            | Suporte crescimento |
| **Balanceamento**        | Ausente    | Automático      | Distribuição carga  |
| **Processamento**        | Sequencial | Paralelo com IA | Automação           |
| **Previsibilidade**      | Zero       | Total           | Planejamento        |

---

## 4.2 Justificativas para RNFs

### 4.2.1 Controle de Riscos e Mitigação

| **RNF**             | **Risco**                           | **Impacto**                               | **Mitigação**                               |
| ------------------- | ----------------------------------- | ----------------------------------------- | ------------------------------------------- |
| **Rastreabilidade** | Logs limitados impedem auditoria    | Violação compliance TCE + multas          | Logs 100% + trilha integrada + hash SHA-256 |
| **Segurança**       | Dados expostos a políticas externas | Vazamento estratégico + LGPD              | RBAC + detecção 100% + AES-256              |
| **Escalabilidade**  | Gargalos impedem crescimento        | Operações paralisadas + expansão inviável | Auto-scaling + balanceamento + IA           |

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

| **RNF**             | **Atual**                                             | **Novo**                                          | **Ganhos**                                             |
| ------------------- | ----------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------ |
| **Rastreabilidade** | Logs limitados<br>Sem trilha<br>Compliance violado    | 100% logs<br>Trilha integrada<br>Compliance total | Auditabilidade<br>Recuperação <2s<br>Conformidade TCE  |
| **Segurança**       | Controle limitado<br>0% detecção<br>LGPD não atendida | RBAC<br>100% detecção<br>LGPD atendida            | Segmentação<br>Proteção proativa<br>Conformidade legal |
| **Escalabilidade**  | Usuários limitados<br>Sem balanceamento<br>Sequencial | 100+ usuários<br>Auto-scaling<br>Paralelo IA      | Suporte crescimento<br>Distribuição carga<br>Automação |

### 4.3.2 Indicadores Consolidados

| **Indicador**             | **Atual**           | **Meta**       | **Impacto**       |
| ------------------------- | ------------------- | -------------- | ----------------- |
| **Autonomia operacional** | Dependência externa | Controle total | Decisões ágeis    |
| **Auditabilidade**        | Limitada            | 100%           | Compliance TCE    |
| **Detecção ameaças**      | 0%                  | 100%           | Proteção integral |
| **Usuários simultâneos**  | Limitado            | 100+           | Expansão viável   |
| **Conformidade legal**    | Violada             | Atendida       | LGPD + TCE        |

### 4.3.3 Benefícios Transversais

- **Autonomia:** Fim da dependência de SLA externo
- **Governança:** Auditabilidade total para TCE
- **Proteção:** R$ 10 bi em projetos seguros
- **Crescimento:** Preparação para expansão + IA

---

## 4.4 Consolidação dos Requisitos e Diretrizes para a Nova Arquitetura

### 4.4.1 Requisitos Não Funcionais (Priorizados)

| **ID**     | **RNF**             | **Critérios**                      | **Prioridade** |
| ---------- | ------------------- | ---------------------------------- | -------------- |
| **RNF-01** | **Rastreabilidade** | 100% logs + recuperação <2s + hash | ALTA           |
| **RNF-02** | **Segurança**       | RBAC + 100% detecção + AES-256     | ALTA           |
| **RNF-03** | **Escalabilidade**  | 100+ usuários + auto-scaling + IA  | ALTA           |

### 4.4.2 Requisitos Funcionais (Suporte)

| **RF**    | **Descrição**                           | **RNFs**       |
| --------- | --------------------------------------- | -------------- |
| **RF-01** | Logs centralizado (100% + hash SHA-256) | RNF-02, RNF-03 |
| **RF-02** | Autenticação RBAC + MFA                 | RNF-03         |
| **RF-03** | Failover automático <5s                 | RNF-01         |
| **RF-04** | Backup contínuo + replicação            | RNF-01         |
| **RF-05** | Painel auditoria <2s                    | RNF-02         |
| **RF-06** | Detecção ameaças (WAF + IDS/IPS)        | RNF-03         |
| **RF-07** | Balanceador carga automático            | RNF-04         |
| **RF-08** | Auto-scaling elástico                   | RNF-04         |

### 4.4.3 Diretrizes Arquiteturais

1. **Infraestrutura Própria:** Controle total eliminando dependência externa
2. **Redundância Automática:** Failover <5s + replicação ativa
3. **Segurança em Camadas:** RBAC + WAF + IDS/IPS + AES-256
4. **Auditabilidade Total:** Event sourcing + logs 100% + hash
5. **Escalabilidade Elástica:** Auto-scaling + balanceamento automático

### 4.4.4 Mapa de Rastreabilidade

| **Business Driver**      | **RNF** | **RF**       | **Benefício**    |
| ------------------------ | ------- | ------------ | ---------------- |
| "Rastreabilidade total"  | RNF-01  | RF-01, RF-05 | 100% auditável   |
| "Segurança com controle" | RNF-02  | RF-02, RF-06 | RBAC + proteção  |
| "Escalabilidade futura"  | RNF-03  | RF-07, RF-08 | Crescimento + IA |

---

# 5. Avaliação dos Mecanismos Utilizados no Sistema Atual (Diagnóstico ATAM)

Esta seção detalha os **mecanismos e componentes arquiteturais** do sistema atual que justificam as **limitações e vulnerabilidades** observadas nos RNFs.  
O objetivo é compreender **as causas dos defeitos** e construir a base para propor **táticas e soluções evolutivas**.

---

## 5.1 Mapa de RNFs

_(Definir o mapa da de RNFs e definir se será realmente o decidido na última sprint)_

## 5.2 Revisão do Mapa de RNFs e Vulnerabilidades

&emsp;Esta seção apresenta a consolidação dos Requisitos Não Funcionais (RNFs) priorizados para a análise do sistema atual (AS-IS), focando nas vulnerabilidades críticas que justificam a necessidade de uma nova arquitetura. Os RNFs analisados são Escalabilidade, Segurança e Rastreabilidade.

&emsp;A análise detalhada a seguir utiliza como referência as 5 etapas do fluxo de trabalho do Portfólio de Projetos, conforme mapeado pelo grupo.

### **Fluxo de Trabalho do Sistema Atual (AS-IS)**

O sistema atual é composto por um fluxo de trabalho sequencial e manual, dividido nas seguintes etapas:

| Etapa        | Descrição                           | Ferramentas Envolvidas     |
| :----------- | :---------------------------------- | :------------------------- |
| **1ª Etapa** | **Elaborar Cronograma**             | Miro, MS Office            |
| **2ª Etapa** | **Documentação do Miro para o TAP** | SharePoint, Miro           |
| **3ª Etapa** | **Reporte Mensal de Status**        | SharePoint, Power BI       |
| **4ª Etapa** | **Armazenamento de Dados**          | SharePoint, Power Automate |
| **5ª Etapa** | **Geração de Relatórios**           | Power BI, SharePoint       |

### **Consolidação dos RNFs e Vulnerabilidades Mapeadas**

A tabela a seguir resume as principais vulnerabilidades identificadas no sistema atual, correlacionando-as com as etapas do processo e os RNFs afetados, com a linguagem técnica concisa:

| RNF                 | Etapa do Processo                         | Vulnerabilidade Mapeada (Descrição Técnica Concisa)                                                                                      |
| :------------------ | :---------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| **Segurança**       | 1ª Etapa: Elaborar Cronograma             | **Controle de Acesso Insuficiente:** Dependência exclusiva do controle nativo do SharePoint.                                             |
| **Segurança**       | 2ª Etapa: Documentação do Miro para o TAP | **Autorização Ampla e Manual:** Permissões excessivas (todos os projetos) devido à gestão manual.                                        |
| **Rastreabilidade** | 2ª Etapa: Documentação do Miro para o TAP | **Auditoria Descentralizada:** Falta de log unificado e imutável para ações em ferramentas externas (Miro).                              |
| **Escalabilidade**  | 3ª Etapa: Reporte Mensal de Status        | **Falta de Padronização:** Ausência de formato de dados e processo de _reporting_ padronizado.                                           |
| **Segurança**       | 4ª Etapa: Armazenamento de Dados          | **Gestão de Permissões Manual:** Processo de concessão/revogação não auditável (risco de acesso indevido).                               |
| **Rastreabilidade** | 4ª Etapa: Armazenamento de Dados          | **Integridade de Dados Comprometida:** Falha na captura consistente de metadados de auditoria (_quem, o quê, quando_).                   |
| **Escalabilidade**  | 4ª Etapa: Armazenamento de Dados          | **Arquitetura de Dados Inadequada:** Uso de repositórios de arquivos (SharePoint) como banco de dados transacional.                      |
| **Segurança**       | 5ª Etapa: Geração de Relatórios           | **Risco de Exposição de Dados:** Gestão de permissões baseada na ferramenta de _reporting_ (Power BI), sem camada de acesso segura.      |
| **Rastreabilidade** | 5ª Etapa: Geração de Relatórios           | **Falta de Rastreabilidade de Consulta:** Ausência de auditoria sobre as consultas e dados acessados durante a geração de relatórios.    |
| **Escalabilidade**  | 5ª Etapa: Geração de Relatórios           | **Performance de Consulta Crítica:** Dependência de repositórios de arquivos, causando lentidão e falhas em relatórios de grande volume. |

---

### 5.2.1 RNF-01 — Escalabilidade

&emsp;A Escalabilidade é um requisito não funcional crítico para o sistema de gestão de portfólio do Metrô de São Paulo, uma vez que a instituição lida com dezenas de projetos ativos simultaneamente e depende da atualização constante de informações estratégicas. A capacidade de o sistema suportar o aumento de usuários, dados e transações sem perda de desempenho é determinante para garantir a eficiência operacional e a confiabilidade dos processos de governança.

&emsp;Atualmente, o sistema é composto por um ecossistema de ferramentas como Miro e do ambiente Microsoft 365, como SharePoint, Power Automate e Power BI. Apesar de atenderem parcialmente à demanda atual, essas plataformas apresentam limitações estruturais e dependência de integrações manuais, o que restringe a expansão das operações e impede o controle direto de capacidade por parte da equipe de TI do Metrô.

&emsp;A seguir, são detalhados os elementos de entrada, saída e controle que evidenciam as vulnerabilidades relacionadas à escalabilidade do ambiente atual (AS-IS).

#### A. Entrada - Dados e Transações de Entrada

&emsp;A entrada de dados no sistema atual ocorre de forma descentralizada e não estruturada, o que impacta diretamente a escalabilidade.

- **Volume de Acessos:** O sistema suporta a entrada e atualização de dados por aproximadamente 40 a 60 usuários ativos (líderes de projeto e equipe) em ciclos mensais. As transações envolvem a edição de listas no SharePoint, a atualização de quadros no Miro e a execução de fluxos no Power Automate.

- **Transações Críticas:** As operações de maior impacto na escalabilidade são o Reporte Mensal de Status (etapa 3), a transferência manual de dados para o SharePoint (etapa 4) e a geração de relatórios no Power BI (etapa 5). Todas essas atividades exigem processamento intenso e síncrono, ocasionando sobrecarga dos serviços e aumento do tempo de resposta.

- **Vulnerabilidade:** A principal vulnerabilidade está na ausência de uma API centralizada, o que impede o controle técnico do tráfego de dados. Todas as integrações dependem de interfaces de usuário e conectores de terceiros (como Power Automate), impossibilitando a implementação de mecanismos de Rate Limiting, Load Balancing ou Parallel Processing, necessários para absorver picos de uso sem degradação.

&emsp;Essas restrições estruturais tornam o sistema sensível a variações no volume de dados, comprometendo a capacidade de expansão e a estabilidade das operações críticas.

#### B. Saída – Registros de Transações Corretas e Inadequadas

&emsp;A análise da saída de dados evidencia como o sistema responde ao processamento das informações e às operações realizadas pelos usuários. A seguir, aborda-se o comportamento das transações corretas e inadequadas, destacando gargalos de desempenho e falhas que afetam a confiabilidade e a estabilidade do ambiente.

- **Transações Corretas:** Em condições normais, as operações são concluídas com sucesso, resultando em listas e relatórios atualizados no SharePoint e Power BI. O sistema consegue atender às demandas de uso cotidiano, desde que o volume de requisições simultâneas se mantenha baixo.

- **Transações Inadequadas:** Durante períodos de alta utilização, o sistema apresenta erros de Throttling (limitação de requisições) impostos pelo SharePoint Online, impactando diretamente fluxos críticos. Os principais sintomas observados são:

  - Lentidão perceptível na execução de consultas e carregamento de dados;
  - Perda de dados em fluxos interrompidos no Power Automate, que não completam suas execuções;
  - Indisponibilidade temporária, devido ao bloqueio de serviços após o limite de requisições simultâneas ser atingido.

&emsp;Essas falhas geram impactos diretos na governança do portfólio, uma vez que relatórios mensais e indicadores estratégicos podem conter informações incompletas ou desatualizadas, comprometendo a tomada de decisão da diretoria.

- **Vulnerabilidade:** O sistema não possui mecanismos de Retry (reexecução automática) nem Message Queues (filas de mensagens). Assim, quando uma transação falha, ela não é reprocessada nem registrada adequadamente, exigindo intervenção manual e aumentando a probabilidade de inconsistências.

&emsp;Em um contexto de portfólio corporativo com grande volume de projetos, essa limitação representa uma ameaça à continuidade operacional e à precisão das informações compartilhadas entre as equipes.

#### C. Controle do RNF – Indicação de Controle

&emsp;A análise do controle do requisito de escalabilidade permite compreender como o sistema é monitorado e administrado diante de variações de carga e limitações de desempenho. A seguir, são descritos os controles sistêmicos e manuais existentes, suas restrições operacionais e as melhorias recomendadas para garantir maior autonomia e estabilidade ao ambiente.

- **Controle Sistêmico:** A infraestrutura de escalabilidade é totalmente gerida pela Microsoft (SharePoint Online), o que significa que o Metrô não possui autonomia para ajustar ou otimizar parâmetros de capacidade, balanceamento de carga ou recursos de hardware.

- **Controle Manual:** O único controle existente é de natureza operacional, consistindo em orientações manuais para os usuários — como evitar horários de pico ou dividir tarefas grandes em partes menores. Esse tipo de mitigação não resolve o problema de forma arquitetural e depende do comportamento dos usuários, o que reduz a confiabilidade do sistema.

- **Vulnerabilidade:** Essa dependência de um único fornecedor representa um risco crítico de disponibilidade e dificulta a gestão de performance. A falta de observabilidade (monitoramento contínuo de métricas de uso e falhas) impede que a equipe de TI detecte problemas antes que afetem o usuário final.

- **Melhoria Recomendada:** A arquitetura proposta deve prever a implementação de ferramentas de monitoramento centralizado, integrando métricas de uso, logs de eventos e alertas automáticos. Isso permitiria uma reação preventiva e não apenas corretiva a incidentes, além de subsidiar futuras estratégias de escalabilidade, como o uso de serviços modulares, balanceamento dinâmico e processamento assíncrono.

---

### 5.2.2 RNF-02 — <Segurança>

&emsp;A Segurança é um requisito não funcional crítico para o sistema de Portfólio do Metrô, pois a proteção de dados sensíveis de projetos, o controle de acesso granular e a integridade de informações são fundamentais para a governança adequada do portfólio. No sistema atual, composto por ferramentas como SharePoint, Miro e Power BI, a segurança apresenta vulnerabilidades significativas relacionadas ao controle manual de permissões, ausência de granularidade de acesso por projeto e falta de validação de integridade em transferências manuais de dados.

#### A. Entrada - Dados e Transações de Entrada

&emsp;A entrada de dados no sistema atual ocorre nas cinco etapas do processo de gestão de portfólio, com controles de segurança descentralizados e vulnerabilidades críticas em cada camada.

**Volume de Acessos:** O sistema suporta a entrada de dados e transações de 40 a 60 usuários ativos (Líderes de Projeto, Equipe, Gestores do Portfólio, PMO) em ciclo contínuo. As transações envolvem a criação e edição de cronogramas no SharePoint (1ª etapa), transferência manual de planejamento do Miro para documentos TAP (2ª etapa), atualização de reportes mensais (3ª etapa), armazenamento geral de documentos (4ª etapa) e acesso a relatórios consolidados (5ª etapa).

**Transações Críticas:** As transações de maior risco para segurança são a Transferência Manual do Miro para o SharePoint (2ª etapa) e o Armazenamento de Dados sem validação de aprovação (4ª etapa). A primeira apresenta vulnerabilidade de manipulação de dados sem rastreabilidade da correspondência entre fontes. A segunda permite inserção/alteração de documentos críticos (TAP aprovado, cronograma baseline) sem workflow de aprovação formal. Ambas comprometem a integridade e a governança do portfólio.

**Vulnerabilidade:** A principal vulnerabilidade reside na gestão manual de permissões no SharePoint com acesso amplo a todos os projetos do portfólio. Todas as etapas dependem de permissões concedidas no nível de biblioteca geral, não por projeto individual, violando sistematicamente o princípio do menor privilégio. Usuários autorizados no SharePoint podem acessar cronogramas, TAPs, reportes e documentos de todos os projetos, não apenas aqueles de sua responsabilidade. Não há mecanismo sistêmico para segregação de acesso por projeto/subfolder, resultando em exposição indevida de informações estratégicas e sensíveis.

#### B. Saída - Registros de Transações Corretas e Inadequadas

&emsp;A saída do sistema atual evidencia diferentes níveis de rastreabilidade conforme a etapa e o componente, mas com falhas críticas na detecção de acessos inadequados devido ao controle de permissões amplo.

- **Transações Corretas (Nominais):** Em condições de operação normal, as transações são concluídas com rastreabilidade básica:

1. Etapa (Cronogramas): Documentos criados/editados no SharePoint com versionamento automático e log de auditoria (usuário, data/hora, ação). Rastreabilidade de quando foi alterado, mas não de qual parte específica do cronograma foi modificada.

2. Etapa (Miro/TAP): Miro registra quem fez o que com granularidade total (usuário, ação específica como "adicionou card" ou "apagou texto", timestamp, conteúdo antes/depois). SharePoint registra criação/edição de TAPs com versionamento. **Porém, a transferência manual Miro → SharePoint não é rastreada sistematicamente**, não há validação de correspondência entre planejamento original e documento formal.

3. Etapa (Reporte Mensal): Atualizações registradas em log de auditoria do SharePoint (usuário, data/hora, documento modificado). Versionamento de documentos.

4. Etapa (Armazenamento): Todos os uploads/modificações registrados em log de auditoria com identificação de quem altera/insere os dados e quando (usuário autenticado via Microsoft 365, timestamp preciso). Versionamento completo (até 500 versões). Recuperação via lixeira (93+93 dias).

5. Etapa (Relatórios): Power BI registra acessos, visualizações e exportações (usuário, data/hora, relatório específico, formato exportado). Documentos consolidados no SharePoint com versionamento e log de auditoria.

**Transações Inadequadas (Falhas de Segurança):** Em momentos de tentativas de acesso indevido ou violações de políticas, o sistema apresenta falhas críticas de detecção:

- Acesso Não Autorizado Total: Tentativas de acesso por usuários sem permissão alguma no SharePoint são bloqueadas e registradas em log de auditoria (status: acesso negado).

- Acesso Inadequado por Permissão Ampla (Vulnerabilidade Crítica): Usuário autorizado no SharePoint acessa cronogramas, TAPs, reportes ou documentos de projetos para os quais não deveria ter acesso. O sistema registra como transação "correta" (usuário tem permissão técnica), mas do ponto de vista de governança é uma violação de segregação de acesso por projeto. Não é detectado automaticamente como transação inadequada.

- Manipulação Durante Transferência Manual: Alteração de dados do planejamento original (Miro) durante transcrição para TAP no SharePoint (2ª etapa). Não detectada automaticamente - requer auditoria manual comparando Miro vs. TAP.

- Inserção/Alteração Sem Aprovação: Modificação de documentos críticos (TAP aprovado, cronograma baseline) sem workflow de aprovação formal (4ª etapa). Registrado em log de auditoria, mas não bloqueado preventivamente - sistema atual não distingue documentos que requerem aprovação vs. documentos de trabalho.

- Exportação Descontrolada: Download de cronogramas, TAPs, relatórios para ambiente local. Registrado em log, mas sem controle posterior - documentos podem ser compartilhados externamente (e-mail, WhatsApp) sem rastreabilidade.

**Vulnerabilidade:** A vulnerabilidade crítica é a falta de detecção sistêmica de acessos inadequados quando o usuário possui permissão técnica ampla. Logs registram ações de usuários autorizados, mas não identificam violações lógicas de segregação por projeto. A ausência de validação de integridade em transferências manuais e a falta de workflow de aprovação para alterações críticas impedem controle adequado de governança. O sistema depende de auditoria manual posterior para identificar violações, forçando resposta reativa ao invés de preventiva.

#### C. Controle do RNF - Indicação de Controle

&emsp;O controle da Segurança no sistema atual é híbrido, com dependência crítica de controles sistêmicos da Microsoft 365 para autenticação e criptografia, mas totalmente manual e vulnerável para autorização granular e validação de processos de governança.

**Controle Sistêmico (Microsoft 365 - Camada Base):** A infraestrutura de segurança base é gerenciada integralmente pela Microsoft, incluindo autenticação (SSO via Microsoft Entra ID), criptografia em trânsito (TLS 1.2+) e em repouso (AES-256), logs de auditoria nativos (90 dias de retenção padrão), versionamento automático de documentos (até 500 versões), backup e redundância (snapshots a cada 12 horas, geo-redundância), e SLA de disponibilidade (99,9%). O Metrô não possui visibilidade ou controle sobre a infraestrutura física, chaves de criptografia ou políticas de throttling - apenas consome o serviço dentro dos limites pré-estabelecidos pela Microsoft.

**Controle Manual (Metrô - Camada de Autorização e Processos):** O Metrô possui controle sobre configurações de permissões e definição de processos organizacionais, mas com limitações críticas de implementação sistêmica:

#### 1ª Etapa (Elaboração de Cronograma) - Controle de Acesso ao SharePoint:

- Tipo: Manual via SharePoint Admin Center
- Níveis Implementados: Administrador (controle total), Colaborador (criar/editar/excluir), Visualizador (somente leitura)
- Processo: Gestor do Portfólio/PMO solicita acesso para usuário → Administrador do SharePoint concede permissão manualmente na biblioteca "Cronogramas"
- Limitação Crítica: Permissões concedidas no nível de biblioteca geral, não por projeto individual. Usuário com permissão de "Colaborador" acessa cronogramas de todos os projetos do portfólio. Não há segregação granular por projeto/subfolder implementada.
- Vulnerabilidade: Violação do princípio do menor privilégio. Gestão manual sujeita a erro humano (esquecimento de revogar acesso, concessão excessiva por comodidade). Usuários podem visualizar informações estratégicas de projetos concorrentes ou sensíveis (datas críticas, recursos alocados, dependências).

#### 2ª Etapa (Documentação Miro/TAP) - Duplo Controle:

- Controle no Miro: Sistêmico - acesso por projeto (apenas membros convidados do board), rastreabilidade total e automática de alterações, integração com SSO Microsoft 365.
- Controle no SharePoint (TAPs): Manual - mesma vulnerabilidade de acesso amplo descrita acima. Usuários autorizados no SharePoint têm acesso a todos os TAPs de todos os projetos.
- Processo de Transferência: Manual - Líder de Projeto copia/transcreve dados do Miro para documento TAP no Word/PowerPoint → salva no SharePoint. Sem validação sistêmica de integridade (checksum, hash, comparação automática).
- Vulnerabilidade Crítica: Possibilidade de manipulação durante transcrição (alteração de escopo, benefícios, premissas) sem detecção automática. Inconsistência entre planejamento original (Miro) e documento formal (TAP) identificável apenas por auditoria manual posterior. Comprometimento da governança de projetos.

#### 3ª Etapa (Reporte Mensal) - Controle de Atualização:

- Tipo: Manual via permissões do SharePoint + processo organizacional
- Processo: Líder de Projeto atualiza status no SharePoint (lista ou documento) → PMO revisa manualmente → consolida informações em relatório gerencial.
- Limitação: Não há workflow sistêmico de aprovação. Ausência de validação formal antes de consolidação. Mesma vulnerabilidade de acesso amplo - usuários podem visualizar/editar reportes de projetos não autorizados.
- Vulnerabilidade: Possibilidade de alteração não autorizada de status (maquiagem de indicadores, ocultação de problemas críticos) sem bloqueio preventivo.

#### 4ª Etapa (Armazenamento de Dados) - Controle de Inserção/Alteração:

- Tipo: Manual via permissões do SharePoint + definição organizacional de processos (não sistêmico)
- Níveis de Permissão Implementados: Colaborador pode inserir/alterar qualquer documento. Não há distinção sistêmica entre documentos de trabalho vs. documentos críticos que requerem aprovação.
- Estrutura de Armazenamento: Arquivos organizados por pastas/projetos no SharePoint (estrutura específica não documentada no contexto fornecido, necessita mapeamento na fase atual do projeto).
- Processo Atual (Informal): Documentos críticos (TAP aprovado, cronograma baseline) deveriam seguir processo de aprovação formal (comitê, assinatura), mas não há workflow sistêmico no SharePoint bloqueando alterações posteriores ou requerendo aprovação para modificações.
- Vulnerabilidade Crítica: Usuário com permissão de "Colaborador" pode alterar documentos já aprovados (baseline de cronograma, orçamento, escopo do TAP) sem validação/aprovação de mudança. Sistema registra alteração em log, mas não bloqueia preventivamente. Perda de integridade de documentação de governança. Depende de controles manuais e disciplina organizacional (não sistêmicos).

#### 5ª Etapa (Geração de Relatórios) - Controle de Acesso e Exportação:

- Power BI: Controle sistêmico via permissões de workspace (Administrador, Membro, Colaborador, Visualizador). Row-Level Security (RLS) configurável (status de implementação não especificado assumido como não implementado por projeto). Logs de exportação automáticos.
- Limitação Power BI: Permissão de workspace é "tudo ou nada" - usuário com acesso visualiza relatórios de todo o portfólio consolidado (todos os projetos, orçamentos, desvios). Não há controle granular por projeto dentro do workspace. Exportações (.csv, .xlsx) não são bloqueadas - apenas registradas em log.
- Documentos Consolidados (Word/PowerPoint/Excel): Mesma vulnerabilidade de acesso amplo do SharePoint. Relatórios mensais/semestrais/anuais acessíveis por todos os usuários com permissão na biblioteca.
- Vulnerabilidade: Exposição de indicadores consolidados do portfólio completo (orçamento total, projetos críticos, desvios acumulados) para usuários que deveriam ter acesso apenas a projetos específicos. Documentos exportados para ambiente local perdem criptografia automática e podem ser compartilhados externamente (e-mail, pen drive) sem controle ou rastreabilidade.

**Monitoramento e Observabilidade:**

- Sistêmico: Logs nativos do SharePoint, Miro e Power BI registrando acessos, modificações e exportações. Alertas automáticos de segurança via Microsoft Defender (detecção de malware, login suspeito) se licenciado.
- Manual: Análise periódica de logs de auditoria (frequência não especificada - assumido como reativa, após incidente). Revisão de permissões no SharePoint (não há auditoria sistemática trimestral implementada).
- Vulnerabilidade: Ausência de SIEM (Security Information and Event Management) corporativo ou dashboard consolidado de segurança. Logs dispersos em múltiplas plataformas (SharePoint, Miro, Power BI) sem correlação automatizada. Análise predominantemente reativa (após falha ou incidente). Não há ferramentas de monitoramento que permitam à equipe do Metrô prever ou reagir proativamente a violações de segregação de acesso. O diagnóstico de acessos inadequados (usuário acessando projetos não autorizados) depende de auditoria manual posterior.

**Vulnerabilidade Final:** A vulnerabilidade sistêmica crítica é a dependência de controle manual de permissões com acesso amplo no nível de biblioteca/workspace, sem segregação granular por projeto, combinada com a ausência de validação de integridade em transferências manuais (Miro → SharePoint) e a falta de workflow sistêmico de aprovação para alterações em documentos críticos. O Metrô não possui controle sobre infraestrutura, mas também não implementa controles granulares nas camadas que estão sob sua governança (permissões, processos de aprovação). O sistema depende de disciplina organizacional e processos manuais não sistêmicos para garantir segregação de acesso e integridade de documentação, o que é inaceitável para um sistema de missão crítica de governança de portfólio.

---

### 5.2.3 RNF-03 — Rastreabilidade

&emsp; A Rastreabilidade é um requisito não funcional crítico para o sistema de Portfólio do Metrô, pois a capacidade de auditar a origem, as modificações e o ciclo de vida dos dados é fundamental para a governança, conformidade e tomada de decisão. Na arquitetura atual, o fluxo de informações depende de processos manuais e ferramentas descentralizadas (Miro, Excel, SharePoint), criando pontos cegos que comprometem a capacidade de rastrear a linhagem dos dados de ponta a ponta, caracterizando uma vulnerabilidade significativa.

#### A. Entrada

&emsp; A entrada de dados no sistema atual ocorre de forma descentralizada e não auditada, o que compromete fundamentalmente a rastreabilidade desde sua origem, tornando impossível para o sistema garantir a proveniência das informações que armazena.

- **Transações de Entrada:** O fluxo de entrada se inicia em múltiplos componentes antes de chegar ao repositório central (SharePoint). As transações incluem a coleta de novas iniciativas via **Forms**, a priorização em planilhas **Excel** locais, e a criação de mapas de benefícios no **Miro**. Essas transações, embora normais do ponto de vista operacional, ocorrem fora do perímetro de auditoria do sistema principal, impedindo o registro de quem as realizou e quando.

- **Transação Crítica para Auditoria:** A transação de maior impacto na rastreabilidade é a **transferência manual de dados do Miro e Excel para o SharePoint**. Este processo representa a entrada oficial dos dados no sistema de registro, mas opera como uma "caixa-preta". A ação de inserir ou atualizar os dados no SharePoint não é registrada de forma a conectá-la à sua fonte, tornando impossível verificar se os dados foram transcritos fielmente ou alterados no processo.

- **Vulnerabilidade:** A principal vulnerabilidade reside na **ausência de um ponto de entrada de dados unificado e transacional**. Sem uma API ou um conector que gerencie a ingestão de dados de forma atômica e auditável, o sistema não tem como validar a integridade ou a origem das informações que recebe. Isso significa que uma transação de entrada inadequada (seja por erro humano ou intenção maliciosa) não é diferenciada de uma transação normal, resultando em uma corrupção silenciosa dos dados desde a sua concepção.

#### B. Saída

&emsp; A saída do sistema atual evidencia a falta de rastreabilidade não por erros que geram logs, mas pela **geração de dados cuja origem e integridade não podem ser verificadas**, mesmo que as operações individuais sejam concluídas com sucesso.

- **Transações Corretas (Nominais):** Uma transação é considerada "correta" do ponto de vista técnico quando os dados são transferidos com sucesso e armazenados no SharePoint, e os relatórios são gerados no Power BI. O **resultado** é um sistema funcional, com listas e documentos atualizados, mas que esconde uma falha de rastreabilidade.

- **Transações Inadequadas (Falhas de Rastreabilidade):** A inadequação não está em uma falha da transação que gera um erro, mas no **resultado** que ela produz. Uma transação que depende da transferência manual de dados do Miro/Excel para o SharePoint, mesmo que concluída sem erros, é inerentemente inadequada. O resultado é:

  - **Dados Órfãos:** O sistema armazena dados no SharePoint que são "órfãos", sem qualquer vínculo sistêmico com sua fonte original no Miro ou Excel. O resultado é a impossibilidade de provar de onde veio a informação.
  - **Integridade Comprometida:** O resultado final é um conjunto de dados no SharePoint cuja integridade é questionável. Como a transferência é manual, alterações (intencionais ou acidentais) podem ocorrer, e o sistema armazena o dado corrompido como se fosse válido.
  - **Auditoria Impossível:** O resultado é a incapacidade de realizar uma auditoria de ponta a ponta. Se for necessário verificar por que um valor específico está no relatório final, o sistema não oferece um caminho de volta à origem.

- **Vulnerabilidade:** A vulnerabilidade aqui é que o sistema **não possui um mecanismo para diferenciar dados confiáveis de dados não confiáveis**. Ele trata todos os dados armazenados no SharePoint como válidos, mesmo que sua origem seja desconhecida. A falta de um **ID de Correlação** e de um **processo de ingestão auditável** significa que o sistema armazena e processa dados potencialmente inválidos sem qualquer controle.

#### C. Controle do RNF

&emsp; O controle sobre a Rastreabilidade no sistema atual é inexistente do ponto de vista de ponta a ponta, sendo uma solução puramente operacional e reativa, não arquitetural.

- **Controle Sistêmico:** Não há controle sistêmico por parte do Metrô para a rastreabilidade do fluxo completo. O controle se resume às funcionalidades de auditoria de cada plataforma (SharePoint, Power Platform), que não são integradas. O fato de o Power Automate realizar a "Aprovação de TAP" não constitui um controle de rastreabilidade, pois ele opera sobre dados que já foram inseridos manualmente, confiando implicitamente em sua integridade, sem validá-la ou rastreá-la.

- **Controle Manual:** O único "controle" é a **investigação forense reativa**, de responsabilidade do PMO ou da equipe de TI. Este processo consiste em entrevistar os envolvidos e cruzar manualmente os logs isolados de cada ferramenta para tentar reconstruir a sequência de eventos após a descoberta de uma inconsistência. É uma solução operacional frágil, dependente da memória e boa-fé das pessoas.

- **Vulnerabilidade:** A vulnerabilidade final é a **dependência de um processo manual não auditado para uma etapa crítica do fluxo de dados**. A integridade de todo o sistema de portfólio depende de uma ação humana que não é registrada, validada ou controlada por nenhum sistema, o que é inaceitável para um processo de missão crítica e representa um risco de governança severo.

---

## 5.3 Táticas Arquiteturais e Componentes Adotados

&emsp;Esta seção descreve as táticas arquiteturais e componentes tecnológicos que suportam a execução e o controle dos Requisitos Não Funcionais (RNFs) no sistema atual de gestão de Portfólio do Metrô. Para cada RNF identificado na seção 5.2, são detalhados os mecanismos de monitoramento, as estratégias preventivas e reativas de atendimento, e os procedimentos de recuperação diante de falhas ou quebras de níveis de serviço.

&emsp;O sistema atual é composto por ferramentas de produtividade e colaboração da Microsoft 365 (SharePoint, Microsoft Teams, Power BI, Power Automate) e plataformas de terceiros (Miro), operando de forma integrada através de autenticação única (SSO) e processos manuais de transferência de dados. Esta arquitetura híbrida - combinando serviços gerenciados em nuvem (SaaS) com processos organizacionais customizados - apresenta características específicas de controle e monitoramento que variam significativamente entre os diferentes RNFs.

**Estrutura da Documentação:**

Para cada RNF, são apresentadas três dimensões críticas de análise:

**A. Como monitorar o RNF:** Identificação dos componentes de monitoramento (sistêmicos e manuais), métricas coletadas, indicadores de nível de serviço (SLIs/SLOs propostos), e limitações/vulnerabilidades de observabilidade. Esta seção responde à questão: _"Como sabemos se o RNF está sendo atendido?"_

**B. Como resolver o RNF (Preventivo e Reativo):** Descrição das táticas arquiteturais preventivas (controles que impedem violações antes que ocorram) e reativas (mecanismos de detecção, contenção e correção após violações). Esta seção responde à questão: _"O que o sistema faz para garantir o atendimento do RNF?"_

**C. Como recuperar/subsidiar o tratamento de impactos:** Procedimentos de recuperação diante de falhas que causem quebras de níveis de serviço, incluindo componentes utilizados, tempos de recuperação (RTO/RPO), justificativas para gestão e documentação de suporte para auditoria. Esta seção responde à questão: _"Como respondemos quando o RNF não é atendido?"_

**Contexto Arquitetural Comum:**

Todos os RNFs compartilham as seguintes características do sistema atual:

1. **Dependência de Infraestrutura Terceirizada:** A infraestrutura base (autenticação, criptografia, armazenamento, backup, redundância) é gerenciada integralmente pela Microsoft (Microsoft 365) e Miro. O Metrô não possui controle direto sobre hardware, políticas de throttling, capacidade de processamento ou disponibilidade - apenas consome os serviços dentro dos limites e SLAs pré-estabelecidos pelos fornecedores.

2. **Controle Híbrido (Sistêmico + Manual):** Controles de baixo nível (autenticação, criptografia, logs de auditoria, versionamento) são sistêmicos e automatizados pelas plataformas. Controles de alto nível (autorização granular, validação de processos de governança, auditoria de conformidade) são predominantemente manuais, dependendo de ações de administradores e processos organizacionais não sistêmicos.

3. **Observabilidade Descentralizada:** Logs e métricas são gerados nativamente por cada ferramenta (SharePoint, Miro, Power BI) em formatos e localizações distintas, sem consolidação ou correlação automatizada. Não há SIEM (Security Information and Event Management) corporativo ou dashboard unificado de monitoramento de RNFs.

4. **Ausência de Controle sobre Limites e Capacidade:** O Metrô não possui visibilidade ou controle sobre recursos de hardware, capacidade de processamento alocada, políticas de rate limiting ou throttling. As plataformas SaaS operam como "caixas pretas" - o Metrô observa comportamentos externos (tempos de resposta, erros), mas não pode ajustar parâmetros internos de performance ou escalabilidade.

5. **Monitoramento Predominantemente Reativo:** A maioria dos RNFs é monitorada através de análise manual reativa de logs após incidentes ou em auditorias esporádicas. Alertas automáticos existem apenas para ameaças externas óbvias (malware, login suspeito - se Defender licenciado) e indisponibilidades reportadas pela Microsoft. Violações de políticas de governança (acessos inadequados, alterações não aprovadas, problemas de escalabilidade) dependem de detecção manual.

Estas características arquiteturais fundamentais impactam diretamente a capacidade de atendimento, monitoramento e recuperação de cada RNF, conforme detalhado nas subseções a seguir. As vulnerabilidades identificadas refletem não apenas limitações técnicas das ferramentas, mas principalmente a **ausência de camadas customizadas de controle, monitoramento e automação** que seriam necessárias para um sistema de missão crítica de governança de portfólio.

### 5.3.1 RNF-01 — Escalabilidade

&emsp;A análise do RNF de Escalabilidade no sistema atual (AS-IS) deve focar na descrição das **táticas arquiteturais e componentes** que, mesmo de forma limitada, ajudam na execução e controle deste requisito. Conforme a seção 5.2.1, o sistema atual é baseado em um ecossistema de ferramentas Microsoft (SharePoint, Power Automate, Power BI) e Miro, o que implica que a maioria das táticas de escalabilidade são **inerentes e gerenciadas pelo provedor (Microsoft)**, e não pela equipe de TI do Metrô.

#### A. Como monitorar o RNF

&emsp;O monitoramento do RNF de Escalabilidade é **predominantemente sistêmico, mas com visibilidade e controle limitados** por parte do Metrô.

| Aspecto                            | Descrição no Sistema Atual (AS-IS)                                                                                                                                                                                                  | Limitações/Vulnerabilidades                                                                                                                                                                                             |
| :--------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Componentes de Monitoramento**   | **SharePoint Online e Power Automate Logs:** O monitoramento é realizado pelas ferramentas nativas do Microsoft 365. O SharePoint registra o uso de recursos e o Power Automate fornece logs de execução de fluxos (sucesso/falha). | A equipe de TI do Metrô não tem acesso a métricas de infraestrutura (CPU, memória, latência de rede) e o monitoramento é limitado a logs de aplicação e _throttling_ (limitação de requisições) imposto pela Microsoft. |
| **Métricas/SLIs/SLOs**             | **SLI Implícito:** Taxa de sucesso na execução de fluxos do Power Automate e tempo de carregamento de páginas/listas no SharePoint.                                                                                                 | Não existem **SLOs (Service Level Objectives)** formalmente definidos e controlados pelo Metrô. O **SLI** de performance é monitorado de forma reativa, através de reclamações de usuários sobre lentidão.              |
| **Monitoramento Manual/Sistêmico** | **Sistêmico:** Logs e alertas de _throttling_ do SharePoint. **Manual:** Acompanhamento visual dos _dashboards_ de uso do Power BI e verificação manual dos logs de falha no Power Automate.                                        | A falta de uma ferramenta de **Observabilidade** centralizada impede a correlação de eventos e a detecção proativa de gargalos. O monitoramento manual é ineficiente e propenso a falhas.                               |

#### B. Como resolver o RNF (Preventivo e Reativo)

&emsp;As táticas de resolução para a Escalabilidade no sistema atual são limitadas, dependendo majoritariamente de políticas de uso e das limitações impostas pelo fornecedor.

| Tática         | Componente/Mecanismo                                                                                                                              | Natureza             | Vulnerabilidade                                                                                                                                              |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Preventiva** | **Políticas de Uso:** Orientação manual aos usuários para evitar picos de uso e dividir grandes tarefas em partes menores.                        | Manual/Processual    | Dependência do **comportamento do usuário**; não é uma tática arquitetural. Não há _Rate Limiting_ ou _Load Balancing_ sob controle do Metrô.                |
| **Preventiva** | **Limites do SharePoint Online:** O provedor impõe limites de requisições (_throttling_) por usuário e por aplicação.                             | Sistêmica (Provedor) | Os limites são **rígidos e não configuráveis**, levando a interrupções de serviço quando atingidos. A prevenção é feita pelo provedor, não pela arquitetura. |
| **Reativa**    | **Alertas de Falha no Power Automate:** Notificações automáticas quando um fluxo falha.                                                           | Sistêmica (Provedor) | O alerta é apenas um **sintoma** da quebra de escalabilidade (_throttling_). A correção exige intervenção manual (reexecução do fluxo).                      |
| **Reativa**    | **Contenção Manual:** A equipe de TI pode solicitar a reexecução manual de fluxos falhos ou aguardar a liberação do _throttling_ pelo SharePoint. | Manual/Processual    | Alto **MTTR** (Mean Time to Recovery) e risco de inconsistência de dados devido à falta de mecanismos de _Retry_ automático.                                 |

#### C. Como recuperar/subsidiar o tratamento de impactos

&emsp;A recuperação de impactos no sistema atual é **extremamente frágil e dependente de intervenção humana**, sem mecanismos arquiteturais robustos para _Failover_ ou reprocessamento automático.

| Componente/Procedimento         | Descrição                                                                                                                                                                                                | Justificativa/Impacto                                                                                                                                                                                              |
| :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Registro de Falhas**          | **Logs do Power Automate:** Registra o _status_ de falha e a causa (ex: erro de _throttling_).                                                                                                           | **Subsidia a Justificativa:** O log é a única evidência técnica para justificar a quebra do nível de serviço. O detalhamento é superficial, indicando a falha, mas não o impacto total no negócio.                 |
| **Procedimento de Recuperação** | **Reexecução Manual:** A equipe de suporte ou o usuário deve reexecutar manualmente o fluxo falho no Power Automate.                                                                                     | **Alto Custo Operacional:** O procedimento é lento e não garante a ordem de processamento, podendo levar a **inconsistências de dados** (se os dados de origem tiverem sido alterados após a falha).               |
| **Componente de Recuperação**   | **Nenhum:** O sistema atual **não possui** componentes de recuperação arquiteturalmente definidos, como _Message Queues_ (filas de mensagens) ou _Dead Letter Queues_ (DLQ) para reprocessamento seguro. | **Risco Crítico:** A falta de mecanismos de _Retry_ e DLQ significa que transações perdidas exigem **reentrada manual de dados**, o que é a maior vulnerabilidade para a integridade e disponibilidade do sistema. |

&emsp;A ausência de táticas arquiteturais de recuperação e a dependência de mecanismos de _throttling_ de terceiros demonstram que o RNF de Escalabilidade é **mal atendido** no sistema AS-IS, justificando a necessidade de uma nova arquitetura com controle de tráfego, filas de mensagens e _failover_ explícitos.

---

### 5.3.2 RNF-02 — <Segurança>

#### A. Como monitorar o RNF

O monitoramento da Segurança no sistema atual é realizado através de componentes nativos das ferramentas Microsoft 365, Miro e Power BI, porém de forma descentralizada e com análise predominantemente manual, caracterizando uma vulnerabilidade de observabilidade crítica.

**Componentes de Monitoramento por Etapa:**

##### 1ª Etapa (Elaboração de Cronograma) - SharePoint Audit Logs:

- **Tipo:** Sistêmico com análise manual
- **Funcionalidades Monitoradas:** Acessos a documentos de cronograma (visualização, download, edição), modificações de arquivos (quem, quando, tipo de ação), alterações de permissões (concessão/revogação de acesso), compartilhamentos externos (se habilitados).
- **Métricas Coletadas:** Número de acessos por usuário/documento/período. Número de modificações em cronogramas por usuário. Alterações de permissões realizadas por administradores.
- **Retenção:** 90 dias (padrão SharePoint Online), extensível manualmente a 1 ano via Microsoft Purview.
- **Limitação Crítica:** Logs registram acessos de usuários autorizados tecnicamente, mas **não identificam acessos inadequados** (usuário acessando cronograma de projeto não autorizado, pois tem permissão ampla na biblioteca). Análise requer exportação manual de logs e cruzamento com matriz de responsabilidades (planilha externa) para identificar violações de segregação por projeto.

##### 2ª Etapa (Documentação Miro/TAP):

**Miro - Activity Log Nativo:**

- **Tipo:** Sistêmico com visualização direta no board
- **Funcionalidades Monitoradas:** Todas as alterações com granularidade total - quem adicionou/apagou/moveu elementos, qual conteúdo foi modificado (antes/depois), timestamp preciso.
- **Métricas Coletadas:** Alterações por usuário/período. Padrões de edição (horários, volume, tipos de ação).
- **Retenção:** Indefinida (enquanto o board existir no Miro).
- **Limitação:** Histórico interno ao Miro, não integrado aos logs corporativos do Metrô. **Não há monitoramento da transferência manual Miro → SharePoint** - ausência de validação sistêmica de correspondência entre planejamento (Miro) e documento formal (TAP no SharePoint).

**SharePoint (TAPs) - Audit Logs:**

- **Tipo:** Sistêmico com análise manual
- **Funcionalidades Monitoradas:** Criação/edição de documentos TAP, versionamento, acessos.
- **Limitação:** Mesma vulnerabilidade da 1ª etapa - não identifica acessos inadequados por permissão ampla. **Não monitora integridade entre Miro e TAP**.

##### 3ª Etapa (Reporte Mensal) - SharePoint Audit Logs:

- **Tipo:** Sistêmico com análise manual
- **Funcionalidades Monitoradas:** Atualizações em listas de status, modificações em documentos de reporte mensal, acessos a reportes.
- **Limitação:** Não há monitoramento de validação/aprovação de reportes antes de consolidação (processo informal, não sistêmico). Mesma vulnerabilidade de acesso amplo.

##### 4ª Etapa (Armazenamento de Dados) - SharePoint Audit Logs:

- **Tipo:** Sistêmico com análise manual
- **Funcionalidades Monitoradas:** Upload de novos documentos (quem inseriu, quando, qual arquivo), modificações em documentos existentes (quem alterou, quando), exclusões (autor, timestamp, se via lixeira ou permanente), alterações de permissões em pastas/arquivos específicos.
- **Métricas Coletadas:** Volume de uploads por usuário/período. Modificações em documentos críticos (se identificados por tag/pasta específica). Exclusões (acidentais ou maliciosas).
- **Limitação Crítica:** Sistema **não distingue automaticamente** documentos críticos (TAP aprovado, cronograma baseline) vs. documentos de trabalho. Não há monitoramento de workflow de aprovação (pois não existe sistematicamente). **Não identifica alterações em documentos já aprovados sem re-aprovação**. Análise de conformidade depende de auditoria manual cruzando logs com lista de documentos críticos mantida externamente.

##### 5ª Etapa (Geração de Relatórios):

**Power BI - Activity Log:**

- **Tipo:** Sistêmico com exportação para análise
- **Funcionalidades Monitoradas:** Acessos a relatórios/dashboards (usuário, timestamp, relatório específico), visualizações de páginas, exportações de dados (formato .csv/.xlsx/.pdf, volume de linhas exportadas), compartilhamentos de relatórios, tentativas de acesso negadas a workspaces restritos.
- **Métricas Coletadas:** Acessos por usuário/relatório/período. Taxa de exportações por usuário. Compartilhamentos externos (se habilitados).
- **Retenção:** 90 dias (Power BI Service).
- **Limitação:** Logs requerem exportação via API REST ou Power BI Admin Portal para análise detalhada. **Não há alertas automáticos** para exportações em massa ou acessos anômalos. Permissão de workspace é "tudo ou nada" - não monitora se usuário deveria ter acesso apenas a projetos específicos (pois controle granular não existe).

**SharePoint (Documentos Consolidados) - Audit Logs:**

- **Tipo:** Sistêmico com análise manual
- **Funcionalidades Monitoradas:** Acessos a relatórios mensais/semestrais/anuais salvos no SharePoint, downloads.
- **Limitação:** Mesma vulnerabilidade de acesso amplo. **Não monitora o que acontece com documentos após download local** (compartilhamento externo via e-mail, pen drive não é rastreável).

##### Componentes Transversais de Monitoramento de Segurança:

**Microsoft 365 Security & Compliance Center (se licenciado):**

- **Tipo:** Sistêmico com alertas configuráveis
- **Funcionalidades:** Detecção de login suspeito (localização atípica, múltiplas falhas), atividades anômalas de usuários (acesso em horários incomuns, volume atípico de downloads), violações de políticas DLP (se configuradas), detecção de malware.
- **Limitação:** Requer licenciamento específico (Microsoft 365 E3/E5). Alertas requerem configuração manual. **Não monitora violações de segregação lógica por projeto** (acesso amplo permitido tecnicamente).

**Microsoft Defender for Cloud Apps (se licenciado):**

- **Tipo:** Sistêmico com UEBA (User and Entity Behavior Analytics)
- **Funcionalidades:** Detecção de comportamento anômalo via análise estatística (desvios de padrões normais), sessões de risco (IPs suspeitos, dispositivos não gerenciados), downloads em massa.
- **Limitação:** Requer licenciamento específico (Microsoft 365 E5). Foco em ameaças externas e comportamentos obviamente anômalos. **Não detecta acessos inadequados quando usuário tem permissão técnica ampla**.

##### Indicadores de Nível de Serviço de Segurança (SLIs/SLOs):

| **SLI**                                           | **Descrição**                                                                | **SLO Proposto**       | **Status Atual**                   | **Método de Medição**                                              |
| ------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------- | ---------------------------------- | ------------------------------------------------------------------ |
| Taxa de disponibilidade do sistema                | % de tempo que sistema está acessível (inclui indisponibilidade por ataques) | ≥99,9% (Microsoft SLA) | Atingido (sistêmico)               | Microsoft Service Health Dashboard                                 |
| Tentativas de acesso totalmente não autorizado    | Número de acessos negados/total de acessos                                   | <0,5%                  | Não medido sistematicamente        | SharePoint Audit Logs (requer dashboard customizado)               |
| Tempo de detecção de ameaças conhecidas           | Tempo entre ocorrência e detecção de malware/ransomware                      | <15 minutos            | Atingido (se Defender licenciado)  | Microsoft Defender for Office 365                                  |
| Conformidade com segregação de acesso por projeto | % de usuários com acessos apenas aos projetos autorizados após auditoria     | 100%                   | Não auditado sistematicamente      | Auditoria manual (não implementada regularmente)                   |
| Identificação de acessos inadequados              | % de acessos a projetos não autorizados detectados automaticamente           | >95%                   | 0% (não detectado automaticamente) | Não disponível (requer correlação de logs com matriz de projetos)  |
| Integridade de transferências manuais             | % de TAPs validados como íntegros em relação ao planejamento Miro            | 100%                   | Não medido                         | Não disponível (requer auditoria manual Miro vs. TAP)              |
| Documentos críticos alterados sem aprovação       | Número de alterações em TAPs/baselines sem workflow de aprovação             | 0                      | Não medido                         | Não disponível (requer marcação de documentos críticos + workflow) |

##### Tipo de Monitoramento:

- **Sistêmico (Registro Automático):** Logs de auditoria do SharePoint, histórico do Miro, activity log do Power BI, alertas do Defender (se licenciado). Representa coleta de dados brutos.
- **Manual (Análise e Interpretação):** Exportação de logs, cruzamento com matriz de responsabilidades por projeto, identificação de violações de segregação, auditoria de integridade Miro vs. TAP, validação de conformidade de alterações em documentos críticos. Representa 100% da análise de conformidade com políticas de governança.

**Vulnerabilidade de Observabilidade:** A vulnerabilidade crítica é a **ausência de monitoramento sistêmico automatizado para as vulnerabilidades mais relevantes de governança**: acessos inadequados por permissão ampla, integridade de transferências manuais, e alterações em documentos críticos sem aprovação. O sistema monitora apenas ameaças externas óbvias (malware, login suspeito) e registra ações brutas (acessos, modificações), mas **não detecta violações de políticas de segregação e governança** que dependem de contexto (qual projeto o usuário deveria acessar, quais documentos requerem aprovação). Não há ferramentas de monitoramento que permitam à equipe do Metrô prever ou reagir proativamente a estas violações. O diagnóstico depende de auditoria manual reativa (após incidente ou em revisões esporádicas), o que é inaceitável para um sistema de missão crítica.

---

#### B. Como resolver o RNF (Preventivo e Reativo)

O atendimento ao RNF de Segurança no sistema atual combina controles preventivos sistêmicos da plataforma Microsoft 365 (camada base de autenticação e criptografia) com controles manuais vulneráveis (camada de autorização), e táticas reativas limitadas pela ausência de detecção automatizada de violações de governança.

##### Táticas Preventivas:

###### 1ª Etapa (Elaboração de Cronograma) - Controle de Acesso:

**Componentes:**

- **Microsoft Entra ID (Azure AD):** Autenticação obrigatória via SSO. Suporte a MFA (status de implementação não especificado - assumido como disponível mas não obrigatório universalmente).
- **SharePoint Online:** Sistema de permissões por biblioteca/pasta com níveis predefinidos (Administrador, Colaborador, Visualizador).

**Táticas Implementadas (Preventivas):**

- **Autenticação Forte:** SSO obrigatório para acesso ao SharePoint. Credenciais corporativas gerenciadas centralmente. Bloqueio automático após múltiplas tentativas de login falhas (configurável via Entra ID).
- **Controle de Acesso Baseado em Função (RBAC):** Permissões concedidas por nível (Administrador = controle total, Colaborador = edição, Visualizador = leitura). Usuário sem permissão **alguma** é bloqueado automaticamente.
- **Versionamento Automático:** SharePoint preserva até 500 versões de cada documento. Permite reversão em caso de alteração indevida.
- **Lixeira de Recuperação:** Documentos excluídos mantidos em lixeira de 1º estágio (93 dias) e 2º estágio (mais 93 dias), permitindo recuperação.

**Limitações/Vulnerabilidades Preventivas:**

- **Ausência de Granularidade:** Permissões concedidas no nível de biblioteca, não por projeto. **Não previne** acesso inadequado (usuário autorizado acessando cronograma de projeto não autorizado).
- **Gestão Manual Propensa a Erros:** Concessão/revogação de permissões requer ação manual do administrador. Risco de permissões esquecidas após mudança de função/projeto.
- **Sem Validação de Contexto:** Sistema bloqueia acesso totalmente não autorizado, mas **não valida** se usuário autorizado deveria acessar aquele documento específico (contexto de projeto).

###### 2ª Etapa (Documentação Miro/TAP) - Rastreabilidade e Controle de Integridade:

**Componentes:**

- **Miro:** Sistema de controle de acesso por board + histórico imutável de alterações.
- **SharePoint:** Versionamento de documentos TAP.

**Táticas Implementadas (Preventivas):**

- **Controle de Acesso por Board (Miro):** Acesso restrito apenas a membros convidados do board específico. Previne acesso não autorizado ao planejamento inicial.
- **Rastreabilidade Total (Miro):** Registro automático e imutável de todas as alterações (quem fez o que, quando, conteúdo antes/depois). Permite auditoria posterior.
- **Integração SSO (Miro):** Autenticação via Microsoft 365, garantindo identidade validada.
- **Versionamento (SharePoint):** TAPs versionados automaticamente, permitindo comparação entre versões.

**Limitações/Vulnerabilidades Preventivas:**

- **Transferência Manual Sem Validação:** Processo de cópia Miro → SharePoint é manual. **Não há validação sistêmica de integridade** (checksum, hash, comparação automatizada). Não previne manipulação durante transcrição.
- **Acesso Amplo ao TAP (SharePoint):** Mesma vulnerabilidade da 1ª etapa - usuários autorizados no SharePoint podem acessar TAPs de todos os projetos.
- **Rastreabilidade Não Correlacionada:** Histórico do Miro e versionamento do SharePoint são sistemas separados. \*\*

###### 3ª Etapa (Reporte Mensal) - Validação de Status:

**Componentes:**

- **SharePoint:** Versionamento de documentos de reporte.

**Táticas Implementadas (Preventivas):**

- **Versionamento:** Permite rastreamento de alterações em reportes ao longo do tempo.
- **Revisão Manual (PMO):** Processo organizacional de revisão antes de consolidação (não sistêmico).

**Limitações/Vulnerabilidades Preventivas:**

- **Sem Workflow de Aprovação Sistêmico:** Não há validação formal automatizada de reportes antes de consolidação. **Não previne** alteração de status sem aprovação adequada.
- **Acesso Amplo:** Mesma vulnerabilidade - usuários podem visualizar/editar reportes de projetos não autorizados.

###### 4ª Etapa (Armazenamento de Dados) - Controle de Alterações Críticas:

**Componentes:**

- **SharePoint:** Versionamento, lixeira, audit logs.

**Táticas Implementadas (Preventivas):**

- **Versionamento Completo:** Até 500 versões preservadas. Permite reversão de alterações indevidas.
- **Lixeira de Recuperação:** Proteção contra exclusões acidentais (até 186 dias de recuperação total).
- **Criptografia em Repouso:** AES-256 para todos os documentos armazenados. Previne acesso direto a arquivos em infraestrutura.

**Limitações/Vulnerabilidades Preventivas:**

- **Sem Distinção de Documentos Críticos:** Sistema não identifica automaticamente quais documentos requerem workflow de aprovação para alteração (TAP aprovado, cronograma baseline, atas de comitê). **Não previne** alteração não autorizada de documentos já aprovados.
- **Sem Workflow de Aprovação:** Usuário com permissão de "Colaborador" pode alterar qualquer documento sem aprovação formal. Sistema registra alteração (log), mas **não bloqueia preventivamente**.
- **Acesso Amplo:** Mesma vulnerabilidade - usuários podem inserir/alterar documentos de projetos não autorizados.

###### 5ª Etapa (Geração de Relatórios) - Controle de Exportação:

**Componentes:**

- **Power BI:** Permissões de workspace, Row-Level Security (RLS - se configurado), activity logs.
- **SharePoint:** Controle de acesso a documentos consolidados.

**Táticas Implementadas (Preventivas):**

- **Permissões de Workspace (Power BI):** Acesso restrito por função (Admin, Member, Contributor, Viewer). Usuário sem permissão ao workspace é bloqueado.
- **Row-Level Security (RLS - se configurado):** Filtragem de dados por perfil de usuário. Permite segregação de visualização por projeto dentro do mesmo relatório (status de implementação não especificado - assumido como não implementado).
- **Audit Logs (Power BI):** Registro de exportações para detecção posterior.
- **Versionamento (SharePoint - documentos consolidados):** Proteção de relatórios formais salvos no SharePoint.

**Limitações/Vulnerabilidades Preventivas:**

- **Permissão de Workspace "Tudo ou Nada":** Usuário com acesso ao workspace visualiza relatórios de **todo o portfólio**. Se RLS não implementado, **não previne** visualização de projetos não autorizados.
- **Exportações Não Bloqueadas:** Sistema registra exportações, mas **não bloqueia** (.csv, .xlsx, .pdf). Não previne vazamento de dados via exportação.
- **Perda de Controle Pós-Download:** Documentos exportados para ambiente local (relatórios Word/PowerPoint, exportações Power BI) perdem criptografia automática. **Não previne** compartilhamento externo via e-mail, WhatsApp, pen drive.

###### Táticas Preventivas Transversais (Microsoft 365):

**Criptografia:**

- **Em Trânsito:** TLS 1.2+ obrigatório para todas as conexões (SharePoint, Miro via navegador, Power BI). Previne interceptação de dados.
- **Em Repouso:** AES-256 no SharePoint/OneDrive. Previne acesso direto a arquivos na infraestrutura Microsoft.

**Backup e Redundância:**

- **Snapshots Automáticos (SharePoint):** A cada 12 horas. Previne perda total de dados.
- **Geo-Redundância:** Dados replicados em múltiplos datacenters. Previne indisponibilidade por falha de datacenter único.

**Detecção de Malware (se Defender licenciado):**

- **Scan em Tempo Real:** Arquivos verificados no upload. Previne introdução de malware no repositório.

**Limitação Geral das Táticas Preventivas:** Os controles preventivos sistêmicos (autenticação, criptografia, versionamento, backup) são eficazes para ameaças externas e erros técnicos, mas **não previnem as vulnerabilidades críticas de governança**: acesso inadequado por permissão ampla, manipulação em transferências manuais, alterações em documentos críticos sem aprovação. O sistema depende de disciplina organizacional e processos manuais (não sistêmicos) para prevenção destas violações, o que é insuficiente.

##### Táticas Reativas:

###### Detecção de Violações:

**Componentes:**

- **SharePoint Audit Logs:** Registro de todas as ações para análise posterior.
- **Miro Activity Log:** Histórico de alterações para auditoria.
- **Power BI Activity Log:** Registro de acessos e exportações.
- **Microsoft Defender/Security Center (se licenciado):** Alertas automáticos para ameaças conhecidas (malware, login suspeito).

**Táticas Implementadas (Reativas):**

- **Logs de Auditoria:** Todos os componentes (SharePoint, Miro, Power BI) registram ações automaticamente. Permite investigação forense após incidente.
- **Alertas Automáticos (Ameaças Conhecidas):** Se Defender licenciado, alertas para malware, ransomware, login de localização atípica. Notificação via e-mail/Teams para administradores.
- **Análise Manual de Logs:** Administradores podem exportar logs do SharePoint/Power BI e analisar acessos, modificações, exportações.

**Limitações/Vulnerabilidades Reativas:**

- **Detecção Reativa, Não Proativa:** Logs registram ações, mas **não alertam automaticamente** para violações de segregação por projeto. Detecção requer auditoria manual posterior.
- **Análise Manual Esporádica:** Não há processo sistemático de auditoria periódica (semanal, mensal). Análise ocorre após incidente reportado ou em revisões ad hoc.
- **Sem Correlação Automatizada:** Logs dispersos em múltiplas plataformas (SharePoint, Miro, Power BI). **Não há SIEM** (Security Information and Event Management) correlacionando eventos. Identificação de padrões suspeitos depende de análise manual.

###### Contenção de Incidentes:

**Componentes:**

- **Microsoft Entra ID:** Suspensão de contas comprometidas.
- **SharePoint Admin Center:** Revogação de permissões, bloqueio de compartilhamentos.
- **Microsoft Defender (se licenciado):** Quarentena automática de malware.

**Táticas Implementadas (Reativas):**

- **Suspensão de Conta:** Administrador pode desativar conta de usuário comprometido via Entra ID (<5 minutos). Bloqueio imediato de acesso a todos os sistemas Microsoft 365.
- **Revogação de Permissões:** Administrador do SharePoint pode revogar acesso específico a biblioteca/pasta (<10 minutos para ação manual).
- **Quarentena de Malware:** Defender (se licenciado) isola automaticamente arquivos infectados, impedindo propagação.
- **Bloqueio de Compartilhamentos Externos:** Administrador pode desativar compartilhamentos externos no SharePoint (temporariamente ou permanentemente).

**Limitações/Vulnerabilidades Reativas:**

- **Dependência de Detecção Manual:** Contenção requer que violação seja detectada primeiro. Como detecção de violações de governança é manual e esporádica, **tempo de contenção pode ser muito longo** (dias, semanas até descoberta).
- **Sem Automação de Contenção:** Todas as ações de contenção (suspensão de conta, revogação de permissões) são manuais. Requerem intervenção do administrador.

###### Correção e Recuperação:

**Componentes:**

- **SharePoint:** Versionamento, lixeira, suporte Microsoft para restauração.
- **Miro:** Histórico de versões, restauração de board.
- **Power BI:** Backups gerenciados pela Microsoft (sem controle direto).

**Táticas Implementadas (Reativas):**

- **Reversão de Versões (SharePoint):** Administrador ou usuário autorizado pode restaurar versão anterior de documento alterado indevidamente (<15 minutos para ação). Recupera integridade de cronogramas, TAPs, reportes, documentos.
- **Recuperação de Lixeira (SharePoint):** Documentos excluídos acidentalmente ou maliciosamente podem ser restaurados via lixeira de 1º estágio (self-service, <5 minutos) ou 2º estágio (administrador, <30 minutos). Até 186 dias de janela de recuperação total.
- **Restauração de Board (Miro):** Miro permite restaurar board completo para versão anterior ou duplicar versão limpa. Recupera planejamento corrompido.
- **Reset de Credenciais:** Após comprometimento de conta, administrador força troca de senha e re-registro de MFA.
- **Reprocessamento Manual:** Transações críticas que falharam (ex.: transferência Miro → SharePoint corrompida) requerem reexecução manual completa.

**Limitações/Vulnerabilidades Reativas:**

- **Recuperação Depende de Identificação Rápida:** Quanto mais tempo entre violação e detecção, maior a complexidade de recuperação (múltiplas versões alteradas, dificuldade de identificar versão limpa).
- **Sem Automação de Recuperação:** Todas as ações de recuperação são manuais. Requerem análise de logs, identificação de versão correta, ações de restauração por administrador.
- **Reprocessamento Manual Custoso:** Transferências manuais corrompidas (Miro → TAP) requerem reexecução completa do trabalho. Sem backup automatizado da transferência, pode haver perda de trabalho.

**Vulnerabilidade Geral das Táticas Reativas:** A eficácia das táticas reativas é severamente limitada pela **ausência de detecção automatizada e proativa de violações de governança**. O sistema detecta e reage rapidamente a ameaças externas óbvias (malware, login suspeito via Defender), mas **não detecta automaticamente** as vulnerabilidades críticas (acesso inadequado, manipulação em transferências, alterações sem aprovação). A resposta a estas violações depende de detecção manual esporádica, resultando em **tempo de resposta inaceitavelmente longo** (dias a semanas). Quando detectadas, as ações de contenção e recuperação são manuais e custosas. O sistema é fundamentalmente reativo para as vulnerabilidades mais relevantes de governança, o que é inaceitável para um sistema de missão crítica.

---

#### C. Como recuperar/subsidiar o tratamento de impactos

Os procedimentos de recuperação e subsídio ao tratamento de impactos de falhas de segurança no sistema atual dependem fundamentalmente dos componentes de versionamento e backup do SharePoint, histórico do Miro, e logs de auditoria para investigação forense, porém com limitações críticas relacionadas à ausência de detecção automatizada e processos de auditoria sistemáticos.

##### Componentes de Recuperação por Tipo de Incidente:

###### 1. Acesso Inadequado a Cronogramas/TAPs/Documentos (Violação de Segregação por Projeto):

**Componente de Suporte:**

- **SharePoint Audit Logs:** Registro de quem acessou qual documento, quando, ação realizada (visualização, download, edição).

**Procedimento de Detecção e Recuperação:**

1. **Detecção (Manual, Reativa):** Violação identificada através de:

   - Usuário reporta acesso indevido observado (ex.: viu documento de projeto que não deveria conhecer)
   - Auditoria periódica de logs (se implementada - atualmente não sistemática)
   - Investigação após vazamento de informação (incidente já consumado)

2. **Investigação Forense:** Administrador exporta SharePoint Audit Logs → filtra por usuário suspeito e/ou documentos sensíveis → identifica acessos indevidos (cruzamento manual com matriz de responsabilidades por projeto).

3. **Avaliação de Impacto:** Determinar quais informações foram visualizadas/baixadas, criticidade (estratégico, financeiro, técnico), se houve exportação (download) ou apenas visualização.

4. **Contenção:** Revogação imediata de permissões amplas do usuário → concessão de permissões restritas apenas aos projetos autorizados (processo manual de ajuste de permissões).

5. **Recuperação de Dados (se aplicável):** Se documentos foram alterados indevidamente durante acesso inadequado → restauração de versão anterior via versionamento do SharePoint.

6. **Comunicação:** Notificação ao líder do projeto afetado sobre acesso indevido → avaliação de necessidade de comunicação a stakeholders/alta gestão.

**Tempo de Recuperação (RTO):**

- Detecção: Indeterminado (depende de quando auditoria manual ocorrer ou incidente ser reportado - pode ser dias, semanas, meses após violação)
- Investigação: 2-8 horas (dependendo do volume de logs e número de usuários/documentos envolvidos)
- Contenção: <1 hora (revogação de permissões)
- Recuperação: <30 minutos (se alteração indevida ocorreu)

**Justificativa para Gestão (Quebra de Nível de Serviço de Governança):**

- **Causa Raiz:** Vulnerabilidade arquitetural - ausência de segregação granular de acesso por projeto no SharePoint. Sistema permite acesso amplo a todos os projetos para usuários autorizados tecnicamente.
- **Evidências:** SharePoint Audit Logs exportados mostrando acessos indevidos (usuário, timestamp, documentos acessados). Matriz de responsabilidades por projeto demonstrando que usuário não tinha autorização lógica.
- **Impacto:** Exposição de informações estratégicas/sensíveis (cronogramas, orçamentos, riscos, decisões) de projetos a usuários não autorizados. Potencial vazamento de informações competitivas ou confidenciais.
- **Ações Corretivas:** Revisão de permissões de todos os usuários com acesso amplo → ajuste manual para acesso restrito. Implementação de auditoria periódica mensal de acessos (processo manual proposto). Médio prazo: implementar segregação granular por projeto via quebra de herança de permissões ou migração de estrutura.

###### 2. Manipulação de Dados em Transferência Manual (Miro → TAP no SharePoint):

**Componentes de Suporte:**

- **Miro Activity Log:** Histórico completo do planejamento original.
- **SharePoint Audit Logs + Versionamento:** Registro de criação/edição do TAP e versões do documento.

**Procedimento de Detecção e Recuperação:**

1. **Detecção (Manual, Reativa):** Violação identificada através de:

   - Stakeholder identifica inconsistência entre planejamento apresentado (Miro) e documento formal (TAP)
   - Auditoria de qualidade de TAPs (se implementada - atualmente não sistemática)
   - Problema no projeto decorrente de escopo/benefícios incorretos documentados

2. **Investigação Forense:**

   - Acesso ao Miro Activity Log → identificação do estado do planejamento na data da transferência
   - Acesso ao SharePoint → identificação da primeira versão do TAP e quem criou
   - Comparação manual entre conteúdo do Miro (escopo, benefícios, premissas, riscos) e TAP no SharePoint
   - Identificação de divergências (omissões, alterações, adições não justificadas)

3. **Avaliação de Impacto:** Determinar criticidade das divergências (escopo alterado, benefícios inflacionados, riscos omitidos), impacto em aprovações já realizadas, decisões tomadas baseadas em informação incorreta.

4. **Recuperação de Integridade:**

   - Criação de nova versão do TAP corrigida com base no planejamento original do Miro
   - Versionamento no SharePoint preserva documento incorreto para auditoria
   - Se TAP já foi aprovado com informações incorretas → necessidade de reaprovação formal

5. **Investigação de Responsabilidade:** Cruzamento de quem realizou a transferência (autor do TAP no SharePoint) com intenção (erro humano vs. manipulação intencional) via entrevista.

6. **Comunicação:** Notificação ao comitê de aprovação sobre correção de TAP → reavaliação de aprovação → comunicação à equipe do projeto.

**Tempo de Recuperação (RTO):**

- Detecção: Indeterminado (depende de quando inconsistência é percebida - pode ser semanas, meses após transferência, potencialmente após aprovação e início do projeto)
- Investigação: 4-12 horas (comparação manual detalhada Miro vs. TAP)
- Recuperação: 2-8 horas (recriação de TAP correto) + tempo de reaprovação (dias a semanas)
- Impacto Total: Pode incluir retrabalho significativo se projeto já iniciado com base em TAP incorreto

**Justificativa para Gestão (Quebra de Integridade de Documentação):**

- **Causa Raiz:** Vulnerabilidade de processo - transferência manual sem validação sistêmica de integridade. Ausência de checksum, hash ou comparação automatizada entre Miro e SharePoint.
- **Evidências:**
  - Miro Activity Log mostrando estado do planejamento original (exportação com timestamp)
  - TAP no SharePoint com divergências documentadas
  - Análise comparativa (relatório de auditoria manual)
- **Impacto:** Documento formal de governança (TAP) com informações incorretas. Aprovações baseadas em premissas falsas. Potencial execução de projeto com escopo/benefícios não alinhados ao planejamento original. Comprometimento da governança de portfólio.
- **Ações Corretivas:** Correção imediata do TAP. Reavaliação de aprovação. Curto prazo: implementar checklist de validação manual (revisão por segundo usuário). Médio prazo: automação da transferência Miro → SharePoint via API com validação de integridade ou template estruturado com campos obrigatórios reduzindo margem para erro/manipulação.

###### 3. Alteração Não Autorizada de Documentos Críticos (TAP Aprovado, Cronograma Baseline):

**Componentes de Suporte:**

- **SharePoint Versionamento:** Preservação de todas as versões anteriores (até 500 versões).
- **SharePoint Audit Logs:** Registro de quem alterou, quando.

**Procedimento de Detecção e Recuperação:**

1. **Detecção (Manual, Reativa):** Violação identificada através de:

   - Usuário autorizado percebe alteração não comunicada em documento crítico
   - Comparação de versões durante revisão de projeto
   - Auditoria de integridade de baselines (se implementada - atualmente não sistemática)

2. **Investigação Forense:**

   - Acesso ao histórico de versões do SharePoint → identificação de todas as versões do documento
   - Análise de diff entre versões → identificação exata do que foi alterado (escopo, datas, orçamento, etc.)
   - Acesso ao Audit Log → identificação de quem realizou a alteração e quando
   - Verificação se houve workflow de aprovação de mudança (processo organizacional - não sistêmico)

3. **Avaliação de Impacto:** Determinar se alteração foi acidental (erro de usuário editando documento errado) ou intencional, criticidade da alteração (mudança de baseline de cronograma afeta todo o planejamento, alteração de escopo do TAP invalida aprovação), impacto em decisões/ações já tomadas.

4. **Recuperação de Integridade:**

   - Restauração da versão aprovada anterior via versionamento do SharePoint (<15 minutos)
   - Notificação ao autor da alteração sobre reversão
   - Se alteração era legítima mas sem aprovação formal → iniciar workflow correto de aprovação de mudança

5. **Prevenção Futura (Medida Manual):** Implementação de permissão somente leitura para documentos aprovados críticos (requer identificação manual de quais documentos + alteração manual de permissões por documento).

6. **Comunicação:** Notificação ao líder do projeto e PMO sobre alteração não autorizada e reversão → investigação de necessidade de ações disciplinares se intencional.

**Tempo de Recuperação (RTO):**

- Detecção: Indeterminado (depende de quando alteração é percebida - dias, semanas, meses após modificação)
- Investigação: 1-4 horas (análise de versões e logs)
- Recuperação: <30 minutos (restauração de versão)
- Reaprovação (se necessário): Dias a semanas

**Justificativa para Gestão (Quebra de Integridade de Baseline):**

- **Causa Raiz:** Vulnerabilidade de controle - ausência de workflow sistêmico de aprovação de mudanças para documentos críticos. Sistema não distingue documentos aprovados que requerem controle de mudança vs. documentos de trabalho.
- **Evidências:**
  - Histórico de versões do SharePoint mostrando alteração e diff entre versões
  - Audit Log identificando autor e timestamp
  - Ausência de registro de aprovação formal de mudança (se aplicável)
- **Impacto:** Perda de integridade de baseline aprovada. Potencial execução de projeto com parâmetros não aprovados. Comprometimento da rastreabilidade de decisões de mudança (change control).
- **Ações Corretivas:** Restauração imediata da versão aprovada. Implementação de permissão somente leitura para documentos críticos identificados (processo manual). Médio prazo: implementar workflow sistêmico de aprovação de mudanças com bloqueio de edição de documentos em status "aprovado" ou biblioteca específica de baselines com permissões restritas.

###### 4. Exclusão Acidental ou Maliciosa de Documentos:

**Componentes de Suporte:**

- **SharePoint Lixeira de 1º Estágio (Usuário):** 93 dias de retenção.
- **SharePoint Lixeira de 2º Estágio (Site Collection):** Mais 93 dias de retenção.
- **SharePoint Audit Logs:** Registro de exclusão.

**Procedimento de Detecção e Recuperação:**

1. **Detecção (Imediata ou Reativa):** Exclusão identificada quando:

   - Usuário tenta acessar documento e não encontra (imediata)
   - Auditoria de estrutura de pastas/documentos (reativa)

2. **Investigação:** Acesso ao Audit Log → identificação de quem excluiu, quando, se exclusão foi via interface (acidental provável) ou programática (maliciosa potencial).

3. **Recuperação:**

   - **Se dentro de 93 dias:** Usuário acessa própria lixeira (1º estágio) → restaura documento ao local original (<5 minutos, self-service)
   - **Se entre 93-186 dias:** Administrador acessa lixeira de 2º estágio → restaura documento (<30 minutos)
   - **Se após 186 dias:** Documento permanentemente perdido → necessidade de reconstrução manual ou restauração via suporte Microsoft (snapshot de site, disponível até 14 dias retroativos, processo complexo e demorado)

4. **Validação:** Verificação de integridade do documento restaurado (versão correta, conteúdo íntegro).

**Tempo de Recuperação (RTO):**

- Detecção: Imediata (se usuário tenta acessar) ou indeterminada (se ninguém procura o documento)
- Recuperação: <5 minutos (1º estágio) a <30 minutos (2º estágio) a 4-24 horas (suporte Microsoft após 186 dias)

**Justificativa para Gestão (Quebra de Disponibilidade Temporária):**

- **Causa Raiz:** Erro humano (exclusão acidental por usuário com permissão de Colaborador) ou ação maliciosa (sabotagem).
- **Evidências:** Audit Log mostrando exclusão (usuário, timestamp, documento).
- **Impacto:** Indisponibilidade temporária de documento crítico. Se não detectado dentro de 186 dias, perda permanente. Interrupção de trabalho de equipe do projeto.
- **Ações Corretivas:** Restauração imediata. Se maliciosa: suspensão de conta e investigação disciplinar. Prevenção: treinamento de usuários sobre lixeira. Médio prazo: implementar permissões mais restritivas (Collaborate sem permissão de exclusão) para documentos críticos ou bloqueio de exclusão em bibliotecas de baselines.

###### 5. Exportação Não Autorizada e Vazamento de Informações:

**Componentes de Suporte:**

- **SharePoint Audit Logs:** Registro de downloads.
- **Power BI Activity Logs:** Registro de exportações de relatórios.

**Procedimento de Detecção e Recuperação:**

1. **Detecção (Manual, Reativa - Pós-Incidente):** Vazamento identificado quando:

   - Informação sensível aparece em canal não autorizado (e-mail externo, mídia, concorrente)
   - Denúncia de compartilhamento inadequado
   - Auditoria de exportações (se implementada - atualmente não sistemática)

2. **Investigação Forense:**

   - Acesso ao SharePoint/Power BI Audit Logs → identificação de quem exportou/baixou o documento/relatório, quando
   - Análise de padrão (volume atípico de downloads, horário suspeito, exportação de múltiplos documentos sensíveis em curto período)
   - Cruzamento com evidência externa (se informação vazada tem marcas d'água, metadados identificáveis)
   - Investigação de destino (para onde foi compartilhado, quem teve acesso indevido)

3. **Avaliação de Impacto:** Determinar criticidade da informação vazada (estratégico, financeiro, regulatório), abrangência (quantas pessoas tiveram acesso indevido), dano potencial (vantagem competitiva perdida, exposição regulatória, dano reputacional).

4. **Contenção (Limitada):**

   - Suspensão da conta do usuário responsável pelo vazamento
   - Revogação de permissões de exportação (se possível - Power BI permite bloquear exportações por workspace, SharePoint não permite bloquear downloads seletivamente)
   - Comunicação de recall (se informação foi compartilhada via e-mail corporativo - eficácia limitada)
   - **Limitação Crítica:** Informação já vazada **não pode ser recuperada**. Contenção impede apenas vazamentos adicionais.

5. **Ações Legais/Disciplinares:** Dependendo da gravidade, envolvimento de jurídico, RH, potencialmente autoridades externas (se violação de LGPD ou regulamentação setorial).

6. **Comunicação:** Notificação à alta gestão, avaliação de necessidade de comunicação externa (se impacto regulatório ou contratual com stakeholders externos), comunicação interna sobre reforço de políticas de segurança.

**Tempo de Recuperação (RTO):**

- **Não Aplicável:** Informação vazada não pode ser "recuperada". Contenção de danos adicionais: <2 horas. Investigação completa: Dias a semanas.

**Justificativa para Gestão (Quebra de Confidencialidade - Irreversível):**

- **Causa Raiz:** Vulnerabilidade de controle - ausência de bloqueio sistêmico de exportações para usuários autorizados + perda de controle sobre documentos após download local. Sistema registra exportações, mas não previne.
- **Evidências:**
  - Audit Logs mostrando exportação/download (usuário, timestamp, documento/relatório)
  - Evidência externa de vazamento (e-mail, documento físico, screenshot)
  - Análise forense de metadados (se disponível)
- **Impacto:** **Irreversível** - informação sensível exposta a partes não autorizadas. Potencial perda de vantagem competitiva, dano reputacional, exposição legal/regulatória (se dados pessoais/sensíveis segundo LGPD), perda de confiança de stakeholders.
- **Ações Corretivas:** Contenção de danos adicionais (suspensão de conta, bloqueio de exportações). Ações disciplinares/legais. Curto prazo: reforço de treinamento e políticas de segurança. Médio prazo: implementar DLP (Data Loss Prevention) com bloqueio de compartilhamento externo de documentos classificados, Azure Information Protection com criptografia persistente (documentos protegidos mesmo após download, requerem autenticação para abertura), revisão de permissões para reduzir acesso amplo. **Longo prazo:** Considerar migração para plataforma com controle mais granular de exportação ou implementar virtualização de ambiente (acesso via VDI sem possibilidade de download local).

###### 6. Indisponibilidade por Falha da Microsoft 365:

**Componentes de Suporte:**

- **Microsoft Service Health Dashboard:** Status de serviços Microsoft 365.
- **Suporte Microsoft:** Tickets de suporte prioritários.
- **SLA Microsoft:** 99,9% de disponibilidade (até 43,2 minutos de downtime/mês permitido).

**Procedimento de Detecção e Recuperação:**

1. **Detecção (Sistêmica):** Usuários reportam impossibilidade de acesso ao SharePoint/Miro (web)/Power BI.

2. **Verificação:** Administrador acessa Microsoft Service Health Dashboard → confirma indisponibilidade reportada pela Microsoft (incidente com ID específico).

3. **Comunicação Proativa:** Notificação aos usuários via canal alternativo (e-mail corporativo, Teams se disponível, telefone) informando indisponibilidade conhecida, estimativa de recuperação (se fornecida pela Microsoft), orientação para aguardar.

4. **Monitoramento:** Acompanhamento contínuo do status via Service Health Dashboard (atualizações a cada 30-60 minutos pela Microsoft).

5. **Recuperação (Automática pela Microsoft):** Restauração do serviço pela Microsoft (failover para datacenter alternativo, correção de falha). Metrô não tem ação direta na recuperação.

6. **Validação Pós-Restauração:** Após notificação de recuperação pela Microsoft, administrador valida acesso ao SharePoint/Power BI, integridade de dados (verificação amostral de documentos), funcionalidades críticas (upload, download, edição).

**Tempo de Recuperação (RTO):**

- Detecção: <15 minutos (usuários reportam + verificação de Service Health)
- Recuperação: Dependente da Microsoft - geralmente <4 horas para incidentes críticos (conforme SLA). Pode chegar a 24 horas em casos excepcionais (falha de datacenter inteiro).
- **RPO (Recovery Point Objective):** <15 minutos (último snapshot/versionamento antes da falha - geralmente sem perda de dados devido a redundância).

**Justificativa para Gestão (Quebra de Disponibilidade por Terceiro):**

- **Causa Raiz:** Falha de infraestrutura terceirizada (Microsoft 365). Indisponibilidade de datacenter, falha de rede, bug em atualização de plataforma, ataque DDoS contra Microsoft.
- **Evidências:**
  - Microsoft Service Health Dashboard mostrando incidente reportado (ID do incidente, descrição, timeline)
  - Ticket de suporte aberto com Microsoft (se aplicável)
  - Comunicações enviadas aos usuários (transparência de ações tomadas)
- **Impacto:** Indisponibilidade temporária de acesso a cronogramas, TAPs, documentos, reportes, relatórios. Interrupção de trabalho de todas as equipes de projetos. Impossibilidade de atualização de status, elaboração de relatórios, acessos a informações críticas para reuniões/decisões. Perda de produtividade (horas-homem paradas).
- **Justificativa para SLA:** **Dependência de infraestrutura gerenciada por terceiro (Microsoft)**. Metrô não possui controle sobre infraestrutura física, lógica, políticas de manutenção ou capacidade de failover. SLA Microsoft 365 garante 99,9% de disponibilidade mensal (~43 minutos de downtime permitido). Incidente atual dentro ou fora do SLA (especificar duração). Todas as ações de comunicação e monitoramento possíveis foram executadas pela equipe do Metrô conforme playbook. **Nenhuma ação corretiva interna é necessária** - falha externa sem controle.
- **Ações Pós-Incidente:** Acompanhamento de post-mortem da Microsoft (geralmente publicado 5-7 dias após incidente). Validação se compensação de SLA é aplicável (crédito proporcional ao tempo de indisponibilidade acima do permitido). Revisão de plano de continuidade de negócios para considerar cenários de indisponibilidade prolongada (>4 horas) - alternativas de trabalho offline, priorização de atividades críticas que não dependem de acesso online.

---

### 5.3.3 RNF-03 — Rastreabilidade

&emsp;A análise do RNF de Rastreabilidade no sistema atual (AS-IS) deve focar na descrição das **táticas arquiteturais e componentes** que, mesmo de forma limitada, ajudam na execução e controle deste requisito. Conforme a seção 5.2.3, o sistema atual é baseado em um ecossistema de ferramentas Microsoft (SharePoint, Power Automate) e ferramentas externas (Miro, Excel), o que implica que a rastreabilidade de ponta a ponta é **inexistente**, e as táticas se limitam a silos de auditoria dentro de componentes específicos.

#### A. Como monitorar o RNF

&emsp;O monitoramento da Rastreabilidade é **parcial, fragmentado e predominantemente manual**, sendo incapaz de fornecer uma visão de ponta a ponta sobre a integridade e a linhagem dos dados.

| Aspecto                            | Descrição no Sistema Atual (AS-IS)                                                                                                                                                                                                                   | Limitações/Vulnerabilidades                                                                                                                                                                                             |
| :--------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Componentes de Monitoramento**   | **Log de Auditoria do SharePoint e Histórico do Power Automate:** O monitoramento se limita aos logs gerados por cada ferramenta individualmente. O SharePoint registra alterações em arquivos e o Power Automate registra o histórico de execuções. | A ausência de um **ID de Correlação** entre os logs impede o monitoramento do fluxo de negócio. O ponto cego principal, a **transferência manual de dados**, não possui nenhum componente de monitoramento.             |
| **Métricas/SLIs/SLOs**             | **Nenhuma:** Não existem métricas, SLIs ou SLOs definidos para a rastreabilidade.                                                                                                                                                                    | O monitoramento é puramente qualitativo e reativo. Não há como medir o nível de atendimento do requisito, como "percentual de dados com linhagem comprovada".                                                           |
| **Monitoramento Manual/Sistêmico** | **Sistêmico (em silos):** Consulta aos logs individuais de cada ferramenta. **Manual:** A correlação de eventos e a reconstrução da trilha de auditoria são processos 100% manuais, baseados em entrevistas e análise de timestamps.                 | A falta de uma ferramenta de **SIEM (Security Information and Event Management)** para agregação e correlação de logs torna o monitoramento proativo impossível e o diagnóstico de incidentes extremamente ineficiente. |

#### B. Como resolver o RNF (Preventivo e Reativo)

&emsp;As táticas de resolução para a Rastreabilidade no sistema atual são mínimas e focadas em controle de acesso, não em auditoria de transações, sendo ineficazes para garantir a integridade do fluxo de dados.

| Tática         | Componente/Mecanismo                                                                                                                                                                | Natureza               | Vulnerabilidade                                                                                                                                                                                |
| :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Preventiva** | **Controle de Acesso (RBAC) no SharePoint:** Limita quem pode inserir ou modificar dados no repositório central.                                                                    | Sistêmica (SharePoint) | **Insuficiente:** Não impede que um usuário autorizado cometa um erro ou fraude durante a transferência manual de dados, e não gera um log detalhado da transação em si.                       |
| **Preventiva** | **Nenhuma:** Não há políticas de auditoria, validações de integridade ou mecanismos de _checksum_ para garantir que os dados transferidos manualmente sejam idênticos aos da fonte. | Processual             | A prevenção depende inteiramente da **disciplina e boa-fé do usuário**, o que não é uma tática arquitetural confiável.                                                                         |
| **Reativa**    | **Logs de Auditoria do SharePoint e Power Automate:** Permitem verificar _a posteriori_ quem alterou um dado _dentro do SharePoint_ ou qual fluxo foi executado.                    | Sistêmica (em silos)   | **Diagnóstico Incompleto:** Os logs não respondem à pergunta fundamental: "De onde veio este dado?". A reatividade é limitada a um fragmento do problema.                                      |
| **Reativa**    | **Investigação Manual Forense:** Entrevistar usuários para reconstruir a sequência de eventos que levaram a uma inconsistência de dados.                                            | Manual/Processual      | **Ineficiente e Não Confiável:** Processo lento, sujeito a falhas de memória humana e sem garantia de precisão. O MTTR (Mean Time to Recovery) para um incidente de dados é extremamente alto. |

#### C. Como recuperar/subsidiar o tratamento de impactos

&emsp;A recuperação de impactos causados por falhas de rastreabilidade é **extremamente frágil, não sistêmica e baseada em arqueologia de dados**, sem componentes arquiteturais que garantam a recuperação da integridade.

| Componente/Procedimento         | Descrição                                                                                                                                                                                                                                  | Justificativa/Impacto                                                                                                                                                                                                                                              |
| :------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Registro de Falhas**          | **Nenhum:** A falha de rastreabilidade (ex: um dado inserido incorretamente) **não gera um registro de falha**. O único registro é o log de auditoria do SharePoint que mostra a alteração, mas a classifica como uma operação normal.     | **Impossibilidade de Justificativa:** Sem um registro claro da transação original (transferência manual), é impossível justificar formalmente a causa de uma inconsistência de dados. A "falha" é silenciosa.                                                      |
| **Procedimento de Recuperação** | **Investigação Manual e Correção Direta:** O procedimento envolve (1) identificar a inconsistência, (2) investigar manualmente a origem através de entrevistas, e (3) corrigir o dado diretamente no SharePoint.                           | **Risco de Novos Erros:** A correção manual é, em si, outra transação não rastreada em seu contexto de negócio. Não há um vínculo formal entre o incidente e a correção, perpetuando o ciclo de falta de rastreabilidade.                                          |
| **Componente de Recuperação**   | **Nenhum:** O sistema **não possui** componentes de recuperação arquiteturalmente definidos para a integridade dos dados, como versionamento de dados com justificativa, _rollback_ de transações de negócio ou um _log de imutabilidade_. | **Risco Crítico:** A falta de mecanismos de recuperação significa que a integridade dos dados históricos não pode ser garantida. Uma vez que um dado incorreto é inserido e processado, a confiança em todo o conjunto de dados fica permanentemente comprometida. |

&emsp;A ausência de táticas arquiteturais para garantir uma trilha de auditoria de ponta a ponta e a dependência de processos manuais não auditados demonstram que o RNF de Rastreabilidade é **criticamente mal atendido** no sistema AS-IS, justificando a necessidade de uma nova arquitetura com um ponto de ingestão de dados centralizado, transacional e auditável, e o uso de um ID de Correlação em todo o fluxo.

---

## 5.4 Análise de Causas e Impactos

### 5.4.1 RNF-01 — Escalabilidade

Esta seção aprofunda a análise do RNF de Escalabilidade no sistema atual (AS-IS), focando na correlação entre as vulnerabilidades identificadas, suas causas raiz e os impactos diretos no negócio do Metrô-SP.

#### Causas e Impactos da Quebra de Escalabilidade

A principal causa da quebra de escalabilidade reside na **Arquitetura de Dados Inadequada** (uso de repositórios de arquivos como banco de dados transacional) e na **Dependência de um Único Fornecedor** (Microsoft SharePoint Online), conforme detalhado na seção 5.2.1.

| Causa Raiz (Vulnerabilidade)                             | Cenário de Falha (Gatilho)                                                  | Impacto no Negócio (Consequência)                                                                                                                                                                                                                                        |
| :------------------------------------------------------- | :-------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Arquitetura de Dados Inadequada** (SharePoint como DB) | Geração de relatórios de grande volume (Etapa 5) ou consultas complexas.    | **Degradação Crítica de Performance:** Lentidão no acesso a dados e falhas na geração de relatórios estratégicos. **Impacto:** Atraso na tomada de decisão da diretoria e perda de credibilidade nos dados do PMO.                                                       |
| **Dependência de um Único Fornecedor** (Throttling)      | Picos de acesso simultâneo durante o ciclo de reporte mensal (Etapa 3 e 4). | **Indisponibilidade Operacional:** Bloqueio temporário de requisições (_throttling_). **Impacto:** Interrupção dos fluxos de trabalho do Power Automate, perda de dados e necessidade de intervenção manual para reprocessamento.                                        |
| **Ausência de API Centralizada**                         | Tentativa de processamento assíncrono ou _load balancing_ de requisições.   | **Incapacidade de Controle Técnico:** Impossibilidade de implementar táticas arquiteturais preventivas (_Rate Limiting_, _Load Balancing_) sob controle do Metrô. **Impacto:** Risco não mitigável de sobrecarga, dependendo exclusivamente das políticas do fornecedor. |

#### Detalhamento da Quebra de Nível de Serviço

A quebra do nível de serviço (SLA) de escalabilidade se manifesta principalmente pela não-conclusão de transações críticas dentro do tempo esperado (latência excessiva) ou pela interrupção total do serviço (indisponibilidade).

- **Quebra por Latência:** O tempo de resposta para a geração de relatórios (Etapa 5) excede o limite aceitável, resultando em relatórios desatualizados ou incompletos.
- **Quebra por Indisponibilidade:** O sistema atinge o limite de _throttling_ do SharePoint, impedindo que os fluxos do Power Automate (Etapa 4) concluam a transferência de dados.

O impacto direto é a **inconsistência de dados** entre as fontes (Miro, SharePoint, Power BI), comprometendo a **integridade** e a **confiabilidade** das informações estratégicas do portfólio.

#### Como recuperar/subsidiar o tratamento de impactos

Esta seção detalha os procedimentos e componentes (ou a falta deles) usados para subsidiar o tratamento de falhas causadas pela quebra de escalabilidade, focando na **justificativa** para a necessidade de mudança.

| Componente/Procedimento           | Descrição Detalhada                                                                                                                                                                                                             | Justificativa da Inadequação (Racional para a Nova Arquitetura)                                                                                                                                                                                                                                                          |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Registro de Falhas (Subsídio)** | **Logs do Power Automate:** O log registra a falha (ex: `429 Too Many Requests` do SharePoint) e o momento da ocorrência.                                                                                                       | O log **apenas registra o sintoma**, mas não oferece o contexto completo da transação (ex: quais dados foram perdidos, qual o impacto exato no projeto X). O subsídio é insuficiente para uma **análise de causa raiz (RCA)** eficiente, pois não há correlação com métricas de infraestrutura.                          |
| **Procedimento de Recuperação**   | **Intervenção Manual e Reexecução:** A equipe de suporte deve identificar o fluxo falho, analisar o log e reexecutá-lo manualmente, muitas vezes após um período de espera para que o _throttling_ do SharePoint seja liberado. | **Alto MTTR e Risco de Inconsistência:** O procedimento é lento e oneroso (alto custo operacional). A reexecução manual não garante a **ordem de processamento** e pode resultar em **dados duplicados** ou **desatualizados** se a fonte original tiver sido modificada.                                                |
| **Componentes de Recuperação**    | **Nenhum Mecanismo Arquitetural:** Não existem componentes como _Message Queues_ (Filas de Mensagens) ou _Dead Letter Queues_ (DLQ) para reprocessamento automático e seguro.                                                   | **Vulnerabilidade Crítica de Integridade:** A ausência de um mecanismo de _Retry_ automático e seguro significa que a **perda de transações** é um risco constante. A nova arquitetura deve introduzir **processamento assíncrono** com filas para garantir a entrega e o reprocessamento de mensagens em caso de falha. |

A atual dependência de processos manuais para recuperação e a falta de um subsídio técnico adequado para a análise de falhas reforçam a conclusão de que o sistema AS-IS não é tolerante a falhas de escalabilidade, sendo imperativo o redesenho arquitetural.

---

### 5.4.2 RNF-02 — <Segurança>

#### C. Como recuperar/subsidiar o tratamento de impactos

##### Matriz Consolidada de Recuperação por Tipo de Incidente:

| **Tipo de Incidente**                         | **RTO (Tempo de Recuperação)**                                    | **RPO (Perda de Dados)**                  | **Componente Principal**                     | **Procedimento-Chave**                           | **Reversibilidade**                                                                                         |
| --------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------- | -------------------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| Acesso inadequado por permissão ampla         | Indeterminado (detecção) + <1h (contenção)                        | N/A (não há perda de dados)               | SharePoint Audit Logs + Permissões           | Auditoria manual de logs → Ajuste de permissões  | Reversível (contenção impede acessos futuros, mas exposição passada é irreversível)                         |
| Manipulação em transferência Miro→TAP         | Indeterminado (detecção) + 4-12h (investigação) + 2-8h (correção) | Integridade comprometida até detecção     | Miro Activity Log + SharePoint Versionamento | Comparação manual Miro vs. TAP → Correção de TAP | Reversível (correção de documento, mas decisões tomadas com base em informação incorreta são irreversíveis) |
| Alteração não autorizada de documento crítico | Indeterminado (detecção) + <30min (restauração)                   | <15min (última versão antes da alteração) | SharePoint Versionamento                     | Restauração de versão anterior                   | Totalmente reversível (se detectado antes de versões serem purgadas)                                        |
| Exclusão acidental/maliciosa                  | Imediata (se usuário percebe) + <5-30min (restauração)            | 0 (se dentro de 186 dias)                 | SharePoint Lixeira (1º e 2º estágio)         | Restauração via lixeira                          | Totalmente reversível (até 186 dias)                                                                        |
| Exportação não autorizada/vazamento           | Imediata (se reportado) + <2h (contenção)                         | **Irreversível**                          | SharePoint/Power BI Audit Logs               | Suspensão de conta + Investigação forense        | **Irreversível** - informação exposta não pode ser recuperada                                               |
| Indisponibilidade Microsoft 365               | <15min (detecção) + <4h (recuperação Microsoft)                   | <15min (snapshots)                        | Microsoft Service Health + Suporte Microsoft | Monitoramento + Comunicação aos usuários         | Totalmente reversível (recuperação automática pela Microsoft)                                               |

##### Template de Relatório de Incidente para Gestão:

```
RELATÓRIO DE INCIDENTE DE SEGURANÇA - RNF-02
ID do Incidente: [SEC-YYYY-MM-NNN]
Data/Hora de Detecção: [DD/MM/YYYY HH:MM]
Severidade: [Crítica / Alta / Média / Baixa]

1. SUMÁRIO EXECUTIVO
[Descrição em 2-3 linhas do que ocorreu, impacto principal, status atual]

2. TIMELINE DO INCIDENTE
- [HH:MM] Ocorrência da violação/falha (estimado ou confirmado)
- [HH:MM] Detecção do incidente (como foi detectado: usuário reportou / auditoria / alerta automático)
- [HH:MM] Início da investigação
- [HH:MM] Contenção executada (ações tomadas)
- [HH:MM] Recuperação concluída / Incidente encerrado

Tempo Total: Detecção: [X horas/dias], Contenção: [X minutos/horas], Recuperação: [X minutos/horas/dias]

3. CAUSA RAIZ
[Vulnerabilidade explorada, falha de controle, erro humano, falha externa]
Categoria: [Acesso Inadequado / Manipulação de Dados / Alteração Não Autorizada / Exclusão / Vazamento / Indisponibilidade]

4. EVIDÊNCIAS TÉCNICAS
- Logs de Auditoria: [SharePoint/Miro/Power BI - período analisado, usuários envolvidos]
- Versões de Documentos: [Documentos afetados, versões comparadas]
- Prints/Exportações: [Anexos de evidências]

5. IMPACTO
- Projetos Afetados: [Lista de projetos]
- Usuários Impactados: [Número e/ou nomes]
- Dados Comprometidos: [Tipo e volume - cronogramas, TAPs, relatórios, etc.]
- Criticidade da Informação: [Estratégica / Financeira / Operacional / Pública]
- Perda de Dados: [Volume e período - ou N/A se recuperado]
- Interrupção de Serviço: [Duração total de indisponibilidade - ou N/A]

6. AÇÕES DE CONTENÇÃO E RECUPERAÇÃO EXECUTADAS
- [Lista numerada de ações tomadas, por quem, quando]
- Componentes Utilizados: [SharePoint Versionamento / Lixeira / Logs / Suporte Microsoft]
- Resultado: [Recuperado totalmente / Parcialmente / Irreversível]

7. CONFORMIDADE COM SLA/SLO
- SLO Aplicável: [Ex.: Tempo de resposta <2h para incidentes críticos]
- Atingido: [Sim / Não - Justificativa se não atingido]
- SLA Microsoft 365: [Aplicável se indisponibilidade - 99,9% mensal]

8. JUSTIFICATIVA PARA GESTÃO
[Explicação clara da causa raiz como vulnerabilidade arquitetural/processual conhecida]
[Argumento de que ações corretivas sistêmicas requerem mudanças arquiteturais/investimento]
[Demonstração de que equipe agiu conforme procedimentos disponíveis]

9. AÇÕES CORRETIVAS IMEDIATAS
- Curto Prazo (<30 dias): [Ex.: Ajuste manual de permissões, treinamento de usuários]
- Médio Prazo (30-90 dias): [Ex.: Implementação de auditoria periódica, workflow de aprovação]
- Longo Prazo (>90 dias): [Ex.: Redesenho de arquitetura, implementação de SIEM, segregação granular]

10. LIÇÕES APRENDIDAS
- [O que funcionou bem na resposta ao incidente]
- [O que precisa melhorar]
- [Indicadores para adicionar ao monitoramento]

Responsável pelo Relatório: [Nome, Cargo]
Data do Relatório: [DD/MM/YYYY]
Aprovado por: [Gestor de TI / CISO / Gestor do Portfólio]
```

##### Documentação de Suporte para Justificativas (Anexos-Padrão):

1. **Exportação de SharePoint Audit Logs** (CSV formatado com filtros aplicados)
2. **Matriz de Responsabilidades por Projeto** (planilha mostrando quem deveria ter acesso a quais projetos)
3. **Análise Comparativa** (para manipulação Miro→TAP: documento mostrando divergências identificadas)
4. **Histórico de Versões** (print do SharePoint mostrando versões do documento afetado)
5. **Comunicações Enviadas** (cópia de e-mails/mensagens enviados aos usuários durante incidente)
6. **Status Microsoft Service Health** (print mostrando incidente reportado pela Microsoft, se aplicável)
7. **Plano de Ação Corretiva** (documento detalhado com responsáveis e prazos)

##### Critérios para Escalonamento de Incidentes:

| **Severidade** | **Critérios**                                                                                                                                          | **Notificação Imediata**                       | **SLA de Resposta**                 |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------- | ----------------------------------- |
| **Crítica**    | Vazamento de informações estratégicas; Alteração de múltiplos documentos críticos; Indisponibilidade >4h; Evidência de ataque malicioso                | CISO, Gestor do Portfólio, Diretoria, Jurídico | <30min (detecção) + <2h (contenção) |
| **Alta**       | Acesso inadequado a documentos sensíveis por múltiplos usuários; Manipulação detectada em TAP; Exclusão de documentos críticos; Indisponibilidade 1-4h | Gestor de TI, Gestor do Portfólio, PMO         | <2h (detecção) + <4h (contenção)    |
| **Média**      | Acesso inadequado isolado; Alteração não autorizada em documento de trabalho; Exclusão acidental recuperável                                           | Administrador do SharePoint, Gestor de TI      | <8h (detecção) + <8h (recuperação)  |
| **Baixa**      | Falso positivo; Anomalia benigna; Indisponibilidade <30min                                                                                             | Log interno apenas                             | <24h (documentação)                 |

##### Exemplo de Justificativa Consolidada para Alta Gestão:

```
JUSTIFICATIVA DE INCIDENTE DE SEGURANÇA - ACESSO INADEQUADO A PROJETOS

Contexto:
Durante auditoria mensal de logs do SharePoint (implementada após incidentes anteriores),
identificou-se que 5 usuários acessaram cronogramas e TAPs de projetos para os quais não
possuíam autorização lógica, embora tivessem permissão técnica no sistema.

Causa Raiz Arquitetural:
O sistema atual (SharePoint Online) possui vulnerabilidade arquitetural conhecida e documentada:
- Permissões são concedidas no nível de BIBLIOTECA GERAL (ex.: "Cronogramas", "TAPs")
- Usuário com permissão de "Colaborador" na biblioteca acessa TODOS os projetos do portfólio
- Não há segregação granular por projeto/subfolder implementada sistematicamente

Esta vulnerabilidade é resultado de:
1. Limitação técnica da forma como o SharePoint foi estruturado inicialmente (herança de permissões)
2. Ausência de investimento em reestruturação para quebra de herança por projeto
3. Gestão manual de permissões não escala para 40-60 usuários em 20-40 projetos simultâneos

Impacto do Incidente Atual:
- 5 usuários visualizaram/baixaram documentos de 12 projetos não autorizados
- Exposição de informações estratégicas (cronogramas, orçamentos, riscos, decisões)
- Nenhuma alteração indevida identificada (apenas leitura/download)
- Potencial vazamento de informações competitivas (sob investigação)

Ações Imediatas Executadas:
1. Revogação de permissões amplas dos 5 usuários identificados (concluído em 2 horas)
2. Concessão de permissões restritas apenas aos projetos autorizados (processo manual, 6 horas)
3. Notificação aos líderes dos 12 projetos afetados sobre potencial exposição
4. Investigação forense completa (análise de 90 dias de logs - 12 horas de trabalho)

Por Que Este Incidente Não Representa Falha da Equipe de TI:
1. Sistema opera conforme projetado - permissões amplas são funcionalidade, não bug
2. Equipe de TI não possui ferramentas de detecção automatizada de "acessos inadequados"
   (sistema não diferencia acesso tecnicamente permitido vs. logicamente não autorizado)
3. Detecção dependeu de auditoria manual implementada proativamente pela equipe
4. Tempo de resposta pós-detecção foi adequado (<2h para contenção)

Limitações Sistêmicas Atuais:
- Microsoft 365 não fornece controle granular sobre infraestrutura (gerenciado pela Microsoft)
- SharePoint Audit Logs registram "acessos permitidos", não "violações de segregação lógica"
- Correlação manual de logs com matriz de projetos é única forma de detecção (processo intensivo)
- Ausência de SIEM corporativo impede correlação automatizada e alertas proativos

Ações Corretivas Propostas:

Curto Prazo (<30 dias):
- Implementar auditoria mensal sistemática de acessos (processo manual - 16h/mês)
- Revisão completa de permissões de todos os usuários (estimado 40 horas)
- Treinamento de usuários sobre políticas de acesso e confidencialidade

Médio Prazo (30-90 dias):
- Projeto piloto de reestruturação de permissões em 3 projetos críticos (quebra de herança)
- Implementação de dashboard Power BI com métricas de acesso para monitoramento contínuo
- Criação de matriz automatizada de auditoria (cruzamento de logs com matriz de projetos via Power BI)

Longo Prazo (>90 dias - Requer Investimento):
- Reestruturação completa da arquitetura de permissões do SharePoint (quebra de herança por projeto)
  Estimativa: 200 horas de trabalho + consultoria especializada
- Implementação de SIEM corporativo (Azure Sentinel ou similar) para correlação automatizada
  Estimativa: Investimento em licenciamento + configuração
- Migração para estrutura de SharePoint Sites por projeto (isolamento completo)
  Estimativa: Projeto de 6 meses

Conclusão:
O incidente atual é resultado de vulnerabilidade arquitetural conhecida e documentada,
não de falha operacional da equipe. A detecção proativa via auditoria manual representa
MELHORIA em relação ao cenário anterior (ausência de auditoria). Ações corretivas de
curto/médio prazo são viáveis dentro de recursos atuais. Solução definitiva requer
investimento em reestruturação arquitetural e ferramentas de monitoramento avançadas.

Aprovação Solicitada:
- Priorização de recursos para implementação de ações de médio/longo prazo
- Alocação de orçamento para consultoria especializada e licenciamento de ferramentas
- Autorização para criação de grupo de trabalho dedicado à reestruturação de segurança
```

##### Vulnerabilidade Final de Recuperação:

O sistema atual possui **capacidade técnica de recuperação adequada para falhas técnicas** (exclusões, alterações indevidas de documentos individuais, indisponibilidades temporárias) através de versionamento robusto, lixeira com retenção longa e redundância da Microsoft. Porém, possui **capacidade crítica inadequada de recuperação para violações de governança** (acessos inadequados, manipulações em transferências manuais, vazamentos) devido à **dependência de detecção manual reativa**.

O tempo entre violação e detecção pode ser semanas a meses, período durante o qual danos (exposição de informações, decisões baseadas em dados incorretos) são acumulados e tornam-se **irreversíveis**. A recuperação é eficaz quando o incidente é detectado rapidamente, mas **ineficaz quando a detecção é tardia** devido à ausência de monitoramento automatizado de conformidade com políticas de segregação e integridade.

O sistema não subsidia adequadamente o tratamento proativo de impactos - apenas possibilita resposta reativa após consumação do dano. Esta limitação é resultado de:

1. **Ausência de detecção automatizada** de violações de políticas de governança que dependem de contexto
2. **Dependência de auditoria manual esporádica** para identificação de violações
3. **Logs dispersos em múltiplas plataformas** sem correlação automatizada (sem SIEM)
4. **Vulnerabilidades arquiteturais** (permissões amplas, transferências manuais sem validação) que tornam violações difíceis de detectar
5. **Falta de processos sistêmicos** de auditoria periódica (atualmente não implementados regularmente)

Para um sistema de missão crítica de governança de portfólio, esta dependência de detecção reativa tardia é **inaceitável** e representa **risco significativo** de danos irreversíveis (vazamento de informações estratégicas, aprovações baseadas em documentação corrompida, perda de integridade de baselines).Tentar novamente

---

### 5.4.3 RNF-03 — Rastreabilidade

&emsp; Esta seção aprofunda a análise de causa e impacto em relação ao requisito não funcional de rastreabilidade.

#### Causas e Impactos da Quebra de Rastreabilidade

&emsp; A principal causa da quebra de rastreabilidade reside no **Processo Manual Não Auditado** (transferência de dados entre ferramentas) e na **Arquitetura de Dados Fragmentada** (silos de informação sem conexão), conforme detalhado na seção 5.2.3.

| Causa Raiz (Vulnerabilidade)                                             | Cenário de Falha (Gatilho)                                                                                                | Impacto no Negócio (Consequência)                                                                                                                                                                                                                                 |
| :----------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Processo Manual Não Auditado** (Transferência Miro/Excel → SharePoint) | Um usuário comete um erro (acidental ou intencional) ao copiar dados para o SharePoint (Etapa 2).                         | **Corrupção Silenciosa de Dados:** Decisões estratégicas são tomadas com base em informações incorretas, sem que ninguém perceba a falha. **Impacto:** Risco de investimentos equivocados e perda de credibilidade do PMO perante a diretoria.                    |
| **Arquitetura de Dados Fragmentada** (Silos de Logs)                     | Um auditor solicita a trilha de auditoria completa de um indicador de desempenho, desde sua origem até o relatório final. | **Impossibilidade de Auditoria e Conformidade:** A equipe de TI é incapaz de fornecer uma trilha de auditoria ponta a ponta. **Impacto:** Falha em atender a requisitos de governança interna e risco de não conformidade com regulações futuras.                 |
| **Ausência de ID de Correlação**                                         | Ocorre uma inconsistência de dados em um relatório do Power BI (Etapa 5) e é necessário encontrar a causa raiz.           | **Diagnóstico Ineficiente e Custo Operacional Elevado:** A equipe gasta horas ou dias em uma investigação manual, entrevistando pessoas e cruzando logs. **Impacto:** Alto custo de suporte (horas/homem) e lentidão na resolução de problemas críticos de dados. |

#### Detalhamento da Quebra de Nível de Serviço

&emsp; A quebra do nível de serviço (SLA) de rastreabilidade não se manifesta como uma falha sistêmica (erro 404 ou 500), mas sim pela **incapacidade do sistema de garantir a integridade e a proveniência dos dados que ele fornece**, o que é uma falha crítica para um sistema de registro.

- **Quebra por Integridade:** O sistema armazena e apresenta dados que podem ter sido corrompidos durante a entrada manual, tratando-os como informações válidas e confiáveis.
- **Quebra por Auditabilidade:** O sistema é incapaz de responder a perguntas fundamentais de auditoria, como "Quem alterou este valor e quando, durante a transição do Miro para o SharePoint?" ou "Qual a origem deste dado no relatório?".

&emsp;O impacto direto é a **erosão da confiança nos dados**, o que compromete a função primária do sistema de Portfólio: fornecer uma visão única e verdadeira sobre os projetos estratégicos do Metrô.

#### Como recuperar/subsidiar o tratamento de impactos

&emsp; Esta seção detalha os procedimentos e componentes (ou a falta deles) usados para subsidiar o tratamento de falhas causadas pela quebra de rastreabilidade, focando na **justificativa** para a necessidade de mudança.

| Componente/Procedimento           | Descrição Detalhada                                                                                                                                                                                                              | Justificativa da Inadequação (Racional para a Nova Arquitetura)                                                                                                                                                                                                                                                         |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Registro de Falhas (Subsídio)** | **Logs de Auditoria do SharePoint:** O log registra que uma alteração foi feita com sucesso por um usuário autorizado, mas não tem o contexto da transação de negócio (ex: "transferência de dados do Miro").                    | O log **registra uma operação técnica, não uma transação de negócio**. Ele subsidia a informação de "quem alterou no SharePoint", mas é insuficiente para uma **análise de causa raiz (RCA)**, pois a origem da informação (Miro/Excel) é desconhecida.                                                                 |
| **Procedimento de Recuperação**   | **Investigação Manual e Correção Direta:** A equipe de TI ou o PMO deve (1) identificar a inconsistência, (2) entrevistar os envolvidos para tentar descobrir a origem do erro, e (3) corrigir o dado diretamente no SharePoint. | **Alto MTTR e Risco de Perpetuar Erros:** O procedimento é lento, não confiável e depende da memória humana. A correção manual é, em si, outra transação sem rastreabilidade de negócio, o que agrava o problema de governança e não garante a integridade a longo prazo.                                               |
| **Componentes de Recuperação**    | **Nenhum Mecanismo Arquitetural:** Não existem componentes como _versionamento de dados com justificativa de negócio_, _rollback_ de transações ou um _log de imutabilidade_ que conecte as diferentes etapas do fluxo.          | **Vulnerabilidade Crítica de Governança:** A ausência de um mecanismo de recuperação auditável significa que a **integridade dos dados históricos não pode ser garantida**. A nova arquitetura deve introduzir um **ponto de ingestão transacional e auditável** que registre a linhagem de cada dado desde sua origem. |

&emsp; Sendo assim, o sistema AS-IS não é auditável, sendo necessário o redesenho da arquitetura para garantir a rastreabilidade de ponta a ponta.

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

#### B. Saída

#### C. Controle do RNF

### 6.2.2 RNF-02 — <Segurança>

#### A. Entrada

&nbsp; O sistema novo de gerenciamento de projetos do Metrô de São Paulo deve controlar rigorosamente os dados e transações de entrada, assegurando confiabilidade, confidencialidade e integridade desde o ponto inicial de acesso. Detalhes importantes incluem:

- Tentativas de Login:
&nbsp;Todas as tentativas de autenticação, incluindo sucesso, falhas, bloqueios temporários e uso de MFA, serão registradas. O sistema preverá limites máximos para tentativas mal-sucedidas para mitigar ataques de força bruta e evitar bloqueios indevidos. Controles adaptativos poderão bloquear acessos de localizações ou dispositivos suspeitos.

- Chamadas Autenticadas:
&nbsp;APIs do sistema aceitarão somente chamadas autenticadas com tokens válidos emitidos após autorização adequada. Tokens terão validade limitada e sofrerão renovação e revogação automatizadas em caso de anomalias.

- Volume de Queries e Usuários:
&nbsp;O sistema é dimensionado para suportar, com baixa latência, um volume médio de 40 a 60 usuários simultâneos em operação contínua e picos até 100 simultâneos, sem perda de desempenho ou degradação dos controles de segurança. As consultas são sujeitas a limites para evitar negação de serviço por abuso.

- Validação e Verificação de Dados:
&nbsp;Toda inserção ou modificação em documentos, cronogramas e formulários passa por validações automáticas para garantir formatos corretos, integridade semântica e ausência de alterações não autorizadas, incluindo identificação e bloqueio de transações suspeitas.

- Detecção Precoce e Bloqueio de Acessos Indevidos:
&nbsp;Mecanismos proativos atuarão para identificar padrões de comportamento anômalo já nas fases iniciais (ex.: tentativas sequenciais de acesso a recursos não autorizados), garantindo medidas instantâneas de bloqueio, isolamento e alerta.

#### B. Saída

&nbsp;A saída do sistema novo demonstra ganhos significativos em segurança e rastreabilidade, visíveis por meio dos registros produzidos:

- Logs Detalhados e Imutáveis:
&nbsp;Todas as ações realizadas dentro do sistema, desde autenticações até modificações em documentos e uso de agentes de IA, geram entradas de log criptografadas, armazenadas em local seguro e protegido contra adulterações. Estes logs suportam auditorias internas e externas com total transparência.

- Transações Fraudulentas/Bloqueadas:
&nbsp;Eventos como tentativas de login não autorizadas, ataques de negação de serviço, uso de credenciais inválidas e acessos a áreas restritas são categorizados com detalhamento suficiente para investigação posterior e possibilitam bloqueio automático e revogação imediata de sessões ou permissões.

- Correlação e Contextualização de Eventos:
&nbsp;O sistema integra dados de múltiplos módulos (portal usuário, agentes de IA, base documental) permitindo cruzar eventos para identificar tentativas multifacetadas de comprometimento, reforçando a segurança por meio da análise combinada.

- Indicadores de Segurança:
&nbsp;Relatórios e dashboards em tempo real exibem métricas sobre volumes de acesso, tentativas bloqueadas, status das sessões e padrões de uso, permitindo que equipes de segurança ajustem políticas e verifiquem a eficácia dos controles implantados.
#### C. Controle do RNF

&nbsp;O controle do requisito RNF-02 assegura a robustez da segurança por meio de um ecossistema integrado de políticas, mecanismos técnicos e procedimentos operacionalizados:

- Políticas de Controle de Acesso:
&nbsp;Estabelecem regras claras para concessão, revisão e revogação de acessos, com segregação de funções e perímetros definidos, compatíveis com a criticidade dos dados e operações. Revisões periódicas garantem alinhamento atempado às mudanças organizacionais e de perfil.

- Autenticação Robusta e Autorização Dinâmica:
&nbsp;Implementação obrigatória de MFA para acessos sensíveis, aplicação rigorosa de RBAC e ABAC, com adaptações contextuais em tempo real para ajuste fino das permissões.

- Criptografia End-to-End:
&nbsp;Dados são protegidos durante todo o ciclo - desde a transmissão via canais TLS até o armazenamento com chaves gerenciadas, neutralizando riscos de interceptação, acesso físico indevido e vazamento.

- Monitoramento Contínuo e Alarmes:
&nbsp;Sistemas de SIEM recebem inputs contínuos dos módulos de registro, análise e alerta, assegurando resposta rápida a incidentes, com workflows automatizados para investigação, bloqueio e mitigação.

- Processos e Workflows de Aprovação:
&nbsp;Implementação de procedimentos sistêmicos para validação formal de alterações em documentos e dados sensíveis, garantindo que somente ações aprovadas sejam efetivadas no sistema.

- Capacitação e Sensibilização:
&nbsp;Incluem treinamentos periódicos aos usuários para reforçar boas práticas, reconhecer tentativas de fraude e incentivar o reporte imediato de incidentes, fechando o ciclo de governança com foco no fator humano.

- Auditorias Regulares e Testes de Segurança:
&nbsp;Revisões de conformidade e testes periódicos (pentests e monitoramento de vulnerabilidades) garantem a manutenção dos níveis de segurança conforme requisitos legais e técnicos.

&nbsp;Dessa maneira, o sistema novo supera as fragilidades de segurança do modelo atual, oferecendo um ambiente confiável, auditável e resiliente, fundamental para a governança eficaz dos projetos do Metrô de São Paulo.


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

&nbsp;O monitoramento constante do requisito RNF-02 é crucial para manter a segurança e a integridade do sistema novo do Metrô. Para isso, será adotada a integração de múltiplas soluções e técnicas:

- Sistema SIEM (Security Information and Event Management): Coleta, centraliza e correlaciona logs e eventos de segurança provenientes de diversos componentes do sistema, tais como servidores de autenticação, gates de API, agentes de IA e subsistemas de armazenamento. A análise em tempo real permite identificar rapidamente tentativas de intrusão, acesso não autorizado ou ataques, automatizando alertas e medidas iniciais de contenção.

- Alertas e Relatórios do IAM: O sistema de gerenciamento de identidades e acessos gera notificações instantâneas em casos de tentativas suspeitas, como múltiplas falhas de login, acessos fora do perímetro definido, alterações abruptas de privilégios ou uso simultâneo indevido de contas.

- Firewall de Aplicação Web (WAF): Foca na proteção contra ataques direcionados às interfaces web da solução, filtrando requisições maliciosas, prevenindo injeção de código e garantindo que acessos indevidos sejam bloqueados no perímetro da aplicação.

- Monitoramento Comportamental por IA: Módulos inteligentes monitoram padrões de acesso e uso, identificando variações atípicas relacionadas a usuários e agentes, como acessos em horários incomuns, volumes anormais de dados e sequências fora do padrão, aumentando a precisão da detecção.

&nbsp;Essa arquitetura conjunta supera as limitações do sistema atual, que carece de componentes integrados de monitoramento, dificultando a identificação eficiente e o bloqueio de ameaças.
#### B. Como resolver o RNF (Preventivo e Reativo)

&nbsp;Para mitigar riscos e responder a incidentes, o sistema novo integra um conjunto robusto de componentes e estratégias:

- Preventivos:

  - Autenticação poderosa com MFA obrigatória para acessos sensíveis, evitando comprometimento por simples vazamento de senhas.

  - Implementação de RBAC e ABAC, permitindo controle fino e dinâmico sobre quem pode acessar o quê, baseado em função, contexto e atributos do usuário.

  - Criptografia forte (TLS 1.2+ para dados em trânsito e AES-256 para dados armazenados) garantindo que informações estejam protegidas contra interceptação e vazamento.

  - Validação e sanitização rigorosas para prevenir injeções e manipulações maliciosas.

  - Versionamento automático em documentos críticos, permitindo rastreamento e reversão de alterações.

- Reativos:

  - Detecção automática de anomalias baseada em inteligência artificial, com identificação precoce de tentativas de fraude, uso irregular de credenciais e comportamentos fora do padrão.

  - Contenção automática de ameaças, como bloqueio temporário ou permanente de contas suspeitas, isolamento de sessões comprometidas e restrição de privilégios.

  - Revogação rápida de sessões de usuários ou agentes que apresentem risco, garantindo o corte imediato do acesso não autorizado.

  - Notificações em tempo real para equipe de segurança, permitindo resposta rápida e eficaz a incidentes.

#### C. Como recuperar/subsidiar o tratamento de impactos

&nbsp;Para minimizar os impactos após incidentes, o sistema conta com procedimentos claros e estruturados:

- Auditoria detalhada e análise forense: A partir dos logs imutáveis centralizados e das correlações do SIEM, é possível identificar os responsáveis, os vetores da invasão e os dados afetados, suportando ações legais e correções eficazes.

- Recuperação de dados e versões: Utilização de backups regulares e mecanismos de versionamento que permitem restaurar estados anteriores ao incidente, mantendo a integridade das informações críticas.

- Comunicação transparente e controlada: Relatórios e notificações formais são gerados para os gestores do Metrô e áreas afetadas, detalhando o incidente e as medidas adotadas.

- Aperfeiçoamento contínuo: Aprendizado a partir dos incidentes para fortalecer políticas de segurança, melhorar detecção e respostas, atualizando processos e tecnologias.

- Testes periódicos: Exercícios simulados e testes de restauração são realizados para garantir que os planos de recuperação funcionem efetivamente, reduzindo o tempo de indisponibilidade.


&nbsp;A seção 6.3.2 RNF-02 reforça que a segurança do sistema novo será garantida por monitoramento integrado e contínuo, controles preventivos rigorosos e respostas rápidas a incidentes. Com o uso de SIEM, IAM, WAF e IA para análise comportamental, o sistema elimina as vulnerabilidades atuais, assegurando proteção, rastreabilidade e resiliência. O foco na recuperação ágil pós-incidente fecha o ciclo de segurança, garantindo governança eficaz e continuidade para os projetos do Metrô de São Paulo.

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
