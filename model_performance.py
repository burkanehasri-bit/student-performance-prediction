import matplotlib.pyplot as plt

metrics = ["MAE", "MSE", "R²"]
scores = [1.022, 2.806, 0.863]

plt.figure(figsize=(8, 5))
plt.bar(metrics, scores)

plt.title("Student Performance Prediction - Model Performance")
plt.xlabel("Evaluation Metrics")
plt.ylabel("Score")

for i, score in enumerate(scores):
    plt.text(i, score, f"{score:.3f}", ha="center", va="bottom")

plt.tight_layout()
plt.savefig("model_performance.png", dpi=300)
plt.show()