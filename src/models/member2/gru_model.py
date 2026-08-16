import os
import joblib
import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Embedding,
    GRU,
    Dense,
    Dropout
)
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.callbacks import (
    EarlyStopping,
    ReduceLROnPlateau
)
from tensorflow.keras.optimizers import Adam

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)


# ============================================================
# CONFIGURATION
# ============================================================

DATA_PATH = "data/processed/customer_support_en.csv"

MODEL_DIR = "models/member2"

MODEL_PATH = f"{MODEL_DIR}/gru.keras"
TOKENIZER_PATH = f"{MODEL_DIR}/gru_tokenizer.pkl"
ENCODER_PATH = f"{MODEL_DIR}/gru_label_encoder.pkl"


# Text settings
MAX_WORDS = 10000
MAX_LEN = 100


# Neural network settings
EMBEDDING_DIM = 128
GRU_UNITS = 64

DROPOUT_RATE = 0.30
DENSE_DROPOUT_RATE = 0.20


# Training settings
EPOCHS = 15
BATCH_SIZE = 32
LEARNING_RATE = 0.001

TEST_SIZE = 0.20
VALIDATION_SIZE = 0.10

RANDOM_STATE = 42


# ============================================================
# REPRODUCIBILITY
# ============================================================

np.random.seed(RANDOM_STATE)

tf.random.set_seed(RANDOM_STATE)

tf.keras.utils.set_random_seed(
    RANDOM_STATE
)


# ============================================================
# START
# ============================================================

print("=" * 70)
print("MEMBER 2 - OPTIMIZED GRU MODEL")
print("Support Queue Routing")
print("=" * 70)


# ============================================================
# 1. LOAD PROCESSED DATASET
# ============================================================

print("\n[1/14] Loading processed dataset...")

df = pd.read_csv(
    DATA_PATH
)

print(
    "Dataset shape:",
    df.shape
)


# ============================================================
# 2. VERIFY REQUIRED COLUMNS
# ============================================================

