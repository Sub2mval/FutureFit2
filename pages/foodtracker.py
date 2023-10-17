import streamlit as st
import datetime as dt
import numpy as np
import pandas as pd

st.set_page_config(page_title="Enter Meals", page_icon="📈")

nv = pd.read_csv("nv.csv")  # Load data
diary = pd.read_csv("user.csv")

def update_user_diary(foodname, amount, meal, heat, diary):
  for foodname in nv['Description']:
    day = dt.date.today()
    multiplier = amount/nv.loc[nv['Description']==foodname, 'Data.Household Weights.1st Household Weight'].values[0]
    carbs = nv.loc[nv['Description']==foodname, 'Data.Carbohydrate'].values[0]*multiplier
    proteins = nv.loc[nv['Description']==foodname, 'Data.Protein'].values[0]*multiplier
    fiber = nv.loc[nv['Description']==foodname, 'Data.Fiber'].values[0]*multiplier
    sugar = nv.loc[nv['Description']==foodname, 'Data.Sugar Total'].values[0]*multiplier
    fat = nv.loc[nv['Description']==foodname, 'Data.Fat.Total Lipid'].values[0]*multiplier
    saturated_fat = nv.loc[nv['Description']==foodname, 'Data.Fat.Saturated Fat'].values[0]*multiplier
    mono_fat = nv.loc[nv['Description']==foodname, 'Data.Fat.Monosaturated Fat'].values[0]*multiplier
    PUFA = nv.loc[nv['Description']==foodname, 'Data.Fat.Polysaturated Fat'].values[0]*multiplier
    calories = nv.loc[nv['Description']==foodname, 'Data.Kilocalories'].values[0]*multiplier
    diary.loc[len(diary.index)] = [day, meal, amount, carbs, fiber, sugar, fat, saturated_fat, mono_fat, PUFA, proteins, calories, heat]
    diary.to_csv('user.csv')

choice = nv['Description'].values.tolist()

st.markdown("# Food Diary")
st.write(
    """Add your current meal to the diary."""
)



st.write("## Add Meal")
foodname = st.selectbox( 'What did you eat Today', choice)
meal = st.selectbox('What meal was it?', ['Breakfast', 'Lunch', 'Dinner', 'Snack'])
amount = st.number_input('How much did you eat (in grams)?', min_value=0.0, max_value=10000.0, value=0.0, step=0.1)
heat = st.selectbox('Was it cooked?', ['Yes', 'No'])
if st.button("Add to Diary"):
        update_user_diary(foodname, amount, meal, heat, diary)
        st.success("Meal added to diary!")
else:
        st.info("Click on 'Add to Diary' to add your meal to the diary.")

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")