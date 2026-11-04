
import streamlit as st

st.set_page_config(page_title="Birthday Test")

st.title("🎂 Birthday Surprise")

st.success("Your Streamlit app is working!")

name = st.text_input("Enter your name")

if st.button("Unlock Surprise"):
    st.balloons()
    st.header(f"Happy Birthday {name}! 🎉")
