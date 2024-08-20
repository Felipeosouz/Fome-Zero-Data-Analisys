import streamlit as st
st.set_page_config(layout="wide")

# Navigation
home_page = st.Page("home.py", title="Home")
cuisines_page = st.Page("cuisines.py", title="Cuisines")
country_page = st.Page("country.py", title="Country")
city_page = st.Page("city.py", title="City")
pg = st.navigation([home_page, cuisines_page, country_page, city_page])
pg.run()




# page = st.sidebar.radio("Navegação", ["Home", "Country", "City", "Cuisines"])
# st.navigation("teste")

# if page == "Home":
#     st.title("Seja bem-vindo ao Projeto de análise Fome Zero")
#     st.dataframe(df.head())
# elif page == "Country":
#     show_country_page(df)
# elif page == "City":
#     show_city_page(df)
# elif page == "Cuisines":
#     show_cuisines_page(df)

# st.sidebar.header("Filtros")

# st.sidebar.subheader("Country")
# countries = ["Mostrar todos"] + df["Country"].unique().tolist()

# country = st.sidebar.selectbox("Selecione o país: ", countries)

# min_cost, max_cost = st.sidebar.slider("Faixa de custo médio para 2: ",
#                                        float(df["Average Cost for two usd"].min()),
#                                        float(df["Average Cost for two usd"].max()),
#                                        (float(df['Average Cost for two usd'].min()), 
#                                         float(df['Average Cost for two usd'].max())))

# if country != "Mostrar todos":
#     df_filtered = df[df["Country"] == country]
# else:
#     df_filtered = df

# df_filtered = df_filtered[(df_filtered["Average Cost for two usd"] >= min_cost) & 
#                           (df_filtered["Average Cost for two usd"] <= max_cost)]

# st.header("Dataset com filtro")
# st.dataframe(df_filtered)

# st.header("Distribuição de restaurantes por tipo de culinária")

# cuisine_counts = df_filtered["Cuisines"].value_counts()

# plt.figure(figsize=(10,5))
# df_filtered["Cuisines"].value_counts().nlargest(10).plot(kind="bar")
# plt.xticks(rotation=45, ha="right")
# plt.xlabel("Tipo de culinária")
# plt.ylabel("Número de restaurantes")
# plt.title(f"Distribuição de Restaurantes por Tipo de Culinária (Filtros aplicados)")

# st.pyplot(plt)
