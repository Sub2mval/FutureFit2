import streamlit as st
import datetime as dt  
import pandas as pd

st.set_page_config(
    page_title="Essential Health Biomarkers",
    page_icon="⚕️",
)

df = pd.read_csv("Health.csv")

st.write("# Essential Health Biomarkers")
date = st.date_input('Select Date', dt.date.today())
st.write("## Add new Value")
st.write("### Blood Pressure")
blood_pressure = st.number_input("Enter Your Blood Pressure (mm Hg):")
st.write("### Heart Rate Variability")
HeartRV = st.number_input("Enter Your Heart Rate Variablity:")
st.write("### Heart Rate")
heart_rate = st.number_input("Enter Your Heart Rate (bpm):")
st.write("### Body Temperature")
body_temperature = st.number_input("Enter Your Body Temperature (°C):")
st.write("### Respiratory Rate")
respiratory_rate = st.number_input("Enter Your Respiratory Rate (breaths per minute):")
st.write("### Oxygen Saturation")
oxygen_saturation = st.number_input("Enter Your Oxygen Saturation (%):")
st.write("### Body Mass Index")
body_mass_index = st.number_input("Enter Your Body Mass Index (kg/m²):")
st.write("### Waist Circumference")
waist_circumference = st.number_input("Enter Your Waist Circumference (cm):")
st.write("### Hip Circumference")
hip_circumference = st.number_input("Enter Your Hip Circumference (cm):")
st.write("### Waist to Hip Ratio")
waist_to_hip_ratio = st.number_input("Enter Your Waist to Hip Ratio:")
st.write("### Waist to Height Ratio")
waist_to_height_ratio = st.number_input("Enter Your Waist to Height Ratio:")
st.write("### Vo2 Max")
Vo2_Max = st.number_input("Enter Your Vo2 Max:")
if st.button("Update: "):
    df.loc[len(df.index)] = [date, blood_pressure, HeartRV, heart_rate, body_temperature, respiratory_rate, oxygen_saturation, body_mass_index, waist_circumference, hip_circumference, waist_to_hip_ratio, waist_to_height_ratio, Vo2_Max]
    df.to_csv('Health.csv')
    st.success("Value added to Health Record!")
else:
    st.info("Click on 'Update' to add your value to the Health Record.")


