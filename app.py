
import streamlit as st

st.set_page_config(
    page_title="My AI Coder",
    page_icon="🤖"
)

st.title("🤖 My AI Coder")

st.write("Welcome to your AI Coding Assistant!")

name = st.text_input("Enter your name")

if name:
    st.success(f"Welcome {name}!")
  
