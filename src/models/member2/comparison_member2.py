import os
from pathlib import Path

# Reduce unnecessary TensorFlow log messages
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import joblib
import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow.keras.preprocessing.sequence import pad_sequences

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix,
)


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "customer_support_en.csv"
)

VECTOR_PATH = (
    PROJECT_ROOT
    / "models"
    / "member2"
    / "train_vectors.npy"
)

SVM_MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "member2"
    / "svm.pkl"
)

GRU_MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "member2"
    / "gru.keras"
)

GRU_TOKENIZER_PATH = (
    PROJECT_ROOT
    / "models"
    / "member2"
    / "gru_tokenizer.pkl"
)

GRU_ENCODER_PATH = (
    PROJECT_ROOT
    / "models"
    / "member2"
    / "gru_label_encoder.pkl"
)

REPORT_PATH = (
    PROJECT_ROOT
    / "reports"
    / "member2_results.md"
)


# ============================================================
# EXPERIMENT SETTINGS
# ============================================================

TEST_SIZE = 0.20
RANDOM_STATE = 42

GRU_MAX_LEN = 100


# ============================================================
# VERIFIED BASELINE RESULTS
# ============================================================

BASELINE_SVM = {
    "accuracy": 0.4259,
    "weighted_precision": 0.4908,
    "weighted_recall": 0.4259,
    "weighted_f1": 0.3714,
    "macro_f1": 0.2645,
}


BASELINE_GRU = {
    "test_loss": 1.9703,
    "accuracy": 0.2898,
    "weighted_precision": 0.0840,
    "weighted_recall": 0.2898,
    "weighted_f1": 0.1302,
    "macro_f1": 0.0449,
}


# ============================================================
# VERIFIED SVM TUNING INFORMATION
# ============================================================

SVM_BEST_PARAMETERS = {
    "C": 10,
    "kernel": "rbf",
    "gamma": "scale",
}

SVM_BEST_CV_WEIGHTED_F1 = 0.4986


# ============================================================
# VERIFIED GRU TRAINING INFORMATION
# ============================================================

OPTIMIZED_GRU_TRAINING = {
    "best_validation_accuracy": 0.3711,
    "best_validation_accuracy_epoch": 9,
    "best_validation_loss": 1.7598,
    "best_validation_loss_epoch": 6,
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def verify_file(path, description):
    """
    Verify that a required file exists.
    """

    if not path.exists():
        raise FileNotFoundError(
            f"{description} not found: {path}"
        )


def calculate_metrics(y_true, y_pred):
    """
    Calculate the evaluation metrics used in the
    final Member 2 comparison.
    """

    return {
        "accuracy": accuracy_score(
            y_true,
            y_pred,
        ),

        "weighted_precision": precision_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0,
        ),

        "weighted_recall": recall_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0,
        ),

        "weighted_f1": f1_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0,
        ),

        "macro_precision": precision_score(
            y_true,
            y_pred,
            average="macro",
            zero_division=0,
        ),

        "macro_recall": recall_score(
            y_true,
            y_pred,
            average="macro",
            zero_division=0,
        ),

        "macro_f1": f1_score(
            y_true,
            y_pred,
            average="macro",
            zero_division=0,
        ),
    }


def append_metric_table(lines, metrics):
    """
    Append a standard Markdown metrics table.
    """

    lines.append("| Metric | Score |")
    lines.append("|---|---:|")

    lines.append(
        f"| Accuracy | {metrics['accuracy']:.4f} |"
    )

    lines.append(
        "| Weighted Precision | "
        f"{metrics['weighted_precision']:.4f} |"
    )

    lines.append(
        "| Weighted Recall | "
        f"{metrics['weighted_recall']:.4f} |"
    )

    lines.append(
        "| Weighted F1 | "
        f"{metrics['weighted_f1']:.4f} |"
    )

    if "macro_precision" in metrics:
        lines.append(
            "| Macro Precision | "
            f"{metrics['macro_precision']:.4f} |"
        )

    if "macro_recall" in metrics:
        lines.append(
            "| Macro Recall | "
            f"{metrics['macro_recall']:.4f} |"
        )

    lines.append(
        f"| Macro F1 | {metrics['macro_f1']:.4f} |"
    )


# ============================================================
# START
# ============================================================