required_columns = [
    "clean_text",
    "queue"
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


print(
    "Required columns verified."
)


# ============================================================
# 3. PREPARE TEXT
# ============================================================

print("\n[2/14] Preparing ticket text...")

texts = (
    df["clean_text"]
    .fillna("")
    .astype(str)
    .values
)


# ============================================================
# 4. ENCODE TARGET LABELS
# ============================================================

print("\n[3/14] Encoding queue labels...")

label_encoder = LabelEncoder()

y = label_encoder.fit_transform(
    df["queue"].astype(str)
)

num_classes = len(
    label_encoder.classes_
)


print(
    "Number of classes:",
    num_classes
)


print("\nQueue classes:")

for index, queue_name in enumerate(
    label_encoder.classes_
):

    print(
        f"{index}: {queue_name}"
    )


# ============================================================
# 5. TRAIN / TEST SPLIT BEFORE TOKENIZER TRAINING
# ============================================================

print(
    "\n[4/14] Creating train/test split..."
)

(
    text_train_full,
    text_test,
    y_train_full,
    y_test
) = train_test_split(
    texts,
    y,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE,
    stratify=y
)


# ============================================================
# 6. CREATE TRAIN / VALIDATION SPLIT
# ============================================================

(
    text_train,
    text_val,
    y_train,
    y_val
) = train_test_split(
    text_train_full,
    y_train_full,
    test_size=VALIDATION_SIZE,
    random_state=RANDOM_STATE,
    stratify=y_train_full
)


print(
    "Training samples:",
    len(text_train)
)

print(
    "Validation samples:",
    len(text_val)
)

print(
    "Testing samples:",
    len(text_test)
)


# ============================================================
# 7. TOKENIZER
# ============================================================

print(
    "\n[5/14] Training tokenizer..."
)

tokenizer = Tokenizer(
    num_words=MAX_WORDS,
    oov_token="<OOV>"
)


# Fit tokenizer ONLY on training text
tokenizer.fit_on_texts(
    text_train
)


train_sequences = tokenizer.texts_to_sequences(
    text_train
)

val_sequences = tokenizer.texts_to_sequences(
    text_val
)

test_sequences = tokenizer.texts_to_sequences(
    text_test
)


# ============================================================
# 8. SEQUENCE PADDING
# ============================================================

print(
    "\n[6/14] Padding sequences..."
)


X_train = pad_sequences(
    train_sequences,
    maxlen=MAX_LEN,
    padding="post",
    truncating="post"
)


X_val = pad_sequences(
    val_sequences,
    maxlen=MAX_LEN,
    padding="post",
    truncating="post"
)


X_test = pad_sequences(
    test_sequences,
    maxlen=MAX_LEN,
    padding="post",
    truncating="post"
)


print(
    "Training matrix:",
    X_train.shape
)

print(
    "Validation matrix:",
    X_val.shape
)

print(
    "Testing matrix:",
    X_test.shape
)


# ============================================================
# 9. CALCULATE CLASS WEIGHTS
# ============================================================

print(
    "\n[7/14] Calculating class weights..."
)


classes = np.unique(
    y_train
)


weights = compute_class_weight(
    class_weight="balanced",
    classes=classes,
    y=y_train
)


class_weights = {
    int(class_id): float(weight)
    for class_id, weight in zip(
        classes,
        weights
    )
}


print("\nClass weights:")

for class_id, weight in class_weights.items():

    queue_name = (
        label_encoder
        .inverse_transform(
            [class_id]
        )[0]
    )

    print(
        f"{queue_name:<35} "
        f"{weight:.4f}"
    )


# ============================================================
# 10. BUILD GRU ARCHITECTURE
# ============================================================

print(
    "\n[8/14] Building optimized GRU model..."
)


model = Sequential([

    # --------------------------------------------------------
    # Word embedding layer
    #
    # mask_zero=True is important because sequences are padded
    # using zero values. The GRU will therefore ignore padding.
    # --------------------------------------------------------

    Embedding(
        input_dim=MAX_WORDS,
        output_dim=EMBEDDING_DIM,
        mask_zero=True
    ),


    # --------------------------------------------------------
    # GRU sequence model
    # --------------------------------------------------------

    GRU(
        GRU_UNITS,
        return_sequences=False
    ),


    # --------------------------------------------------------
    # Regularization
    # --------------------------------------------------------

    Dropout(
        DROPOUT_RATE
    ),


    # --------------------------------------------------------
    # Dense representation
    # --------------------------------------------------------

    Dense(
        32,
        activation="relu"
    ),


    Dropout(
        DENSE_DROPOUT_RATE
    ),


    # --------------------------------------------------------
    # Multiclass output
    # --------------------------------------------------------

    Dense(
        num_classes,
        activation="softmax"
    )

])


# ============================================================
# 11. COMPILE MODEL
# ============================================================

optimizer = Adam(
    learning_rate=LEARNING_RATE
)


model.compile(
    optimizer=optimizer,
    loss="sparse_categorical_crossentropy",
    metrics=[
        "accuracy"
    ]
)


model.build(
    input_shape=(
        None,
        MAX_LEN
    )
)


print(
    "\nModel Architecture:\n"
)

model.summary()


# ============================================================
# 12. CALLBACKS
# ============================================================

print(
    "\n[9/14] Preparing training callbacks..."
)


early_stopping = EarlyStopping(
    monitor="val_loss",
    patience=3,
    restore_best_weights=True,
    verbose=1
)


reduce_learning_rate = ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.5,
    patience=2,
    min_lr=1e-6,
    verbose=1
)


# ============================================================
# 13. TRAIN MODEL
# ============================================================

print(
    "\n[10/14] Training optimized GRU...\n"
)


history = model.fit(

    X_train,
    y_train,

    validation_data=(
        X_val,
        y_val
    ),

    epochs=EPOCHS,

    batch_size=BATCH_SIZE,

    class_weight=class_weights,

    callbacks=[
        early_stopping,
        reduce_learning_rate
    ],

    verbose=1
)


# ============================================================
# 14. TEST SET EVALUATION
# ============================================================

print(
    "\n[11/14] Evaluating model on held-out test set..."
)


test_loss, keras_test_accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)


# ============================================================
# 15. GENERATE PREDICTIONS
# ============================================================

