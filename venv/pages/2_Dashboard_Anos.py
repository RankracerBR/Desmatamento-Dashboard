import streamlit as st
import pandas as pd
import plotly.express as px


DIR = 'venv/dataset/deforestation.csv'

st.title('Desmatamento(Anos)')

df = pd.read_csv(DIR)

fig_long = df.melt(id_vars="iso3c", value_vars=["forests_2000", "forests_2020"],
                   var_name="Ano", value_name="Cobertura Florestal(%)")

fig_long["Ano"] = fig_long["Ano"].replace({"forests_2000": "2000", "forests_2020": "2020"})

fig = px.bar(fig_long, x="iso3c", y="Cobertura Florestal(%)", color="Ano", barmode="group",
             title="Cobertura Florestal pelos Países(2000-2020)",
             labels={"iso3c": " País", "Cobertura Florestal(%)": "Area Florestal(%)"})

fig.update_layout(
    xaxis_title="País(iso3c)",
    yaxis_title="Cobertura Florestal(%)",
    legend_title="Ano",
)

st.plotly_chart(fig)