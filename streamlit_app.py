import pandas as pd
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px 
import matplotlib as mpl

import re as re

import seaborn as sns
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
# # st.write("##### First Bar graph using Alt")


# # status_plot = alt.Chart(an).mark_bar().encode(
# #     x="Would you be willing to bring up a physical health issue with a potential employer in an interview?",
# #     y="Physical Category"
# # ).properties(height=700)


# st.write("##### First Bar graph using Simple")
# st.bar_chart(an, x="Would you be willing to bring up a physical health issue with a potential employer in an interview?", y="Physical Category")

st.write("##### Figured out how to take the graph from analysis to streamlit but not interactive using chatgpt")
    
   # Streamlit app
def main():
    st.title('Physical Health Issues During an Interview')

    # Group by Physical Category and Issue Type, then get size
    grouped = an.groupby(['Physical Category', an.iloc[:,36]]).size()

    # Create the bar chart
    fig, ax = plt.subplots()
    grouped.plot(kind='barh', ax=ax, title='Bringing up Physical Health Issues During an Interview')
    ax.set_xlabel('Count')
    ax.set_ylabel('Category')
    
    # Show the plot in Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()


st.write("##### Now make it interactive")



# Streamlit app
def main():
    st.title('Interactive Physical Health Issues During an Interview')

    # Create sidebar for user input
    st.sidebar.header('Filter Options')
    
    # Dropdown to select Physical Category
    physical_category = st.sidebar.selectbox(
        'Select Physical Category:',
        options=an['Physical Category'].unique()
    )
    
    # Filter DataFrame based on selected Physical Category
    filtered_an = an[an['Physical Category'] == physical_category]

    # Group by Physical Category and Issue Type, then get size
    grouped = filtered_an.groupby(['Physical Category', 'Issue Type']).size().reset_index(name='Count')

    # Create the bar chart using Plotly
    fig = px.bar(
        grouped,
        x='Count',
        y='Issue Type',
        color='Issue Type',
        title=f'Bringing up Physical Health Issues for {physical_category}',
        labels={'Count': 'Count', 'Issue Type': 'Issue Type'},
        orientation='h'  # Horizontal bar chart
    )

    # Show the plot in Streamlit
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
