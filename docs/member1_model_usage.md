
# Member 1 Model Usage Documentation

## Overview

Member 1 implemented two NLP classification models for the SupportIQ customer support ticket classification system:

1. Logistic Regression with TF-IDF feature extraction
2. BiLSTM Deep Learning classifier

Both models use the same NLP preprocessing pipeline before classification.

---

# 1. Logistic Regression Model

## Model Description

The Logistic Regression model is used as the classical machine learning baseline for ticket classification.

The model uses TF-IDF feature representation with n-gram features to convert customer support text into numerical vectors.

---

## Pipeline

```

Customer Support Text

```
    ↓
```

Text Preprocessing

(Cleaning, Tokenization, Stopword Removal, Lemmatization)

```
    ↓
```

TF-IDF Feature Extraction

```
    ↓
```

Logistic Regression Classifier

```
    ↓
```

Predicted Ticket Category

```

---

## Model File

```

src/models/member1/logistic_regression.pkl

```

---

## Input

The model receives raw customer support ticket text.

Example:

```

"I cannot access my account"

```

---

## Processing

Before prediction, the input text must pass through the preprocessing pipeline:

```

preprocess_text()

```

Located at:

```

src/preprocessing/pipeline.py

```

The preprocessing steps include:

- Text cleaning
- Lowercase conversion
- Tokenization
- Stopword removal
- Lemmatization

---

## Output

The model predicts one of the customer support ticket categories:

```

Incident
Request
Problem
Change

```

---

# 2. BiLSTM Model

## Model Description

The BiLSTM model is a deep learning based sequence classifier.

Unlike traditional machine learning approaches, BiLSTM learns contextual relationships between words in customer support messages.

---

## Pipeline

```

Customer Support Text

```
    ↓
```

Text Preprocessing

```
    ↓
```

Tokenizer

```
    ↓
```

Sequence Padding

```
    ↓
```

Embedding Layer

```
    ↓
```

Bidirectional LSTM Layer

```
    ↓
```

Dense Classification Layer

```
    ↓
```

Predicted Ticket Category

```

---

## Model Files

```

src/models/member1/

bilstm_model.keras
tokenizer.pkl
label_encoder.pkl

````

---

## Model Loading

```python
from tensorflow.keras.models import load_model
import joblib


model = load_model(
    "src/models/member1/bilstm_model.keras"
)


tokenizer = joblib.load(
    "src/models/member1/tokenizer.pkl"
)


label_encoder = joblib.load(
    "src/models/member1/label_encoder.pkl"
)
````

---

# Example Prediction Flow

## Input

```
"I cannot access my account"
```

---

## Processing

```
Raw Text

↓

Preprocessing Pipeline

↓

Tokenizer

↓

Sequence Padding

↓

BiLSTM Model

↓

Label Encoder
```

---

## Output

```
Incident
```

---

# Model Performance

## BiLSTM Model

Accuracy:

```
85.5%
```

The BiLSTM model achieved strong performance in classifying customer support tickets, especially for Request and Change categories.

---

## Logistic Regression Model

The Logistic Regression model was developed as the baseline machine learning approach using TF-IDF features.

It provides a fast and interpretable comparison against the deep learning approach.

---

# Integration Notes

For backend integration:

1. Load the trained model files from:

```
src/models/member1/
```

2. Apply the same preprocessing pipeline used during training.

3. Ensure input text follows the same format as the training data.

4. Return the predicted ticket category to the backend prediction service.

---

# Member 1 Deliverables

Completed components:

```
src/preprocessing/

cleaning.py
tokenization.py
stopwords.py
lemmatization.py
pipeline.py


src/models/member1/

logistic_regression.pkl
bilstm_model.keras
tokenizer.pkl
label_encoder.pkl


notebooks/

02_member1_logistic_regression.ipynb
03_member1_bilstm.ipynb


reports/

member1_results.md
```

---

# Conclusion

Member 1 developed both traditional machine learning and deep learning approaches for customer support ticket classification.

The Logistic Regression model provides a strong baseline, while the BiLSTM model improves contextual understanding of customer messages.

Both models are prepared for integration into the SupportIQ backend prediction pipeline.

```
```