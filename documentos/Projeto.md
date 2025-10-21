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
Incluir Sumário

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

### Business Drivers e Finalidade Baseada em Dados
- **Setor de aplicação:** _(Informe o(s) setor(es) ou domínio(s) de atuação do sistema.)_
- **Adição de valor:** _(Explique como o sistema agrega valor ao negócio ou aos usuários.)_
- **Processos de negócio e fluxos críticos suportados:**  
  _(Descreva os fluxos de negócio suportados e o papel do sistema nesses fluxos. Inclua diagramas, fluxogramas ou tabelas se necessário.)_
- **Volumes operacionais:**  
  _(Informe dados quantitativos como número de usuários, transações, registros, incidentes ou falhas relevantes.)_
- **Estratégias de crescimento:**  
  _(Explique planos ou estratégias de evolução do sistema frente aos desafios identificados.)_

---

## 2.2 Riscos e Oportunidades
_(Identifique riscos e oportunidades associados ao sistema atual, considerando aspectos técnicos, de negócio e legais.)_

### Matriz de Riscos
_(Insira aqui uma tabela com probabilidade × impacto dos riscos identificados.)_

### Riscos ligados ao sistema
_(Liste vulnerabilidades técnicas, de negócio ou de conformidade legal observadas no sistema.)_

### Oportunidades de melhoria dos SLAs
_(Descreva possibilidades de aprimorar níveis de serviço, incluindo segurança, disponibilidade, desempenho e tolerância a falhas.)_

---

# 3. Visão de Modelo Comportamental (Simulação do Sistema Atual)

Esta seção deve apresentar a **modelagem comportamental** do sistema atual e os **experimentos de simulação** realizados para observar seu comportamento frente a cenários críticos, especialmente aqueles relacionados a **Requisitos Não Funcionais (RNFs)**, como desempenho, segurança, privacidade e tolerância a falhas.

---

## 3.1 Estrutura Estática do Modelo
_(Apresente os elementos e parâmetros da simulação, evidenciando como o modelo representa o comportamento do sistema atual.)_

- **Elementos do sistema envolvidos nos RNFs selecionados:**  
  _(Liste os componentes, módulos, serviços ou processos do sistema que serão considerados na simulação, e associe-os aos RNFs analisados.)_

- **Estrutura e conexões entre os elementos:**  
  _(Descreva as relações entre os componentes simulados e justifique a escolha dos parâmetros de simulação. Pode incluir diagramas, fluxos de dados, filas, threads e elementos paralelos de processamento.)_

---

## 3.2 Modelagem Comportamental e Simulação dos RNFs
_(Descreva os cenários de simulação definidos, os dados utilizados, as execuções realizadas e os resultados obtidos.)_

- **Cenários de simulação:** _(Liste os cenários e parâmetros simulados.)_  
- **Dados e evidências:** _(Apresente os registros de simulação e as métricas observadas.)_

---

## 3.3 Consolidação dos Resultados da Simulação
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

## 4.2 Justificativas e Melhorias Esperadas
_(Apresente a argumentação técnica e de negócio para os RNFs selecionados, evidenciando os ganhos projetados para o novo sistema.)_

- **Controle de riscos e mitigação:** _(Explique como o novo sistema corrige os problemas identificados no atual.)_  
- **Melhorias em usabilidade e experiência:** _(Descreva ganhos esperados de eficiência e confiabilidade.)_  
- **Indicadores e evidências de melhoria:** _(Liste métricas que poderão comprovar os resultados esperados.)_

---

## 4.3 Consolidação dos Requisitos e Diretrizes para a Nova Arquitetura
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

