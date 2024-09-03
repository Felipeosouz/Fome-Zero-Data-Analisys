import streamlit as st
st.set_page_config(layout="wide")

# Navigation
home_page = st.Page("home.py", title="Home")
cuisines_page = st.Page("cuisines.py", title="Cuisines")
country_page = st.Page("country.py", title="Country")
city_page = st.Page("city.py", title="City")
pg = st.navigation([home_page, country_page, city_page, cuisines_page])
pg.run()

