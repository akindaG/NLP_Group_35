# Member 2 Model Results

## SupportIQ NLP Project

**Member:** Member 2
**Student ID:** CIT-24-01-0023

---

# 1. Prediction Task

Member 2 evaluated machine-learning and deep-learning approaches for **Support Queue Routing**.

Target column:

`queue`

Processed English-language dataset size: **16,338 tickets**

Number of support queue classes: **10**

---

# 2. Queue Distribution

| Queue | Records |
|---|---:|
| Technical Support | 4737 |
| Product Support | 3073 |
| Customer Service | 2410 |
| IT Support | 1942 |
| Billing and Payments | 1595 |
| Returns and Exchanges | 820 |
| Service Outages and Maintenance | 664 |
| Sales and Pre-Sales | 513 |
| Human Resources | 348 |
| General Inquiry | 236 |

The support queue dataset is class-imbalanced. Therefore accuracy, weighted F1 and macro F1 were considered during evaluation.

---

# 3. Word2Vec Feature Engineering

The Support Vector Machine uses dense sentence embeddings generated from the cleaned ticket text.

Word2Vec configuration:

- Vector size: 100
- Context window: 5
- Minimum word count: 2
- Training epochs: 10

Sentence-vector matrix: `(16338, 100)`

---

# 4. Baseline Support Vector Machine

Baseline configuration:

- Kernel: RBF
- C: 1.0
- Gamma: scale
- Test size: 20%
- Random state: 42
- Stratified split: Yes

## Baseline SVM Results

| Metric | Score |
|---|---:|
| Accuracy | 0.4259 |
| Weighted Precision | 0.4908 |
| Weighted Recall | 0.4259 |
| Weighted F1 | 0.3714 |
| Macro F1 | 0.2645 |

---

# 5. Tuned Support Vector Machine

GridSearchCV was used to optimize the SVM using weighted F1 as the scoring metric.

Best hyperparameters:

- C: 10
- Kernel: RBF
- Gamma: scale

Best cross-validation weighted F1: **0.4986**

## Tuned SVM Test Results

| Metric | Score |
|---|---:|
| Accuracy | 0.5508 |
| Weighted Precision | 0.5792 |
| Weighted Recall | 0.5508 |
| Weighted F1 | 0.5376 |
| Macro Precision | 0.6621 |
| Macro Recall | 0.4443 |
| Macro F1 | 0.4987 |

## SVM Improvement After Tuning

| Metric | Baseline | Tuned | Gain |
|---|---:|---:|---:|
| Accuracy | 0.4259 | 0.5508 | +0.1249 |
| Weighted F1 | 0.3714 | 0.5376 | +0.1662 |
| Macro F1 | 0.2645 | 0.4987 | +0.2342 |

### Tuned SVM Classification Report

```text
                                 precision    recall  f1-score   support

           Billing and Payments       0.84      0.73      0.78       319
               Customer Service       0.48      0.48      0.48       482
                General Inquiry       0.62      0.17      0.27        47
                Human Resources       0.83      0.36      0.50        70
                     IT Support       0.56      0.32      0.41       388
                Product Support       0.49      0.47      0.48       615
          Returns and Exchanges       0.79      0.25      0.38       164
            Sales and Pre-Sales       0.76      0.28      0.41       103
Service Outages and Maintenance       0.74      0.60      0.66       133
              Technical Support       0.51      0.78      0.61       947

                       accuracy                           0.55      3268
                      macro avg       0.66      0.44      0.50      3268
                   weighted avg       0.58      0.55      0.54      3268
```

### Tuned SVM Confusion Matrix

Class order:

`Billing and Payments, Customer Service, General Inquiry, Human Resources, IT Support, Product Support, Returns and Exchanges, Sales and Pre-Sales, Service Outages and Maintenance, Technical Support`

```text
[[234  25   0   2   3  18   1   1   0  35]
 [ 16 229   3   1  22  62   3   2   3 141]
 [  0   7   8   0   4   8   0   0   0  20]
 [  1   7   0  25   3  12   0   0   0  22]
 [  3  28   0   0 126  45   1   0   5 180]
 [  8  58   0   0  18 287   5   3   5 231]
 [  6  31   1   0   1  34  41   0   1  49]
 [  0  31   0   0   3  23   0  29   1  16]
 [  0   8   0   0   8   8   0   0  80  29]
 [ 11  53   1   2  36  86   1   3  13 741]]
```

---

# 6. Baseline GRU

Initial GRU configuration:

- Maximum vocabulary size: 10,000
- Maximum sequence length: 100
- Embedding dimension: 128
- GRU units: 64
- Dropout: 0.30
- Dense hidden layer: 32 units
- Output activation: Softmax
- Epochs: 5
- Batch size: 32

The baseline GRU suffered from majority-class collapse and predicted the dominant Technical Support class for most test examples.

## Baseline GRU Results

