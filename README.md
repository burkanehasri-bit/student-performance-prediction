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
- GitHub version control

---

## 🎯 Objectives

- Analyze student performance data
- Identify useful features for prediction
- Preprocess categorical and numerical data
- Train a Machine Learning regression model
- Evaluate model performance
- Save the trained model
- Build an interactive prediction application

---

## 📊 Dataset

The project uses the **Student Performance Dataset** from the UCI Machine Learning Repository.

The dataset contains information about students from Portuguese secondary schools.

### Features

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

The following features are used:

```text
school
sex
age
studytime
failures
absences
G1
G2
```

### 3. Data Preprocessing

Categorical features are encoded using:

```text
OneHotEncoder
```

Numerical features are standardized using:

```text
StandardScaler
```

### 4. Model

The project uses:

```text
Random Forest Regressor
```

with:

```text
n_estimators = 200
random_state = 42
```

### 5. Train/Test Split

The dataset is divided into:

- 80% training data
- 20% testing data

---

## 📈 Model Performance

The Random Forest Regressor was evaluated on the test dataset.

| Metric | Score |
|---|---:|
| Mean Absolute Error (MAE) | 1.022 |
| Mean Squared Error (MSE) | 2.806 |
| R² Score | 0.863 |

### Interpretation

- **MAE = 1.022** — The average prediction error is approximately 1.02 grade points.
- **MSE = 2.806** — Measures the average squared prediction error.
- **R² = 0.863** — The model explains approximately 86.3% of the variation in final grades on the test set.

> **Note:** These results are based on an 80/20 train-test split with `random_state=42`.

---

## 🌐 Streamlit Application

The project includes an interactive Streamlit application.

Users can enter:

- School
- Gender
- Age
- Weekly study time
- Previous failures
- Absences
- First-period grade
- Second-period grade

The application predicts the student's expected final grade.

### Application Flow

```text
User Input
    ↓
Data Preprocessing
    ↓
Random Forest Model
    ↓
Predicted Final Grade
```

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib
- Seaborn
- VS Code
- Git
- GitHub

---

## 📁 Project Structure

```text
Student_Performance_Prediction/
│
├── app.py
├── train_model.py
├── student-mat.csv
├── student_performance_pipeline.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd Student_Performance_Prediction
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

---

## 🔮 Future Improvements

- Hyperparameter tuning
- Compare multiple Machine Learning algorithms
- Feature importance visualization
- Cross-validation
- Improved UI/UX
- Interactive data visualizations
- Cloud deployment
- Prediction history

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Python programming
- Data preprocessing
- Machine Learning regression
- Feature selection
- Model evaluation
- Scikit-learn pipelines
- Model serialization using Joblib
- Streamlit development
- Git and GitHub

---

## 👩‍💻 Author

**Buruka Neha Sri**

Integrated M.Tech — Computer Science and Engineering  
Computational & Data Science

---

## ⭐ Project Status

**Completed — Version 1.0**