print(
    "\n[12/14] Generating predictions..."
)


probabilities = model.predict(
    X_test,
    verbose=0
)


y_pred = np.argmax(
    probabilities,
    axis=1
)


# ============================================================
# 16. CALCULATE METRICS
# ============================================================

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


macro_precision = precision_score(
    y_test,
    y_pred,
    average="macro",
    zero_division=0
)


macro_recall = recall_score(
    y_test,
    y_pred,
    average="macro",
    zero_division=0
)


# ============================================================
# 17. TRAINING HISTORY
# ============================================================

best_validation_accuracy = max(
    history.history[
        "val_accuracy"
    ]
)


best_validation_loss = min(
    history.history[
        "val_loss"
    ]
)


best_validation_accuracy_epoch = (
    np.argmax(
        history.history[
            "val_accuracy"
        ]
    )
    + 1
)


best_validation_loss_epoch = (
    np.argmin(
        history.history[
            "val_loss"
        ]
    )
    + 1
)


# ============================================================
# 18. PRINT FINAL RESULTS
# ============================================================

print(
    "\n" + "=" * 70
)

print(
    "OPTIMIZED GRU TEST RESULTS"
)

print(
    "=" * 70
)


print(
    f"Test Loss:            "
    f"{test_loss:.4f}"
)

print(
    f"Keras Test Accuracy:  "
    f"{keras_test_accuracy:.4f}"
)


print(
    f"Accuracy:             "
    f"{accuracy:.4f}"
)


print(
    f"Weighted Precision:   "
    f"{weighted_precision:.4f}"
)


print(
    f"Weighted Recall:      "
    f"{weighted_recall:.4f}"
)


print(
    f"Weighted F1:          "
    f"{weighted_f1:.4f}"
)


print(
    f"Macro Precision:      "
    f"{macro_precision:.4f}"
)


print(
    f"Macro Recall:         "
    f"{macro_recall:.4f}"
)


print(
    f"Macro F1:             "
    f"{macro_f1:.4f}"
)


print(
    f"\nBest Validation Accuracy: "
    f"{best_validation_accuracy:.4f}"
)

print(
    f"Best Validation Accuracy Epoch: "
    f"{best_validation_accuracy_epoch}"
)


print(
    f"Best Validation Loss: "
    f"{best_validation_loss:.4f}"
)

print(
    f"Best Validation Loss Epoch: "
    f"{best_validation_loss_epoch}"
)


# ============================================================
# 19. CLASSIFICATION REPORT
# ============================================================

print(
    "\nClassification Report:\n"
)


print(
    classification_report(
        y_test,
        y_pred,
        target_names=label_encoder.classes_,
        zero_division=0
    )
)


# ============================================================
# 20. CONFUSION MATRIX
# ============================================================

confusion = confusion_matrix(
    y_test,
    y_pred
)


print(
    "\nConfusion Matrix:"
)


print(
    confusion
)


# ============================================================
# 21. SAVE ARTIFACTS
# ============================================================

print(
    "\n[13/14] Saving GRU artifacts..."
)


os.makedirs(
    MODEL_DIR,
    exist_ok=True
)


# Save neural network
model.save(
    MODEL_PATH
)


# Save tokenizer
joblib.dump(
    tokenizer,
    TOKENIZER_PATH
)


# Save label encoder
joblib.dump(
    label_encoder,
    ENCODER_PATH
)


print(
    "\nArtifacts saved:"
)

print(
    "-",
    MODEL_PATH
)

print(
    "-",
    TOKENIZER_PATH
)

print(
    "-",
    ENCODER_PATH
)


# ============================================================
# 22. FINAL SUMMARY
# ============================================================

print(
    "\n" + "=" * 70
)

print(
    "MEMBER 2 OPTIMIZED GRU COMPLETE"
)

print(
    "=" * 70
)


print(
    "\nImportant metrics to record:"
)

print(
    f"Accuracy:    {accuracy:.4f}"
)

print(
    f"Weighted F1: {weighted_f1:.4f}"
)

print(
    f"Macro F1:    {macro_f1:.4f}"
)


print(
    "\nOptimized GRU training completed successfully."
)