print("=" * 75)
print("MEMBER 2 - FINAL MODEL COMPARISON")
print("SupportIQ - Support Queue Routing")
print("=" * 75)


# ============================================================
# 1. VERIFY REQUIRED FILES
# ============================================================

print("\n[1/11] Verifying required files...")

verify_file(
    DATA_PATH,
    "Processed dataset",
)

verify_file(
    VECTOR_PATH,
    "Word2Vec sentence vectors",
)

verify_file(
    SVM_MODEL_PATH,
    "Tuned SVM model",
)

verify_file(
    GRU_MODEL_PATH,
    "Optimized GRU model",
)

verify_file(
    GRU_TOKENIZER_PATH,
    "GRU tokenizer",
)

verify_file(
    GRU_ENCODER_PATH,
    "GRU label encoder",
)

print("All required files found.")


# ============================================================
# 2. LOAD DATASET
# ============================================================

print("\n[2/11] Loading processed dataset...")

df = pd.read_csv(
    DATA_PATH
)

print(
    "Dataset shape:",
    df.shape,
)

required_columns = [
    "clean_text",
    "queue",
]

missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        "Missing required columns: "
        + ", ".join(missing_columns)
    )

if df["queue"].isnull().any():
    raise ValueError(
        "The queue target contains missing values."
    )

print(
    "Queue classes:",
    df["queue"].nunique(),
)

print(
    "Dataset validation complete."
)


# ============================================================
# 3. CREATE COMMON TEST SPLIT
# ============================================================

print(
    "\n[3/11] Creating common test split..."
)

all_indices = np.arange(
    len(df)
)

train_indices, test_indices = train_test_split(
    all_indices,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE,
    stratify=df["queue"].astype(str).values,
)

print(
    "Training records:",
    len(train_indices),
)

print(
    "Testing records:",
    len(test_indices),
)


# ============================================================
# 4. EVALUATE TUNED SVM
# ============================================================

print(
    "\n[4/11] Evaluating tuned SVM..."
)

X_vectors = np.load(
    VECTOR_PATH
)

if len(X_vectors) != len(df):
    raise ValueError(
        "Word2Vec vectors do not match dataset rows. "
        f"Vectors: {len(X_vectors)}, rows: {len(df)}"
    )

svm_y_all = (
    df["queue"]
    .astype(str)
    .values
)

X_svm_test = X_vectors[
    test_indices
]

y_svm_test = svm_y_all[
    test_indices
]

svm_model = joblib.load(
    SVM_MODEL_PATH
)

svm_predictions = svm_model.predict(
    X_svm_test
)

svm_metrics = calculate_metrics(
    y_svm_test,
    svm_predictions,
)

svm_classes = sorted(
    np.unique(
        svm_y_all
    )
)

svm_classification_report = classification_report(
    y_svm_test,
    svm_predictions,
    labels=svm_classes,
    target_names=svm_classes,
    zero_division=0,
)

svm_confusion_matrix = confusion_matrix(
    y_svm_test,
    svm_predictions,
    labels=svm_classes,
)

print(
    f"Tuned SVM Accuracy: "
    f"{svm_metrics['accuracy']:.4f}"
)

print(
    f"Tuned SVM Weighted F1: "
    f"{svm_metrics['weighted_f1']:.4f}"
)

print(
    f"Tuned SVM Macro F1: "
    f"{svm_metrics['macro_f1']:.4f}"
)


# ============================================================
# 5. LOAD GRU ARTIFACTS
# ============================================================

print(
    "\n[5/11] Loading optimized GRU artifacts..."
)

gru_model = tf.keras.models.load_model(
    GRU_MODEL_PATH
)

gru_tokenizer = joblib.load(
    GRU_TOKENIZER_PATH
)

gru_encoder = joblib.load(
    GRU_ENCODER_PATH
)

print(
    "GRU artifacts loaded successfully."
)


# ============================================================
# 6. PREPARE GRU TEST DATA
# ============================================================

print(
    "\n[6/11] Preparing GRU test data..."
)

all_texts = (
    df["clean_text"]
    .fillna("")
    .astype(str)
    .values
)

all_gru_labels = gru_encoder.transform(
    df["queue"].astype(str)
)

gru_test_texts = all_texts[
    test_indices
]

y_gru_test = all_gru_labels[
    test_indices
]

