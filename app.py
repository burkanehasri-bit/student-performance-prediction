import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("student_performance_pipeline.pkl")


# Page configuration
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)


# Title
st.title("🎓 Student Performance Predictor")

st.write(
    "Enter the student's information below to predict their final grade."
)

st.divider()


# Student information
st.header("📋 Student Information")


school = st.selectbox(
    "School",
    ["GP", "MS"]
)


sex = st.selectbox(
    "Gender",
    ["F", "M"]
)


age = st.number_input(
    "Age",
    min_value=15,
    max_value=25,
    value=17
)


studytime = st.selectbox(
    "Weekly Study Time",
    [1, 2, 3, 4],
    format_func=lambda x: {
        1: "Less than 2 hours",
        2: "2–5 hours",
        3: "5–10 hours",
        4: "More than 10 hours"
    }[x]
)


failures = st.number_input(
    "Number of Previous Failures",
    min_value=0,
    max_value=4,
    value=0
)


absences = st.number_input(
    "Number of Absences",
    min_value=0,
    max_value=100,
    value=5
)


G1 = st.number_input(
    "First Period Grade (G1)",
    min_value=0,
    max_value=20,
    value=10
)


G2 = st.number_input(
    "Second Period Grade (G2)",
    min_value=0,
    max_value=20,
    value=10
)


st.divider()


# Prediction button
if st.button(
    "🔮 Predict Final Grade",
    use_container_width=True
):

    # Create input DataFrame
    input_data = pd.DataFrame({
        "school": [school],
        "sex": [sex],
        "age": [age],
        "studytime": [studytime],
        "failures": [failures],
        "absences": [absences],
        "G1": [G1],
        "G2": [G2]
    })


    # Make prediction
    prediction = model.predict(input_data)[0]


    # Keep grade within valid range
    prediction = max(0, min(20, prediction))


    # Display result
    st.success(
        f"🎯 Predicted Final Grade (G3): {prediction:.2f} / 20"
    )


    # Performance category
    if prediction >= 16:
        st.balloons()
        st.info("🌟 Excellent performance!")

    elif prediction >= 12:
        st.info("👍 Good performance!")

    elif prediction >= 10:
        st.warning("📚 Average performance. There is room for improvement.")

    else:
        st.error("⚠️ The student may need additional academic support.")