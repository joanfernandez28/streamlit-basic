import streamlit as st


disasters = st.Page("disasters.py", title="Disasters", icon=":material/add_circle:")
cars = st.Page("cars.py", title="Cars", icon=":material/add_circle:")

pg = st.navigation([disasters,cars])
st.set_page_config(
    page_title="Streamlit | Joan",
    page_icon="J",
    initial_sidebar_state="expanded"
)

pg.run()