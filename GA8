import streamlit as st

st.write("""
# Greatest of 3 Calculator

This app calculates the largest of 3 numbers
""")
#Get Input

st.header('User Input Parameters')

def user_input_features():
    num1 = st.number_input("First Number")
    num2 = st.number_input("Second Number")
    num3 = st.number_input("Third Number")
    return max(num1,num2,num3)

if st.button("Find the Largest Number of 3"):
      largest_number = user_input_features()
      st.success(f"The largest number is: {largest_number}")
