import streamlit as st

st.set_page_config(
    page_title="ReciSalvador",
    page_icon="♻️",
    layout="wide",
)

st.title("Encontre mais informações abaixo")

st.write(
    """ 
    Em Salvador, 74 mil toneladas de lixo são geradas mensalmente, mas menos de 1% é reciclado, apesar de 46% ter potencial para reaproveitamento. A reciclagem traz benefícios enormes:

    - Reduz o impacto ambiental, preservando solos e águas, e diminuindo a emissão de gases de efeito estufa.

    - Gera empregos para cerca de 800 mil brasileiros, muitos ligados a cooperativas, promovendo inclusão social e economia sustentável.

    -  Economiza recursos naturais e energia: reciclar alumínio, por exemplo, economiza 95% da energia necessária para produzir o material do zero.

    -  Contribui para uma cidade mais limpa, prevenindo doenças e a proliferação de vetores como mosquitos e ratos.
    """
)

st.markdown(""" 
            Para saber mais visite: 
            - [https://www.reciclasampa.com.br/artigo/dados-e-estatisticas-sobre-reciclagem-no-brasil]
            - [https://sustentabilidade.salvador.ba.gov.br/coleta-seletiva/]
            """
            )