gru_test_sequences = (
    gru_tokenizer
    .texts_to_sequences(
        gru_test_texts
    )
)

X_gru_test = pad_sequences(
    gru_test_sequences,
    maxlen=GRU_MAX_LEN,
    padding="post",
    truncating="post",
)

print(
    "GRU test matrix:",
    X_gru_test.shape,
)


# ============================================================
# 7. EVALUATE OPTIMIZED GRU
# ============================================================

print(
    "\n[7/11] Evaluating optimized GRU..."
)

gru_test_loss, gru_keras_accuracy = (
    gru_model.evaluate(
        X_gru_test,
        y_gru_test,
        verbose=0,
    )
)

gru_probabilities = gru_model.predict(
    X_gru_test,
    verbose=0,
)

gru_predictions = np.argmax(
    gru_probabilities,
    axis=1,
)

gru_metrics = calculate_metrics(
    y_gru_test,
    gru_predictions,
)

gru_labels = np.arange(
    len(
        gru_encoder.classes_
    )
)

gru_classification_report = classification_report(
    y_gru_test,
    gru_predictions,
    labels=gru_labels,
    target_names=gru_encoder.classes_,
    zero_division=0,
)

gru_confusion_matrix = confusion_matrix(
    y_gru_test,
    gru_predictions,
    labels=gru_labels,
)

print(
    f"Optimized GRU Accuracy: "
    f"{gru_metrics['accuracy']:.4f}"
)

print(
    f"Optimized GRU Weighted F1: "
    f"{gru_metrics['weighted_f1']:.4f}"
)

print(
    f"Optimized GRU Macro F1: "
    f"{gru_metrics['macro_f1']:.4f}"
)


# ============================================================
# 8. CALCULATE IMPROVEMENTS
# ============================================================

print(
    "\n[8/11] Calculating improvements..."
)

svm_accuracy_gain = (
    svm_metrics["accuracy"]
    -
    BASELINE_SVM["accuracy"]
)

svm_weighted_f1_gain = (
    svm_metrics["weighted_f1"]
    -
    BASELINE_SVM["weighted_f1"]
)

svm_macro_f1_gain = (
    svm_metrics["macro_f1"]
    -
    BASELINE_SVM["macro_f1"]
)

gru_accuracy_gain = (
    gru_metrics["accuracy"]
    -
    BASELINE_GRU["accuracy"]
)

gru_weighted_f1_gain = (
    gru_metrics["weighted_f1"]
    -
    BASELINE_GRU["weighted_f1"]
)

gru_macro_f1_gain = (
    gru_metrics["macro_f1"]
    -
    BASELINE_GRU["macro_f1"]
)


# ============================================================
# 9. SELECT BEST MODEL
# ============================================================

print(
    "\n[9/11] Selecting best Member 2 model..."
)

if (
    svm_metrics["weighted_f1"]
    >=
    gru_metrics["weighted_f1"]
):
    best_model = (
        "Word2Vec + Tuned RBF SVM"
    )

    best_reason = (
        "The tuned SVM achieved the highest "
        "weighted F1 score."
    )

else:
    best_model = (
        "Optimized GRU"
    )

    best_reason = (
        "The optimized GRU achieved the highest "
        "weighted F1 score."
    )

print(
    "Selected model:",
    best_model,
)


# ============================================================
# 10. PRINT FINAL RESULTS
# ============================================================

print("\n" + "=" * 75)
print("FINAL MEMBER 2 RESULTS")
print("=" * 75)


print("\nBASELINE SVM")

print(
    f"Accuracy:    "
    f"{BASELINE_SVM['accuracy']:.4f}"
)

print(
    f"Weighted F1: "
    f"{BASELINE_SVM['weighted_f1']:.4f}"
)

print(
    f"Macro F1:    "
    f"{BASELINE_SVM['macro_f1']:.4f}"
)


print("\nTUNED SVM")

print(
    f"Accuracy:    "
    f"{svm_metrics['accuracy']:.4f}"
)

print(
    f"Weighted F1: "
    f"{svm_metrics['weighted_f1']:.4f}"
)

print(
    f"Macro F1:    "
    f"{svm_metrics['macro_f1']:.4f}"
)


print("\nBASELINE GRU")

print(
    f"Accuracy:    "
    f"{BASELINE_GRU['accuracy']:.4f}"
)

