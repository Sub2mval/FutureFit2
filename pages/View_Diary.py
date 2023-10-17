import streamlit as st
import datetime as dt
import numpy as np
import pandas as pd

st.set_page_config(page_title="View Meals", page_icon="📈")

nv = pd.read_csv("nv.csv")  # Load data
diary = pd.read_csv("user.csv")



choice = nv['Description'].values.tolist()

st.markdown("# Food Diary")
st.write(
    """View your previous meals."""
)


a = st.date_input('Select Date', dt.date.today())
st.write("## View Diary")
diary = pd.read_csv("user.csv")
today = diary.loc[diary['Date']==a]
st.dataframe(today)
if today['heat'] == "Yes":
    if today['PUFA'].sum() >= 5.0:
     st.write("Heating Polyunsaturated Fatty Acids can cause them to oxidize and become harmful to your health. Try to avoid heating foods with high PUFA content.")


# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")