import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Cuisines")

# Filtros
st.sidebar.header("Filtros")

df = pd.read_csv("./data/df_tratado.csv")

countries = ["Todos os países"] + df["Country"].unique().tolist()
selected_country = st.sidebar.selectbox("Selecione o País", countries)

if selected_country == "Todos os países":
    df_country = df
else:
    df_country = df[df["Country"] == selected_country]

cuisines = ["Todas as culinárias"] + df["Cuisines"].unique().tolist()
selected_cuisine = st.sidebar.selectbox("Selecione a culinária: ", cuisines)

if selected_cuisine == "Todas as culinárias":
    df_cuisines = df    
else:
    df_cuisines = df_country[df_country["Cuisines"] == selected_cuisine]

st.subheader(selected_cuisine)
# Métricas
st.title("Overral Metrics")
tab1, tab2 = st.tabs(["Visão Geral", " "])

with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("Número de Restaurantes", df_cuisines["Restaurant ID"].nunique())
    col2.metric("Avaliação Média", round(df_cuisines["Aggregate rating"].mean(), 2))
    col3.metric("Preço Médio para Dois (USD)", round(df_cuisines["Average Cost for two usd"].mean(), 2))

# Gráfico de barras
cuisine_counts = df_country['Cuisines'].value_counts().reset_index()
cuisine_counts.columns = ['Cuisines', 'Count']

fig1 = px.bar(cuisine_counts.head(10), 
              x='Cuisines', 
              y='Count', 
              title='Top 10 Tipos de Culinária com Mais Restaurantes', 
              labels={'Cuisines': 'Tipo de Culinária', 'Count': 'Quantidade de Restaurantes'},
              text='Count')

st.plotly_chart(fig1)

# Gráfico de pizza
cuisine_ratings = df_country.groupby('Cuisines')['Aggregate rating'].mean().reset_index()
cuisine_ratings.columns = ['Cuisines', 'Average Rating']

top_10_cuisines = cuisine_ratings.sort_values(by='Average Rating', ascending=False).head(10)

fig2 = px.pie(top_10_cuisines, 
              values='Average Rating', 
              names='Cuisines', 
              title='Top 10 Tipos de Culinária por Média de Avaliações',
              labels={'Average Rating': 'Média de Avaliações', 'Cuisines': 'Tipo de Culinária'},
              hole=0.3)

st.plotly_chart(fig2)

st.subheader("Observações importantes")

culinaria_maior_custo = df.loc[df['Average Cost for two usd'].idxmax(), 'Cuisines']
maior_custo = df["Average Cost for two usd"].max()

st.markdown(f"A culinária com maior custo é {culinaria_maior_custo}, com uma nota média de {maior_custo:.2f} dólares.")

culinaria_maior_nota = df.loc[df['Aggregate rating'].idxmax(), 'Cuisines']
maior_nota = df["Aggregate rating"].max()

st.markdown(f"A culinária com maior nota é {culinaria_maior_nota}, com uma nota média de {maior_nota:.2f}.")

restaurantes_online_entregas = df[(df['Has Online delivery'] == 1) & (df['Is delivering now'] == 1)]

culinarias_count = restaurantes_online_entregas['Cuisines'].value_counts()

tipo_culinaria_mais_restaurantes = culinarias_count.idxmax()
numero_restaurantes = culinarias_count.max()

st.markdown(f"O tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas é '{tipo_culinaria_mais_restaurantes}', com {numero_restaurantes} restaurantes.")