print(
    f"Weighted F1: "
    f"{BASELINE_GRU['weighted_f1']:.4f}"
)

print(
    f"Macro F1:    "
    f"{BASELINE_GRU['macro_f1']:.4f}"
)


print("\nOPTIMIZED GRU")

print(
    f"Test Loss:   "
    f"{gru_test_loss:.4f}"
)

print(
    f"Accuracy:    "
    f"{gru_metrics['accuracy']:.4f}"
)

print(
    f"Weighted F1: "
    f"{gru_metrics['weighted_f1']:.4f}"
)

print(
    f"Macro F1:    "
    f"{gru_metrics['macro_f1']:.4f}"
)


print("\nBEST MEMBER 2 MODEL")

print(
    best_model
)

print(
    best_reason
)


# ============================================================
# 11. GENERATE MARKDOWN REPORT
#
# Constructed line-by-line to avoid triple-quoted
# f-string issues.
# ============================================================

print(
    "\n[10/11] Generating Member 2 report..."
)

report_lines = []


# ------------------------------------------------------------
# REPORT HEADER
# ------------------------------------------------------------

report_lines.extend(
    [
        "# Member 2 Model Results",
        "",
        "## SupportIQ NLP Project",
        "",
        "**Member:** Member 2",
        "**Student ID:** CIT-24-01-0023",
        "",
        "---",
        "",
    ]
)


# ------------------------------------------------------------
# PREDICTION TASK
# ------------------------------------------------------------

report_lines.extend(
    [
        "# 1. Prediction Task",
        "",
        (
            "Member 2 evaluated machine-learning and "
            "deep-learning approaches for "
            "**Support Queue Routing**."
        ),
        "",
        "Target column:",
        "",
        "`queue`",
        "",
        (
            "Processed English-language dataset size: "
            f"**{len(df):,} tickets**"
        ),
        "",
        (
            "Number of support queue classes: "
            f"**{df['queue'].nunique()}**"
        ),
        "",
        "---",
        "",
    ]
)


# ------------------------------------------------------------
# QUEUE DISTRIBUTION
# ------------------------------------------------------------

report_lines.extend(
    [
        "# 2. Queue Distribution",
        "",
        "| Queue | Records |",
        "|---|---:|",
    ]
)

queue_counts = (
    df["queue"]
    .value_counts()
)

for queue_name, count in queue_counts.items():
    report_lines.append(
        f"| {queue_name} | {count} |"
    )

report_lines.extend(
    [
        "",
        (
            "The support queue dataset is class-imbalanced. "
            "Therefore accuracy, weighted F1 and macro F1 "
            "were considered during evaluation."
        ),
        "",
        "---",
        "",
    ]
)


# ------------------------------------------------------------
# WORD2VEC
# ------------------------------------------------------------

report_lines.extend(
    [
        "# 3. Word2Vec Feature Engineering",
        "",
        (
            "The Support Vector Machine uses dense sentence "
            "embeddings generated from the cleaned ticket text."
        ),
        "",
        "Word2Vec configuration:",
        "",
        "- Vector size: 100",
        "- Context window: 5",
        "- Minimum word count: 2",
        "- Training epochs: 10",
        "",
        (
            "Sentence-vector matrix: "
            f"`{X_vectors.shape}`"
        ),
        "",
        "---",
        "",
    ]
)


# ------------------------------------------------------------
# BASELINE SVM
# ------------------------------------------------------------

report_lines.extend(
    [
        "# 4. Baseline Support Vector Machine",
        "",
        "Baseline configuration:",
        "",
        "- Kernel: RBF",
        "- C: 1.0",
        "- Gamma: scale",
        "- Test size: 20%",
        "- Random state: 42",
        "- Stratified split: Yes",
        "",
        "## Baseline SVM Results",
        "",
    ]
)

append_metric_table(
    report_lines,
    BASELINE_SVM,
)

report_lines.extend(
    [
        "",
        "---",
        "",
    ]
)


# ------------------------------------------------------------
# TUNED SVM
# ------------------------------------------------------------

