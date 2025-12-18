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


Esta documentação está organizada em diferentes arquivos e pastas. Use esta página como índice para navegar entre os artefatos de negócio, arquitetura e código.

## Documentos de Gestão do Projeto

- **Gestão do Projeto**  
  - [`GestaoProjeto.md`](./GestaoProjeto.md) – Planejamento, escopo, cronograma, stakeholders e acompanhamento das sprints.  
  - [`GestaoConfiguracao.md`](./GestaoConfiguracao.md) – Processo de gestão de configuração, versionamento, controle de mudanças e baseline dos artefatos.  
  - [`Orçamento.md`](./Orçamento.md) – Premissas, estimativas e análise de viabilidade econômica/financeira do projeto.

## Processo de Desenvolvimento de Software

- **Padrões e Processo**  
  - [`GuiaPadroesDesenvolvimento.md`](./GuiaPadroesDesenvolvimento.md) – Convenções de código, boas práticas, estrutura de pastas e padrões adotados no desenvolvimento.  

## Arquitetura, Storytelling e Modelagem

- **Storytelling Arquitetural**  
  - [`Projeto.md`](./Projeto.md) – Documento principal de arquitetura: contexto de negócio, descrição do sistema atual, requisitos, modelagem de RNFs, simulações (Capítulo 7) e storytelling da evolução arquitetural.  
  - [`arquitetura_final.md`](./arquitetura_final.md) – Storytelling final focado na evolução da arquitetura, decisões tomadas, evidências de simulação e métricas do sistema novo.

## Código, Simulações e Testes

- **Visão Geral do Repositório**  
  - [`readme.md`](../readme.md) – Visão geral do projeto, contexto, estrutura de pastas e links principais de documentação.

- **Simulação Unificada do Sistema Novo (`src/Simulacao-Unificada`)**  
  - [`API/README.md`](../src/Simulacao-Unificada/API/README.md) – Descrição da API mock que simula Miro, SharePoint, Copilot, Office e Sentinel, com formatos de resposta e parâmetros de consulta.  
  - [`Middleware-Validacao/README.md`](../src/Simulacao-Unificada/Middleware-Validacao/README.md) – Middleware FastAPI que implementa as táticas de Segurança, Escalabilidade e Rastreabilidade (RNF-01, RNF-02, RNF-03).  
  - [`Middleware-Validacao/tests/README.md`](../src/Simulacao-Unificada/Middleware-Validacao/tests/README.md) – Organização dos testes automatizados do middleware (unitários e de integração).  
  - [`Testes-Automatizados/README.md`](../src/Simulacao-Unificada/Testes-Automatizados/README.md) – Suite de testes de RNFs (segurança, escalabilidade, rastreabilidade), cenários cobertos, comandos de execução e métricas.

## RNFs e Simulações por Sprint (`src/RNFs`)

- **RNF-01 – Escalabilidade**  
  - [`Sprint 3/README.md`](../src/RNFs/RNF-01-Escalabilidade/Sprint%203/README.md) – Visão geral da solução de escalabilidade, scripts de simulação, estrutura de código e testes.  
  - [`Sprint 3/docs/ingestor-README.md`](../src/RNFs/RNF-01-Escalabilidade/Sprint%203/docs/ingestor-README.md) – Documentação do módulo de ingestão.  
  - [`Sprint 3/docs/orchestrator-README.md`](../src/RNFs/RNF-01-Escalabilidade/Sprint%203/docs/orchestrator-README.md) – Documentação do orquestrador de cargas/processos.  
  - [`Sprint 3/docs/sharepoint-README.md`](../src/RNFs/RNF-01-Escalabilidade/Sprint%203/docs/sharepoint-README.md) – Documentação da integração simulada com SharePoint.  
  - [`Sprint 3/docs/iam-README.md`](../src/RNFs/RNF-01-Escalabilidade/Sprint%203/docs/iam-README.md) – Documentação do módulo de identidade e acesso (IAM).  
  - [`Sprint 3/docs/audit-README.md`](../src/RNFs/RNF-01-Escalabilidade/Sprint%203/docs/audit-README.md) – Documentação do módulo de auditoria e logs.  

- **RNF-02 – Segurança**  
  - [`RNF-02-Segurança/Sprint 3/Configuracao.md`](../src/RNFs/RNF-02-Segurança/Sprint%203/Configuracao.md) – Configuração da API de segurança, cenários simulados e parâmetros de teste.  

- **RNF-03 – Rastreabilidade**  
  - [`RNF-03-Rastreabilidade/Sprint 3/Configuracao.md`](../src/RNFs/RNF-03-Rastreabilidade/Sprint%203/Configuracao.md) – Configuração da solução de rastreabilidade, modelos de estados e simulações de perda/ganho de trilha.

## Licença

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/ENDEREÇOGRUPO>"><nome do projeto></a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/ENDEREÇOGRUPO">INTELI, Gabriel Santos do Nascimento, Iasmim Santos Silva de Jesus, Milena Aparecida Vieira Castro, Nicolas Ramon da Silva, Paulo Henrique Ribeiro, Thalyta da Silva Viana, Vinicius dos Reis Savian</a> is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>
