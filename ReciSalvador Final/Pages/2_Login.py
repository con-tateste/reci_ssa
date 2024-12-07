import streamlit as st
import sqlite3

def autenticar_usuario(email,senha):
    with sqlite3.connect('usuarios_cadastrados.db',check_same_thread=True,timeout=10.0) as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT email , senha , nome FROM cadastros WHERE email = ? AND senha = ?" , (email,senha))
        usuario = cursor.fetchone()

        if usuario:
            st.session_state.nome = usuario[2]
            return True
        else:
            return False 

def tela_login():

    st.title("Login")
    login = st.form(key="Usuarios",clear_on_submit=True)

    with login:
        input_email = st.text_input("Email: ",placeholder="Insira seu email")
        input_senha = st.text_input("Senha: ",placeholder="Insira sua senha",type="password")

        botao_login = login.form_submit_button("Entrar")

        if botao_login:
            if input_email and input_senha:
                usuario = autenticar_usuario(input_email,input_senha)
                if usuario:
                    st.session_state.login_feito = True
                    st.success(f"Login feito com sucesso")
                else:
                    st.error("Email ou senha incorretos. Tente novamente.")
            else:
                st.error("Insira email e senha")
    
def tela_do_salve():
    if "login_feito" in st.session_state:
        nome = st.session_state.nome
        st.write(f"Bem vindo(a) de volta {nome}")

    botao_sair = st.button("Sair da sessão")
    if botao_sair:
        st.session_state.clear()
        st.write("Desconectado")

def main():
    if "login_feito" not in st.session_state:   
        tela_login()
    else:
        tela_do_salve()

if __name__ == "__main__":
    main()
