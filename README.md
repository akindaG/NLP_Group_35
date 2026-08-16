# SupportIQ

## Enterprise Customer Support Intelligence Platform Using NLP

SupportIQ is an end-to-end Natural Language Processing system developed for the **CCS3356 . Natural Language Processing** module at **Sri Lanka Technology Campus (SLTC)**.

The project investigates how traditional machine learning, deep learning, and transformer-based NLP approaches can be applied to customer-support ticket analysis.

The final application provides an interactive web interface for analyzing customer-support tickets, predicting the appropriate support queue, estimating confidence, recommending ticket priority, generating lightweight sentiment information, extracting informative keywords, storing prediction history, and visualizing analytics.

---

## 📌 Project Information

**Project Name:** SupportIQ
**Module:** CCS3356 . Natural Language Processing
**Institution:** Sri Lanka Technology Campus
**Academic Year:** 2026
**Group:** 35

**GitHub Repository:**
[https://github.com/akindaG/NLP_Group_35](https://github.com/akindaG/NLP_Group_35)

---

# 👥 Team Members

| Member   | Student ID     | Main Responsibilities                                                               |
| -------- | -------------- | ----------------------------------------------------------------------------------- |
| Member 1 | CIT-24-01-0453 | Text preprocessing, TF-IDF, Logistic Regression, BiLSTM                             |
| Member 2 | CIT-24-01-0023 | Word2Vec, Support Vector Machine, GRU, model comparison                             |
| Member 3 | CIT-24-01-0125 | Exploratory Data Analysis, XGBoost, DistilBERT, backend API, full-stack integration |

---

# 🎯 Project Objectives

The main objectives of SupportIQ are to:

1. Apply NLP preprocessing techniques to customer-support ticket text.
2. Develop and evaluate multiple machine-learning and deep-learning models.
3. Compare traditional, recurrent neural-network, and transformer-based NLP approaches.
4. Automatically predict an appropriate customer-support queue.
5. Provide confidence information for deployed model predictions.
6. Recommend ticket priority using a lightweight business-rule layer.
7. Provide lightweight sentiment information for decision support.
8. Extract informative keywords from processed ticket text.
9. Provide prediction-history and analytics functionality.
10. Deliver the NLP pipeline through a functional full-stack web application.

---

# 📊 Dataset

## Multilingual Customer Support Tickets Dataset

The project uses the **Multilingual Customer Support Tickets Dataset**.

Dataset source:

[https://www.kaggle.com/datasets/tobiasbueck/multilingual-customer-support-tickets](https://www.kaggle.com/datasets/tobiasbueck/multilingual-customer-support-tickets)

The original dataset contains multilingual customer-support tickets across multiple support domains.

For the experiments in this project, English-language records were selected to improve consistency and reduce multilingual variation during model development.

The processed English dataset contains approximately:

```text
16,338 records
```

---

# 📋 Dataset Fields

Important fields include:

| Field             | Description                 |
| ----------------- | --------------------------- |
| `subject`         | Ticket title or subject     |
| `body`            | Customer-support request    |
| `answer`          | Support response            |
| `type`            | Ticket type                 |
| `queue`           | Support queue or department |
| `priority`        | Ticket priority             |
| `language`        | Ticket language             |
| `version`         | Dataset version             |
| `tag_1` . `tag_8` | Ticket-related tags         |

---

# 🧠 NLP Tasks

The project contains experiments for more than one prediction target.

## Task 1 . Ticket Type Classification

Target variable:

```text
type
```

Classes include:

```text
Incident
Request
Problem
Change
```

Models developed for this task include:

* Logistic Regression
* BiLSTM
* Support Vector Machine
* GRU

---

## Task 2 . Support Queue Routing

Target variable:

```text
queue
```

The support-queue classes include:

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

Models evaluated for this task include:

* XGBoost
* DistilBERT

The final deployed application currently uses:

```text
TF-IDF + XGBoost
```

for support-queue routing.

---

# 🏗️ System Architecture

```text
Customer Support Ticket
          |
          v
Text Preprocessing
          |
          v
Feature Representation
          |
          v
ML / DL / Transformer Models
          |
          v
Model Evaluation
          |
          v
Selected Deployment Model
          |
          v
FastAPI Backend
          |
          v
React + Vite Frontend
          |
          v
Prediction + Analytics Dashboard
```

---

# 🔄 NLP Pipeline

The overall NLP workflow is:

```text
Raw Ticket
    |
    v
Language Filtering
    |
    v
Text Combination
    |
    v
Text Cleaning
    |
    v
Tokenization / Normalization
    |
    v
Feature Extraction
    |
    v
Model Training
    |
    v
Evaluation
    |
    v
Model Selection
    |
    v
Application Integration
```

---

# 🧹 Text Preprocessing

The project preprocessing pipeline includes techniques such as:

* Lowercasing
* Text normalization
* Removing unnecessary characters
* Tokenization
* Stopword handling
* Lemmatization where applicable
* Combining relevant ticket text fields

Reusable preprocessing code is stored under:

```text
src/preprocessing/
```

---

# 🤖 Model Implementations

## Member 1 . Logistic Regression

### Model

```text
Logistic Regression
```

### Feature Representation

```text
TF-IDF
```

### Task

```text
Ticket Type Classification
```

### Verified Accuracy

```text
83.69%
```

### Key Configuration

* 80/20 train-test split
* Random state: 42
* TF-IDF vocabulary limit: 5,000 features
* Maximum Logistic Regression iterations: 1,000

### Relevant Files

```text
notebooks/02_member1_logistic_regression.ipynb
reports/member1_results.md
src/preprocessing/
```

---

# 🧠 Member 1 . BiLSTM

## Model

```text
Bidirectional Long Short-Term Memory
```

### Task

```text
Ticket Type Classification
```

### Verified Accuracy

```text
85.53%
```

The model uses sequential text representations and a bidirectional recurrent architecture to capture contextual information from both directions of the input sequence.

### Saved Artifacts

```text
src/models/member1/bilstm_model.keras
src/models/member1/tokenizer.pkl
src/models/member1/label_encoder.pkl
```

### Relevant Files

```text
notebooks/03_member1_bilstm.ipynb
reports/member1_results.md
reports/images/member1_bilstm_confusion_matrix.png
```

---

# 🤖 Member 2 . Support Vector Machine

Member 2 is responsible for implementing a Support Vector Machine classifier using Word2Vec-based text representations.

### Main Responsibilities

* Word2Vec feature generation
* SVM training
* Hyperparameter tuning
* Model evaluation
* Classification metrics
* Confusion-matrix analysis

### Relevant Source Location

```text
src/models/member2/
```

Member 2's final evaluation values should be reported using the actual completed experiment outputs.

---

# 🧠 Member 2 . GRU

Member 2 is also responsible for implementing a Gated Recurrent Unit neural network.

### Main Responsibilities

* Text sequence preparation
* GRU architecture development
* Model training
* Validation
* Evaluation
* Comparison against the SVM approach

### Relevant Source Location

```text
src/models/member2/
```

The final SVM and GRU results should be documented using the actual experiment outputs rather than estimated values.

---

# 🌲 Member 3 . XGBoost

## Model

```text
XGBoost Classifier
```

### Feature Representation

```text
TF-IDF
```

### Task

```text
Support Queue Routing
```

### Number of Classes

```text
10
```

### Verified Results

```text
Accuracy: 53.06%
Weighted F1-score: 0.51
Macro F1-score: 0.49
```

### Saved Deployment Artifacts

```text
models/member3/xgboost.pkl
models/member3/tfidf_vectorizer.pkl
models/member3/label_encoder.pkl
```

These artifacts allow the deployed application to perform inference without retraining the model.

### Relevant Files

```text
notebooks/member3_xgboost.ipynb
reports/member3_xgboost_results.md
```

---

# 🤗 Member 3 . DistilBERT

## Base Model

```text
distilbert-base-uncased
```

### Task

```text
Support Queue Routing
```

### Number of Classes

```text
10
```

### Training Configuration

```text
Epochs: 3
GPU Acceleration: CUDA
GPU: NVIDIA GeForce RTX 3050 Laptop GPU
```

### Verified Results

```text
Accuracy: 36.83%
Evaluation Loss: 1.6687
```

### Relevant Files

```text
notebooks/member3_distilbert.ipynb
reports/member3_distilbert_results.json
reports/member3_distilbert_summary.json
```

Large transformer checkpoint files are intentionally excluded from Git tracking to avoid storing large model artifacts directly in the repository.

---

# 📈 Verified Model Results

The models in this project solve different prediction targets. Therefore, model results should be interpreted within their respective tasks rather than compared blindly across different targets.

## Ticket Type Classification

| Model               |                           Accuracy |
| ------------------- | ---------------------------------: |
| Logistic Regression |                             83.69% |
| BiLSTM              |                             85.53% |
| SVM                 | Refer to Member 2 final experiment |
| GRU                 | Refer to Member 2 final experiment |

---

## Support Queue Routing

| Model      | Accuracy |
| ---------- | -------: |
| XGBoost    |   53.06% |
| DistilBERT |   36.83% |

For the support-queue routing task, XGBoost achieved the stronger verified result and was selected as the deployment model.

---

# ✅ Final Deployment Model

The final application currently uses:

```text
TF-IDF + XGBoost
```

for support-queue routing.

The model selection was based on:

* Better verified performance than the DistilBERT experiment for the same target
* Lightweight local inference
* Saved deployable artifacts
* Lower inference complexity
* Straightforward integration with FastAPI
* Suitability for the final application demonstration

---

# ⚠️ Important Model Comparison Note

The following models should not be directly ranked against each other solely by accuracy:

```text
BiLSTM -> Ticket Type Classification
XGBoost -> Support Queue Routing
```

They predict different target variables and different numbers of classes.

Model comparison in the final report should therefore be organized by prediction task.

---

# 🚀 Final Application

SupportIQ includes a full-stack web application.

The application consists of:

```text
React + Vite Frontend
          |
          v
FastAPI REST API
          |
          v
Text Preprocessing
          |
          v
TF-IDF Vectorization
          |
          v
XGBoost Model
          |
          v
Prediction Response
          |
          v
Analytics + History
```

---

# ⚙️ Backend

## Framework

```text
FastAPI
```

The backend is responsible for:

* Loading saved NLP model artifacts
* Preprocessing incoming tickets
* Applying TF-IDF vectorization
* Running XGBoost inference
* Decoding model predictions
* Calculating confidence scores
* Generating priority recommendations
* Generating lightweight sentiment recommendations
* Extracting keywords
* Saving prediction history
* Providing analytics data

---

# 🔌 Backend API Endpoints

Important endpoints include:

```text
GET  /
GET  /health
POST /predict/
GET  /analytics/
GET  /analytics/history
```

---

# 📥 Example Prediction Request

```json
{
  "text": "My payment failed and I cannot complete the transaction."
}
```

---

# 📤 Example Prediction Response Structure

```json
{
  "category": "Predicted support queue",
  "confidence": 0.53,
  "priority": "High",
  "department": "Predicted support queue",
  "sentiment": "Negative",
  "model_used": "TF-IDF + XGBoost",
  "keywords": [
    "payment",
    "failed",
    "complete",
    "transaction"
  ],
  "cleaned_text": "processed ticket text"
}
```

The actual category, confidence, sentiment, priority, and extracted keywords depend on the submitted ticket.

---

# 🚦 Priority Recommendation

Priority recommendation is implemented as a lightweight deterministic business-rule layer.

It considers urgency-related language such as:

```text
urgent
critical
security breach
outage
cannot
unable
failed
blocked
error
```

Possible outputs are:

```text
High
Medium
Low
```

Priority recommendation is separate from the XGBoost support-queue classification model.

---

# 🙂 Sentiment Recommendation

The deployed application includes a lightweight lexicon-based sentiment component.

It uses positive and negative language indicators to provide one of the following outputs:

```text
Positive
Neutral
Negative
```

This component is intended for decision support.

It should not be interpreted as a separately trained supervised sentiment-classification model.

---

# 🔍 Keyword-Based Explanation

The deployed application provides lightweight explanation by extracting informative words from the processed ticket.

The extracted keywords are displayed alongside the model prediction to give users a simple indication of important terms present in the ticket.

The deployed implementation uses lightweight keyword-based explanation rather than external post-hoc explainability frameworks.

---

# 📊 Analytics Dashboard

The SupportIQ analytics dashboard provides information such as:

* Total processed tickets
* High-priority ticket count
* Deployed model accuracy
* Average prediction confidence
* Most common predicted support queue
* Support-queue distribution
* Sentiment distribution
* Recent predictions
* Verified model evaluation results
* Backend/model service status

---

# 🕘 Prediction History

Each successful prediction can be stored by the backend.

Prediction-history information includes fields such as:

```text
Prediction ID
Timestamp
Predicted Queue
Priority
Sentiment
Confidence
Model Used
Keywords
Processed Text
```

The analytics dashboard uses this history to generate statistics and visualizations.

---

# 💻 Frontend

## Framework

```text
React + Vite
```

The frontend provides:

* Landing page
* Ticket Analyzer
* Prediction Result Card
* Confidence visualization
* Keyword explanation
* Analytics Dashboard
* Prediction history visualization
* Backend health information

---

# 🖥️ Main Frontend Routes

```text
/            Landing Page
/analyzer    AI Ticket Analyzer
/dashboard   Analytics Dashboard
```

---

# 📂 Project Structure

```text
NLP_Group_35/
│
├── backend/
│   ├── __init__.py
│   ├── app.py
│   ├── requirements.txt
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── prediction.py
│   │   └── analytics.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── model_loader.py
│       ├── preprocessing.py
│       ├── prediction_service.py
│       ├── business_rules.py
│       └── history_service.py
│
├── data/
│   └── processed/
│       └── customer_support_en.csv
│
├── docs/
│
├── frontend/
│   ├── public/
│   │
│   ├── src/
│   │   ├── components/
│   │   ├── layouts/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
├── models/
│   ├── member2/
│   └── member3/
│       ├── xgboost.pkl
│       ├── tfidf_vectorizer.pkl
│       └── label_encoder.pkl
│
├── notebooks/
│   ├── 01_data_profiling.ipynb
│   ├── 02_member1_logistic_regression.ipynb
│   ├── 03_member1_bilstm.ipynb
│   ├── member3_xgboost.ipynb
│   └── member3_distilbert.ipynb
│
├── reports/
│   ├── eda_summary.md
│   ├── member1_results.md
│   ├── member3_xgboost_results.md
│   ├── member3_distilbert_results.json
│   ├── member3_distilbert_summary.json
│   └── images/
│
├── screenshots/
│
├── src/
│   ├── models/
│   │   ├── member1/
│   │   ├── member2/
│   │   └── member3/
│   │
│   └── preprocessing/
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

# 🛠️ Technology Stack

## Programming Languages

* Python
* JavaScript

## Data Processing

* Pandas
* NumPy

## NLP

* NLTK
* Hugging Face Transformers

## Machine Learning

* Scikit-learn
* XGBoost

## Deep Learning

* TensorFlow
* PyTorch

## Backend

* FastAPI
* Uvicorn

## Frontend

* React
* Vite
* Recharts
* Framer Motion
* Lucide React

## Visualization

* Matplotlib
* Recharts

## Version Control

* Git
* GitHub

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/akindaG/NLP_Group_35.git
```

Navigate to the project directory:

```bash
cd NLP_Group_35
```

---

# 🐍 Backend Setup

## 2. Create a Python Virtual Environment

### macOS / Linux

```bash
python3 -m venv integration_env
```

Activate it:

```bash
source integration_env/bin/activate
```

### Windows

```powershell
python -m venv integration_env
```

Activate it:

```powershell
.\integration_env\Scripts\Activate.ps1
```

---

## 3. Install Backend Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 4. Run the FastAPI Backend

From the project root:

```bash
python -m uvicorn backend.app:app --reload
```

The backend should run at:

```text
http://127.0.0.1:8000
```

---

## 5. Open API Documentation

FastAPI Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# ⚛️ Frontend Setup

Open a second terminal.

Navigate to:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the Vite development server:

```bash
npm run dev
```

The frontend should run at:

```text
http://localhost:5173
```

---

# 🧪 Testing the Application

Example ticket:

```text
My payment failed and I cannot complete the transaction.
```

The deployed pipeline performs:

```text
Input Ticket
     |
     v
Text Cleaning
     |
     v
TF-IDF Transformation
     |
     v
XGBoost Prediction
     |
     v
Support Queue Decoding
     |
     v
Confidence Calculation
     |
     +-------------------+
     |                   |
     v                   v
Priority Rule        Sentiment Rule
     |                   |
     +---------+---------+
               |
               v
         Keyword Extraction
               |
               v
       Prediction Response
               |
               v
        React Interface
```

---

# 🔎 API Testing

A prediction can also be tested through Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Use:

```text
POST /predict/
```

with:

```json
{
  "text": "Our service is down and customers cannot access their accounts."
}
```

---

# 📉 Current Limitations

The current system has several limitations:

* Support-queue routing contains 10 classes and remains a challenging classification task.
* Several support queues contain semantically overlapping language.
* Dataset class imbalance can affect recall for minority categories.
* Priority recommendation is rule-based.
* Sentiment recommendation is lexicon-based.
* Keyword extraction provides lightweight rather than advanced model-specific explanation.
* DistilBERT training requires considerably more computational resources.
* Large transformer checkpoints are not stored directly in Git.
* Prediction quality depends on the quality and domain similarity of incoming ticket text.

---

# ⚖️ Ethics and Responsible Use

SupportIQ is intended as a **decision-support system**, not a completely autonomous customer-support decision maker.

Important considerations include:

* Incorrect ticket routing
* Incorrect priority recommendations
* Model bias
* Class imbalance
* Customer-data privacy
* Misclassification of urgent cases
* Over-reliance on automated predictions
* Transparency of AI recommendations

Human review remains important for operational customer-support environments.

---

# 🔐 Privacy

Customer-support tickets may contain personally identifiable or sensitive information.

A production deployment should therefore include:

* Secure storage
* Access control
* Data minimization
* Appropriate retention policies
* Encryption
* Privacy-compliant logging
* Removal or masking of personal information where appropriate

---

# 🌿 Git Workflow

Development is organized using individual feature branches.

Important branches include:

```text
main

feature/member1-cit-24-01-0453-logreg-bilstm

feature/member2-cit-24-01-0023-svm-gru

feature/member3-cit-24-01-0125-xgboost-distilbert

feature/frontend-ui

feature/fullstack-integration

release/final-submission
```

The final project version is consolidated through:

```text
release/final-submission
```

before final integration into:

```text
main
```

---

# 📝 Git Contribution Principles

The repository uses:

* Individual feature branches
* Meaningful commit messages
* Pull requests
* Merge history
* Separate member contributions
* Final integration work

Git history is retained as evidence of each team member's contribution.

---

# 📑 Project Reports

Important reports include:

```text
reports/eda_summary.md

reports/member1_results.md

reports/member3_xgboost_results.md

reports/member3_distilbert_results.json

reports/member3_distilbert_summary.json
```

Additional Member 2 results should be included once the final SVM and GRU experiments are completed and pushed.

---

# 📷 Visual Evidence

Project screenshots are stored under:

```text
screenshots/
```

These include visual evidence related to:

* Dataset profiling
* Preprocessing
* Data distributions
* Model evaluation
* Application functionality where available

---

# 🎓 Academic Context

SupportIQ was developed as a group assignment for:

```text
CCS3356 . Natural Language Processing
```

at:

```text
Sri Lanka Technology Campus
```

The project demonstrates practical experience with:

* NLP preprocessing
* Feature engineering
* Traditional machine learning
* Deep learning
* Transformer models
* Model evaluation
* API development
* Frontend development
* Full-stack NLP integration
* Git-based collaborative development

---

# 👥 Authors

## Group 35

### Member 1

```text
CIT-24-01-0453
```

### Member 2

```text
CIT-24-01-0023
```

### Member 3

```text
CIT-24-01-0125
```

---

# 📄 License

This repository includes a `LICENSE` file.

---

# SupportIQ

**Enterprise Customer Support Intelligence Platform Using NLP**

**CCS3356 . Natural Language Processing**

**Sri Lanka Technology Campus . 2026**
