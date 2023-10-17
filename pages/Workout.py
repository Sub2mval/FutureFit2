import streamlit as st
import datetime as dt
import numpy as np
import pandas as pd

st.set_page_config(page_title="Workout Log", page_icon="📈")




st.markdown("# Workout Log")
st.sidebar.header("Workout Log")
st.write(
    """View your previous workouts."""
)


a = st.date_input('Select Date', dt.date.today())
if st.button("View Diary"):
    st.write("## View Diary")
    diary = pd.read_csv("Workout.csv")
    today = diary.loc[diary['Day']==a]
    st.dataframe(today)
else:
    st.info("Click on 'View Diary' to view your diary.")

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")