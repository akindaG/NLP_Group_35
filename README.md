---

# NLP_Group_35

# SupportIQ  
## Enterprise Customer Support Intelligence Platform using NLP

---

## 📌 Project Overview

SupportIQ is an end-to-end Natural Language Processing (NLP) based customer support intelligence system developed for the **CCS3356 – Natural Language Processing** module at **Sri Lanka Technology Campus (SLTC)**.

The system automatically analyzes customer support tickets and performs intelligent tasks including:

- Ticket Type Classification
- Department Routing
- Priority Prediction
- Sentiment Analysis
- Explainable AI Analysis
- Interactive Analytics Dashboard

The project evaluates and compares traditional Machine Learning models, Deep Learning models, and Transformer-based architectures for automated customer support ticket analysis.

---

# 🎯 Project Objectives

The main objectives of this project are:

### 1. Ticket Classification

Automatically identify the category of customer support tickets.

### 2. Department Routing

Assign incoming tickets to the most suitable support department.

### 3. Priority Prediction

Predict ticket urgency levels to improve support response efficiency.

### 4. Sentiment Analysis

Analyze customer emotions and sentiment from ticket content.

### 5. Explainable AI

Provide interpretable explanations for model predictions using explainability techniques.

### 6. Model Comparison

Compare different NLP architectures and evaluate their performance.

---

# 📊 Dataset

## Dataset Name

**Multilingual Customer Support Tickets Dataset**

Source:

https://www.kaggle.com/datasets/tobiasbueck/multilingual-customer-support-tickets


## Dataset Description

The dataset contains multilingual customer support conversations collected from different support domains.

Each record includes:

- Subject
- Customer Message Body
- Support Response
- Ticket Type
- Support Queue
- Priority Level
- Language


## Dataset Schema

| Column | Description |
|---|---|
| subject | Ticket title |
| body | Customer support request |
| answer | Support response |
| type | Ticket category |
| queue | Support department |
| priority | Ticket priority |
| language | Ticket language |


## Selected Dataset for Training

Only English-language tickets are selected for model development.

```python
df = df[df["language"] == "en"]
````

This improves consistency and reduces multilingual noise.

---

# 🎯 Prediction Tasks

## Task 1: Ticket Type Classification

Target:

```
type
```

Classes:

```
Incident
Request
Problem
Change
```

---

## Task 2: Priority Prediction

Target:

```
priority
```

Classes:

```
Low
Medium
High
```

---

## Task 3: Department Routing

Target:

```
queue
```

Classes:

```
Technical Support
Product Support
Customer Service
IT Support
Billing and Payments
Returns and Exchanges
Sales and Pre-Sales
Human Resources
General Inquiry
Service Outages and Maintenance
```

---

# 👨‍💻 Team Responsibilities

---

# Member 1

## CIT-24-01-0453

### Responsibilities

* Text preprocessing
* TF-IDF feature engineering
* Logistic Regression implementation
* BiLSTM implementation
* Model evaluation

### Main Files

```
src/preprocessing/

cleaning.py
tokenization.py
stopwords.py
lemmatization.py
pipeline.py


src/models/member1/

logistic_regression.py
bilstm.py
```

---

# Member 2

## CIT-24-01-0023

### Responsibilities

* Word2Vec embeddings
* SVM classifier
* GRU model implementation
* Model evaluation

### Main Files

```
src/models/member2/

word2vec_features.py
svm_classifier.py
gru_model.py
```

---

# Member 3

## CIT-24-01-0125

### Responsibilities

* Exploratory Data Analysis
* XGBoost classifier implementation
* DistilBERT transformer classifier
* Model training and evaluation
* Explainability integration support
* Final model integration support

### Main Files

```
src/models/member3/

xgboost_classifier.py
distilbert_classifier.py


reports/

member3_distilbert_results.json
member3_distilbert_summary.json
member3_xgboost_results.md


notebooks/

member3_distilbert.ipynb
member3_xgboost.ipynb
```

---

# 🏗 System Architecture

```
Customer Support Ticket

          │

          ▼

