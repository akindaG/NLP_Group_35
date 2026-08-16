import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.svm import SVC

# Load Data
df = pd.read_csv("data/processed/customer_support_en.csv")
X = np.load("models/member2/train_vectors.npy")
y = df["queue"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Grid Search Setup
param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf'],
    'gamma': ['scale', 'auto']
}

grid = GridSearchCV(SVC(), param_grid, cv=3, scoring='f1_weighted', verbose=1)
grid.fit(X_train, y_train)

print("Best Parameters:", grid.best_params_)
print("Best Score:", grid.best_score_)

# Save Optimized Model
joblib.dump(grid.best_estimator_, "models/member2/svm.pkl")
print("Optimized SVM model saved.")