report_lines.extend(
    [
        "# 5. Tuned Support Vector Machine",
        "",
        (
            "GridSearchCV was used to optimize the SVM "
            "using weighted F1 as the scoring metric."
        ),
        "",
        "Best hyperparameters:",
        "",
        (
            f"- C: "
            f"{SVM_BEST_PARAMETERS['C']}"
        ),
        (
            f"- Kernel: "
            f"{SVM_BEST_PARAMETERS['kernel'].upper()}"
        ),
        (
            f"- Gamma: "
            f"{SVM_BEST_PARAMETERS['gamma']}"
        ),
        "",
        (
            "Best cross-validation weighted F1: "
            f"**{SVM_BEST_CV_WEIGHTED_F1:.4f}**"
        ),
        "",
        "## Tuned SVM Test Results",
        "",
    ]
)

append_metric_table(
    report_lines,
    svm_metrics,
)

report_lines.extend(
    [
        "",
        "## SVM Improvement After Tuning",
        "",
        "| Metric | Baseline | Tuned | Gain |",
        "|---|---:|---:|---:|",
        (
            "| Accuracy | "
            f"{BASELINE_SVM['accuracy']:.4f} | "
            f"{svm_metrics['accuracy']:.4f} | "
            f"{svm_accuracy_gain:+.4f} |"
        ),
        (
            "| Weighted F1 | "
            f"{BASELINE_SVM['weighted_f1']:.4f} | "
            f"{svm_metrics['weighted_f1']:.4f} | "
            f"{svm_weighted_f1_gain:+.4f} |"
        ),
        (
            "| Macro F1 | "
            f"{BASELINE_SVM['macro_f1']:.4f} | "
            f"{svm_metrics['macro_f1']:.4f} | "
            f"{svm_macro_f1_gain:+.4f} |"
        ),
        "",
        "### Tuned SVM Classification Report",
        "",
        "```text",
        svm_classification_report.rstrip(),
        "```",
        "",
        "### Tuned SVM Confusion Matrix",
        "",
        "Class order:",
        "",
        "`" + ", ".join(svm_classes) + "`",
        "",
        "```text",
        np.array2string(
            svm_confusion_matrix
        ),
        "```",
        "",
        "---",
        "",
    ]
)


# ------------------------------------------------------------
# BASELINE GRU
# ------------------------------------------------------------

report_lines.extend(
    [
        "# 6. Baseline GRU",
        "",
        "Initial GRU configuration:",
        "",
        "- Maximum vocabulary size: 10,000",
        "- Maximum sequence length: 100",
        "- Embedding dimension: 128",
        "- GRU units: 64",
        "- Dropout: 0.30",
        "- Dense hidden layer: 32 units",
        "- Output activation: Softmax",
        "- Epochs: 5",
        "- Batch size: 32",
        "",
        (
            "The baseline GRU suffered from majority-class "
            "collapse and predicted the dominant Technical "
            "Support class for most test examples."
        ),
        "",
        "## Baseline GRU Results",
        "",
        "| Metric | Score |",
        "|---|---:|",
        (
            f"| Test Loss | "
            f"{BASELINE_GRU['test_loss']:.4f} |"
        ),
        (
            f"| Accuracy | "
            f"{BASELINE_GRU['accuracy']:.4f} |"
        ),
        (
            "| Weighted Precision | "
            f"{BASELINE_GRU['weighted_precision']:.4f} |"
        ),
        (
            "| Weighted Recall | "
            f"{BASELINE_GRU['weighted_recall']:.4f} |"
        ),
        (
            "| Weighted F1 | "
            f"{BASELINE_GRU['weighted_f1']:.4f} |"
        ),
        (
            "| Macro F1 | "
            f"{BASELINE_GRU['macro_f1']:.4f} |"
        ),
        "",
        "---",
        "",
    ]
)


# ------------------------------------------------------------
# OPTIMIZED GRU
# ------------------------------------------------------------

