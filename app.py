import streamlit as st
import joblib

# Load model
model = joblib.load("teja.pkl")

st.title("Student Performance Predictor")

# Inputs
hours = st.number_input("Study Hours", min_value=0.0)
attendance = st.number_input("Attendance %", min_value=0.0, max_value=100.0)

if st.button("Predict"):
    prediction = model.predict([[hours, attendance]])
    st.success(f"Predicted Result: {prediction[0]}")