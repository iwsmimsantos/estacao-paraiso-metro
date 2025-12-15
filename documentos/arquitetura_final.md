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

incluir Sumário

# Storytelling de Dados da Arquitetura do Sistema Novo

Este documento consolida a **evolução arquitetural do sistema**, narrando como o projeto evoluiu ao longo das sprints — das motivações iniciais até os resultados medidos.  
O foco é evidenciar o **racional de decisões**, os **Requisitos Não Funcionais (RNFs)** controlados e os **impactos observados** com a nova arquitetura.

> _As evidências podem incluir imagens, vídeos, gráficos, simulações, slides ou outros artefatos multimídia, sempre considerando a audiência técnica e executiva (Inteli e parceiro externo)._

---

## 1. Business Drivers

_(Apresente o contexto e as motivações de negócio que originaram o projeto e direcionaram a evolução do sistema.)_

- **Cenário do sistema atual:** _(Descreva brevemente o ponto de partida e os desafios enfrentados.)_
- **Evidências:** _(Inclua prints, diagramas ou dados que ilustrem os desafios de crescimento, escalabilidade ou segurança.)_
- **Pitch:** _(Resuma como os business drivers justificaram a necessidade de evolução arquitetural.)_

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

_(Mostre o processo de escolha dos RNFs mais críticos e o porquê dessa priorização.)_

- **RNFs selecionados:** _(Descreva os requisitos críticos abordados.)_
- **Critérios de seleção:** _(Explique as motivações para o foco em determinados RNFs — desempenho, tolerância a falhas, privacidade, etc.)_
- **Evidências e pitch:** _(Apresente gráficos, métricas iniciais e decisões de foco.)_

---

## 4. Simulação do Sistema Atual

_(Apresente evidências do comportamento do sistema antes da evolução.)_

- **Cenários simulados:** _(Descreva os experimentos realizados e os resultados observados.)_
- **Evidências:** _(Inclua gráficos de desempenho, diagramas de arquitetura antiga, logs ou resultados de simulação.)_
- **Pitch:** _(Resuma o que a equipe aprendeu com essa simulação e quais vulnerabilidades foram identificadas.)_

---

## 5. Decisões Arquiteturais e Simulação do Novo Sistema

_(Mostre como as decisões arquiteturais foram implementadas e simuladas no novo contexto.)_

- **Táticas e decisões aplicadas:** _(Liste as principais decisões e o racional por trás delas.)_
- **Evidências:** _(Inclua diagramas atualizados, prints de execução, simulações ou comparativos.)_
- **Pitch:** _(Explique como as novas táticas se traduziram em ganhos mensuráveis.)_

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
