import streamlit as st
import datetime as dt  
import pandas as pd

st.set_page_config(
    page_title="Essential Health Biomarkers over time",
    page_icon="⚕️",
)

df = pd.read_csv("Health.csv")


st.write("## View Health Record")
df = pd.read_csv("Health.csv")
st.dataframe(df)
z = st.selectbox('Select Biomarker', ['Blood Pressure', 'Heart Rate Variability', 'Heart Rate', 'Body Temperature', 'Respiratory Rate', 'Oxygen Saturation', 'Body Mass Index', 'Waist Circumference', 'Hip Circumference', 'Waist to Hip Ratio', 'Waist to Height Ratio', 'Vo2 Max'])

st.line_chart(df,
        x='Date',
        y= z,
        )
