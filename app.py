import streamlit as st
import requests
import json

def get_prediction(payload):
    endpoint = st.secrets["API-ENDPOINT"]
    headers = {
        "Content-Type": "application/json",
        "x-api-key": st.secrets["API-KEY"]
    }

    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()

        """
        ### Predição de Score de Crédito

        De acordo com os dados fornecidos, seu Score de Crédito será...
        """

        predicted_score_formatted = result["prediction"]

        if predicted_score_formatted == 0:
            st.warning("**Ruim (Poor)**", icon="👎")
        elif predicted_score_formatted == 1:
            st.info("**Padrão (Standard)**", icon="😐")
        elif predicted_score_formatted == 2:
            st.success("**Bom (Good)**", icon="👍")
        else:
            st.markdown("Erro ao obter a previsão. Por favor, tente novamente mais tarde ou revise seus dados.")
    else:
        st.error(f"Erro ao contatar a API. Código: {response.status_code}")
        st.json(response.text)

# --- Interface do Streamlit ---

st.set_page_config(layout="wide", page_title="Predição de Score de Crédito")

st.title("Trabalho Final - FIAP - 10DTSR - MLOPS")
st.markdown("Ana Cristina Lourenço Maria: RM359310")
st.markdown("Jayana da Silva Alves: RM359631")
st.markdown("Pedro Silva de Sá Monnerat: RM359532")
st.markdown("---")

st.title("Predição de Score de Crédito")
st.markdown("Este modelo prevê a classificação do score de crédito de um cliente com base em suas características financeiras e históricas.")
st.markdown("---")

# --- Formulário para coletar dados do cliente ---
st.header("Insira as Características do Cliente")

# O formulário é dividido em colunas para melhor organização
col1, col2 = st.columns(2)

with col1:
    st.subheader("Informações Pessoais e de Renda")
    age = st.number_input("Idade", min_value=18, max_value=120, step=1)
    annual_income = st.number_input("Renda Anual (USD)", min_value=0.0, format="%.2f")
    monthly_inhand_salary = st.number_input("Salário Mensal Líquido (USD)", min_value=0.0, format="%.2f")
    occupation = st.selectbox("Profissão", ("Accountant", "Architect", "Desconhecido", "Developer", "Doctor",
        "Engineer", "Entrepreneur", "Journalist", "Lawyer", "Manager",
        "Mechanic", "Media_Manager", "Musician", "Scientist", "Teacher", "Writer"))

with col2:
    st.subheader("Informações Bancárias e de Crédito")
    num_bank_accounts = st.number_input("Número de Contas Bancárias", min_value=0, step=1)
    num_credit_card = st.number_input("Número de Cartões de Crédito", min_value=0, step=1)
    num_of_loan = st.number_input("Número de Empréstimos Ativos", min_value=0, step=1)
    interest_rate = st.number_input("Taxa de Juros Média (%) nos Empréstimos", min_value=0, step=1)

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    st.subheader("Histórico e Comportamento de Pagamento")
    credit_history_age = st.number_input("Idade do Histórico de Crédito (em meses)", min_value=0, step=1)
    delay_from_due_date = st.number_input("Dias de Atraso Médio Após Vencimento", min_value=0, step=1)
    num_of_delayed_payment = st.number_input("Número de Pagamentos em Atraso (total)", min_value=0, step=1)
    payment_behaviour = st.selectbox("Comportamento de Pagamento", ("Desconhecido", "High_spent_Large_value_payments", 
        "High_spent_Medium_value_payments", "High_spent_Small_value_payments", "Low_spent_Large_value_payments",
        "Low_spent_Medium_value_payments", "Low_spent_Small_value_payments"))
    payment_of_min_amount = st.selectbox("Paga o Valor Mínimo da Fatura?", ("NM", "No", "Yes"))

with col4:
    st.subheader("Dívidas e Investimentos")
    outstanding_debt = st.number_input("Dívida em Aberto (USD)", min_value=0.0, format="%.2f")
    total_emi_per_month = st.number_input("Total de Parcelas (EMI) por Mês (USD)", min_value=0.0, format="%.2f")
    credit_utilization_ratio = st.number_input("Taxa de Utilização de Crédito (%)", min_value=0.0, max_value=100.0, format="%.2f")
    amount_invested_monthly = st.number_input("Valor Investido Mensalmente (USD)", min_value=0.0, format="%.2f")
    monthly_balance = st.number_input("Saldo Mensal Restante (USD)", min_value=0.0, format="%.2f")


st.markdown("---")

st.subheader("Outras Informações de Crédito")
col5, col6, col7 = st.columns(3)
with col5:
    credit_mix = st.selectbox("Mix de Crédito (qualidade geral)", ("Bad", "Desconhecido", "Good", "Standard"))
with col6:
    changed_credit_limit = st.number_input("Alteração no Limite de Crédito Recente", min_value=0.0, format="%.2f")
with col7:
    num_credit_inquiries = st.number_input("Número de Consultas de Crédito Recentes", min_value=0, step=1)

# Botão para enviar os dados para predição
if st.button("Estimar Score de Crédito", type="primary", use_container_width=True):
    # Cria o payload com base nos dados do formulário
    payload = {"data": {
        "Age": str(age),
        "Annual_Income": str(annual_income),
        "Monthly_Inhand_Salary": str(monthly_inhand_salary),
        "Num_Bank_Accounts": str(num_bank_accounts),
        "Num_Credit_Card": str(num_credit_card),
        "Interest_Rate": str(interest_rate),
        "Num_of_Loan": str(num_of_loan),
        "Delay_from_due_date": str(delay_from_due_date),
        "Num_of_Delayed_Payment": str(num_of_delayed_payment),
        "Changed_Credit_Limit": str(changed_credit_limit),
        "Num_Credit_Inquiries": str(num_credit_inquiries),
        "Outstanding_Debt": str(outstanding_debt),
        "Credit_Utilization_Ratio": str(credit_utilization_ratio),
        "Credit_History_Age": str(credit_history_age),
        "Total_EMI_per_month": str(total_emi_per_month),
        "Amount_invested_monthly": str(amount_invested_monthly),
        "Monthly_Balance": str(monthly_balance),
        "Occupation": str(occupation),
        "Credit_Mix": str(credit_mix),
        "Payment_of_Min_Amount": str(payment_of_min_amount),
        "Payment_Behaviour": str(payment_behaviour)
    }}

    # Adiciona um spinner enquanto a API é chamada
    with st.spinner("Analisando perfil de crédito..."):
        get_prediction(payload)