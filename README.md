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