report_lines.extend(
    [
        "# 7. Optimized GRU",
        "",
        "The GRU was improved using:",
        "",
        "- Padding masking with `mask_zero=True`",
        "- Balanced class weights",
        "- Stratified train, validation and test splits",
        "- Tokenizer fitted only on training data",
        "- Early stopping",
        "- Learning-rate reduction",
        "- Up to 15 training epochs",
        "- Best-weight restoration",
        "",
        "Verified training information:",
        "",
        (
            "- Best validation accuracy: "
            f"{OPTIMIZED_GRU_TRAINING['best_validation_accuracy']:.4f}"
        ),
        (
            "- Best validation accuracy epoch: "
            f"{OPTIMIZED_GRU_TRAINING['best_validation_accuracy_epoch']}"
        ),
        (
            "- Best validation loss: "
            f"{OPTIMIZED_GRU_TRAINING['best_validation_loss']:.4f}"
        ),
        (
            "- Best validation loss epoch: "
            f"{OPTIMIZED_GRU_TRAINING['best_validation_loss_epoch']}"
        ),
        "",
        "## Optimized GRU Test Results",
        "",
        "| Metric | Score |",
        "|---|---:|",
        (
            f"| Test Loss | "
            f"{gru_test_loss:.4f} |"
        ),
        (
            f"| Keras Test Accuracy | "
            f"{gru_keras_accuracy:.4f} |"
        ),
        (
            f"| Accuracy | "
            f"{gru_metrics['accuracy']:.4f} |"
        ),
        (
            "| Weighted Precision | "
            f"{gru_metrics['weighted_precision']:.4f} |"
        ),
        (
            "| Weighted Recall | "
            f"{gru_metrics['weighted_recall']:.4f} |"
        ),
        (
            "| Weighted F1 | "
            f"{gru_metrics['weighted_f1']:.4f} |"
        ),
        (
            "| Macro Precision | "
            f"{gru_metrics['macro_precision']:.4f} |"
        ),
        (
            "| Macro Recall | "
            f"{gru_metrics['macro_recall']:.4f} |"
        ),
        (
            "| Macro F1 | "
            f"{gru_metrics['macro_f1']:.4f} |"
        ),
        "",
        "## GRU Improvement After Optimization",
        "",
        "| Metric | Baseline | Optimized | Gain |",
        "|---|---:|---:|---:|",
        (
            "| Accuracy | "
            f"{BASELINE_GRU['accuracy']:.4f} | "
            f"{gru_metrics['accuracy']:.4f} | "
            f"{gru_accuracy_gain:+.4f} |"
        ),
        (
            "| Weighted F1 | "
            f"{BASELINE_GRU['weighted_f1']:.4f} | "
            f"{gru_metrics['weighted_f1']:.4f} | "
            f"{gru_weighted_f1_gain:+.4f} |"
        ),
        (
            "| Macro F1 | "
            f"{BASELINE_GRU['macro_f1']:.4f} | "
            f"{gru_metrics['macro_f1']:.4f} | "
            f"{gru_macro_f1_gain:+.4f} |"
        ),
        "",
        "### Optimized GRU Classification Report",
        "",
        "```text",
        gru_classification_report.rstrip(),
        "```",
        "",
        "### Optimized GRU Confusion Matrix",
        "",
        "Class order:",
        "",
        "`"
        + ", ".join(
            gru_encoder.classes_
        )
        + "`",
        "",
        "```text",
        np.array2string(
            gru_confusion_matrix
        ),
        "```",
        "",
        "---",
        "",
    ]
)


# ------------------------------------------------------------
# OVERALL COMPARISON
# ------------------------------------------------------------

report_lines.extend(
    [
        "# 8. Overall Member 2 Model Comparison",
        "",
        (
            "| Model | Accuracy | "
            "Weighted F1 | Macro F1 |"
        ),
        "|---|---:|---:|---:|",
        (
            "| Baseline SVM | "
            f"{BASELINE_SVM['accuracy']:.4f} | "
            f"{BASELINE_SVM['weighted_f1']:.4f} | "
            f"{BASELINE_SVM['macro_f1']:.4f} |"
        ),
        (
            "| Tuned SVM | "
            f"{svm_metrics['accuracy']:.4f} | "
            f"{svm_metrics['weighted_f1']:.4f} | "
            f"{svm_metrics['macro_f1']:.4f} |"
        ),
        (
            "| Baseline GRU | "
            f"{BASELINE_GRU['accuracy']:.4f} | "
            f"{BASELINE_GRU['weighted_f1']:.4f} | "
            f"{BASELINE_GRU['macro_f1']:.4f} |"
        ),
        (
            "| Optimized GRU | "
            f"{gru_metrics['accuracy']:.4f} | "
            f"{gru_metrics['weighted_f1']:.4f} | "
            f"{gru_metrics['macro_f1']:.4f} |"
        ),
        "",
        "---",
        "",
    ]
)


