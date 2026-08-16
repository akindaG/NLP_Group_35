import sys
from pathlib import Path
import csv
import pandas as pd


# =========================================================
# Make project root importable
# =========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from src.preprocessing.pipeline import preprocess_text


# =========================================================
# Paths
# =========================================================

RAW_PATH = PROJECT_ROOT / "data" / "raw" / (
    "aa_dataset-tickets-multi-lang-5-2-50-version.csv"
)

OUTPUT_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "customer_support_en.csv"
)


# =========================================================
# Load original dataset
# =========================================================

print("=" * 60)
print("MEMBER 2 - REBUILD PROCESSED DATASET")
print("=" * 60)

print("\nLoading original dataset...")

df = pd.read_csv(RAW_PATH)

print("Original shape:", df.shape)


# =========================================================
# Filter English-language tickets
# =========================================================

df = df[df["language"] == "en"].copy()

df.reset_index(drop=True, inplace=True)

print("English ticket count:", len(df))


# =========================================================
# Create text input
# =========================================================

df["combined_text"] = (
    df["subject"].fillna("").astype(str)
    + " "
    + df["body"].fillna("").astype(str)
)


# =========================================================
# Apply existing shared preprocessing pipeline
# =========================================================

print("\nPreprocessing ticket text...")
print("This may take a little while.\n")

df["clean_text"] = df["combined_text"].apply(
    preprocess_text
)


# Temporary column is no longer required
df.drop(
    columns=["combined_text"],
    inplace=True
)


# =========================================================
# Save safely
# =========================================================

OUTPUT_PATH.parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    OUTPUT_PATH,
    index=False,
    encoding="utf-8",
    quoting=csv.QUOTE_ALL
)


# =========================================================
# Verification
# =========================================================

print("\n" + "=" * 60)
print("DATASET REBUILD COMPLETE")
print("=" * 60)

print("Saved to:")
print(OUTPUT_PATH)

print("\nFinal shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing target values:")
print("queue:", df["queue"].isnull().sum())

print("\nMissing clean_text values:")
print(df["clean_text"].isnull().sum())

print("\nQueue distribution:")
print(df["queue"].value_counts())

print("\nDone.")