import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

df = pd.read_csv("./data/df_tratado.csv")

num_restaurantes = df['Restaurant Name'].nunique()
num_paises = df['Country'].nunique()
num_cidades = df['City'].nunique()
total_avaliacoes = df['Votes'].sum()
num_culinarias = df['Cuisines'].nunique()

st.title("Fome Zero Data Analisys")
st.subheader("Descrição")
st.markdown("A Fome Zero conecta clientes e restaurantes, oferecendo um espaço onde os restaurantes podem se cadastrar e exibir informações relevantes, como tipo de culinária, possibilidade de reservas, serviço de entrega, avaliações, entre outros. A análise visa identificar pontos-chave para auxiliar na tomada de decisões estratégicas.")
st.title("Overral Metrics")
tab1, tab2 = st.tabs(["Visão Geral", " "])

with tab1:
    with st.container():

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            col1.metric('Restaurants',value=num_restaurantes)
        with col2:
            col2.metric("Countries", value=num_paises)
        with col3:
            col3.metric("Cities", value=num_cidades)
        with col4:
            col4.metric("Cuisines", value=num_culinarias)
        with col5:
            col5.metric("Votes", value=total_avaliacoes)


with st.container():
    st.subheader("Restaurant Location Map")
    df_map = df.loc[:,['Restaurant ID','Restaurant Name','City','Longitude','Latitude','Price range','Aggregate rating','Rating color']]
    map_ = folium.Map(location=[0, 0], zoom_start=3, tiles="Cartodb Positron")

    marker_cluster = MarkerCluster().add_to(map_)

    for i in range(len(df_map)):
        popup_content = (
            f"Id: {df_map.loc[i, "Restaurant ID"]}<br>"
            f"Name: {df_map.loc[i, "Restaurant Name"]}<br>"
            f"Rating: {df_map.loc[i, "Aggregate rating"]}"
        )

        folium.Marker(
            location=[ df_map.loc[ i,'Latitude' ] , df_map.loc[ i,'Longitude' ] ],
            popup=folium.Popup(popup_content, max_width=300),
            icon=folium.Icon(color=df_map.loc[i,'Rating color'], icon='home'),
        ).add_to(marker_cluster)

    folium_static(map_, width=1100, height=800)
