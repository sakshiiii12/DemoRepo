import streamlit as st

# Title
st.title("Addition App 🧮")

# User Inputs
num1 = st.number_input("Enter First Number")
num2 = st.number_input("Enter Second Number")

# Button
if st.button("Add"):
    result = num1 + num2
    st.success(f"Result: {result}")
