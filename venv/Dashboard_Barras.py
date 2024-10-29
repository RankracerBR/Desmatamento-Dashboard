import streamlit as st
import pandas as pd
import plotly.express as px


DIR = 'venv/dataset/deforestation.csv'

st.title("Dados Desmatamento(2000-2020)")

load_ = pd.read_csv(DIR)

st.write("Dados")
st.write(load_)

fig = px.bar(load_, x="iso3c", y="trend", color="trend",
             title="Variação percentual das florestas(2000-2020)",
             labels={"iso3c":"Country", "trend": "Mudanças(%)"},
             color_continuous_scale="RdYlGn",
             range_color=[-20,20])

fig.update_layout(
    xaxis_title="Country(iso3c)",
    yaxis_title="Trend(%)",
    coloraxis_colorbar=dict(title="Mudanças(%)")
)

st.plotly_chart(fig)