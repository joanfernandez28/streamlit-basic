import streamlit as st
import altair as alt
import vega_datasets

@st.cache_data
def load_data():
    return vega_datasets.data.jobs()

jobs = load_data()

st.write(jobs)

mpg = alt.Chart(jobs).mark_bar().encode(
    alt.X('job'),
    alt.Y('average(count)')
).interactive()

sja = alt.Chart(jobs).mark_bar().encode(
    alt.X('max(count)'),
    alt.Y('sex'),
    tooltip=['sex', 'job']
).interactive()

jsp = alt.Chart(jobs).mark_bar().encode(
    alt.X('job'),
    alt.Y('perc'),
    tooltip=['sex', 'job']
).interactive()

chart = mpg
st.altair_chart(chart)

chart = sja
st.altair_chart(chart)