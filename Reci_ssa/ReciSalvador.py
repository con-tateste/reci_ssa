import streamlit as st

#O que fazer:
#-As imagens inseridas não vão para o bando de dados
#-Criar uma sessão funcional com login do usuario para saber os residuos que ele colocou usando o streamlit_authenticator
#-Em registrar residuos inserir a opcao de selecionar o local onde ele descartou

st.set_page_config(
    page_title="ReciSalvador",
    page_icon="♻️",
    layout="centered",
)

st.title("Pontos de Coleta em Salvador")

st.write("Confira abaixo o mapa com pontos de coleta")

link_pro_mapa = """
<iframe 
    src="https://www.google.com/maps/d/embed?mid=1-bBNeDfTF4JcG0ElG0RTdBmwFRgg9yEY&ehbc=2E312F" 
    width="720" 
    height="480">
</iframe>
"""
st.components.v1.html(link_pro_mapa, height=480)
