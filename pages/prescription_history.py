import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
st.set_page_config(page_title="Prescription History", page_icon="💊")

st.markdown("# Prescription History")


medic_history = pd.read_csv("medic_history.csv")
st.dataframe(medic_history)
