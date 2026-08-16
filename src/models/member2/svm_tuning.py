import os
import joblib
import numpy as np
import pandas as pd

from sklearn.model_selection import (
    train_test_split,
    GridSearchCV
)

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

print("=" * 65)
print("MEMBER 2 - SVM HYPERPARAMETER TUNING")
print("=" * 65)

print("\nLoading dataset...")

df = pd.read_csv(
    DATA_PATH
)

X = np.load(
    VECTOR_PATH
)

y = df["queue"].astype(str)


print("Dataset rows:", len(df))
print("Vector shape:", X.shape)
print("Target rows:", len(y))
print("Classes:", y.nunique())


# =========================================================
# 2. Validate alignment
# =========================================================

if len(X) != len(y):

    raise ValueError(
        f"Feature/target mismatch: "
        f"{len(X)} vectors vs {len(y)} labels."
    )


# =========================================================
# 3. Train-test split
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
# 4. Hyperparameter search space
# =========================================================

param_grid = [

    {
        "kernel": ["linear"],
        "C": [0.1, 1, 10]
    },

    {
        "kernel": ["rbf"],
        "C": [0.1, 1, 10],
        "gamma": ["scale", "auto"]
    },

    {
        "kernel": ["poly"],
        "C": [0.1, 1, 10],
        "gamma": ["scale"],
        "degree": [2, 3]
    }

]


# =========================================================
# 5. GridSearchCV
# =========================================================

print("\nStarting GridSearchCV...")
print("This may take a while.\n")


grid_search = GridSearchCV(

    estimator=SVC(),

    param_grid=param_grid,

    scoring="f1_weighted",

    cv=3,

    n_jobs=-1,

    verbose=2,

    refit=True

)


grid_search.fit(
    X_train,
    y_train
)


# =========================================================
# 6. Best cross-validation configuration
# =========================================================

print("\n" + "=" * 65)
print("GRID SEARCH RESULTS")
print("=" * 65)

print(
    "\nBest Parameters:"
)

print(
    grid_search.best_params_
)

print(
    f"\nBest Cross-Validation Weighted F1: "
    f"{grid_search.best_score_:.4f}"
)


# =========================================================
# 7. Evaluate optimized model on held-out test set
# =========================================================

best_model = grid_search.best_estimator_

print("\nEvaluating best model on test set...")

y_pred = best_model.predict(
    X_test
)


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
# 8. Print final tuned SVM metrics
# =========================================================

print("\n" + "=" * 65)
print("TUNED SVM TEST RESULTS")
print("=" * 65)

print(
    f"Accuracy:           {accuracy:.4f}"
)

print(
    f"Weighted Precision: {weighted_precision:.4f}"
)

print(
    f"Weighted Recall:    {weighted_recall:.4f}"
)

print(
    f"Weighted F1:        {weighted_f1:.4f}"
)

print(
    f"Macro F1:           {macro_f1:.4f}"
)


# =========================================================
# 9. Classification report
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
# 10. Confusion matrix
# =========================================================

cm = confusion_matrix(
    y_test,
    y_pred
)

print("\nConfusion Matrix:")

print(
    cm
)


# =========================================================
# 11. Save optimized SVM
# =========================================================

os.makedirs(
    "models/member2",
    exist_ok=True
)


joblib.dump(
    best_model,
    MODEL_PATH
)


print(
    f"\nOptimized SVM saved to: "
    f"{MODEL_PATH}"
)

print(
    "\nMember 2 SVM tuning complete."
)