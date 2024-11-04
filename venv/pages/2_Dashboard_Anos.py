import streamlit as st
import pandas as pd
import plotly.express as px

DIR = 'venv/dataset/deforestation.csv'

st.title("Forest Coverage Comparison (2000 vs 2020)")

# Load the data
load_ = pd.read_csv(DIR)

# Reshape data to long format for Plotly Express
load_long = load_.melt(id_vars="iso3c", value_vars=["forests_2000", "forests_2020"],
                       var_name="Year", value_name="Forest Coverage (%)")

# Rename columns to improve readability
load_long["Year"] = load_long["Year"].replace({"forests_2000": "2000", "forests_2020": "2020"})

# Create grouped bar chart
fig = px.bar(load_long, x="iso3c", y="Forest Coverage (%)", color="Year", barmode="group",
             title="Forest Coverage by Country (2000 vs 2020)",
             labels={"iso3c": "Country", "Forest Coverage (%)": "Forest Area (%)"})

# Customize layout
fig.update_layout(
    xaxis_title="Country (iso3c)",
    yaxis_title="Forest Coverage (%)",
    legend_title="Year"
)

# Display the chart
st.plotly_chart(fig)
