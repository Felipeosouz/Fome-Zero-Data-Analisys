import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
from app import df

st.title("Análise por país")

st.subheader("País com mais cidades registradas")
country_with_most_cities = df['Country'].value_counts().idxmax()
st.write(f"O país com mais cidades registradas é {country_with_most_cities}.")


top_10_countries = df.groupby('Country')['City'].nunique().nlargest(10).reset_index()
top_10_countries.columns = ['Country', 'Number of Cities']

# Criar o gráfico com plotly
fig = px.bar(top_10_countries, x='Country', y='Number of Cities',
                title='Top 10 Countries by Number of Cities',
                labels={'Country': 'Country', 'Number of Cities': 'Number of Cities'},
                text='Number of Cities')

# Configurar o layout do gráfico
fig.update_traces(texttemplate='%{text}', textposition='outside',
                  marker=dict(color="#0688aa", line=dict(color='black', width=0.5)),
                  width=0.8)
fig.update_layout(xaxis_title='Country',
                    yaxis_title='Number of Cities',
                    xaxis_tickangle=-45,
                    height=600)

st.plotly_chart(fig)

# st.text(f"{pais_mais_cidades} , {num_cidades_pais}")


# st.header("Distribuição de restaurantes por tipo de culinária")

# cuisine_counts = df_filtered["Cuisines"].value_counts()

# plt.figure(figsize=(10,5))
# df_filtered["Cuisines"].value_counts().nlargest(10).plot(kind="bar")
# plt.xticks(rotation=45, ha="right")
# plt.xlabel("Tipo de culinária")
# plt.ylabel("Número de restaurantes")
# plt.title(f"Distribuição de Restaurantes por Tipo de Culinária (Filtros aplicados)")

# st.pyplot(plt)