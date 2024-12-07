import sqlite3
import streamlit as st

def criar_tabela():
    with sqlite3.connect('usuarios_cadastrados.db',check_same_thread=True,timeout=10.0) as conexao:
        cursor = conexao.cursor()
        cursor.execute ("""
        CREATE TABLE IF NOT EXISTS cadastros(
        nome text,
        idade integer,
        email text,
        senha text,
        genero text)
        """)
    conexao.commit()

def inserir_dados(nome,idade,email,senha,genero):

    with sqlite3.connect('usuarios_cadastrados.db',check_same_thread=True,timeout=10.0) as conexao:
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO cadastros VALUES (?,?,?,?,?)",(nome,idade,email,senha,genero))
        conexao.commit()
        st.success(("Usuario cadastrado com sucesso"))

def cadastro():
    st.title("Cadastre-se")

    cadastro = st.form(key="Usuarios",clear_on_submit=True)
    generos = ["Masculino","Feminino","Outro"]

    with cadastro:
        input_nome = st.text_input("Nome: ",placeholder="Insira seu nome")
        input_idade = st.number_input("Idade: ", min_value=1 , max_value=100 , step=1 , value=25)
        input_email = st.text_input("Email: ",placeholder="Insira seu email")
        input_senha = st.text_input("Senha: ",placeholder="Insira sua senha",type="password")
        input_genero = st.selectbox("Qual seu genêro: ",generos)

        botao_salvar = cadastro.form_submit_button("Salvar")    

        if botao_salvar:
            st.write("Cadastro relizado com sucesso")
            inserir_dados(input_nome,input_idade,input_email,input_senha,input_genero)

criar_tabela()
cadastro()                  
