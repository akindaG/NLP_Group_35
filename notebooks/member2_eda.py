import pandas as pd
df = pd.read_csv(
"data/raw/aa_dataset-tickets-multi-lang-5-2-50-version.csv"
)
print(df.head())
print(df.columns.tolist())
print(df.shape)
print(df.isnull().sum())


import pandas as pd

df = pd.read_csv(
    "data/raw/aa_dataset-tickets-multi-lang-5-2-50-version.csv"
)

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns.tolist())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())