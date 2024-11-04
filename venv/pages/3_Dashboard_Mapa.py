import streamlit as st
import pandas as pd
import plotly.express as px


DIR = 'venv/dataset/deforestation.csv'

st.title('Desmatamento(Mapa)')

fig = pd.read_csv(DIR)

botao_opcoes = st.selectbox('Selecione o Ano', ["Cobertura Florestal 2020", "Mudança Trend(2000-2020)"])

if botao_opcoes == 'Cobertura Florestal 2020':
    fig_ = px.choropleth(fig, locations='iso3c', color='forests_2020',
                         title='Cobertura Florestal 2020 (%) por País',
                         color_continuous_scale='Greens',
                         range_color=[0, 100],
                         labels={"forests_2020": "Cobertura Florestal(%)"})

else:
    fig_ = px.choropleth(fig, locations='iso3c', color='forests_2020',
                         title='Cobertura Florestal 2000-2020 (%) por País',
                         color_continuous_scale='RdYlGn',
                         range_color=[-20,20],
                         labels={"trend": "Cobertura Florestal(%)"})

fig_.update_geos(showcoastlines=True, coastlinecolor='Black', projection_type='natural earth')
fig_.update_layout(
    coloraxis_colorbar=dict(title='Cobertura Florestal (%)' if botao_opcoes == 'Cobertura Florestal 2020' else 'Trend (%)'),
    geo=dict(showframe=False, showcoastlines=True)
)

st.plotly_chart(fig_)