import streamlit as st
import pandas as pd

df = pd.read_csv("./data/df_tratado.csv")

st.title("Comçando com streamlit")

st.write("Registro do dataset:")
st.dataframe(df.head())

st.sidebar.header("Filtros")

countries = ["Mostrar todos"] + df["Country"].unique().tolist()

country = st.sidebar.selectbox("Selecione o país: ", countries)

min_cost, max_cost = st.sidebar.slider("Faixa de custo médio para 2: ",
                                       float(df["Average Cost for two usd"].min()),
                                       float(df["Average Cost for two usd"].max()),
                                       (float(df['Average Cost for two usd'].min()), 
                                        float(df['Average Cost for two usd'].max())))

if country != "Mostrar todos":
    df_filtered = df[df["Country"] == country]
else:
    df_filtered = df

df_filtered = df_filtered[(df_filtered["Average Cost for two usd"] >= min_cost) & 
                          (df_filtered["Average Cost for two usd"] <= max_cost)]

st.header("Dataset com filtro")
st.dataframe(df_filtered)