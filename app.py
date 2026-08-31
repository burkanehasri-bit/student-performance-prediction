import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered"
)


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

@st.cache_resource
def load_model():
    return joblib.load("student_performance_pipeline.pkl")


model = load_model()


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🎓 Student Performance Predictor")

st.markdown(
    """
    Predict a student's **final academic grade (G3)** using
    demographic, study, attendance, and previous academic
    performance information.
    """
)

st.divider()


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("ℹ️ About the Model")

    st.write(
        """
        This application uses a **Random Forest Regressor**
        trained on the Student Performance Dataset.
        """
    )

    st.markdown("### 📊 Model Performance")

    st.metric("MAE", "1.022")
    st.metric("MSE", "2.806")
    st.metric("R² Score", "0.863")

    st.divider()

    st.caption(
        "Final grade is predicted on a scale from 0 to 20."
    )


# --------------------------------------------------
# STUDENT INFORMATION
# --------------------------------------------------

st.header("📋 Student Information")

col1, col2 = st.columns(2)


with col1:

    school = st.selectbox(
        "🏫 School",
        ["GP", "MS"]
    )

    sex = st.selectbox(
        "👤 Gender",
        ["F", "M"]
    )

    age = st.number_input(
        "🎂 Age",
        min_value=15,
        max_value=25,
        value=17
    )

    failures = st.number_input(
        "❌ Previous Failures",
        min_value=0,
        max_value=4,
        value=0
    )


with col2:

    studytime = st.selectbox(
        "📚 Weekly Study Time",
        [1, 2, 3, 4],
        format_func=lambda x: {
            1: "Less than 2 hours",
            2: "2–5 hours",
            3: "5–10 hours",
            4: "More than 10 hours"
        }[x]
    )

    absences = st.number_input(
        "📅 Number of Absences",
        min_value=0,
        max_value=100,
        value=5
    )

    G1 = st.number_input(
        "📝 First Period Grade (G1)",
        min_value=0,
        max_value=20,
        value=10
    )

    G2 = st.number_input(
        "📝 Second Period Grade (G2)",
        min_value=0,
        max_value=20,
        value=10
    )


st.divider()


# --------------------------------------------------
# GRADE INFORMATION
# --------------------------------------------------

st.info(
    "💡 Grades are measured on a scale from 0 to 20. "
    "G1 and G2 represent earlier period grades."
)


# --------------------------------------------------
# PREDICTION
# --------------------------------------------------

col1, col2 = st.columns(2)


with col1:

    predict_button = st.button(
        "🔮 Predict Final Grade",
        use_container_width=True
    )


with col2:

    reset_button = st.button(
        "🔄 Reset",
        use_container_width=True
    )


# --------------------------------------------------
# RESET
# --------------------------------------------------

if reset_button:

    st.rerun()


# --------------------------------------------------
# MAKE PREDICTION
# --------------------------------------------------

if predict_button:

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


    # Keep prediction within valid range

    prediction = max(
        0,
        min(20, prediction)
    )


    # --------------------------------------------------
    # DISPLAY RESULT
    # --------------------------------------------------

    st.divider()

    st.subheader("🎯 Prediction Result")

    st.metric(
        label="Predicted Final Grade (G3)",
        value=f"{prediction:.2f} / 20"
    )


    # --------------------------------------------------
    # PERFORMANCE CATEGORY
    # --------------------------------------------------

    if prediction >= 16:

        st.success(
            "🌟 Excellent performance!"
        )

        st.balloons()


    elif prediction >= 12:

        st.success(
            "👍 Good performance!"
        )


    elif prediction >= 10:

        st.warning(
            "📚 Average performance. "
            "There is room for improvement."
        )


    else:

        st.error(
            "⚠️ The student may need "
            "additional academic support."
        )


    # --------------------------------------------------
    # ADDITIONAL INFORMATION
    # --------------------------------------------------

    st.caption(
        "This prediction is generated by the trained "
        "Machine Learning model and should be treated "
        "as an estimate."
    )