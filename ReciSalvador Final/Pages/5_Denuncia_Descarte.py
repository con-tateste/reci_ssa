import streamlit as st
from datetime import datetime
import sqlite3

st.set_page_config(
    page_title="ReciSalvador",
    page_icon="♻️",
    layout="wide",
)

st.write("""
         # Denuncie descartes inadequados de residuos
         Registre aqui locais que você reconheceu descarte irregular de residuos que poderiam ter sido postos para reciclagem
         """)

def criar_tabela():
    with sqlite3.connect('descarte_inadequado.db',check_same_thread=True,timeout=10.0) as conexao:
        cursor = conexao.cursor()
        cursor.execute ("""
        CREATE TABLE IF NOT EXISTS locais(
        tipo text,
        endereco text,                
        data text,
        horario integer,
        descricao text)
        """)
        conexao.commit()

def inserir_no_sql( tipo , endereco , data , horario , descricao  ):
    #converter horario pro sql pq ele nao aceita o nativo do streamlit
    horario_conv = horario.strftime('%H:%M:%S')
    with sqlite3.connect ('descarte_inadequado.db',check_same_thread=True, timeout=10.0) as conexao:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO locais (tipo,endereco,data,horario,descricao) VALUES (?,?,?,?,?)",(tipo , endereco , data , horario_conv , descricao))
        conexao.commit()
        st.success("Registro feito com sucesso")

def pegar_informacoes():
    registrar = st.form(key="descarte_inadequado",clear_on_submit=False)
    tipos_de_residuo = ["Papel", "Plástico", "Vidro", "Metais", "Eletrônicos", "Orgânicos", "Têxteis", "Madeira", "Óleo de Cozinha"]

    with registrar:
        input_tipo = st.selectbox(("Tipo do Residuo encontrado"),tipos_de_residuo)
        input_endereco = st.text_input("Insira o endereço do local",placeholder=("Endereço completo")) 
        input_data = st.date_input("Data")
        input_horario = st.time_input("Horario")
        input_descricao = st.text_area("Descreva em mais detalhes o que registrou")
        
        receber_imagem = st.file_uploader("Insira a foto.", type=["jpg", "jpeg", "png"])
        
        if receber_imagem == None:
            st.error("Por favor insira um imagem")
        
        botao_registrar = registrar.form_submit_button("Salvar Registro")   

        if botao_registrar:
            data_registro = datetime.now().strftime(('%d-%m-%Y %H:%M:%S'))
            if input_tipo and input_endereco and input_data and input_horario and input_descricao:
                st.success("Registro Salvo. Obrigado!!")
                inserir_no_sql(input_tipo , input_endereco , input_data , input_horario , input_descricao)
            else:
                st.error("Preencha todos os dados")

criar_tabela()
pegar_informacoes()


    


