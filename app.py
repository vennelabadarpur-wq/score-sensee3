import streamlit as st
import joblib
import os

# Load model safely
try:
    model_path = os.path.join(os.path.dirname(__file__), "teja.pkl")
    model = joblib.load(model_path)
except Exception as e:
    st.error(f"Model failed to load: {e}")
    model = None

st.title("🎓 Student GPA Predictor")

# Integer Inputs
study = st.number_input("📚 Study Hours", min_value=0, step=1, format="%d")
social = st.number_input("📱 Social Media Hours", min_value=0, step=1, format="%d")
attendance = st.number_input("🏫 Attendance %", min_value=0, max_value=100, step=1, format="%d")
sleep = st.number_input("😴 Sleep Hours", min_value=0, step=1, format="%d")

# Predict Button
if st.button("🚀 Predict GPA"):
    if model is not None:
        try:
            # Force inputs to int
            inputs = [[int(study), int(social), int(attendance), int(sleep)]]
            prediction = model.predict(inputs)

            # Convert to GPA 0–10
            gpa = round(max(0, min(prediction[0] / 10, 10)), 2)
            st.success(f"🎯 Predicted GPA: {gpa}")

            # Advice
            if gpa < 5:
                st.error("⚠️ Increase study & sleep")
            elif gpa < 7:
                st.warning("👍 Can improve attendance")
            else:
                st.balloons()
                st.success("🎉 Excellent performance!")
        except Exception as e:
            st.error(f"Prediction failed: {e}")
    else:
        st.error("Model not loaded!")
