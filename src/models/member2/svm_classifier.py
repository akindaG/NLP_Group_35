import os
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix

# 1. Load Data and Embeddings
df = pd.read_csv("data/processed/customer_support_en.csv")
X = np.load("models/member2/train_vectors.npy")
y = df["queue"]  # Using 'queue' as ticket classification target

# 2. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 3. Train Base SVM
svm_clf = SVC(kernel="rbf", C=1.0)
svm_clf.fit(X_train, y_train)

# 4. Predict & Evaluate
y_pred = svm_clf.predict(X_test)
print("SVM Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 5. Save Model
joblib.dump(svm_clf, "models/member2/svm.pkl")
print("SVM classifier saved to models/member2/svm.pkl.")