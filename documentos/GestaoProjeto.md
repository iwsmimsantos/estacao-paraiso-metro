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

- [1. Introdução](#1-introdução)
- [2. Avaliação das Sprints](#2-avaliação-das-sprints)
  - [2.1 Sprint 1](#21-sprint-1)
  - [2.2 Sprint 2](#21-sprint-2)
  - [2.3 Sprint 3](#21-sprint-3)
  - [2.4 Sprint 4](#21-sprint-4)
  - [2.5 Sprint 5](#21-sprint-5)
- [3. Tabelas de Acompanhamento](#3-tabelas-de-acompanhamento)
  - [Acompanhamento de Progresso](#acompanhamento-de-progresso---sprints-1234-e-5)
  - [Acompanhamento de Riscos](#acompanhamento-de-riscos---sprints-1234-e-5)
- [4. Análise Post Mortem](#5-análise-post-mortem)
  - [4.1 Sucessos do Projeto](#51-sucessos-do-projeto)
  - [4.2 Oportunidades de Melhoria](#52-oportunidades-de-melhoria)
  - [4.3 Lições Aprendidas](#53-lições-aprendidas)

# 1. Introdução

&emsp; O documento de gestão de projetos tem como objetivo definir e mapear boas práticas que apoiem o planejamento e o monitoramento das iniciativas, promovendo maior eficiência e colaboração entre os membros da equipe. Sua finalidade é orientar e padronizar as práticas de gestão, garantindo consistência e qualidade na condução do projeto.

# 2. Avaliação das Sprints

&emsp; A avaliação de desempenho do grupo ao longo das sprints tem como objetivo analisar a qualidade da organização, a eficiência operacional e a forma como as tarefas são distribuídas entre os integrantes. Durante esse processo, a equipe acompanha o uso do Trello como ferramenta de apoio, verificando os responsáveis por cada atividade, o tempo de execução e a categorização das tarefas em P (30 minutos), M (60 minutos) e G (120 minutos). Além disso, é fundamental avaliar a qualidade das entregas e a efetividade da comunicação entre os membros, assegurando o alinhamento constante entre planejamento e execução.

## Matriz de Risco do Projeto

| ID  | Risco                                | Probabilidade | Impacto | Severidade | Estratégia de Mitigação                       | Responsável  |
| --- | ------------------------------------ | ------------- | ------- | ---------- | --------------------------------------------- | ------------ |
| 1   | Atraso na entrega de tarefas         | Alta          | Alto    | Crítico    | Revisão semanal do cronograma e dailys        | Scrum Master |
| 2   | Falha na comunicação entre membros   | Média         | Médio   | Moderado   | Reuniões regulares e uso de canais oficiais   | Todos        |
| 3   | Problemas técnicos com ferramentas   | Média         | Alto    | Alto       | Treinamento e suporte técnico                 | DevOps       |
| 4   | Escopo mal definido                  | Baixa         | Alto    | Alto       | Revisão do escopo com o cliente               | PO           |
| 5   | Falta de engajamento dos integrantes | Baixa         | Médio   | Moderado   | Feedbacks constantes e acompanhamento         | Scrum Master |
| 6   | Mudanças de requisitos do cliente    | Média         | Alto    | Alto       | Documentação de mudanças e validação contínua | PO           |

## 2.1 Sprint 1

&emsp; A Sprint 1 foi definida como a base do projeto de integração de agentes de IA ao sistema de gestão de projetos do Metrô de São Paulo. O objetivo é criar uma arquitetura escalável que facilite o gerenciamento, garantindo disponibilidade, rastreabilidade e segurança dos dados.

---

### Pontos Fortes

- Discussões produtivas sobre a definição do projeto e entendimento do contexto do Metrô.
- Estruturação inicial da arquitetura escalável para integração de IA.
- Colaboração efetiva e engajamento dos integrantes.
- Agilidade na execução das primeiras tarefas.

### Pontos Fracos

- Dificuldade inicial em compreender a proposta de integração com sistemas existentes (Miro, SharePoint).
- Desafio em mapear requisitos específicos de rastreabilidade e segurança.
- Atrasos na disponibilização das ferramentas (Trello e GitHub), impactando o início do desenvolvimento.

---

### Requisitos Não Funcionais do Sistema Novo

1. **Disponibilidade:** O sistema deve estar disponível 99% do tempo, com monitoramento de falhas.
2. **Rastreabilidade:** Todas as ações realizadas no sistema devem ser registradas e auditáveis.
3. **Segurança:** Garantir autenticação, autorização e proteção dos dados dos projetos.
4. **Escalabilidade:** A arquitetura deve permitir fácil integração de novos agentes de IA e expansão de funcionalidades.

---

### Mapeamento dos Requisitos Não Funcionais para Melhorar o Sistema Atual

- Implementar monitoramento contínuo para garantir disponibilidade.
- Adotar logs detalhados e trilhas de auditoria para rastreabilidade.
- Reforçar políticas de segurança e controle de acesso.
- Estruturar a arquitetura para suportar crescimento e novas integrações.

### Ações de Melhoria Verificáveis

- Documentar decisões técnicas e fluxos de integração em um documento compartilhada.
- Estabelecer prazos curtos para revisão de código (PRs) e feedback.
- Padronizar o uso das ferramentas desde o início da sprint.

---

### Propostas de Melhoria para a Sprint 2

- Implementar reuniões de alinhamento semanal para garantir entendimento coletivo dos objetivos da sprint.
- Adotar checklist de requisitos de rastreabilidade e segurança para validação contínua com o cliente.
- Monitorar engajamento dos integrantes com feedbacks regulares.

## 2.2 Sprint 2

### **Acompanhamento de Progresso**

&emsp;A Sprint 2 teve como foco o mapeamento detalhado da arquitetura do estado atual do sistema de gestão de portfólio do Metrô e o início da especificação da arquitetura futura, com ênfase na definição de padrões arquiteturais que suportem a integração de agentes de IA. Mas além disso, foi pensado em possíveis simulações do sistema antigo e do sistema atual para que fosse possível identificar possíveis pontos de melhoria e medir os principais impactos.

---

#### Resumo de Mudanças da Matriz de Risco para Sprint 2:

- **Risco 1** (Atraso nas entregas): Probabilidade reduzida de Alta para Média devido ao SLA de 24h para revisões
- **Risco 2** (Comunicação): Probabilidade reduzida de Média para Baixa devido às dailys consistentes
- **Risco 4** (Escopo mal definido): Impacto reduzido de Alto para Médio após validações com cliente
- **6 novos riscos técnicos identificados** durante o mapeamento da arquitetura AS-IS e levantamento de requisitos

#### Riscos Críticos Priorizados para Sprint 3:

1. Risco 7 - Acesso às APIs do SharePoint
2. Risco 8 - Compatibilidade de segurança e compliance
3. Risco 12 - Sistemas legados não documentados

---

### Pontos Fortes da Sprint

- Colaboração efetiva da equipe para levantamento técnico do ambiente atual.
- Criação de diagramas C4 (contexto, containers e componentes) que facilitaram o entendimento da arquitetura existente.
- Identificação clara dos pontos de integração entre SharePoint, Power BI, Power Automate e Miro.
- Definição de padrões de segurança e rastreabilidade alinhados com as políticas de compliance do Metrô.
- Melhoria significativa no tempo de resposta das revisões de código (de 48h para 24h em média).

### Pontos Fracos

- Dificuldade inicial em obter informações detalhadas sobre as APIs do SharePoint utilizadas atualmente.
- Necessidade de mais sessões técnicas para compreender os fluxos do Power Automate existentes.
- Dificuldade com entender como poderiamos simular os testes da sprint.
- Desafio em entender como realizar a cadeia de markov com dados projetados pelo grupo.

---

### Entregas da Sprint

- Diagrama de Arquitetura com Modelo C4 explorando o contexto e os containers
- Táticas de arquitetura e identificação das principais vulnerabilidades
- Simulação dos principais requisitos não funcionais escolhidos pelo grupo no sistema atual e novo
- Atualização da matriz de riscos com novos riscos técnicos identificados.

---

### Propostas de Melhoria para a Sprint 3

- Criar planos de contingência (Planos B) para tasks críticas.
- Estabelecer revisões rápidas e contínuas de Pull Requests e tasks no Trello mantendo um prazo de 24 horas.
- Criar mais tasks individuais, diminuindo as dependencias.
- Garantir que todas as tasks estejam claras e detalhadas no Trello antes da execução.

### Ações de Melhoria Verificáveis

- Estabelecido prazo de 24h para revisão de PRs.
- Discussões semanais de 30 minutos com o grupo para validação continua de entendimento do projeto.
- 100% das tarefas no trello devem estar com DOR e DOD, além de uma descrição detalhada.

---

&emsp;Na Sprint 2 houve avanço significativo no entendimento técnico do ambiente atual e na definição de fundamentos arquiteturais. O engajamento com stakeholders técnicos do Metrô foi fundamental para qualidade das entregas. E para a Sprint 3, iremos focar em implementar e validar os mecanismos arquiteturais através de: codificação de testes automatizados com TDD, implementação dos componentes com documentação completa, execução e registro de testes não funcionais, avaliação de desempenho e riscos, e simulação do sistema em cenários normais, de exceção e limites para validar as melhorias.

## 2.3 Sprint 3

&emsp;A Sprint 3 foi mais curta e concentrou um volume maior de artefatos. A equipe reforçou o pareamento, replanejou o quadro do Trello diariamente e concentrou esforços nas histórias com maior dependência técnica para garantir que os componentes críticos e seus registros de teste fossem entregues dentro do ciclo.

#### Resumo de Mudanças da Matriz de Risco para Sprint 3:

- **Risco 1** voltou a ficar em evidência devido ao encurtamento da janela de entrega.
- **Risco 3** aumentou de Severidade Moderada para Alta após problemas no pipeline de automação.
- **Risco 7** manteve-se crítico e ganhou plano de contingência offline para testes.

_Por recomendação do último feedback, passamos a tabela de acompanhamento para uma nova seção: [Acompanhamento de Progresso](#acompanhamento-de-progresso---sprints-1234-e-5), e para os riscos: [Acompanhamento de Riscos](#acompanhamento-de-riscos---sprints-1234-e-5), evitando replicação de conteúdo_

---

### Pontos Fortes da Sprint

- Capacidade da equipe em absorver o escopo adicional mesmo com menos tempo, mantendo as entregas priorizadas.
- Integração contínua entre código, documentação e roteiros de teste, com atualizações simultâneas no repositório e no plano de evidências.
- Revisões assíncronas mais rápidas, permitindo feedback quase imediato e facilitando ajustes incrementais.
- Monitoramento diário do burn-down no Trello, reduzindo surpresas de última hora.

### Pontos Fracos

- Sobrecarga em membros durante a reta final da sprint, especialmente nas histórias com maior complexidade técnica.
- Dependência de dados e cenários de teste ainda incompletos, o que atrasou a confirmação de algumas hipóteses.
- Ajustes de escopo de última hora geraram retrabalho em tarefas de documentação e testes.
- Pouca folga para revisitar artefatos anteriores e garantir consistência narrativa entre as seções do relatório.

---

### Propostas de Melhoria para a Sprint 4

- Balancear alocação da equipe, distribuindo histórias críticas entre mais integrantes e prevendo pares alternados.
- Validar escopo detalhado de cada artefato antes do início da sprint, com checklist simples de critérios de aceite e dependências.
- Garantir que cada história tenha estimativa revisada e apontamento claro de quem revisa o quê, evitando gargalos no fim da semana.

### Ações de Melhorias

- Checkpoints de meio de sprint com checklist de completude (documentação + código + testes).
- Registro diário de impedimentos no Trello para facilitar acompanhamento pelo time.
- Revisão rápida de lições aprendidas ao término de cada história para alimentar o relatório da sprint.

---

&emsp;A Sprint 3 marcou a transição do foco analítico para um ciclo de entrega acelerada de artefatos. Apesar do tempo reduzido, priorizamos riscos críticos, mantivemos o controle do quadro e validamos a baseline arquitetural necessária para evoluir as implementações da próxima sprint.

## 2.4 Sprint 4

&emsp;A Sprint 4 foi marcada por um volume elevado de artefatos e por uma forte dependência sequencial entre as entregas. O que exigiu maior coordenação entre pares e atenção às dependências técnicas. Além disso, parte das descrições dos artefatos estava pouco explicativa no início da sprint, o que gerou dúvidas sobre escopo e critérios de aceite e demandou esforço adicional de refinamento.

---

### Pontos Fortes da Sprint

- Reorganização constante do Trello e Docs para respeitar a ordem lógica dos artefatos.
- Colaboração entre os integrantes para destravar dependências técnicas.
- Consolidação da baseline arquitetural e dos testes definidos nas sprints anteriores.
- Entregas alinhadas com os requisitos não funcionais prioritários (rastreabilidade, segurança e disponibilidade).

### Pontos Fracos

- Dificuldade na distribuição de tasks devido à alta linearidade entre os artefatos.
- Risco de sobrecarga em membros responsáveis por etapas “gatilho” da cadeia de artefatos.
- Descrições iniciais pouco detalhadas, gerando retrabalho em esclarecimentos e ajustes de escopo.
- Menor flexibilidade para trocas de responsável no meio da sprint, pela dependência entre atividades.

---

### Propostas de Melhoria para a Sprint 5

- Fatiar artefatos grandes em subtarefas mais independentes, reduzindo a linearidade extrema.
- Planejar caminhos alternativos de trabalho (histórias em paralelo) para evitar ociosidade quando uma task estiver bloqueada.
- Antecipar alinhamentos com professores e PO para validar expectativas de artefatos críticos antes do início da sprint.

### Ações de Melhoria Verificáveis

- Checklist de refinamento obrigatório (DOR) para cada artefato antes de entrar em “Em andamento”.
- Criação de subtarefas vinculadas no Trello para artefatos maiores, com responsáveis e dependências explícitas.
- Registro de bloqueios e dependências diretamente nas cards, facilitando a visualização pelo time.
- Sessão rápida de revisão de backlog no início da sprint com foco especial nos artefatos mais lineares.

## 2.5 Sprint 5

&emsp;A Sprint 5 representou a fase final de consolidação e entrega do projeto. O foco principal foi a finalização dos artefatos pendentes, a integração de todos os componentes desenvolvidos e a preparação da documentação final. A equipe demonstrou um **compreendimento aprofundado do projeto** e conseguiu realizar uma **distribuição equalitária das tarefas**, aproveitando as **habilidades específicas de cada membro** para otimizar a qualidade e a velocidade das entregas. No entanto, a pressão do prazo final e a necessidade de **maior alinhamento com os professores** foram os principais desafios a serem superados.

---

### Pontos Fortes da Sprint

- **Compreensão Aprofundada do Projeto:** A equipe atingiu um nível de maturidade técnica e de negócio, permitindo a tomada de decisões autônomas e a resolução eficiente de problemas complexos de entedimento do projeto, refletindo o conhecimento acumulado nas sprints anteriores.
- **Distribuição e Divisão Equalitária das Tasks:** O planejamento da Sprint 5 garantiu que a carga de trabalho fosse balanceada, evitando a sobrecarga de membros específicos (problema da Sprint 4) e promovendo a responsabilidade compartilhada, o que contribuiu para a moral da equipe.
- **Alinhamento por Habilidade:** As tarefas foram alocadas de forma estratégica, permitindo que cada membro trabalhasse em áreas onde possuía maior proficiência, o que resultou em maior qualidade e menor tempo de execução para os artefatos finais.

### Pontos Fracos

- **Prazos:** A reta final do projeto exigiu um esforço concentrado, e a gestão do tempo para as últimas entregas foi um ponto de estresse, indicando a necessidade de maior folga no planejamento de sprints finais em projetos futuros.
- **Alinhamento com Professores:** A necessidade de validações finais e esclarecimentos de escopo em momentos críticos da sprint evidenciou a importância de sessões de alinhamento mais frequentes e estruturadas com professores para evitar gargalos de validação.
- **Qualidade das Dailys:** Com a alta demanda de trabalho e a proximidade da entrega, as reuniões diárias (dailys) perderam um pouco de sua qualidade e foco, tornando-se mais um reporte de status do que um momento de identificação e destravamento de impedimentos.

---

### Propostas de Melhoria para Próximos Passos (Lições Aprendidas)

- **Reforçar a Gestão de Tempo:** Implementar um planejamento de tempo melhor para as últimas sprints de projetos futuros, considerando a complexidade da integração final e da documentação.
- **Estruturar Alinhamentos Externos:** Definir um canal e frequência específicos para alinhamento com _stakeholders_ externos (professores/clientes) para evitar gargalos de validação em momentos críticos.
- **Otimizar a Daily:** Retomar o foco da _daily_ como ferramenta de identificação de impedimentos e não apenas de status, garantindo que sejam curtas, objetivas e focadas em "o que me impede de avançar".

### Ações de Melhoria Verificáveis (Implementadas na Sprint 5)

- **Foco no Destravamento:** As _dailys_ foram direcionadas para focar em bloqueios e dependências, otimizando o tempo da equipe.
- **Revisão Cruzada de Documentação:** Implementação de uma revisão cruzada final de todos os artefatos de documentação para garantir consistência narrativa e técnica.
- **Uso de Habilidades Específicas:** Alocação de tarefas finais (como formatação e revisão de código) baseada nas habilidades mais fortes de cada membro para garantir a máxima qualidade na entrega.

---

&emsp;A Sprint 5 foi concluída com sucesso, marcando a entrega final do projeto. O alto nível de colaboração e o entendimento técnico consolidado foram cruciais para superar os desafios de prazo. As lições aprendidas sobre gestão de tempo e alinhamento externo serão fundamentais para o planejamento de projetos futuros.

# 3. Tabelas de Acompanhamento:

## Acompanhamento de Progresso - Sprints 1,2,3,4 e 5

Tabela para acompanhamento dos pontos de melhora e estresse.

| Aspecto                        | Sprint 1                               | Sprint 2                     | Sprint 3                                                  | Sprint 4                                                                 | Sprint 5                                                               |
| :----------------------------- | :------------------------------------- | :--------------------------- | :-------------------------------------------------------- | :----------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| **Pontualidade**               | Ponto de melhora (demora nas revisões) | Melhorou, prazos cumpridos   | Pressionada: ajustes diários para caber no tempo reduzido | Desafiada pelo alto número de artefatos e dependências sequenciais       | Agenda apertada na reta final, mas entregas concluídas                 |
| **Priorização das tasks**      | Funcionou bem                          | Mantido o padrão             | Replanejada diariamente para focar artefatos críticos     | Focada em destravar cadeias lineares e artefatos “gatilho”               | Priorização absoluta das entregas finais e documentação                |
| **Divisão de tarefas**         | Livre e incentivou autonomia           | Mais estruturada             | Pareamento intenso para acelerar entregas                 | Dificultada pela alta linearidade entre artefatos e dependências fortes  | Distribuição equalitária e alinhamento por habilidade                  |
| **Dailys**                     | Produtivas e bem aproveitadas          | Consistentes                 | Curtas e objetivas, focadas em bloqueios                  | Utilizadas para realinhar dependências e replanejar a sequência de tasks | Perda de qualidade e foco, perdendo um pouco do reporte de status      |
| **Revisões (PRs)**             | Demora nas revisões                    | Agilizadas com limite de 24h | Realizadas em até 12h com revisão cruzada                 | Mantidas rápidas para não bloquear cadeias de artefatos                  | Revisão cruzada final de documentação e código                         |
| **Apresentação Sprint Review** | Bem planejada e estruturada            | Técnica e objetiva           | Centrada no protótipo funcional e evidências de testes    | Focada em mostrar o conjunto de artefatos e sua interdependência         | Foco na apresentação completa do projeto e resultados                  |
| **Validação com professores**  | Ótimo, ponto a ser mantido             | Feedbacks incorporados       | Sessões rápidas para validar entregáveis                  | Reforçada para esclarecer escopo de artefatos com descrição pouco clara  | Necessidade de maior alinhamento estruturado em momentos críticos      |
| **Documentação**               | Bem elaborada                          | Diagramas adicionados        | Atualizada em paralelo ao desenvolvimento                 | Ajustada para detalhar melhor os artefatos e suas relações               | Bem elaborada, com revisão final para consistência narrativa e técnica |
| **Sugestões implementadas**    | Identificadas                          | 80% implementadas            | 100% das críticas aplicadas antes da review final         | Foco em tornar descrições mais explicativas e reduzir retrabalho         | Todas as sugestões e lições aprendidas incorporadas                    |
| **Riscos**                     | Definidos na Matriz de Risco           | Atualizados e monitorados    | Repriorizados com foco nos riscos 7, 8 e 12               | Acompanhados com foco em atrasos por dependência e clareza de escopo     | Riscos críticos controlados e projeto entregue                         |

## Acompanhamento de Riscos - Sprints 1,2,3,4 e 5

Tabela para acompanhamento do desenvolvimento dos riscos.

| ID  | Risco                                             | Sprint 1                                                                                                                               | Sprint 2                                                                                                                                                                        | Sprint 3                                                                                                                                                                        | Sprint 4                                                                                                                                                                           | Sprint 5                                                                                                                                                                               |
| --- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Atraso na entrega de tarefas                      | **Probabilidade:** Alta · **Impacto:** Alto · **Severidade:** Crítico · **Estratégia:** Revisão semanal do cronograma e dailys         | **Probabilidade:** Média · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Revisão semanal do cronograma e dailys · **Status:** Mitigado                             | **Probabilidade:** Média · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Replanejamento diário focado em dependências críticas · **Status:** Ativo                 | **Probabilidade:** Média · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Fatiamento de artefatos e controle de cadeia linear · **Status:** Em monitoramento           | **Probabilidade:** Baixa · **Impacto:** Alto · **Severidade:** Moderado · **Estratégia:** Distribuição equalitária de tasks e foco em habilidades · **Status:** Mitigado/Encerrado     |
| 2   | Falha na comunicação entre membros                | **Probabilidade:** Média · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Reuniões regulares e uso de canais oficiais | **Probabilidade:** Baixa · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Reuniões regulares e uso de canais oficiais · **Status:** Controlado                 | **Probabilidade:** Baixa · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Quadros digitais e checkpoints assíncronos · **Status:** Controlado                  | **Probabilidade:** Baixa · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Dailys usadas para esclarecer descrições pouco explicativas · **Status:** Controlado    | **Probabilidade:** Baixa · **Impacto:** Baixo · **Severidade:** Baixo · **Estratégia:** Compreensão aprofundada do projeto e alinhamento por habilidade · **Status:** Encerrado        |
| 3   | Problemas técnicos com ferramentas                | **Probabilidade:** Média · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Treinamento e suporte técnico                    | **Probabilidade:** Média · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Treinamento e suporte técnico · **Status:** Ativo                                         | **Probabilidade:** Média · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Ambiente replicado em containers e playbooks rápidos · **Status:** Ativo                  | **Probabilidade:** Média · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Reuso do ambiente e automação de rotinas críticas · **Status:** Ativo                        | **Probabilidade:** Baixa · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Estabilização do ambiente e entrega final · **Status:** Encerrado                           |
| 4   | Escopo mal definido                               | **Probabilidade:** Baixa · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Revisão do escopo com o cliente                  | **Probabilidade:** Baixa · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Revisão do escopo com o cliente · **Status:** Mitigado                               | **Probabilidade:** Baixa · **Impacto:** Alto · **Severidade:** Moderado · **Estratégia:** Refinamento conjunto PO + Professores antes de cada artefato · **Status:** Controlado | **Probabilidade:** Média · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Refinamento de descrições e checklists de DOR para artefatos lineares · **Status:** Ativo    | **Probabilidade:** Baixa · **Impacto:** Baixo · **Severidade:** Baixo · **Estratégia:** Compreensão aprofundada do projeto e alinhamento final com professores · **Status:** Encerrado |
| 5   | Falta de engajamento dos integrantes              | **Probabilidade:** Baixa · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Feedbacks constantes e acompanhamento       | **Probabilidade:** Baixa · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Feedbacks constantes e acompanhamento · **Status:** Controlado                       | **Probabilidade:** Baixa · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Rotação de papéis críticos e lições por responsável · **Status:** Controlado         | **Probabilidade:** Baixa · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Pareamento em artefatos-chave para manter engajamento · **Status:** Controlado          | **Probabilidade:** Baixa · **Impacto:** Baixo · **Severidade:** Baixo · **Estratégia:** Distribuição equalitária e alinhamento por habilidade · **Status:** Encerrado                  |
| 6   | Mudanças de requisitos do cliente                 | **Probabilidade:** Média · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Documentação de mudanças e validação contínua    | **Probabilidade:** Média · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Documentação de mudanças e validação contínua · **Status:** Ativo                         | **Probabilidade:** Média · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Registro de hipóteses e confirmação rápida · **Status:** Ativo                            | **Probabilidade:** Média · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Validação antecipada de mudanças que afetem múltiplos artefatos · **Status:** Ativo          | **Probabilidade:** Baixa · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Congelamento de escopo para entrega final · **Status:** Encerrado                           |
| 7   | Dificuldade de acesso às APIs do SharePoint       |                                                                                                                                        | **Probabilidade:** Alta · **Impacto:** Alto · **Severidade:** Crítico · **Estratégia:** Sessões de entendimento com equipe do Metrô e documentação Microsoft · **Status:** Novo | **Probabilidade:** Alta · **Impacto:** Alto · **Severidade:** Crítico · **Estratégia:** Cache de testes offline · **Status:** Ativo                                             | **Probabilidade:** Alta · **Impacto:** Alto · **Severidade:** Crítico · **Estratégia:** Planejamento de janelas específicas para testes de integração · **Status:** Ativo          | **Probabilidade:** Baixa · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Testes de integração finalizados e artefatos entregues · **Status:** Encerrado              |
| 8   | Incompatibilidade entre requisitos de segurança   |                                                                                                                                        | **Probabilidade:** Média · **Impacto:** Crítico · **Severidade:** Crítico · **Estratégia:** Workshop com equipe de compliance e segurança da informação · **Status:** Novo      | **Probabilidade:** Média · **Impacto:** Crítico · **Severidade:** Crítico · **Estratégia:** Checklist atualizado e apoio do compliance · **Status:** Ativo                      | **Probabilidade:** Média · **Impacto:** Crítico · **Severidade:** Crítico · **Estratégia:** Revisão de artefatos de segurança em cadeia antes da entrega final · **Status:** Ativo | **Probabilidade:** Baixa · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Validação final de compliance e entrega do projeto · **Status:** Encerrado                  |
| 9   | Complexidade dos fluxos do Power Automate         |                                                                                                                                        | **Probabilidade:** Média · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Mapeamento detalhado e sessões com usuários-chave · **Status:** Novo                 | **Probabilidade:** Média · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Documentação lado a lado (AS-IS x TO-BE) e playback com usuários · **Status:** Ativo      | **Probabilidade:** Média · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Alinhamento dos fluxos com a sequência de artefatos planejada · **Status:** Ativo            | **Probabilidade:** Baixa · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Fluxos de automação finalizados e documentados · **Status:** Encerrado                      |
| 10  | Limitações técnicas do ambiente Microsoft         |                                                                                                                                        | **Probabilidade:** Baixa · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** POCs antecipados e consulta com especialistas Microsoft · **Status:** Novo                | **Probabilidade:** Baixa · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Testes em ambientes espelho · **Status:** Controlado                                      | **Probabilidade:** Baixa · **Impacto:** Alto · **Severidade:** Alto · **Estratégia:** Reuso dos ambientes de teste configurados nas sprints anteriores · **Status:** Controlado    | **Probabilidade:** Baixa · **Impacto:** Baixo · **Severidade:** Baixo · **Estratégia:** Estabilização do ambiente e entrega final · **Status:** Encerrado                              |
| 11  | Dependência de disponibilidade da equipe do Metrô |                                                                                                                                        | **Probabilidade:** Média · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Agendamento antecipado · **Status:** Novo                                            | **Probabilidade:** Média · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Plano alternativo · **Status:** Ativo                                                | **Probabilidade:** Média · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Antecipação de reuniões para artefatos críticos em cadeia · **Status:** Ativo           | **Probabilidade:** Baixa · **Impacto:** Baixo · **Severidade:** Baixo · **Estratégia:** Validações finais concluídas e projeto entregue · **Status:** Encerrado                        |
| 12  | Integração com sistemas legados não documentados  |                                                                                                                                        | **Probabilidade:** Alta · **Impacto:** Crítico · **Severidade:** Crítico · **Estratégia:** Documentação progressiva · **Status:** Novo                                          | **Probabilidade:** Alta · **Impacto:** Crítico · **Severidade:** Crítico · **Estratégia:** Automação de coleta de logs · **Status:** Ativo                                      | **Probabilidade:** Alta · **Impacto:** Crítico · **Severidade:** Crítico · **Estratégia:** Consolidação dos registros de integração nos artefatos da sprint                        | **Probabilidade:** Baixa · **Impacto:** Médio · **Severidade:** Moderado · **Estratégia:** Integração finalizada e documentada · **Status:** Encerrado                                 |

---

# 4. Análise Post Mortem

_conteúdo_

## 4.1 Sucessos do Projeto

_conteúdo_

## 4.2 Oportunidades de Melhoria

_conteúdo_

## 4.3 Lições Aprendidas
