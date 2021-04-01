<h1 align="center">
    <span>Laboratório de Experimentação de Software</span>
</h1>

Tabela de conteúdos
=================
<!--ts-->
   👉 [Sobre o projeto](#page_facing_up-sobre-o-projeto) <br>
   👉 [Metodologia](#----hammer-metodologia) <br>
   👉 [Seleção de Repositórios](#bulb-1-criação-do-dataset) <br>
   👉 [Questões de pesquisa](#dart-2-questões-de-pesquisa) <br>
   👉 [Definição de Métricas](#sparkles-3-definição-de-métricas) <br>
   👉 [Relatório final](#pencil-relatório-final) <br>
   👉 [Bônus](#-bônus-2-pontos) <br>
   👉 [Processo de desenvolvimento](#octocat-processo-de-desenvolvimento) <br>
   👉 [Alunos](#busts_in_silhouette-alunos) <br>
   👉 [Professor responsável](#bust_in_silhouette-professor-responsável) 
<!--te-->

### :page_facing_up: Sobre o projeto

A prática de code review tornou-se uma constante nos processos de desenvolvimento agéis. Em linhas gerais, ela consiste na interação entre desenvolvedores e revisores com o objetivo de inspecionar o código produzido antes de integrá-lo à base principal. Assim, garante-se a qualidade do código integrado, evitando-se também a inclusão de defeitos. No contexto de sistemas open source, mais especificamente dos desenvolvidos através do GitHub, as atividades de code review acontecem a partir da avaliação de contribuições submetidas por meio de Pull Requests (PR). Ou seja, para que se integre um código na branch principal, é necessário que seja realizada uma solicitação de pull, que será avaliada e discutida por um colaborador do projeto. Ao final, a solicitação de merge pode ser aprovada ou rejeitada pelo revisor. Em muitos casos, ferramentas de verificação estática realizam uma primeira análise, avaliando requisitos de estilo de programação ou padrões definidos pela organização.

Neste contexto, o objetivo deste laboratório é analisar a atividade de code review desenvolvida em repositórios populares do GitHub, identificando variáveis que influenciam no merge de um PR, sob a perspectiva de desenvolvedores que submetem código aos repositórios selecionados. 

<h1 align="center">
    <span>:hammer: Metodologia</span>
</h1>

### :bulb: 1. Criação do Dataset

O dataset utilizado neste laboratório será composto por PRs submetidos à repositórios:

- populares (ou seja, avaliaremos PRs submetidos aos 100 repositórios mais populares do GitHub);
- que possuam pelos menos 100 PRs (MERGED + CLOSED).

Além disso, a fim de analisar pull requests que tenham passado pelo processo de code review, selecionaremos apenas aqueles:

- com status MERGED ou CLOSED;
- que possuam pelo menos uma revisão (total count campo review).

Por fim, com o objetivo de remover do nosso dataset PRs que foram revisados de forma automática (através de bots ou ferramentas de CI/CD), selecionaremos aqueles cuja revisão levou pelo menos uma hora (isto é, a diferença entre a data de criação e de merge (ou close) é maior que uma hora).

### :dart: 2. Questões de Pesquisa

- Com base no dataset coletado, responderemos às seguintes questões de pesquisa, definidos de acordo com duas dimensões:

**A. Feedback Final das Revisões (Status do PR)**:

**RQ 01**. Qual a relação entre o **tamanho** dos PRs e o feedback final das revisões? <br>
**RQ 02**. Qual a relação entre o **tempo de análise dos PRs** e o feedback final das revisões? <br>
**RQ 03**. Qual a relação entre a **descrição dos PRs** e o feedback final das revisões? <br> 
**RQ 04**. Qual a relação entre as **interações nos PRs** e o feedback final das revisões?  

**B. Número de Revisões**:

**RQ 05**. Qual a relação entre o **tamanho dos PRs** e o número de revisões realizadas? <br>
**RQ 06**. Qual a relação entre o **tempo de análise dos PRs** e o número de revisões realizadas? <br>
**RQ 07**. Qual a relação entre a **descrição dos PRs** e o número de revisões realizadas? <br> 
**RQ 08**. Qual a relação entre as **interações nos PRs** e o número de revisões realizadas? 

### :sparkles: 3. Definição de Métricas

Para cada dimensão, realizaremos as correlações com as métricas definidas a seguir:

- **Tamanho**: número de arquivos; total de linhas adicionadas e removidas.
- **Tempo de Análise**: intervalo entre a criação do PR e a última atividade (fechamento ou merge).
- **Descrição**: número de caracteres do corpo de descrição do PR (na verdão markdown).
- **Interações**: número de participantes; número de comentários.

### :pencil: Relatório final

Para cada uma questões de pesquisa, faça uma sumarização dos dados obtidos através dos valores medianos (Links para um site externo.) obtidos em todos os PRs. Ou seja, não é necessário dividir suas análises por repositório. Mesmo que de forma informal, elabore hipóteses sobre o que você espera de resposta e tente analisar a partir dos valores obtidos. 

Elabore um documento que apresente (i) uma introdução simples com hipóteses informais; (ii) a metodologia que você utilizou para responder às questões de pesquisa; (iii) os resultados obtidos para cada uma delas; (iii) a discussão sobre o que você esperava como resultado (suas hipóteses) e os valores obtidos.

### 🏁 Bônus (+2 pontos):

Para melhor **analisar a correlação entre os valores obtidos** em cada questão de pesquisa, gere **gráficos de correlação** que permitam visualizar o comportamento dos dados obtidos. Adicionalmente, utilize um teste estatístico que forneça confiança nas análises apresentadas (por exemplo, teste de correlação de **Spearman** ou de **Pearson**).

### :octocat: Processo de desenvolvimento

- [ ] Lab03S01:  Lista de repositórios selecionados + Criação do script de coleta dos PRs e métricas definidas (**6 pontos**)

- [ ] Lab03S02: Dataset completo, com os valores de todas as métricas necessárias (**6 pontos**) 

- [ ] Lab03S03: Análise dos resultados e escrita do documento final (**7 pontos**) 

`Prazo final: **21/04** | Valor total: **20 pontos** | Desconto de **0.5 pontos** por dia de atraso.`

### :busts_in_silhouette: Alunos

- <a href="https://github.com/mcarneirobug" target="_blank">Matheus Santos Rosa Carneiro</a>.
- <a href="https://github.com/raissavilela" target="_blank">Raíssa Carolina Vilela da Silva</a>.
- <a href="https://github.com/ovitorj" target="_blank">Vitor Augusto Alves de Jesus</a>.

### :bust_in_silhouette: Professor responsável

- [Jose Laerte Pires Xavier Junior](https://github.com/xavierlaerte).

<h4 align="center"> 
	🚧  Spring 1 🚀 Em progresso ...  🚧
</h4>
