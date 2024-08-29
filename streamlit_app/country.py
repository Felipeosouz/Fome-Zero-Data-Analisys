import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("./data/df_tratado.csv")

st.title("Análise de restaurantes por país")


# Filtros
st.sidebar.header("Filtros")

df = pd.read_csv("./data/df_tratado.csv")

countries = ["Todos os países"] + df["Country"].unique().tolist()
selected_country = st.sidebar.selectbox("Selecione o País", countries)

if selected_country == "Todos os países":
    df_country = df
else:
    df_country = df[df["Country"] == selected_country]

# Métricas
st.subheader(f"{selected_country}")
st.subheader("Métricas Resumidas")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Número de Cidades", df_country["City"].nunique())
col2.metric("Número de Restaurantes", df_country["Restaurant ID"].nunique())
col3.metric("Avaliação Média", round(df_country["Aggregate rating"].mean(), 2))
col4.metric("Preço Médio para Dois (USD)", round(df_country["Average Cost for two usd"].mean(), 2))

# Gráfico de barras
st.subheader("Distribuição de Restaurantes por País")
country_count = df["Country"].value_counts().reset_index()
country_count.columns = ["Country", "Count"]

fig = px.bar(country_count.head(10), x="Country", y="Count", title="Top 10 Países com Mais Restaurantes",
             labels={"Country": "País", "Count": "Número de Restaurantes"},
             color_discrete_sequence=["#636EFA"])

fig.update_traces(text=country_count.head(10)["Count"], textposition="outside")
fig.update_layout(height=500, width=1000)
st.plotly_chart(fig)

# Gráfico de dispersão
col5, col6 = st.columns(2)
with col5:
    st.subheader("Avaliação Média vs Preço Médio por País")
    country_summary = df.groupby("Country").agg({
        "Average Cost for two usd": "mean",
        "Aggregate rating": "mean",
        "Votes": "sum"
    }).reset_index()

    fig2 = px.scatter(country_summary, x="Average Cost for two usd", y="Aggregate rating",
                    size="Votes", color="Country",
                    hover_name="Country", title="Avaliação vs Preço Médio por País",
                    labels={"Average Cost for two usd": "Preço Médio para Dois (USD)",
                            "Aggregate rating": "Avaliação Média"},
                            size_max=50)

    fig2.update_layout(height=500, width=600)
    st.plotly_chart(fig2)

#Gráfico de pizza
with col6:
    st.subheader("Proporção de Cidades por País")
    df_grouped = df.groupby('Country')['City'].nunique().reset_index()

    fig = px.pie(df_grouped, 
                values='City', 
                names='Country', 
                title='Proporção de Cidades por País',
                hole=0.3)

    # Exibindo o gráfico
    st.plotly_chart(fig, use_container_width=True)



