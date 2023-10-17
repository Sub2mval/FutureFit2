import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to FutureFit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    FutureFit is a platform that allows you to track your health and fitness goals.
    **Stay Up to date with your health and fitness goals with FutureFit!**
    Track important biomarkers, such as blood pressure, heart rate, and body mass index.
"""
)
