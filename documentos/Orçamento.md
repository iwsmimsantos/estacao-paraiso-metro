# Orçamento do projeto

<div align="center">

[**ACESSO AO PDF DO ORÇAMENTO**](../documentos/img/Orçamento%20Projeto.pdf)

</div>

&emsp;Por se tratar de um planejamento financeiro para uma Prova de Conceito (POC), os valores estimados apresentam uma margem relevante de variação em relação ao custo final real. Assim, o objetivo central desta análise não é obter precisão numérica absoluta, mas sim demonstrar o raciocínio econômico por trás da composição de custos, permitindo compreender a lógica do valuation e a proporcionalidade entre os componentes da solução.

O propósito central deste orçamento não é obter precisão numérica absoluta, mas apresentar com clareza:
- A estrutura de custos do projeto
- A lógica de formação de preço
- A separação entre custos de pessoal, despesas operacionais e manutenção
- A aplicação de lucro e impostos
- O valor final a ser transmitido ao cliente

## Custos (pessoal)

Os cálculos consideram salários semanais (w), encargos e período total estimado de trabalho no projeto (10 semanas).

| Nome / Cargo                      | Quantidade | Salário Bruto (w) | INSS Patronal (≈20%) | FGTS (≈8%) | Outros Encargos (≈24,74%) | Período (w) | Total        |
| --------------------------------- | ---------- | ----------------- | -------------------- | ---------- | ------------------------- | ----------- | ------------ |
| Engenheiro de Software            | 2          | R$ 2.250,00       | R$ 450,00            | R$ 180,00  | R$ 556,65                 | 10          | R$ 68.733,00 |
| Engenheiro de IA / LLM Specialist | 2          | R$ 2.000,00       | R$ 400,00            | R$ 160,00  | R$ 494,80                 | 10          | R$ 61.096,00 |
| Data Analyst / BI                 | 1          | R$ 1.500,00       | R$ 300,00            | R$ 120,00  | R$ 371,10                 | 10          | R$ 22.911,00 |
| PM / Tech Lead                    | 1          | R$ 3.000,00       | R$ 600,00            | R$ 240,00  | R$ 742,20                 | 10          | R$ 45.822,00 |


**Total: R$ 129.829,00**

## Despesas operacionais

As despesas operacionais refletem custos indiretos associados ao uso de infraestrutura corporativa, energia, equipamentos e depreciação.
Seguindo práticas de TCO (Total Cost of Ownership), estimou-se 10% dos custos diretos.

| Item                                                                  | Descrição                                                                                                                 | Valor        | Qtd | Total        |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------ | --- | ------------ |
| Infraestrutura física, energia elétrica e depreciação de equipamentos | Uso compartilhado de redes, servidores, ativos e infraestrutura técnica. Estimativa de 10% dos custos diretos do projeto. | R$ 16.289,49 | 1   | R$ 16.289,49 |

**Total: R$ 16.289,49**

> Nota: Não foram incluídas despesas operacionais não recorrentes, pois a solução utiliza ferramentas, processos e licenças já existentes na organização.

## Margem de Lucro

Foi utilizada uma margem de lucro de 10% (0,1).


Essa taxa foi aplicada sobre o valor total da manutenção e serviu para:
- Cobrir riscos operacionais
- Absorver variabilidade de custos durante a execução
- Reforçar a sustentabilidade financeira do serviço
- Manter alinhamento com práticas de mercado para POCs com alta intensidade técnica

| Descrição        | Valor         |
| ---------------- | ------------- |
| Valor sem lucro  | R$ 146.118,49 |
| Lucro (%)        | 10%           |
| Valor com lucro  | R$ 160.730,34 |

## Impostos 

Para simplificar e manter alinhamento com modelos de precificação rápida utilizados em POCs corporativas, adotou-se um fator multiplicador de carga tributária de 0,85.

Ou seja, considera-se que, após impostos (PIS, COFINS, ISS, IRPJ, CSLL), a empresa retém aproximadamente 85% do valor bruto, o que corresponde a uma carga tributária aproximada de 15%.

Esse método:
- Não tenta calcular impostos individualmente (ISS, PIS, COFINS etc.)
- Evita depender do regime tributário específico da organização (Simples, Lucro Presumido, Lucro Real)
- Produz um número rápido e realista para fins de budgeting

| Descrição        | Valor         |
| ---------------- | ------------- |
| Valor com lucro  | R$ 160.730,34 |
| Imposto          | 0,85          |
| Valor com imposto  | R$ 189.094,52 |
| **Valor final a ser transmitido**  | R$ 189.094,52 |


## Custos de Manutenção

Custos recorrentes estimados para operação mensal da solução.

| Nome                                     | Valor Unitário | Quantidade | Total        |
| ---------------------------------------- | -------------- | ---------- | ------------ |
| Microsoft 365 Copilot (Licença)          | R$ 200,30      | 150        | R$ 30.045,00 |
| Sentinel – Ingestão de Logs (≈ 2 GB/mês) | R$ 390,00      | 2          | R$ 780,00    |
| Sentinel – Regras e Analytics            | R$ 150,00      | 1          | R$ 150,00    |
| Copilot – Uso estimado de IA             | R$ 0,01        | 30.000     | R$ 300,00    |
| App Service API – Plano B1               | R$ 290,93      | 1          | R$ 290,93    |
| Logs Analytics (≈ 2 GB/mês)              | R$ 0,05        | 30.000     | R$ 1.500,00  |

**Total: R$ 33.065,93**

Os valores de manutenção para o período de 10 semanas foram consolidados na seguinte tabela:

| Descrição        | Valor         |
| ---------------- | ------------- |
| Valor mensal  |  R$  33.065,93  |
| Período        | 2,5           |
| Total  | R$ 82.664,83 |
| Lucro (%) | 0,1 |
| Valor com lucro | R$ 90.931,31 |
| Imposto | 0,85 |
| Valor com imposto | R$ 106.978,01 |
| **Valor a ser transmitido** | R$ 106.978,01 |


