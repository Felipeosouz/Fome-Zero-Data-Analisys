import streamlit as st
from app import df

st.title("Fome Zero Data Analisys")
st.dataframe(df.head())