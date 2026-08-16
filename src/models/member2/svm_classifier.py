import os
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


# =========================================================
# Configuration
# =========================================================

DATA_PATH = "data/processed/customer_support_en.csv"
VECTOR_PATH = "models/member2/train_vectors.npy"
MODEL_PATH = "models/member2/svm.pkl"


# =========================================================
# 1. Load dataset
# =========================================================

print("=" * 60)
print("MEMBER 2 - SVM BASELINE")
print("=" * 60)

print("\nLoading processed dataset...")

df = pd.read_csv(DATA_PATH)

print("Dataset shape:", df.shape)


# =========================================================
# 2. Load Word2Vec sentence embeddings
# =========================================================

print("\nLoading Word2Vec sentence vectors...")

X = np.load(VECTOR_PATH)

print("Vector shape:", X.shape)


# =========================================================
# 3. Prepare target labels
# =========================================================

y = df["queue"].astype(str)

print("Target samples:", len(y))
print("Number of classes:", y.nunique())

print("\nClasses:")
for queue_name in sorted(y.unique()):
    print("-", queue_name)


# =========================================================
# 4. Verify feature/target alignment
# =========================================================

if len(X) != len(y):
    raise ValueError(
        f"Feature/target mismatch: "
        f"{len(X)} vectors vs {len(y)} labels."
    )

print("\nFeature and target lengths match.")


# =========================================================
# 5. Train-test split
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# =========================================================
# 6. Build baseline SVM
# =========================================================

print("\nTraining baseline SVM...")

svm_model = SVC(
    kernel="rbf",
    C=1.0,
    gamma="scale"
)


# =========================================================
# 7. Train
# =========================================================

svm_model.fit(
    X_train,
    y_train
)

print("SVM training complete.")


# =========================================================
# 8. Predict
# =========================================================

print("\nGenerating predictions...")

y_pred = svm_model.predict(X_test)


# =========================================================
# 9. Evaluation metrics
# =========================================================

accuracy = accuracy_score(
    y_test,
    y_pred
)

weighted_precision = precision_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

weighted_recall = recall_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

weighted_f1 = f1_score(
    y_test,
    y_pred,
    average="weighted",
    zero_division=0
)

macro_f1 = f1_score(
    y_test,
    y_pred,
    average="macro",
    zero_division=0
)


# =========================================================
# 10. Print results
# =========================================================

print("\n" + "=" * 60)
print("SVM RESULTS")
print("=" * 60)

print(f"Accuracy:           {accuracy:.4f}")
print(f"Weighted Precision: {weighted_precision:.4f}")
print(f"Weighted Recall:    {weighted_recall:.4f}")
print(f"Weighted F1:        {weighted_f1:.4f}")
print(f"Macro F1:           {macro_f1:.4f}")


# =========================================================
# 11. Classification report
# =========================================================

print("\nClassification Report:\n")

print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


# =========================================================
# 12. Confusion matrix
# =========================================================

cm = confusion_matrix(
    y_test,
    y_pred
)

print("Confusion Matrix:")
print(cm)


# =========================================================
# 13. Save model
# =========================================================

os.makedirs(
    "models/member2",
    exist_ok=True
)

joblib.dump(
    svm_model,
    MODEL_PATH
)

print(
    f"\nSVM model saved successfully to {MODEL_PATH}"
)

print("\nMember 2 SVM baseline complete.")