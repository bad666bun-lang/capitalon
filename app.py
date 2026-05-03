import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Configuração de Identidade
st.set_page_config(page_title="Capital On | Inteligência Financeira", page_icon="📈", layout="wide")

# CSS para Design Premium (Cores da sua Logo)
st.markdown("""
    <style>
    .stApp { background-color: #001a33; color: white; }
    .main-card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        color: #001a33;
        box-shadow: 0px 10px 25px rgba(0,0,0,0.5);
    }
    .stButton>button {
        background: linear-gradient(90deg, #00d4ff 0%, #00ff88 100%);
        color: #001a33;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        width: 100%;
        height: 3em;
    }
    h1, h2, h3 { color: #00d4ff !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar - Navegação
st.sidebar.title("💎 CAPITAL ON")
menu = st.sidebar.radio("Navegar por:", ["Resgate de Bônus", "Calculadora de Milhas", "Radar de Notícias"])

# 3. Função de Integração Excel (Salvar Leads)
def salvar_lead(nome, whatsapp, interesse):
    novo_lead = pd.DataFrame([[datetime.now(), nome, whatsapp, interesse]], 
                             columns=['Data', 'Nome', 'WhatsApp', 'Interesse'])
    try:
        df_antigo = pd.read_csv('leads_capitalon.csv')
        df_final = pd.concat([df_antigo, novo_lead], ignore_index=True)
    except:
        df_final = novo_lead
    df_final.to_csv('leads_capitalon.csv', index=False)

# --- ABA 1: RESGATE DE BÔNUS ---
if menu == "Resgate de Bônus":
    st.title("Ative seu Bônus Global 🌍")
    with st.container():
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.write("Complete o perfil para liberar até **R$ 100 de bônus** em sua conta internacional.")
        
        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input("Seu nome completo")
        with col2:
            zap = st.text_input("WhatsApp (com DDD)")
        
        renda = st.selectbox("Qual sua renda mensal aprox.?", ["Até R$ 2.000", "R$ 2.000 a R$ 5.000", "Acima de R$ 5.000"])
        
        if st.button("VERIFICAR DISPONIBILIDADE"):
            if nome and zap:
                salvar_lead(nome, zap, f"Bônus Global - Renda {renda}")
                st.success(f"Parabéns {nome}! Bônus de R$ 100 disponível para você.")
                st.balloons()
                st.link_button("ABRIR CONTA REVOLUT E RESGATAR", "https://revolut.com/") # COLOQUE SEU LINK AQUI
            else:
                st.warning("Preencha todos os campos para validar.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- ABA 2: CALCULADORA DE MILHAS ---
elif menu == "Calculadora de Milhas":
    st.title("Quanto dinheiro você está perdendo? 💸")
    st.write("Descubra quanto seus gastos mensais renderiam em viagens ou dinheiro de volta.")
    
    gasto = st.number_input("Quanto você gasta no cartão por mês?", min_value=0, value=1000)
    
    milhas_estimadas = gasto * 2.2 # Média de cartões Black
    valor_em_reais = (milhas_estimadas / 1000) * 20 # Valor médio do milheiro
    
    st.metric("Lucro Anual Estimado", f"R$ {valor_em_reais * 12:,.2f}")
    st.info("Com o cartão certo, você poderia viajar de graça uma vez por ano.")
    
    if st.button("QUERO O CARTÃO QUE PONTUA MAIS"):
        st.write("Redirecionando para análise de crédito...")

# --- ABA 3: RADAR DE NOTÍCIAS ---
elif menu == "Radar de Notícias":
    st.title("Radar Capital On 📡")
    st.write("As últimas do mercado financeiro redigidas por nossa IA.")
    
    # Exemplo de como aparecerão as notícias
    st.markdown("""
    ---
    **[NOTÍCIA] Dólar cai para R$ 4,90: É hora de carregar sua conta global?**
    *Análise Capital On: A queda favorece quem busca o bônus da Revolut esta semana...*
    
    ---
    **[CARTÕES] Novo cartão Black sem anuidade liberado para universitários.**
    *Saiba como o histórico de gastos pode ignorar a exigência de renda alta...*
    """)
