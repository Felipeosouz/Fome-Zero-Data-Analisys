import streamlit as st
import pandas as pd
import plotly.express as px

st.title("City")

# Filtros
st.sidebar.header("Filtros")

df = pd.read_csv("./data/df_tratado.csv")

countries = ["Todos os países"] + df["Country"].unique().tolist()
selected_country = st.sidebar.selectbox("Selecione o País", countries)

if selected_country == "Todos os países":
    df_country = df
    cities = ["Todas as cidades"] + df["City"].unique().tolist()
else:
    df_country = df[df["Country"] == selected_country]
    cities = df_country["City"].unique().tolist()

selected_city = st.sidebar.selectbox("Selecione a cidade: ", cities)

if selected_city == "Todas as cidades":
    df_city = df
else:
    df_city = df[df["City"] == selected_city]

st.subheader(selected_city)
# Métricas
st.title("Overral Metrics")
tab1, tab2 = st.tabs(["Visão Geral", " "])

with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("Número de Restaurantes", df_city["Restaurant ID"].nunique())
    col2.metric("Avaliação Média", round(df_city["Aggregate rating"].mean(), 2))
    col3.metric("Preço Médio para Dois (USD)", round(df_city["Average Cost for two usd"].mean(), 2))

# Gráfico de barras
df_city_restaurants = df_country.groupby('City')['Restaurant Name'].count().reset_index()
df_city_restaurants = df_city_restaurants.sort_values(by='Restaurant Name', ascending=False).head(10)

fig_barras = px.bar(df_city_restaurants, 
                    x='City', 
                    y='Restaurant Name', 
                    title='Top 10 Cidades com Maior Número de Restaurantes',
                    labels={'Restaurant Name': 'Número de Restaurantes'},
                    text='Restaurant Name')

# Adicionando os valores em cima das barras
fig_barras.update_traces(textposition='outside')

# Exibindo o gráfico
st.plotly_chart(fig_barras, use_container_width=True)

# Gráfico de dispersão
df_city_ratings = df_country.groupby('City').agg({'Votes':'sum', 'Aggregate rating':'mean'}).reset_index()
df_city_ratings = df_city_ratings.sort_values(by='Votes', ascending=False).head(10)

fig_dispersao = px.scatter(df_city_ratings, 
                           x='City', 
                           y='Aggregate rating', 
                           size='Votes', 
                           title='Avaliação Média por Cidade e Número de Avaliações',
                           labels={'Aggregate rating': 'Nota Média', 'Votes': 'Número de Avaliações'},
                           color='City',
                           size_max=60)

st.plotly_chart(fig_dispersao, use_container_width=True)

st.subheader("Observações importantes")
st.markdown("A cidade com mais restaurantes com nota média acima de 4 é Bangalore, com 79 restaurantes.")
st.markdown("A cidade com mais restaurantes com nota média abaixo de 2.5 é Gangtok, com 33 restaurantes.")
st.markdown("A cidade com o maior valor médio de um prato para dois é Pasay City, com uma média de 300.00 dolares.")
st.markdown("A cidade com a maior quantidade de tipos de culinária distintos é Birmingham, com 32 tipos distintos de culinária.")