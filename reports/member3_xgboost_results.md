# Member 3 - XGBoost Classifier Results Report

## Student Information

| Field              | Value                                   |
| ------------------ | --------------------------------------- |
| Student ID         | CIT-24-01-0125                          |
| Member Role        | Member 3 - XGBoost & DistilBERT         |
| Model              | XGBoost Classifier                      |
| Dataset            | Customer Support Ticket Routing Dataset |
| Task               | Multi-Class Department Classification   |
| Number of Classes  | 10                                      |
| Feature Extraction | TF-IDF Vectorization                    |
| Test Size          | 20%                                     |
| Random State       | 42                                      |

---

# 1. Objective

The objective of this phase was to develop a machine learning model capable of automatically classifying customer support tickets into the appropriate organizational department based on ticket text.

The XGBoost classifier was selected due to its strong performance in classification tasks, ability to handle sparse TF-IDF feature vectors efficiently, and robustness against overfitting.

The model predicts the correct support queue for incoming customer support tickets.

---

# 2. Dataset Summary

After preprocessing and language filtering, the English dataset contained:

| Metric             | Value  |
| ------------------ | ------ |
| Total Records      | 16,338 |
| Number of Features | 18     |
| Target Classes     | 10     |

Department categories:

1. Billing and Payments
2. Customer Service
3. General Inquiry
4. Human Resources
5. IT Support
6. Product Support
7. Returns and Exchanges
8. Sales and Pre-Sales
9. Service Outages and Maintenance
10. Technical Support

---

# 3. Data Preparation

## Train-Test Split

The dataset was divided into training and testing sets.

| Dataset Portion | Percentage |
| --------------- | ---------- |
| Training Set    | 80%        |
| Testing Set     | 20%        |

Python implementation:

```python
X_train, X_test, y_train, y_test = train_test_split(
    english_df["clean_text"],
    english_df["queue"],
    test_size=0.2,
    random_state=42
)
```

---

# 4. Feature Engineering

## TF-IDF Vectorization

Ticket text was transformed into numerical feature vectors using TF-IDF (Term Frequency-Inverse Document Frequency).

Configuration:

```python
TfidfVectorizer(
    max_features=5000
)
```

### Purpose of TF-IDF

TF-IDF converts textual data into machine-readable numerical vectors by:

* Measuring word frequency within tickets
* Reducing importance of common words
* Highlighting informative terms
* Creating sparse feature representations

Maximum vocabulary size:

```text
5000 features
```

---

# 5. Label Encoding

The target variable (queue) was converted into numerical labels using LabelEncoder.

Example:

| Department           | Encoded Label |
| -------------------- | ------------- |
| Billing and Payments | 0             |
| Customer Service     | 1             |
| IT Support           | 4             |
| Technical Support    | 9             |

This conversion is required because XGBoost operates on numeric labels.

---

# 6. Model Architecture

## XGBoost Classifier

The model used:

```python
XGBClassifier()
```

XGBoost (Extreme Gradient Boosting) is an ensemble learning algorithm that combines multiple decision trees to improve predictive performance.

Advantages:

* High classification accuracy
* Efficient handling of sparse TF-IDF vectors
* Fast training and inference
* Strong performance on structured text features

---

# 7. Model Training

The model was trained using TF-IDF features extracted from ticket text.

Training code:

```python
xgb_model.fit(
    X_train_tfidf,
    y_train_encoded
)
```

The model learned patterns between ticket language and support department labels.

---

# 8. Model Evaluation

## Overall Accuracy

```text
Accuracy = 53.06%
```

Calculated value:

```text
0.5306
```

### Interpretation

The model correctly classified approximately 53 out of every 100 customer support tickets.

Considering:

* 10 target classes
* Class imbalance
* Short text classification challenges

This performance represents a reasonable baseline for a traditional machine learning model.

---

# 9. Classification Report

| Department                      | Precision | Recall | F1 Score |
| ------------------------------- | --------- | ------ | -------- |
| Billing and Payments            | 0.91      | 0.70   | 0.79     |
| Customer Service                | 0.45      | 0.40   | 0.42     |
| General Inquiry                 | 1.00      | 0.26   | 0.41     |
| Human Resources                 | 0.95      | 0.27   | 0.42     |
| IT Support                      | 0.73      | 0.29   | 0.41     |
| Product Support                 | 0.49      | 0.40   | 0.44     |
| Returns and Exchanges           | 0.77      | 0.20   | 0.32     |
| Sales and Pre-Sales             | 0.93      | 0.27   | 0.42     |
| Service Outages and Maintenance | 0.82      | 0.60   | 0.69     |
| Technical Support               | 0.45      | 0.83   | 0.59     |

---

# 10. Aggregate Metrics

| Metric             | Score |
| ------------------ | ----- |
| Accuracy           | 0.53  |
| Macro Precision    | 0.75  |
| Macro Recall       | 0.42  |
| Macro F1-Score     | 0.49  |
| Weighted Precision | 0.60  |
| Weighted Recall    | 0.53  |
| Weighted F1-Score  | 0.51  |

---

# 11. Confusion Matrix Analysis

A confusion matrix was generated to visualize model predictions.

Observations:

* Strong classification performance for Billing and Payments.
* Technical Support achieved high recall.
* Service Outages and Maintenance showed strong separation from other classes.
* Product Support and Customer Service were frequently confused.
* Several minority classes exhibited lower recall due to fewer training examples.

The confusion matrix demonstrates that the model captures major ticket-routing patterns while still facing challenges with semantically similar departments.

---

# 12. Saved Model Artifacts

The following artifacts were successfully saved:

| File                 | Purpose                  |
| -------------------- | ------------------------ |
| xgboost.pkl          | Trained XGBoost model    |
| tfidf_vectorizer.pkl | TF-IDF feature extractor |
| label_encoder.pkl    | Queue label mappings     |

Directory:

```text
models/member3/
```

Files:

```text
models/member3/
├── xgboost.pkl
├── tfidf_vectorizer.pkl
└── label_encoder.pkl
```

These files enable future inference without retraining.

---

# 13. Strengths of the Model

* Successfully handles multi-class classification.
* Efficient training time.
* Uses only textual ticket content.
* Strong precision for several departments.
* Suitable baseline for comparison against deep learning approaches.

---

# 14. Limitations

* Lower performance on minority classes.
* Struggles with overlapping support categories.
* Does not capture deep semantic relationships between words.
* Performance depends heavily on TF-IDF feature quality.

---

# 15. Comparison with Deep Learning

The XGBoost model serves as the traditional machine learning baseline for this project.

In the next phase, a DistilBERT transformer model will be implemented and evaluated.

Expected improvements from DistilBERT:

* Better contextual understanding
* Improved semantic representation
* Higher recall for difficult classes
* Better overall classification accuracy

---

# 16. Conclusion

An XGBoost-based ticket routing system was successfully developed using TF-IDF features extracted from customer support ticket text.

The model achieved:

```text
Accuracy: 53.06%
Weighted F1 Score: 0.51
Macro F1 Score: 0.49
```

The model demonstrated effective performance as a traditional machine learning baseline and provides a strong benchmark for comparison with transformer-based approaches such as DistilBERT.

The trained model, vectorizer, and label encoder were successfully saved for deployment and future inference tasks.
