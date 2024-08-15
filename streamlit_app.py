import pandas as pd
import requests
from io import StringIO
import altair as alt
import streamlit as st

st.title('Mental Health in the TechField 2016')



def load_original_data():
    url = 'https://raw.githubusercontent.com/TCL91/Mental-Health-Project/main/data/processed/Analysis.csv'
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_csv(StringIO(response.text))
    else:
        st.error("Failed to load data from GitHub.")
        return None
    
an = load_original_data()

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
#  Mental Health dashboard

INSERT TEXT HERE
'''
st.write("##### First Bar graph")

status_plot = (
    alt.Chart(an)
    .mark_bar()
    .encode(
        x="Would you be willing to bring up a physical health issue with a potential employer in an interview?",
        y="Physical Category",
    )
    .configure_legend(
        orient="bottom", titleFontSize=14, labelFontSize=14, titlePadding=5
    )
)
st.altair_chart(status_plot, use_container_width=True, theme="streamlit")
