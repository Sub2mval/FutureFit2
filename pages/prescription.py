import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
st.set_page_config(page_title="Prescription", page_icon="💊")

medic_history = pd.read_csv("medic_history.csv")

def update_user_diary(start_date, end_date, medname, amount, freq, diary):
    diary.loc[len(diary.index)] = [medname, start_date, end_date, amount, freq]
    diary.to_csv('medic_history.csv')

st.write("## Update Medical Record:")
start_date = st.date_input('Select Start Date', dt.date.today())
end_date = st.date_input('Select End Date', dt.date.today())
medname = st.text_input('Medicine Name:')
amount = st.text_input('Amount of Medicine taken per dose:')
freq = st.selectbox('Frequency of Medicine:', ['Once a day', 'Twice a day', 'Thrice a day', 'Four times a day', 'Once a week', 'Twice a week', 'Thhrice a week', 'Once every two weeks', 'Once a month', 'One-time dose'])
if st.button("Add to Medical Record"):
        update_user_diary(start_date, end_date, medname, amount, freq, medic_history)
        st.success("Medicine added to Medical Record!")
