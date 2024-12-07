import streamlit as st
import sqlite3
import pandas as pd
import numpy

def acessar_banco():
    with sqlite3.connect('registro_residuos.db',check_same_thread=False,timeout=10.0) as conexao:
        cursor = conexao.cursor()
        query = """
                    SELECT tipo,nome,quantidade,data,local
                    FROM residuos
                """
        
        cursor.execute(query)
        dados = cursor.fetchall()

    return dados

def exibir_graficos():
    dados = acessar_banco()
    df = pd.DataFrame(dados,columns=['tipo', 'nome', 'quantidade', 'data', 'local'])
    if dados:
        
        st.write("Tabela")
        st.write(df.describe())

exibir_graficos()

        


