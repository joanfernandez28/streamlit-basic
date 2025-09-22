import streamlit as st
import altair as alt
import vega_datasets

@st.cache_data
def load_data():
    return vega_datasets.data.disasters()

disasters = load_data()

st.write(disasters)

mpg = alt.Chart(disasters).mark_point().encode(
    alt.X('Year:T'),
    alt.Y('Deaths'),
    color='Entity',
    tooltip=['Entity', 'Deaths']
).interactive()

chart = mpg
st.altair_chart(chart)