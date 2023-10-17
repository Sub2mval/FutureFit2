import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
st.set_page_config(page_title="General Statistics", page_icon="📈")

st.markdown("# General Statistics")
user = pd.read_csv("stats.csv")


st.write("## View Statistics")
y = st.selectbox('What would you like to view?', ['Calories', 'Weight'])
if y == "Weight":
    st.line_chart(user, x='Date', y='Weight')
elif y == "Calories":   
    st.line_chart(user, x='Date', y='Calories')

st.button("Re-run")
