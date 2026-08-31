<<<<<<< HEAD
## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd Student_Performance_Prediction_New
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Train the model

```bash
python train_model.py
```

### 7. Run the Streamlit application

```bash
python -m streamlit run app.py
```

Then open:

```text
http://localhost:8501
```
=======
# 🎓 Student Performance Prediction

A Machine Learning project that predicts a student's final academic grade (`G3`) using demographic, study-related, attendance, and previous academic performance information.

The project includes a trained Machine Learning model and an interactive Streamlit web application.

---

## 📌 Project Overview

Student academic performance can be influenced by several factors such as study time, previous failures, attendance, and earlier examination scores.

This project uses Machine Learning to analyze these factors and predict a student's final grade.

The project was developed from scratch to gain practical experience in:

- Data handling
- Exploratory data analysis
- Feature selection
- Data preprocessing
- Machine Learning
- Model evaluation
- Model deployment
- Streamlit application development
- GitHub project management

---

## 🎯 Objectives

- Analyze student performance data
- Identify useful features for prediction
- Preprocess categorical and numerical data
- Train a Machine Learning regression model
- Evaluate model performance
- Save the trained model
- Build an interactive prediction application
- Deploy the model through Streamlit

---

## 📊 Dataset

The project uses the **Student Performance Dataset** from the UCI Machine Learning Repository.

The dataset contains information about students from Portuguese secondary schools.

For this project, the following features are used:

| Feature | Description |
|---|---|
| `school` | Student's school |
| `sex` | Student's gender |
| `age` | Student's age |
| `studytime` | Weekly study time |
| `failures` | Number of previous failures |
| `absences` | Number of school absences |
| `G1` | First-period grade |
| `G2` | Second-period grade |

### Target Variable

`G3` — Final Grade

The final grade is measured on a scale from **0 to 20**.

---

## 🧠 Machine Learning Approach

### 1. Data Loading

The dataset is downloaded and loaded using Pandas.

### 2. Feature Selection

Eight relevant features were selected:

```text
school
sex
age
studytime
failures
absences
G1
G2
>>>>>>> 6c7ba63013de8c4a18bd3b0fc8e1b4563e5b3b8a
