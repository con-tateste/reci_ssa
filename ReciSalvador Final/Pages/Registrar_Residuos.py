import streamlit as st
import sqlite3
from datetime import datetime

st.set_page_config(
    page_title="ReciSalvador",
    page_icon="♻️",
    layout="wide",
)
st.title("Registre os residuos colocados para reciclagem")

def criar_tabela():
    with sqlite3.connect('registro_residuos.db',check_same_thread=True,timeout=10.0) as conexao:
        cursor = conexao.cursor()
        cursor.execute ("""
        CREATE TABLE IF NOT EXISTS residuos(
        tipo text,
        nome text,
        quantidade integer,
        data text,
        local)
        """)
    conexao.commit()

def inserir_dados(tipo, nome, quantidade, data_registro, local):
    
    with sqlite3.connect('registro_residuos.db',check_same_thread=True,timeout=10.0) as conexao:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO residuos VALUES (?,?,?,?,?)",(tipo,nome,quantidade,data_registro,local))
        conexao.commit()
        st.success("\nDados Inseridos no Banco de Dados com Sucesso")
        
def registrar_residuos():
    registrar = st.form(key="itens",clear_on_submit=True)
    tipos_de_residuo = ["Papel", "Plástico", "Vidro", "Metais", "Eletrônicos", "Orgânicos", "Têxteis", "Madeira", "Óleo de Cozinha"]

    with registrar:
        input_tipo = st.selectbox(("Tipo do Residuo"),tipos_de_residuo)
        input_nome = st.text_input("Nome: ",placeholder="Insira o nome do residuo")
        input_quantidade = st.number_input("Quantidade",min_value=1 , max_value=1000)
        input_local = st.text_input("Insira o local onde colocou os residuos para reciclagem")
    
        botao_registrar = registrar.form_submit_button("Salvar Registro")

        if botao_registrar:
            data_registro = datetime.now().strftime(('%d-%m-%Y %H:%M:%S'))
            if input_tipo and input_nome and input_quantidade and input_local:
                st.success("Registro Salvo. Obrigao")
                inserir_dados(input_tipo, input_nome, input_quantidade, data_registro, input_local)
            else:
                st.error("Preencha todos os dados")


criar_tabela()
registrar_residuos()
