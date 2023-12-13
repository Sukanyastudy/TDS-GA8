import streamlit as st

st.write("""
# Greatest of 3 Calculator

This app calculates the largest of 3 numbers
""")
#Get Input

st.header('User Input Parameters')
num1 = st.number_input("First Number")
num2 = st.number_input("Second Number")
num3 = st.number_input("Third Number")

if st.button("Find the Largest Number of 3"):
    
      largest_number = max(num1,num2,num3)
      st.success(f"The largest number is: {largest_number}")