| Metric | Score |
|---|---:|
| Test Loss | 1.9703 |
| Accuracy | 0.2898 |
| Weighted Precision | 0.0840 |
| Weighted Recall | 0.2898 |
| Weighted F1 | 0.1302 |
| Macro F1 | 0.0449 |

---

# 7. Optimized GRU

The GRU was improved using:

- Padding masking with `mask_zero=True`
- Balanced class weights
- Stratified train, validation and test splits
- Tokenizer fitted only on training data
- Early stopping
- Learning-rate reduction
- Up to 15 training epochs
- Best-weight restoration

Verified training information:

- Best validation accuracy: 0.3711
- Best validation accuracy epoch: 9
- Best validation loss: 1.7598
- Best validation loss epoch: 6

## Optimized GRU Test Results

| Metric | Score |
|---|---:|
| Test Loss | 1.7619 |
| Keras Test Accuracy | 0.3464 |
| Accuracy | 0.3464 |
| Weighted Precision | 0.3624 |
| Weighted Recall | 0.3464 |
| Weighted F1 | 0.3397 |
| Macro Precision | 0.3313 |
| Macro Recall | 0.4385 |
| Macro F1 | 0.3616 |

## GRU Improvement After Optimization

| Metric | Baseline | Optimized | Gain |
|---|---:|---:|---:|
| Accuracy | 0.2898 | 0.3464 | +0.0566 |
| Weighted F1 | 0.1302 | 0.3397 | +0.2095 |
| Macro F1 | 0.0449 | 0.3616 | +0.3167 |

### Optimized GRU Classification Report

```text
                                 precision    recall  f1-score   support

           Billing and Payments       0.63      0.73      0.68       319
               Customer Service       0.28      0.23      0.25       482
                General Inquiry       0.22      0.49      0.30        47
                Human Resources       0.19      0.49      0.27        70
                     IT Support       0.24      0.36      0.28       388
                Product Support       0.30      0.21      0.24       615
          Returns and Exchanges       0.26      0.41      0.32       164
            Sales and Pre-Sales       0.33      0.50      0.40       103
Service Outages and Maintenance       0.43      0.70      0.53       133
              Technical Support       0.44      0.27      0.33       947

                       accuracy                           0.35      3268
                      macro avg       0.33      0.44      0.36      3268
                   weighted avg       0.36      0.35      0.34      3268
```

### Optimized GRU Confusion Matrix

Class order:

`Billing and Payments, Customer Service, General Inquiry, Human Resources, IT Support, Product Support, Returns and Exchanges, Sales and Pre-Sales, Service Outages and Maintenance, Technical Support`

```text
[[234  28   6   6   7   8   9   6   3  12]
 [ 47 110  23  22  62  71  40  24  18  65]
 [  1   8  23   2   6   2   1   2   0   2]
 [  2   2   2  34  10   9   2   2   2   5]
 [ 14  31  10  23 138  35  11  15  30  81]
 [ 22  72  14  35 103 128  65  23  20 133]
 [  5  27   3   7  10  24  68   5   2  13]
 [  5  15   6   2   6   4   7  52   2   4]
 [  5   8   0   2  13   2   1   1  93   8]
 [ 36  88  17  49 226 149  54  29  47 252]]
```

---

# 8. Overall Member 2 Model Comparison

| Model | Accuracy | Weighted F1 | Macro F1 |
|---|---:|---:|---:|
| Baseline SVM | 0.4259 | 0.3714 | 0.2645 |
| Tuned SVM | 0.5508 | 0.5376 | 0.4987 |
| Baseline GRU | 0.2898 | 0.1302 | 0.0449 |
| Optimized GRU | 0.3464 | 0.3397 | 0.3616 |

---

# 9. Best Member 2 Model

The strongest Member 2 model is:

**Word2Vec + Tuned RBF SVM**

The tuned SVM achieved the highest weighted F1 score.

The tuned SVM achieved stronger overall performance than the optimized GRU on the held-out test set.

The SVM achieved higher accuracy, weighted F1 and macro F1 while requiring less training complexity than the GRU.

The optimized GRU nevertheless improved substantially over the baseline GRU. Padding masking, balanced class weights, early stopping and learning-rate scheduling improved minority-class recognition.

---

# 10. Final Conclusion

Member 2's experiments demonstrate that Word2Vec sentence embeddings combined with a tuned RBF Support Vector Machine provide the strongest Member 2 solution for support queue routing.

Best SVM configuration:

- C = 10
- Kernel = RBF
- Gamma = scale

Final tuned SVM results:

- Accuracy: 0.5508
- Weighted F1: 0.5376
- Macro F1: 0.4987

Final optimized GRU results:

- Accuracy: 0.3464
- Weighted F1: 0.3397
- Macro F1: 0.3616

Therefore, **Word2Vec + Tuned RBF SVM** is selected as Member 2's best-performing model.
