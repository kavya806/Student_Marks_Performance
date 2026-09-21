import streamlit as st
import pandas as pd
import joblib

st.title("Student Performance Prediction")

# Load model
model = joblib.load("model/student_performance_model.pkl")

st.write("Enter student details:")

# Inputs
attendance = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0
)

homework = st.number_input(
    "Homework Percentage",
    min_value=0.0,
    max_value=100.0
)

midterm = st.number_input(
    "Midterm Score",
    min_value=0.0,
    max_value=100.0
)

study_hours = st.number_input(
    "Study Hours per Week",
    min_value=0.0
)

# Prediction
if st.button("Predict"):

    input_data = pd.DataFrame(
        [[attendance, homework, midterm, study_hours]],
        columns=[
            "attendance_pct",
            "homework_pct",
            "midterm_score",
            "study_hours_per_week"
        ]
    )

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Prediction: PASS")
    else:
        st.error("Prediction: FAIL")
