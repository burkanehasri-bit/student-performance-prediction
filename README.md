# 🎓 Student Performance Prediction

A machine learning project for analyzing student academic performance using demographic, social, and academic factors.

## 📌 Overview

This project analyzes student performance data and investigates factors that may be associated with students' final grades.

The project uses the **Student Performance dataset** from the UCI Machine Learning Repository.

The analysis focuses on understanding relationships between features such as:

- Study time
- Previous failures
- Absences
- First-period grade (G1)
- Second-period grade (G2)
- Final grade (G3)

## 🎯 Objectives

- Explore and understand the dataset
- Perform exploratory data analysis (EDA)
- Analyze relationships between student characteristics and final grades
- Visualize important patterns
- Perform correlation analysis
- Prepare the dataset for machine learning
- Develop a model for student performance prediction

## 📊 Dataset

The dataset contains information about students from two Portuguese secondary schools.

Important variables include:

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
| `G3` | Final grade |

The target variable for this project is:

**G3 — Final Grade**

## 🔎 Exploratory Data Analysis

The project includes:

- Dataset inspection
- Number of rows and columns
- Data type analysis
- Statistical analysis
- Study time vs final grade visualization
- Absences vs final grade analysis
- Correlation analysis

## 📈 Key Findings

The analysis found several interesting relationships with the final grade (`G3`).

- `G2` has a strong positive relationship with `G3`.
- `G1` also has a strong positive relationship with `G3`.
- Previous failures have a negative relationship with final performance.
- Study time has a relatively weak positive relationship with final grade.
- Absences show a very weak linear relationship with final grade in this dataset.

For example, the analysis produced approximately:

```text
Absences vs G3   :  0.034
Failures vs G3   : -0.360
Studytime vs G3  :  0.098

Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Google Colab

📁 Project Structure
student-performance-prediction/
│
├── Student_Performance_Prediction.ipynb
└── README.md

🚀 Future Improvements

The project will be extended with:

Feature engineering
Categorical feature encoding
Train/test split
Multiple machine learning models
Model comparison
MAE, MSE and R² evaluation
Final grade prediction
Interactive Streamlit application

📚 Dataset Source

UCI Machine Learning Repository — Student Performance Dataset.

👩‍💻 Author

B. Neha Sri
Jupyter Notebook
