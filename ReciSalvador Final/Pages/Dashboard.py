import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3



dados = pd.read_csv("SQLite/tabela_residuos.csv")

st.title("Dashboard")
st.subheader("Tabela com os dados")
st.dataframe(dados)

    # Gráfico de Barras - Quantidade por Tipo de Material
st.subheader("Quantidade de Resíduos por Tipo de Material")
quantidade_por_tipo = dados.groupby('tipo')['quantidade'].sum()
    
fig_bar, ax_bar = plt.subplots(figsize=(10, 6))
quantidade_por_tipo.plot(kind='bar', color='skyblue', edgecolor='black', ax=ax_bar)
ax_bar.set_title('Quantidade de Resíduos por Tipo de Material', fontsize=14)
ax_bar.set_xlabel('Tipo de Material', fontsize=12)
ax_bar.set_ylabel('Quantidade', fontsize=12)
ax_bar.grid(axis='y', linestyle='--', alpha=0.7)
st.pyplot(fig_bar)

    # Gráfico de Pizza - Proporção por Tipo de Material
st.subheader("Proporção de Resíduos por Tipo de Material")
fig_pie, ax_pie = plt.subplots(figsize=(8, 8))
quantidade_por_tipo.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors, ax=ax_pie)
ax_pie.set_title('Proporção de Resíduos por Tipo de Material', fontsize=14)
ax_pie.set_ylabel('')
st.pyplot(fig_pie)

