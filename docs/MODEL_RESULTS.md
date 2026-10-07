# SupportIQ Model Results

This document consolidates the verified model results currently stored in the repository.

## Comparison Rule

SupportIQ contains experiments for two different supervised targets:

1. ticket type classification,
2. support queue routing.

Models should only be ranked directly against other models solving the same target.

---

## Ticket Type Classification

Target:

~~~text
type
~~~

Classes:

~~~text
Incident
Request
Problem
Change
~~~

| Model | Representation | Accuracy |
| --- | --- | ---: |
| Logistic Regression | TF-IDF | 83.69% |
| **BiLSTM** | Sequence representation | **85.53%** |

### Logistic Regression

Verified result:

~~~text
Accuracy: 83.69%
Weighted precision: 0.83
Weighted recall: 0.84
Weighted F1: 0.83
~~~

Evidence:

- [reports/member1_results.md](../reports/member1_results.md)
- [notebooks/02_member1_logistic_regression.ipynb](../notebooks/02_member1_logistic_regression.ipynb)

### BiLSTM

Verified result:

~~~text
Accuracy: 85.53%
~~~

Evidence:

- [reports/member1_results.md](../reports/member1_results.md)
- [notebooks/03_member1_bilstm.ipynb](../notebooks/03_member1_bilstm.ipynb)
- [reports/images/member1_bilstm_confusion_matrix.png](../reports/images/member1_bilstm_confusion_matrix.png)

**Best verified ticket type classifier:** BiLSTM at **85.53% accuracy**.

---

## Support Queue Routing

Target:

~~~text
queue
~~~

The routing problem contains 10 classes.

| Model | Representation | Accuracy | Weighted F1 | Macro F1 |
| --- | --- | ---: | ---: | ---: |
| **Tuned SVM** | Word2Vec sentence vectors | **55.08%** | **53.76%** | **49.87%** |
| XGBoost | TF-IDF | 53.06% | ~51% | ~49% |
| DistilBERT | Transformer | 36.83% | N/A | N/A |
| Optimized GRU | Sequence representation | 34.64% | 33.97% | 36.16% |

### Word2Vec + Tuned SVM

Best hyperparameters recorded in the project:

~~~text
C: 10
Kernel: RBF
Gamma: scale
~~~

Verified result:

~~~text
Accuracy: 55.08%
Weighted F1: 53.76%
Macro F1: 49.87%
~~~

Evidence:

- [reports/member2_results.md](../reports/member2_results.md)
- [src/models/member2/word2vec_features.py](../src/models/member2/word2vec_features.py)
- [src/models/member2/svm_classifier.py](../src/models/member2/svm_classifier.py)
- [src/models/member2/svm_tuning.py](../src/models/member2/svm_tuning.py)

### Optimized GRU

Verified result:

~~~text
Test accuracy: 34.64%
Weighted F1: 33.97%
Macro F1: 36.16%
Test loss: 1.7619
Best validation accuracy: 37.11%
~~~

Evidence:

- [reports/member2_results.md](../reports/member2_results.md)
- [src/models/member2/gru_model.py](../src/models/member2/gru_model.py)
- [src/models/member2/comparison_member2.py](../src/models/member2/comparison_member2.py)

### TF-IDF + XGBoost

Verified result:

~~~text
Accuracy: 53.06%
Weighted F1: approximately 0.51
Macro F1: approximately 0.49
~~~

Evidence:

- [reports/member3_xgboost_results.md](../reports/member3_xgboost_results.md)
- [notebooks/member3_xgboost.ipynb](../notebooks/member3_xgboost.ipynb)
- [screenshots/xgboost/confusion_matrix.png](../screenshots/xgboost/confusion_matrix.png)

Saved deployment artifacts:

~~~text
models/member3/xgboost.pkl
models/member3/tfidf_vectorizer.pkl
models/member3/label_encoder.pkl
~~~

### DistilBERT

Verified result:

~~~text
Accuracy: 36.83%
Evaluation loss: 1.6687
~~~

Evidence:

- [reports/member3_distilbert_results.json](../reports/member3_distilbert_results.json)
- [reports/member3_distilbert_summary.json](../reports/member3_distilbert_summary.json)
- [notebooks/member3_distilbert.ipynb](../notebooks/member3_distilbert.ipynb)

Large transformer checkpoint files are not tracked in Git.

---

## Best Experimental Models

### Ticket type

~~~text
BiLSTM
Accuracy: 85.53%
~~~

### Support queue

~~~text
Word2Vec + Tuned SVM
Accuracy: 55.08%
~~~

---

## Final Deployed Model

The working application deploys:

~~~text
TF-IDF + XGBoost
Support queue accuracy: 53.06%
~~~

The final application continues to use XGBoost even though the tuned SVM achieved a higher experimental queue-routing accuracy.

The XGBoost artifacts were already integrated with:

- runtime text preprocessing,
- FastAPI inference,
- prediction probabilities,
- top alternative predictions,
- prediction history,
- analytics,
- the React analyzer and dashboard.

This is a deployment decision, not a claim that XGBoost was the highest-scoring experimental queue model.

---

## Evaluation Caveats

Accuracy alone is not sufficient for this project because support queues are imbalanced. Macro F1 is especially useful for checking performance across minority and majority classes.

The repository also keeps confusion matrices and detailed classification reports where available.

Do not compare BiLSTM accuracy directly against SVM or XGBoost accuracy because BiLSTM solves ticket type classification while the queue models solve support queue routing.
