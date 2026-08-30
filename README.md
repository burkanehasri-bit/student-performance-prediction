# 🎓 Student Performance Prediction

A Machine Learning project that analyzes student academic performance and identifies factors associated with final grades.

## 📌 Project Overview

This project uses the **Student Performance Dataset** from the UCI Machine Learning Repository.

The dataset contains demographic, social, and academic information about students from Portuguese secondary schools.

The main goal is to understand which factors are associated with students' final academic performance and prepare the data for machine learning-based prediction.

## 🎯 Objectives

- Understand and explore the student performance dataset
- Perform Exploratory Data Analysis (EDA)
- Analyze relationships between student characteristics and final grades
- Visualize important patterns
- Perform correlation analysis
- Identify important factors affecting student performance
- Prepare the dataset for machine learning
- Build a model to predict final student performance

## 📊 Dataset

The dataset contains information about students from two Portuguese secondary schools.

### Important Features

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

### 🎯 Target Variable

**`G3` — Final Grade**

The final grade ranges from 0 to 20.

## 🔎 Exploratory Data Analysis

The project currently includes:

- Dataset loading
- Dataset inspection
- First few records analysis
- Number of rows and columns
- Data type analysis
- Statistical analysis
- Study time vs final grade visualization
- Absences vs final grade analysis
- Correlation analysis

## 📈 Key Findings

The exploratory analysis produced the following observations:

- **G2 has a very strong positive relationship with G3.**
- **G1 also has a strong positive relationship with G3.**
- Previous failures have a **negative relationship** with final performance.
- Study time has a **weak positive relationship** with final grade.
- Absences have a **very weak linear relationship** with final grade in this dataset.

### Correlation Results

| Feature | Correlation with G3 |
|---|---:|
| `G2` | ~0.905 |
| `G1` | ~0.801 |
| `failures` | ~-0.360 |
| `studytime` | ~0.098 |
| `absences` | ~0.034 |

> **Note:** Correlation shows linear association, not causation.

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **Google Colab**
- **Jupyter Notebook**

## 📁 Project Structure

```text
student-performance-prediction/
│
├── Student_Performance_Prediction.ipynb
└── README.md
