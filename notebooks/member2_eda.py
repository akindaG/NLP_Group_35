import pandas as pd

# Load the new dataset from data/processed/
df = pd.read_csv("data/processed/customer_support_en.csv")

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())