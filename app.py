import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard de Salários")

arquivo = st.sidebar.file_uploader("Envie um CSV", type=["csv"])

if arquivo:
    df = pd.read_csv(arquivo)
else:
    df = pd.read_csv("dados.csv")

categoria = st.sidebar.selectbox(
    "Categoria de Salário",
    options=df["categoria_salario"].unique()
)

df_filtrado = df[df["categoria_salario"] == categoria]

fig = px.bar(
    df_filtrado,
    x="cargo",
    y="salario",
    color="categoria_salario",
    title="Salários por Cargo"
)

st.plotly_chart(fig)

st.write("Dados filtrados:")
st.dataframe(df_filtrado)
