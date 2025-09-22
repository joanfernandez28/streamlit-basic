import streamlit as st
import altair as alt
import vega_datasets

@st.cache_data
def load_data():
    return vega_datasets.data.cars()

cars = load_data()

st.write(cars)

mpg = alt.Chart(cars).mark_point().encode(
    alt.X('Weight_in_lbs'),
    alt.Y('Displacement'),
    color='Origin',
    tooltip=['Name', 'Origin']
).interactive()

chart = mpg
st.altair_chart(chart)