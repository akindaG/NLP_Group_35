# Exploratory Data Analysis (EDA) Summary

## Project

**SupportIQ: Intelligent Customer Support Ticket Classification System**

**Course:** CCS3356 – Natural Language Processing

**Group:** NLP_Group_33

**Member Responsible:** CIT-24-01-0125 (Member 03 – Project Leader)

---

# 1. Dataset Information

## Dataset Name

Multilingual Customer Support Tickets Dataset

## Source

Kaggle

Dataset File:

```text
aa_dataset-tickets-multi-lang-5-2-50-version.csv
```

## Objective

The dataset contains multilingual customer support tickets submitted by customers to different support departments. The goal of this project is to automatically classify incoming customer tickets into the correct support queue using Natural Language Processing and Machine Learning techniques.

---

# 2. Dataset Summary

After filtering only English-language tickets for the project, the dataset statistics are:

| Metric               | Value  |
| -------------------- | ------ |
| Total Records        | 16,338 |
| Total Features       | 17     |
| Support Queues       | 10     |
| Ticket Types         | 4      |
| Priority Levels      | 3      |
| Unique Ticket Bodies | 16,338 |
| Duplicate Records    | 0      |
| Total Missing Values | 56,547 |

## Observation

* No duplicate records were found.
* Every ticket body is unique.
* Missing values exist in several columns and will be handled during preprocessing.
* Dataset size is sufficient for machine learning and deep learning experiments.

---

# 3. Language Distribution

## Results

| Language     | Count  |
| ------------ | ------ |
| English (en) | 16,338 |
| German (de)  | 12,249 |

### Observation

The dataset contains two languages:

* English
* German

English tickets represent the largest portion of the dataset and were selected as the common dataset for all team members.

### Screenshot

```text
screenshots/preprocessing/language_distribution.png
```

---

# 4. Queue Distribution

## Results

| Queue                           | Count |
| ------------------------------- | ----: |
| Technical Support               | 4,737 |
| Product Support                 | 3,073 |
| Customer Service                | 2,410 |
| IT Support                      | 1,942 |
| Billing and Payments            | 1,595 |
| Returns and Exchanges           |   820 |
| Service Outages and Maintenance |   664 |
| Sales and Pre-Sales             |   513 |
| Human Resources                 |   348 |
| General Inquiry                 |   236 |

### Observation

* Technical Support is the largest category.
* General Inquiry is the smallest category.
* The dataset is moderately imbalanced.
* Classification models must learn to distinguish between 10 support departments.

### Screenshot

```text
screenshots/preprocessing/queue_distribution.png
```

---

# 5. Ticket Type Distribution

## Results

| Ticket Type | Count |
| ----------- | ----: |
| Incident    | 6,571 |
| Request     | 4,665 |
| Problem     | 3,397 |
| Change      | 1,705 |

### Observation

Incident tickets dominate the dataset.

This indicates that most customers contact support because of existing issues rather than service requests or change requests.

### Screenshot

```text
screenshots/preprocessing/type_distribution.png
```

---

# 6. Priority Distribution

## Results

| Priority | Count |
| -------- | ----: |
| Medium   | 6,618 |
| High     | 6,346 |
| Low      | 3,374 |

### Observation

* Medium and High priority tickets are nearly balanced.
* Low priority tickets occur less frequently.
* Priority information may provide useful contextual features in future experiments.

### Screenshot

```text
screenshots/preprocessing/priority_distribution.png
```

---

# 7. Ticket Body Length Analysis

Text length was calculated using the customer ticket body field.

## Findings

* Most tickets contain between 100 and 600 characters.
* The average ticket length is approximately 350–400 characters.
* Very few tickets exceed 800 characters.

### Observation

The ticket lengths are appropriate for:

* TF-IDF based Machine Learning models
* XGBoost
* Logistic Regression
* Support Vector Machines
* BiLSTM
* GRU
* DistilBERT

### Screenshot

```text
screenshots/preprocessing/text_length_distribution.png
```

---

# 8. Average Ticket Length by Queue

Average ticket length was analyzed across support queues.

## Findings

* General Inquiry tickets contain the longest average text.
* Human Resources tickets contain the shortest average text.
* Most support queues have average ticket lengths between 350 and 400 characters.

### Observation

Ticket length differences between categories may provide useful classification signals for machine learning models.

### Screenshot

```text
screenshots/preprocessing/average_ticket_length_by_queue.png
```

---

# 9. Data Quality Assessment

## Missing Values

Total Missing Values:

```text
56,547
```

### Observation

Missing values are concentrated in non-target columns and can be handled during preprocessing using:

* Removal of irrelevant columns
* Imputation
* Default placeholders where necessary

---

## Duplicate Records

Total Duplicate Records:

```text
0
```

### Observation

No duplicate tickets were found.

This improves dataset quality and reduces the risk of data leakage during model training.

---

# 10. Target Variable Selection

## Input Feature

```text
body
```

The ticket body contains the detailed customer complaint and serves as the primary NLP feature.

## Target Variable

```text
queue
```

The queue field represents the support department assigned to each ticket.

---

# 11. Planned NLP Models

## Member 01

* Logistic Regression
* BiLSTM

## Member 02

* Support Vector Machine (SVM)
* GRU

## Member 03

* XGBoost
* DistilBERT

---

# 12. Key Findings

1. The dataset contains 16,338 English support tickets.
2. There are 10 support queue categories.
3. Ticket bodies are unique and contain meaningful textual information.
4. No duplicate records exist.
5. The dataset is moderately imbalanced but suitable for multiclass classification.
6. Ticket lengths are appropriate for both traditional machine learning and transformer-based models.
7. English tickets provide sufficient data for training and evaluation.
8. Queue classification represents a realistic industry customer support problem.

---

# 13. Conclusion

The Multilingual Customer Support Tickets dataset was selected as the final dataset for the SupportIQ project. After performing exploratory data analysis, the dataset was found to be suitable for multiclass NLP classification.

The English-language subset containing 16,338 records was prepared as the common dataset for all project members. The dataset provides sufficient size, diversity, and complexity to compare traditional machine learning models and deep learning approaches including Logistic Regression, SVM, XGBoost, BiLSTM, GRU, and DistilBERT.

The dataset will be used throughout model development, evaluation, explainability analysis, and final web application integration.
