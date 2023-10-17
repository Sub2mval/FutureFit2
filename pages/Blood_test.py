import pickle
import pandas as pd
import numpy as np
import streamlit as st
import datetime as dt

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
user = pd.read_csv("stats.csv")
age = user['Age'].iloc[-1]
sex = user['Sex'].iloc[-1]  
if sex == "Male":
   sex = 1
else:
   sex = 0

df = pd.read_csv("Heart.csv")

st.set_page_config(page_title="Heart Disease Prediction", page_icon="📈")

st.markdown("# Heart Disease Prediction")
st.title("Heart Disease Risk Assessment")


date = st.date_input('Select Date', dt.date.today())
restbps = st.number_input("Enter Your Resting Blood Pressure (mm Hg):")

# Input field for serum cholesterol
serum_cholesterol = st.number_input("Enter Your Serum Cholesterol (mg/dl):")

# Input field for fasting blood sugar
fasting_blood_sugar = st.number_input("Enter Your Fasting Blood Sugar (mg/dl):")
if fasting_blood_sugar > 120:
    fbs = 1
else:
    fbs = 0

maximum_heart_rate = st.number_input("Enter Your Maximum Heart Rate (bpm):")



# Display results
if st.button("Predict"):
    # Calculate heart disease probability
    heart_disease_probability = loaded_model.predict_proba([[age, sex, restbps, serum_cholesterol, fbs, maximum_heart_rate]])[0][1]

    # Report fasting blood sugar status
    blood_sugar_status = "Normal" if fasting_blood_sugar <= 120 else "High"
    st.write(f"Serum Cholesterol: {serum_cholesterol} mg/dl")
    st.write(f"Fasting Blood Sugar: {fasting_blood_sugar} mg/dl (Status: {blood_sugar_status})")
    st.write(f"Heart Disease Probability: {heart_disease_probability:.2f}")
    df.loc[len(df.index)] = [date, heart_disease_probability]
    df.to_csv('Heart.csv')



st.button("Re-run")