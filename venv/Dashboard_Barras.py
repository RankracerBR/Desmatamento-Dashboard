import streamlit as st
import pandas as pd
import plotly.express as px


DIR = 'venv/dataset/deforestation.csv'

st.title('Desmatamento')

df = pd.read_csv(DIR)

st.write("Dados")
st.write(df)

fig = px.bar(df, x="iso3c", y="trend", color="trend",
             title="Variação percentual das florestas(2000-2020)",
             color_continuous_scale='RdYlGn',
             range_color=[-20,20])

fig.update_layout(
    xaxis_title='Países(iso3c)',
    yaxis_title='Trend(%)',
    coloraxis_colorbar=dict(title='Mudanças(%)')
)

st.plotly_chart(fig)