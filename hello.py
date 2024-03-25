import streamlit as st
import pandas as pd
import plotly as px

st.set_page_config(
    page_title="Office vs Remote",
    page_icon="bar_chart",
    layout="wide",
)

@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Load the data
df = load_data('Correlation.csv')

fig =px.scatter(
        df, 
        x='TotalHoursAtWork (Sum)',
        y='TotalHoursWorkOut (Sum)', 
        color='Work Location',
        hover_data= 'Date',
        labels={'Work Location': 'Location','Date':'Week Ending','TotalHoursAtWork (Sum)': 'Hours At Work', 
                'TotalHoursWorkOut (Sum)': 'Output Hours'} 
    )
st.plotly_chart(fig)
