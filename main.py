import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('notebooks/my_model.joblib')

# Title of the app
st.title("Monthly Sales Prediction App")

# Getting user inputs
st.write("Please Select a Category")
category = st.selectbox(label="Category", options=["Electronics"])

st.write("Please enter Best Seller Rank (BSR).")
bsr_input = st.text_input(label="BSR")
if st.button("Predict"):
    if bsr_input:
        try:
            bsr_input = np.array(int(bsr_input)).reshape(-1, 1)
            prediction = model.predict(bsr_input)
            st.write(f"The estimated monthly sale is {round(prediction[0])}")
        except ValueError:
            st.error("Invalid input. Please enter a valid number for BSR.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {str(e)}")
    else:
        st.error("Please enter a value for BSR.")
