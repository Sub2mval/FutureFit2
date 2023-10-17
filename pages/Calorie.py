import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
st.set_page_config(page_title="General Statistics", page_icon="📈")

st.markdown("# General Statistics")
user = pd.read_csv("stats.csv")

def main(gender, weight, height, age, activity_lvl):
    rest_bmr = calculate_bmr(gender, weight, height, age) 
    calc = total_calculation(rest_bmr, activity_lvl)
    day = dt.date.today()
    user.loc[len(user.index)] = [day, height, weight, gender, activity_lvl, age, calc]
    user.to_csv('stats.csv')
    return print("Your estimated maintainence calories is:", calc)



def calculate_bmr(gender, weight, height, age):
    if gender == "female":
        women = (weight * 10) + (height * 6.25) - (age * 5) - 161
        return int(women)
    else:
        men = (weight * 10) + (height * 6.25) - (age * 5) + 5
        return int(men)



def total_calculation(rest_bmr, activity_lvl):
    user_activity_lvl = activity_lvl    

    maintain = {
      "sedentary" : get_sedentary(rest_bmr), 
      "light" : get_light_activity(rest_bmr), 
      "moderate" : get_moderate_activity(rest_bmr), 
      "active" : get_very_active(rest_bmr)
      }

    if user_activity_lvl == "sedentary":
        return maintain["sedentary"]

    if user_activity_lvl == "light":
        return maintain["light"]

    if user_activity_lvl == "moderate":
        return maintain["moderate"]

    if user_activity_lvl == "active":
        return maintain["active"]




def get_sedentary(rest_bmr):
    sedentary = rest_bmr * 1.25
    return sedentary

def get_light_activity(rest_bmr):
    light = rest_bmr * 1.375
    return light

def get_moderate_activity(rest_bmr):
    moderate = rest_bmr * 1.550
    return moderate

def get_very_active(rest_bmr):
    active = rest_bmr * 1.725
    return active


st.write("## Update Statistics")
height = st.number_input('Enter your height in Centimeters: ', min_value=0.0, max_value=10000.0, value=0.0, step=0.1)
weight = st.number_input('Enter your weight in kilograms: ', min_value=0.0, max_value=10000.0, value=0.0, step=0.1)
gender = st.selectbox('Please select your biological sex: ', ['male', 'female'])
age = st.number_input('Enter your age in years: ', min_value=0.0, max_value=120.0, value=0.0, step=0.1)
activity_lvl = st.selectbox('What is your activity level?', ['sedentary', 'light', 'moderate', 'active'])
if st.button("Update Statistics"):
    st.success("Statistics Updated!")
    st.write("## Your daily calorie intake is: ")
    main(gender, weight, height, age, activity_lvl)
else:
    st.info("Click on 'Update Statistics' to update your statistics.")  


st.button("Re-run")
