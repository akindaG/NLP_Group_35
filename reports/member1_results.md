# Member 1 – Logistic Regression + TF-IDF

## Model Overview

Model: Logistic Regression

Feature Extraction: TF-IDF Vectorization

Dataset: Customer Support Tickets Dataset

Number of Records: 16,338

Number of Classes:

* Incident
* Request
* Problem
* Change

## Preprocessing Steps

* Text Cleaning
* Tokenization
* Stopword Removal
* Lemmatization

## Training Configuration

* Train/Test Split: 80/20
* Random State: 42
* TF-IDF Features: 5000
* Maximum Iterations: 1000

## Results

Accuracy: 83.69%

### Classification Report

| Class    | Precision | Recall | F1-score |
| -------- | --------- | ------ | -------- |
| Change   | 0.99      | 0.96   | 0.98     |
| Incident | 0.76      | 0.89   | 0.82     |
| Problem  | 0.67      | 0.46   | 0.55     |
| Request  | 0.99      | 1.00   | 0.99     |

Weighted Average:

* Precision: 0.83
* Recall: 0.84
* F1-score: 0.83

## Observations

The Logistic Regression model achieved an accuracy of 83.69% on the customer support ticket classification task. The model performed exceptionally well on Request and Change categories. Most classification errors occurred between Incident and Problem categories due to semantic similarity between these ticket types.

The results demonstrate that TF-IDF combined with Logistic Regression provides an effective baseline approach for multiclass ticket classification.