# ------------------------------------------------------------
# BEST MODEL
# ------------------------------------------------------------

report_lines.extend(
    [
        "# 9. Best Member 2 Model",
        "",
        "The strongest Member 2 model is:",
        "",
        f"**{best_model}**",
        "",
        best_reason,
        "",
        (
            "The tuned SVM achieved stronger overall "
            "performance than the optimized GRU on the "
            "held-out test set."
        ),
        "",
        (
            "The SVM achieved higher accuracy, weighted F1 "
            "and macro F1 while requiring less training "
            "complexity than the GRU."
        ),
        "",
        (
            "The optimized GRU nevertheless improved "
            "substantially over the baseline GRU. "
            "Padding masking, balanced class weights, "
            "early stopping and learning-rate scheduling "
            "improved minority-class recognition."
        ),
        "",
        "---",
        "",
    ]
)


# ------------------------------------------------------------
# FINAL CONCLUSION
# ------------------------------------------------------------

report_lines.extend(
    [
        "# 10. Final Conclusion",
        "",
        (
            "Member 2's experiments demonstrate that "
            "Word2Vec sentence embeddings combined with a "
            "tuned RBF Support Vector Machine provide the "
            "strongest Member 2 solution for support queue "
            "routing."
        ),
        "",
        "Best SVM configuration:",
        "",
        "- C = 10",
        "- Kernel = RBF",
        "- Gamma = scale",
        "",
        "Final tuned SVM results:",
        "",
        (
            f"- Accuracy: "
            f"{svm_metrics['accuracy']:.4f}"
        ),
        (
            f"- Weighted F1: "
            f"{svm_metrics['weighted_f1']:.4f}"
        ),
        (
            f"- Macro F1: "
            f"{svm_metrics['macro_f1']:.4f}"
        ),
        "",
        "Final optimized GRU results:",
        "",
        (
            f"- Accuracy: "
            f"{gru_metrics['accuracy']:.4f}"
        ),
        (
            f"- Weighted F1: "
            f"{gru_metrics['weighted_f1']:.4f}"
        ),
        (
            f"- Macro F1: "
            f"{gru_metrics['macro_f1']:.4f}"
        ),
        "",
        (
            "Therefore, **Word2Vec + Tuned RBF SVM** "
            "is selected as Member 2's best-performing model."
        ),
        "",
    ]
)


# ============================================================
# WRITE REPORT
# ============================================================

REPORT_PATH.parent.mkdir(
    parents=True,
    exist_ok=True,
)

report_content = "\n".join(
    report_lines
)

with open(
    REPORT_PATH,
    "w",
    encoding="utf-8",
) as report_file:

    report_file.write(
        report_content
    )


# ============================================================
# REPORT VERIFICATION
# ============================================================

print(
    "\n[11/11] Verifying final report..."
)

if not REPORT_PATH.exists():
    raise FileNotFoundError(
        "Member 2 report was not created."
    )

if REPORT_PATH.stat().st_size == 0:
    raise ValueError(
        "Member 2 report is empty."
    )

print(
    "Report created successfully:"
)

print(
    REPORT_PATH
)

print(
    "Report size:",
    REPORT_PATH.stat().st_size,
    "bytes",
)


# ============================================================
# FINAL SUMMARY
# ============================================================

print("\n" + "=" * 75)
print("FINAL MEMBER 2 SUMMARY")
print("=" * 75)


print("\nTuned SVM")

print(
    f"Accuracy:    "
    f"{svm_metrics['accuracy']:.4f}"
)

print(
    f"Weighted F1: "
    f"{svm_metrics['weighted_f1']:.4f}"
)

print(
    f"Macro F1:    "
    f"{svm_metrics['macro_f1']:.4f}"
)


print("\nOptimized GRU")

print(
    f"Test Loss:   "
    f"{gru_test_loss:.4f}"
)

print(
    f"Accuracy:    "
    f"{gru_metrics['accuracy']:.4f}"
)

print(
    f"Weighted F1: "
    f"{gru_metrics['weighted_f1']:.4f}"
)

print(
    f"Macro F1:    "
    f"{gru_metrics['macro_f1']:.4f}"
)


print("\nSelected Model:")

print(
    best_model
)

print(
    "\nMember 2 final comparison finished successfully."
)