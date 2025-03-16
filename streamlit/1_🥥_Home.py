import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon=":coconut:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.subheader("About this App")
st.markdown("This Streamlit app generates vCards (Virtual Business Cards) based on user input.  It uses the [vobject](https://github.com/py-vobject/vobject) library.")