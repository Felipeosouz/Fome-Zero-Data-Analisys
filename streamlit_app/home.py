import streamlit as st
import pandas as pd

df = pd.read_csv("./data/df_tratado.csv")

st.title("Fome Zero Data Analisys")

tab1, tab2 = st.tabs(["Visão Gerencial", " "])

with tab1:
    with st.container():
        st.title("Overral Metrics")

        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            col1.metric('Restaurantes Únicos Cadastrados',value=100)
        with col2:
            st.title("Coluna 2")
        with col3:
            st.title("Coluna 3")