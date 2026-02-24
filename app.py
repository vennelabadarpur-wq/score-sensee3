import streamlit as st
import joblib

# Load model (saved using joblib)
model = joblib.load("teja.pkl")

st.title("🎓 Student GPA Predictor")

study = st.number_input("📚 Study Hours", min_value=0, step=1, format="%d")
social = st.number_input("📱 Social Media Hours", min_value=0, step=1, format="%d")
attendance = st.number_input("🏫 Attendance %", min_value=0, max_value=100, step=1, format="%d")
sleep = st.number_input("😴 Sleep Hours", min_value=0, step=1, format="%d")

if st.button("🚀 Predict GPA"):

    prediction = model.predict([[study, social, attendance, sleep]])

    # Convert to GPA scale
    gpa = round(max(0, min(prediction[0] / 10, 10)), 2)

    st.success(f"🎯 Predicted GPA: {gpa}")

    if gpa < 5:
        st.error("⚠️ Increase study & sleep")
    elif gpa < 7:
        st.warning("👍 Can improve attendance")
    else:
        st.balloons()
        st.success("🎉 Excellent performance!")
