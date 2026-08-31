import pandas as pd
import joblib
import zipfile
import urllib.request
import os

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ==========================================
# 1. Download the dataset
# ==========================================

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip"

zip_file = "student.zip"

print("Downloading dataset...")

urllib.request.urlretrieve(url, zip_file)

print("Dataset downloaded successfully!")


# ==========================================
# 2. Extract student-mat.csv
# ==========================================

with zipfile.ZipFile(zip_file, "r") as zip_ref:

    zip_ref.extract("student-mat.csv", ".")


print("Dataset extracted successfully!")


# ==========================================
# 3. Load dataset
# ==========================================

df = pd.read_csv(
    "student-mat.csv",
    sep=";"
)

print("Dataset loaded successfully!")

print("Shape:", df.shape)


# ==========================================
# 4. Select features and target
# ==========================================

features = [
    "school",
    "sex",
    "age",
    "studytime",
    "failures",
    "absences",
    "G1",
    "G2"
]

target = "G3"

X = df[features]

y = df[target]


# ==========================================
# 5. Define categorical features
# ==========================================

categorical_features = [
    "school",
    "sex"
]


# ==========================================
# 6. Define numerical features
# ==========================================

numerical_features = [
    "age",
    "studytime",
    "failures",
    "absences",
    "G1",
    "G2"
]


# ==========================================
# 7. Preprocessing
# ==========================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "numerical",
            StandardScaler(),
            numerical_features
        )
    ]
)


# ==========================================
# 8. Machine Learning model
# ==========================================

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)


# ==========================================
# 9. Complete pipeline
# ==========================================

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# ==========================================
# 10. Train/Test split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# 11. Train model
# ==========================================

print("Training model...")

pipeline.fit(
    X_train,
    y_train
)

print("Model trained successfully!")


# ==========================================
# 12. Predictions
# ==========================================

y_pred = pipeline.predict(X_test)


# ==========================================
# 13. Model evaluation
# ==========================================

mae = mean_absolute_error(
    y_test,
    y_pred
)

mse = mean_squared_error(
    y_test,
    y_pred
)

r2 = r2_score(
    y_test,
    y_pred
)


print()
print("====================================")
print("       MODEL PERFORMANCE")
print("====================================")

print("MAE :", round(mae, 3))

print("MSE :", round(mse, 3))

print("R²  :", round(r2, 3))


# ==========================================
# 14. Save model
# ==========================================

joblib.dump(
    pipeline,
    "student_performance_pipeline.pkl"
)

print()
print("====================================")
print("MODEL SAVED SUCCESSFULLY!")
print("====================================")

print("File: student_performance_pipeline.pkl")


# ==========================================
# 15. Remove temporary files
# ==========================================

if os.path.exists(zip_file):
    os.remove(zip_file)

print("Training completed!")