# @TODO: Import the libraries for Pandas and Streamlit
import streamlit as st
import pandas as pd

# @TODO: Create a title for your application using markdown syntax and the
# Streamlit `write` function.
st.write("#Johnathan can do it and so can You!")

# @TODO: Create an opening sentence for your application using regular text and
# the Streamlit `write` function.
st.write("Thank you for viewing my application!")

# @TODO: Create a Pandas dataframe
df = pd.DataFrame({'col1': [4, 3, 8], 'col2': [9, 5 ,1], 'col3': [2, 7, 6]})

# @TODO: Write the Pandas dataframe to the page
st.write(df)

# @TODO: Create a text input box using the Streamlit `text_input` function.
# @TODO: Save the input as a variable.

input_value = st.text_area("Leave a Kind Remark")

# @TODO: Utilize the Streamlit `button` function to display the text input
# variable created in the prior step to the page.
# YOUR CODE HERE!

if st.button("Display Message"):
    st.write(input_value)

# Bonus


st.sidebar.radio(
    label="Pick Your Favorite!",
    options=["Laser Tag", "Ax Throwing", "Trampoline Park"]
)

selectbox = st.selectbox(
    "Select a salary",
    ["Free", "40k", '320k']
)

st.write(f"You selected {selectbox}")