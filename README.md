# Trabalho Final - FIAP - 10DTSR - MLOPS

Ana Cristina Lourenço Maria: RM359310

Jayana da Silva Alves: RM359631

Pedro Silva de Sá Monnerat: RM359532

# Aplicação Streamlit de Predição de Score de Crédito

Este projeto consiste em uma aplicação web desenvolvida com Streamlit que interage com uma API de predição de score de crédito. A aplicação coleta dados do usuário através de um formulário interativo e envia esses dados para uma API externa para obter uma classificação do score de crédito.

# Estrutura do Projeto

- app.py: O código-fonte principal da aplicação Streamlit, responsável pela interface do usuário e pela comunicação com a API de predição.

- packages.txt: Lista de pacotes do sistema operacional adicionais necessários para o deployment no Streamlit Community Cloud (neste caso, locales-all).

- requirements.txt: Lista as dependências Python da aplicação, como streamlit e requests.

# Funcionalidades da Aplicação

A aplicação app.py oferece uma interface intuitiva para que os usuários possam inserir as características financeiras e históricas de um cliente.

## Interface do Usuário

- Título e Identificação: Exibe o título do trabalho e os nomes dos membros do grupo da FIAP.

- Introdução: Uma breve descrição sobre o propósito do modelo de predição de score de crédito.

- Formulário Detalhado: O formulário é dividido em seções (Informações Pessoais e de Renda, Informações Bancárias e de Crédito, Histórico e Comportamento de Pagamento, Dívidas e Investimentos, Outras Informações de Crédito) para facilitar a inserção dos dados. Campos como idade, renda, número de contas, histórico de pagamentos, dívidas e mix de crédito são solicitados.

- Botão de Estimação: O botão "Estimar Score de Crédito" envia os dados para a API.

## Interação com a API

- A função get_prediction é responsável por fazer a requisição POST para a API de predição.

- Utiliza st.secrets para acessar o endpoint e a chave da API de forma segura.

- Se a predição for bem-sucedida (status code 200), a aplicação exibe o score de crédito classificado como Ruim, Padrão ou Bom, com ícones indicativos.

- Em caso de erro na comunicação com a API, uma mensagem de erro é exibida, incluindo o código de status e a resposta da API para depuração.

## Dados de Entrada

A aplicação coleta os seguintes dados, que são serializados em JSON e enviados à API:

- Age (Idade)

- Annual_Income (Renda Anual)

- Monthly_Inhand_Salary (Salário Mensal Líquido)

- Num_Bank_Accounts (Número de Contas Bancárias)

- Num_Credit_Card (Número de Cartões de Crédito)

- Interest_Rate (Taxa de Juros Média nos Empréstimos)

- Num_of_Loan (Número de Empréstimos Ativos)

- Delay_from_due_date (Dias de Atraso Médio Após Vencimento)

- Num_of_Delayed_Payment (Número de Pagamentos em Atraso)

- Changed_Credit_Limit (Alteração no Limite de Crédito Recente)

- Num_Credit_Inquiries (Número de Consultas de Crédito Recentes)

- Outstanding_Debt (Dívida em Aberto)

- Credit_Utilization_Ratio (Taxa de Utilização de Crédito)

- Credit_History_Age (Idade do Histórico de Crédito em meses)

- Total_EMI_per_month (Total de Parcelas (EMI) por Mês)

- Amount_invested_monthly (Valor Investido Mensalmente)

- Monthly_Balance (Saldo Mensal Restante)

- Occupation (Profissão)

- Credit_Mix (Mix de Crédito)

- Payment_of_Min_Amount (Paga o Valor Mínimo da Fatura)

- Payment_Behaviour (Comportamento de Pagamento)

Todos os campos são coletados como strings para corresponder ao formato esperado pela API.
