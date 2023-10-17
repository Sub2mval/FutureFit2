import pickle
import pandas as pd
import numpy as np
import streamlit as st

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

st.set_page_config(page_title="Heart Disease Risk over Time", page_icon="📈")

st.markdown("# Heart Disease Risk over Time")
st.title("Heart Disease Risk over Time")


st.write("## View Statistics")
data_weight = df['Date', 'Risk']
st.scatter_chart(data_weight,
        x='Date',
        y='Risk',
        title='Risk of Heart Disease over time')


st.button("Re-run")