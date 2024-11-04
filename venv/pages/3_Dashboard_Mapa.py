import streamlit as st
import pandas as pd
import plotly.express as px

DIR = 'venv/dataset/deforestation.csv'

st.title("World Map of Forest Coverage Changes (2000-2020)")

# Load the data
load_ = pd.read_csv(DIR)

# Choose whether to display forest coverage or trend
option = st.selectbox("Select Data to Display:", ["Forest Coverage 2020", "Trend Change (2000-2020)"])

# Set up color scale and data for map based on user selection
if option == "Forest Coverage 2020":
    fig = px.choropleth(load_, locations="iso3c", color="forests_2020",
                        title="Forest Coverage in 2020 (%) by Country",
                        color_continuous_scale="Greens",
                        range_color=[0, 100],
                        labels={"forests_2020": "Forest Coverage (%)"})
else:
    fig = px.choropleth(load_, locations="iso3c", color="trend",
                        title="Trend Change in Forest Coverage (2000-2020) by Country",
                        color_continuous_scale="RdYlGn",
                        range_color=[-20, 20],
                        labels={"trend": "Change in Forest Area (%)"})

# Customize layout
fig.update_geos(showcoastlines=True, coastlinecolor="Black", projection_type="natural earth")
fig.update_layout(
    coloraxis_colorbar=dict(title="Forest Coverage (%)" if option == "Forest Coverage 2020" else "Trend Change (%)"),
    geo=dict(showframe=False, showcoastlines=True)
)

# Display the map
st.plotly_chart(fig)