Text Preprocessing

          │

          ▼

Feature Engineering

          │

 ┌────────┼─────────┐

 ▼        ▼         ▼

TF-IDF  Word2Vec  DistilBERT


 ▼        ▼         ▼

Logistic  SVM     XGBoost

Regression GRU    DistilBERT


          │

          ▼

Model Evaluation


          │

          ▼

Explainable AI


          │

          ▼

Application Layer
```

---

# 🤖 Implemented Models

## Traditional Machine Learning

### Logistic Regression

* TF-IDF based baseline classifier
* Used for comparison

### Support Vector Machine (SVM)

* Word2Vec feature representation
* Classification model

### XGBoost

* Gradient boosting based classifier
* High-performance machine learning approach

---

# Deep Learning Models

## BiLSTM

* Learns sequential text patterns
* Captures contextual information

## GRU

* Lightweight recurrent neural architecture
* Efficient sequence modelling

---

# Transformer Model

## DistilBERT

DistilBERT is used as a transformer-based classifier.

Features:

* Pre-trained language representation
* Transfer learning approach
* CUDA GPU training support
* Context-aware text classification

---

# 📈 Explainable AI

Explainability techniques are used to understand model decisions.

## SHAP

Used for:

* Feature importance analysis
* Global model interpretation

## LIME

Used for:

* Individual prediction explanations
* Human-readable model interpretation

---

# 🧹 Data Preprocessing Pipeline

The preprocessing pipeline includes:

* Lowercasing
* Removing special characters
* Stopword removal
* Tokenization
* Lemmatization
* Text normalization

Combined text feature:

```python
df["text"] = df["subject"] + " " + df["body"]
```

---

# 📊 Evaluation Metrics

Models are evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

---

# 🚀 Application Components

## Backend

Framework:

```
Flask
```

Responsibilities:

* Model prediction API
* Request handling
* Integration with trained models

---

## Frontend

Framework:

```
Streamlit
```

Features:

* Ticket input interface
* Prediction visualization
* Analytics dashboard
* Model output display

---

# 📂 Project Structure

```
NLP_Group_35/

│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── notebooks/
│   ├── 01_data_profiling.ipynb
│   ├── member3_distilbert.ipynb
│   └── member3_xgboost.ipynb
│
├── reports/
│   ├── eda_summary.md
│   ├── member3_distilbert_results.json
│   └── member3_xgboost_results.md
│
├── screenshots/
│
├── src/
│   ├── preprocessing/
│   ├── models/
│   ├── routing/
│   └── sentiment/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🔄 Git Workflow

## Main Branch

```
main
```

## Development Branches

```
feature/member1-cit-24-01-0453-logreg-bilstm

feature/member2-cit-24-01-0023-svm-gru

feature/member3-cit-24-01-0125-xgboost-distilbert
```

Each member develops independently and merges changes through Pull Requests.

---

# 🛠 Technology Stack

## Programming

* Python

## Data Processing

* Pandas
* NumPy

## NLP

* NLTK
* Transformers

## Machine Learning

* Scikit-learn
* XGBoost

## Deep Learning

* TensorFlow
* PyTorch

## Explainability

* SHAP
* LIME

## Visualization

* Matplotlib
* Seaborn

## Backend

* Flask

## Frontend

* Streamlit

## Version Control

* Git
* GitHub

---

# 📋 Deliverables

## Source Code

Complete NLP system implementation

## Machine Learning Models

* Logistic Regression
* BiLSTM
* SVM
* GRU
* XGBoost
* DistilBERT

## Reports

* Exploratory Data Analysis Report
* Model Evaluation Reports
* Final Documentation

## Application

* Backend API
* Frontend Dashboard

---

# 🎓 Academic Information

**Module:**
CCS3356 – Natural Language Processing

**Institution:**
Sri Lanka Technology Campus (SLTC)

**Academic Year:**
2026

---

# 👥 Authors

## Group 35

### Member 1

CIT-24-01-0453

### Member 2

CIT-24-01-0023

### Member 3

CIT-24-01-0125

````

