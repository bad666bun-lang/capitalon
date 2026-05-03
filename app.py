import streamlit as st

# Configuração da Identidade Visual (Cores da Logo)
st.set_page_config(page_title="Capital On | Bônus e Crédito", page_icon="📈")

# Estilo CSS para aplicar o Azul e o Ciano da logo
st.markdown(f"""
    <style>
    .stApp {{
        background: linear-gradient(180deg, #001a33 0%, #004aad 100%);
    }}
    .main-box {{
        background-color: #ffffff;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0px 15px 35px rgba(0,0,0,0.3);
        text-align: center;
        color: #001a33;
    }}
    h1 {{ color: #004aad !important; font-family: 'sans-serif'; font-weight: 800; }}
    .stButton>button {{
        background-color: #00d4ff;
        color: #001a33;
        font-weight: bold;
        border: none;
        border-radius: 50px;
        padding: 15px 30px;
        width: 100%;
    }}
    </style>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="main-box">', unsafe_allow_html=True)
    st.title("CAPITAL ON")
    st.write("### Ative seu bônus de conta global hoje")
    st.write("Analisamos as melhores oportunidades de bônus e crédito para você.")

    nome = st.text_input("Nome Completo")
    whatsapp = st.text_input("WhatsApp com DDD")
    
    if st.button("REIVINDICAR MEU BÔNUS"):
        if nome and whatsapp:
            st.success("Diagnóstico concluído! Verifique seu bônus abaixo.")
            st.balloons()
            st.link_button("ABRIR MINHA CONTA AGORA", "https://revolut.com/") # Troque pelo seu link depois
        else:
            st.error("Preencha os dados para validar seu bônus.")
    st.markdown('</div>', unsafe_allow_html=True)
