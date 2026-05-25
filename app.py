import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)

if name:
    st.write("Hello", name)
if age:
    st.write("You are", age, "years old")

