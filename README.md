---
# SupportIQ

## Enterprise Customer Support Intelligence Platform Using NLP

**SupportIQ** is an end-to-end Natural Language Processing system developed for the **CCS3356 . Natural Language Processing** module at **Sri Lanka Technology Campus (SLTC)**.

The project investigates how traditional machine learning, deep learning, and transformer-based NLP approaches can be applied to real-world customer-support ticket intelligence.

SupportIQ combines multiple NLP experiments with a working full-stack application capable of:

- Support queue prediction
- Prediction confidence estimation
- Priority recommendation
- Lightweight sentiment analysis
- Keyword-based explanation
- Prediction history
- Analytics and monitoring
- Interactive web-based ticket analysis

The final deployed demonstration uses a **TF-IDF + XGBoost** inference pipeline exposed through a **FastAPI** backend and consumed by a **React + Vite** frontend.

---

# 📌 Project Information

| Item | Details |
|---|---|
| Project Name | SupportIQ |
| Module | CCS3356 . Natural Language Processing |
| Institution | Sri Lanka Technology Campus |
| Academic Year | 2026 |
| Group | 35 |
| Repository | https://github.com/akindaG/NLP_Group_35 |

---

# 👥 Team Members

| Member | Student ID | Main Responsibilities |
|---|---|---|
| Member 1 | CIT-24-01-0453 | Text preprocessing, TF-IDF, Logistic Regression, BiLSTM |
| Member 2 | CIT-24-01-0023 | Word2Vec, Support Vector Machine, SVM tuning, GRU, model comparison |
| Member 3 | CIT-24-01-0125 | Exploratory Data Analysis, XGBoost, DistilBERT, backend API, integration and application development |

---

# 🎯 Project Objectives

The main objectives of SupportIQ are to:

1. Apply NLP preprocessing techniques to customer-support ticket text.
2. Develop and evaluate multiple machine-learning, deep-learning and transformer-based models.
3. Compare different NLP modelling approaches using verified evaluation results.
4. Perform ticket type classification.
5. Perform support queue routing.
6. Provide prediction confidence for the deployed routing model.
7. Recommend ticket priority through a lightweight rule-based layer.
8. Provide lightweight sentiment information for decision support.
9. Extract informative keywords from customer-support tickets.
10. Store prediction history and derive operational analytics.
11. Deploy an NLP model through a REST API.
12. Deliver the complete pipeline through a functional full-stack web application.

---

# 📊 Dataset

## Multilingual Customer Support Tickets Dataset

The project uses the **Multilingual Customer Support Tickets Dataset**.

Dataset source:

https://www.kaggle.com/datasets/tobiasbueck/multilingual-customer-support-tickets

The original dataset contains multilingual customer-support tickets covering multiple support domains.

For this project, English-language records were selected to improve experimental consistency and reduce multilingual variation during model development.

The processed English dataset contains approximately:

```text
16,338 customer-support tickets
````

---

# 📋 Important Dataset Fields

| Field             | Description                         |
| ----------------- | ----------------------------------- |
| `subject`         | Ticket title or subject             |
| `body`            | Customer-support request            |
| `answer`          | Support response                    |
| `type`            | Ticket type                         |
| `queue`           | Support queue / routing destination |
| `priority`        | Ticket priority                     |
| `language`        | Ticket language                     |
| `version`         | Dataset version                     |
| `tag_1` . `tag_8` | Ticket-related tags                 |

---

# 🧠 NLP Prediction Tasks

SupportIQ contains experiments for **two different supervised NLP targets**.

Results must therefore be compared within the same target rather than ranking every model solely by overall accuracy.

---

## Task 1 . Ticket Type Classification

Target variable:

```text
type
```

Ticket type classes include:

```text
Incident
Request
Problem
Change
```

Models evaluated for this task:

* Logistic Regression
* BiLSTM

---

## Task 2 . Support Queue Routing

Target variable:

```text
queue
```

The routing task contains **10 support queue classes**:

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

Models evaluated for this task:

* Word2Vec + Tuned SVM
* Optimized GRU
* TF-IDF + XGBoost
* DistilBERT

The final working application deploys:

```text
TF-IDF + XGBoost
```

for support queue routing.

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
                +-------------+-------------+
                |                           |
                v                           v
        Experimental Models         Deployment Pipeline
                |                           |
                v                           v
       Model Evaluation             TF-IDF Vectorizer
                |                           |
                v                           v
       Comparative Analysis              XGBoost
                                            |
                                            v
                                    Queue Prediction
                                            |
                          +-----------------+-----------------+
                          |                 |                 |
                          v                 v                 v
                      Priority          Sentiment         Keywords
                       Rules              Rules           Extraction
                          |                 |                 |
                          +-----------------+-----------------+
                                            |
                                            v
                                      FastAPI Backend
                                            |
                                            v
                                      React + Vite
                                            |
                                            v
                              Analyzer + Analytics Dashboard
```

---

# 🔄 NLP Development Pipeline

The overall project workflow is:

```text
Raw Dataset
    |
    v
English Language Filtering
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
Feature Engineering
    |
    +--------------------------+
    |                          |
    v                          v
Traditional ML             Deep Learning
    |                          |
    v                          v
TF-IDF / Word2Vec        Sequence Encoding
    |                          |
    v                          v
LR / SVM / XGBoost      BiLSTM / GRU / DistilBERT
    |                          |
    +------------+-------------+
                 |
                 v
            Evaluation
                 |
                 v
         Model Comparison
                 |
                 v
       Deployment Selection
                 |
                 v
        Full-Stack Integration
```

---

# 🧹 Text Preprocessing

The project preprocessing workflow includes techniques such as:

* Lowercasing
* Text normalization
* Removal of unnecessary characters
* Combining relevant ticket text fields
* Tokenization
* Stopword handling where applicable
* Lemmatization where applicable
* Preparation of cleaned text for downstream feature extraction

Reusable preprocessing code is stored under:

```text
src/preprocessing/
```

The deployed backend also contains runtime preprocessing under:

```text
backend/services/preprocessing.py
```

---

# 🤖 Model Implementations

# Member 1 . Logistic Regression

## Model

```text
Logistic Regression
```

## Task

```text
Ticket Type Classification
```

## Feature Representation

```text
TF-IDF
```

## Verified Accuracy

```text
83.69%
```

## Key Configuration

* 80/20 train-test split
* Random state: 42
* TF-IDF vocabulary limit: 5,000 features
* Maximum Logistic Regression iterations: 1,000

## Relevant Files

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

## Task

```text
Ticket Type Classification
```

## Verified Accuracy

```text
85.53%
```

The model uses sequential text representations and a bidirectional recurrent architecture to capture contextual information from both directions of the ticket sequence.

## Saved Artifacts

```text
src/models/member1/bilstm_model.keras
src/models/member1/tokenizer.pkl
src/models/member1/label_encoder.pkl
```

## Relevant Files

```text
notebooks/03_member1_bilstm.ipynb
reports/member1_results.md
reports/images/member1_bilstm_confusion_matrix.png
```

---

# 🤖 Member 2 . Word2Vec + Support Vector Machine

## Model

```text
Word2Vec + Support Vector Machine
```

## Task

```text
Support Queue Routing
```

## Target Variable

```text
queue
```

## Feature Representation

The SVM uses dense sentence-level representations generated from trained Word2Vec embeddings.

Word2Vec configuration includes approximately:

```text
Vector size: 100
Window size: 5
Minimum count: 2
Training epochs: 10
```

## Final Tuned SVM Results

```text
Accuracy: 55.08%
Weighted F1-score: 53.76%
Macro F1-score: 49.87%
```

## Best Hyperparameters

```text
C: 10
Kernel: RBF
Gamma: scale
```

The tuned Word2Vec + SVM experiment achieved the **highest verified accuracy among the support queue routing experiments**.

## Saved Artifacts

```text
models/member2/word2vec.model
models/member2/train_vectors.npy
models/member2/svm.pkl
```

## Relevant Files

```text
src/models/member2/word2vec_features.py
src/models/member2/svm_classifier.py
src/models/member2/svm_tuning.py
reports/member2_results.md
```

---

# 🧠 Member 2 . Optimized GRU

## Model

```text
Gated Recurrent Unit Neural Network
```

## Task

```text
Support Queue Routing
```

## Target Variable

```text
queue
```

## Architecture

The optimized GRU experiment uses a sequential neural architecture with configuration including:

```text
Vocabulary size: 10,000
Maximum sequence length: 100
Embedding dimension: 128
GRU units: 64
Dropout: 0.30
Dense hidden units: 32
Output activation: Softmax
```

## Training Improvements

The final GRU pipeline includes:

* Stratified dataset splitting
* Training-only tokenizer fitting
* Sequence padding
* `mask_zero=True` support
* Class weighting for class imbalance
* Early stopping
* Learning-rate reduction
* Best-weight restoration

## Verified Results

```text
Test Accuracy: 34.64%
Weighted F1-score: 33.97%
Macro F1-score: 36.16%
Test Loss: 1.7619
Best Validation Accuracy: 37.11%
```

## Saved Artifacts

```text
models/member2/gru.keras
models/member2/gru_tokenizer.pkl
models/member2/gru_label_encoder.pkl
```

## Relevant Files

```text
src/models/member2/gru_model.py
src/models/member2/comparison_member2.py
reports/member2_results.md
```

---

# 🌲 Member 3 . XGBoost

## Model

```text
XGBoost Classifier
```

## Task

```text
Support Queue Routing
```

## Feature Representation

```text
TF-IDF
```

## Number of Classes

```text
10
```

## Verified Results

```text
Accuracy: 53.06%
Weighted F1-score: approximately 0.51
Macro F1-score: approximately 0.49
```

## Saved Deployment Artifacts

```text
models/member3/xgboost.pkl
models/member3/tfidf_vectorizer.pkl
models/member3/label_encoder.pkl
```

These artifacts allow the final application to perform inference without retraining the model.

## Relevant Files

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

## Task

```text
Support Queue Routing
```

## Number of Classes

```text
10
```

## Training Configuration

```text
Epochs: 3
GPU acceleration: CUDA
GPU used during experiment: NVIDIA GeForce RTX 3050 Laptop GPU
```

## Verified Results

```text
Accuracy: 36.83%
Evaluation Loss: 1.6687
```

## Relevant Files

```text
notebooks/member3_distilbert.ipynb
reports/member3_distilbert_results.json
reports/member3_distilbert_summary.json
```

Large transformer checkpoint files are intentionally excluded from Git tracking to avoid storing unnecessarily large model artifacts directly in the repository.

---

# 📈 Verified Model Results

The project contains models trained for different prediction targets.

For a valid comparison, models are grouped according to their respective NLP task.

---

## Ticket Type Classification

| Model               |   Accuracy |
| ------------------- | ---------: |
| Logistic Regression |     83.69% |
| **BiLSTM**          | **85.53%** |

### Best Ticket Type Classification Model

```text
BiLSTM
Accuracy: 85.53%
```

BiLSTM achieved the strongest verified performance for the ticket type classification task.

---

## Support Queue Routing

| Model                    |   Accuracy | Weighted F1 |   Macro F1 |
| ------------------------ | ---------: | ----------: | ---------: |
| **Word2Vec + Tuned SVM** | **55.08%** |  **53.76%** | **49.87%** |
| TF-IDF + XGBoost         |     53.06% |        ~51% |       ~49% |
| DistilBERT               |     36.83% |         N/A |        N/A |
| Optimized GRU            |     34.64% |      33.97% |     36.16% |

### Best Experimental Support Queue Model

```text
Word2Vec + Tuned SVM
Accuracy: 55.08%
```

The tuned RBF SVM using Word2Vec-based feature representations achieved the highest verified experimental accuracy for support queue routing.

---

# ✅ Final Deployment Model

The final working SupportIQ application deploys:

```text
TF-IDF + XGBoost
```

for support queue routing.

Verified deployment-model accuracy:

```text
53.06%
```

Although the later **Word2Vec + Tuned SVM** experiment achieved a higher support queue routing accuracy of **55.08%**, the final demonstration application continues to use XGBoost.

This distinction is intentional.

The XGBoost pipeline had already been fully:

* Serialized
* Integrated
* Connected to runtime preprocessing
* Connected to FastAPI
* Connected to the React frontend
* Connected to prediction history
* Connected to analytics
* Tested using multiple live ticket inputs
* Validated through the production frontend build

Therefore:

```text
Best experimental Support Queue Routing model:
Word2Vec + Tuned SVM . 55.08%

Final deployed Support Queue Routing model:
TF-IDF + XGBoost . 53.06%
```

This distinction prevents experimental model ranking from being confused with application deployment status.

---

# ⚠️ Important Model Comparison Note

Model accuracy should only be directly compared when models solve the same target.

For example:

```text
BiLSTM
Target -> type

Tuned SVM
Target -> queue
```

These models solve different classification problems and therefore should not be ranked directly against each other solely using accuracy.

Within each prediction task:

```text
Ticket Type Classification
├── Logistic Regression . 83.69%
└── BiLSTM . 85.53%

Support Queue Routing
├── Tuned SVM . 55.08%
├── XGBoost . 53.06%
├── DistilBERT . 36.83%
└── Optimized GRU . 34.64%
```

---

# 🚀 Final Application

SupportIQ includes a functional full-stack NLP web application.

The deployed inference workflow is:

```text
React + Vite Frontend
          |
          v
FastAPI REST API
          |
          v
Runtime Text Preprocessing
          |
          v
TF-IDF Vectorization
          |
          v
XGBoost Classification
          |
          v
Support Queue Prediction
          |
          v
Confidence Estimation
          |
          +---------------------------+
          |             |             |
          v             v             v
      Priority       Sentiment     Keywords
       Rules           Rules       Extraction
          |             |             |
          +-------------+-------------+
                        |
                        v
                 Prediction Response
                        |
                        v
             History + Analytics
```

---

# ⚙️ Backend

## Framework

```text
FastAPI
```

The backend performs:

* Loading of saved model artifacts
* Runtime preprocessing
* TF-IDF feature transformation
* XGBoost inference
* Prediction decoding
* Confidence extraction
* Priority recommendation
* Lightweight sentiment recommendation
* Keyword extraction
* Prediction history persistence
* Analytics generation
* Backend health reporting

Important backend components include:

```text
backend/app.py

backend/routes/prediction.py
backend/routes/analytics.py

backend/services/model_loader.py
backend/services/preprocessing.py
backend/services/prediction_service.py
backend/services/business_rules.py
backend/services/history_service.py
```

---

# 🔌 Backend API Endpoints

The final backend exposes important endpoints including:

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

# 📤 Example Prediction Response

A prediction response follows a structure similar to:

```json
{
  "category": "Billing and Payments",
  "confidence": 0.622,
  "priority": "High",
  "department": "Billing and Payments",
  "sentiment": "Negative",
  "model_used": "TF-IDF + XGBoost",
  "keywords": [
    "payment",
    "failed",
    "cannot",
    "complete",
    "transaction"
  ],
  "cleaned_text": "my payment failed and i cannot complete the transaction"
}
```

Actual predictions depend on the submitted ticket.

---

# ✅ Verified Runtime Examples

During final integration testing, different customer-support tickets generated different live predictions.

### Payment Failure Example

Input:

```text
My payment failed and I cannot complete the transaction.
```

Observed output:

```text
Predicted Support Queue: Billing and Payments
Confidence: 62.2%
Priority: High
Sentiment: Negative
Model: TF-IDF + XGBoost
```

### Documentation Request Example

Input:

```text
Could you provide documentation and guidance about integrating this platform?
```

Observed output:

```text
Predicted Support Queue: Product Support
Confidence: 19.4%
Priority: Low
Sentiment: Neutral
Model: TF-IDF + XGBoost
```

### Service Outage Example

Input:

```text
Our production service is down and users cannot access their accounts due to an outage.
```

Observed output:

```text
Predicted Support Queue: Service Outages and Maintenance
Confidence: 64.6%
Priority: High
Sentiment: Negative
Model: TF-IDF + XGBoost
```

These tests demonstrate that the application performs dynamic inference rather than returning static demonstration values.

---

# 🚦 Priority Recommendation

Priority recommendation is implemented through a lightweight deterministic business-rule layer.

It considers urgency-related terms such as:

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

Possible outputs:

```text
High
Medium
Low
```

The priority recommendation layer is **separate from the XGBoost support queue classifier**.

It should therefore not be interpreted as a separately trained priority prediction model.

---

# 🙂 Sentiment Recommendation

The deployed application includes a lightweight lexicon-based sentiment component.

Possible outputs:

```text
Positive
Neutral
Negative
```

The sentiment layer uses simple positive and negative language indicators for decision support.

It is not presented as a separately trained supervised sentiment-classification model.

---

# 🔍 Keyword-Based Explanation

SupportIQ provides lightweight prediction explanation through keyword extraction.

Important words from the processed ticket are displayed alongside the final prediction.

This provides users with a simple indication of meaningful terms present in the input text.

The deployed implementation uses:

```text
Keyword-Based Explanation
```

rather than external post-hoc explainability frameworks such as SHAP or LIME.

---

# 📊 Analytics Dashboard

The SupportIQ analytics dashboard provides information including:

* Total processed tickets
* High-priority ticket count
* Deployed model accuracy
* Average prediction confidence
* Most common predicted support queue
* Support queue distribution
* Sentiment distribution
* Recent predictions
* Verified model evaluation results
* Backend/model health information

The deployed-model accuracy displayed on the operational dashboard refers specifically to:

```text
TF-IDF + XGBoost
Accuracy: 53.06%
```

---

# 🕘 Prediction History

Successful predictions can be stored by the backend.

Prediction history includes information such as:

```text
Prediction ID
Timestamp
Predicted Support Queue
Confidence
Priority
Sentiment
Model Used
Keywords
Processed Text
```

The analytics service uses this history to calculate runtime dashboard statistics.

Runtime prediction history is application-generated data and is excluded from version control where appropriate.

---

# 💻 Frontend

## Framework

```text
React + Vite
```

The frontend provides:

* Landing page
* AI Ticket Analyzer
* Dynamic prediction results
* Prediction confidence visualization
* Predicted support queue
* Routing recommendation
* Priority recommendation
* Sentiment information
* Keyword-based explanation
* Analytics dashboard
* Prediction history visualization
* Model performance information
* Backend health status

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
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── layouts/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   ├── package-lock.json
│   ├── eslint.config.js
│   └── vite.config.js
│
├── models/
│   ├── member2/
│   │   ├── word2vec.model
│   │   ├── train_vectors.npy
│   │   ├── svm.pkl
│   │   ├── gru.keras
│   │   ├── gru_tokenizer.pkl
│   │   └── gru_label_encoder.pkl
│   │
│   └── member3/
│       ├── xgboost.pkl
│       ├── tfidf_vectorizer.pkl
│       └── label_encoder.pkl
│
├── notebooks/
│   ├── 01_data_profiling.ipynb
│   ├── 02_member1_logistic_regression.ipynb
│   ├── 03_member1_bilstm.ipynb
│   ├── member2_eda.py
│   ├── member2_rebuild_processed.py
│   ├── member3_xgboost.ipynb
│   └── member3_distilbert.ipynb
│
├── reports/
│   ├── eda_summary.md
│   ├── member1_results.md
│   ├── member2_results.md
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
│   │   │   ├── word2vec_features.py
│   │   │   ├── svm_classifier.py
│   │   │   ├── svm_tuning.py
│   │   │   ├── gru_model.py
│   │   │   └── comparison_member2.py
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
* Gensim / Word2Vec
* Hugging Face Transformers

## Machine Learning

* Scikit-learn
* XGBoost
* Support Vector Machines

## Deep Learning

* TensorFlow / Keras
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

### Windows PowerShell

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

The final validated environment pins the XGBoost version required by the serialized deployment model.

---

## 4. Run the FastAPI Backend

From the project root:

```bash
python -m uvicorn backend.app:app --reload
```

The backend runs at:

```text
http://127.0.0.1:8000
```

---

## 5. Open FastAPI Documentation

Swagger UI:

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

Start the development server:

```bash
npm run dev
```

The frontend runs at:

```text
http://localhost:5173
```

---

# 🏭 Frontend Production Build

The final frontend can be validated using:

```bash
npm run build
```

The final integration build was successfully tested using the Vite production build process.

---

# 🧪 Running the Complete Application

Start the backend:

```bash
python -m uvicorn backend.app:app --reload
```

Then, in another terminal:

```bash
cd frontend
npm run dev
```

Open:

```text
http://localhost:5173
```

Use the Analyzer page to submit a customer-support ticket.

---

# 🔎 API Testing

The backend can also be tested directly.

## Health Check

```bash
curl http://127.0.0.1:8000/health
```

## Prediction Request

```bash
curl -X POST "http://127.0.0.1:8000/predict/" \
-H "Content-Type: application/json" \
-d '{"text":"My payment failed and I cannot complete the transaction."}'
```

## Analytics

```bash
curl http://127.0.0.1:8000/analytics/
```

## Prediction History

```bash
curl http://127.0.0.1:8000/analytics/history
```

---

# 🧪 Deployment Pipeline

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
     +-----------------------+
     |                       |
     v                       v
Priority Rules         Sentiment Rules
     |                       |
     +-----------+-----------+
                 |
                 v
          Keyword Extraction
                 |
                 v
         Prediction Response
                 |
                 v
       Prediction History
                 |
                 v
         Analytics Service
                 |
                 v
          React Interface
```

---

# 📉 Current Limitations

SupportIQ has several important limitations:

* Support queue routing contains 10 classes and remains a challenging multiclass NLP problem.
* Several support queues contain semantically overlapping language.
* Class imbalance affects minority-class performance.
* The deployed XGBoost model is not the highest-scoring experimental queue-routing model.
* Priority recommendation is rule-based rather than learned from a dedicated supervised model.
* Sentiment recommendation is lexicon-based.
* Keyword extraction provides lightweight explanation rather than model-specific attribution.
* GRU performance is limited by class imbalance and the complexity of the 10-class routing task.
* DistilBERT requires significantly more computational resources than classical models.
* Large transformer checkpoints are not committed directly to Git.
* Runtime prediction quality depends on how closely incoming support tickets resemble the training domain.
* The application is designed as an academic prototype rather than a production customer-support platform.

---

# ⚖️ Ethics and Responsible Use

SupportIQ is designed as a:

```text
Decision-Support System
```

It is **not** intended to replace human customer-support decision making.

Important considerations include:

* Incorrect ticket routing
* Incorrect priority recommendations
* Model bias
* Class imbalance
* Customer-data privacy
* Misclassification of urgent cases
* Over-reliance on automated recommendations
* Transparency of model limitations
* Human review of critical decisions

Human supervision remains important in real operational customer-support environments.

---

# 🔐 Privacy

Customer-support tickets may contain personally identifiable or sensitive information.

A production deployment should therefore include:

* Secure storage
* Access controls
* Data minimization
* Data-retention policies
* Encryption
* Privacy-compliant logging
* PII detection and masking
* Appropriate organizational governance

The academic application should therefore be treated as a prototype rather than a production system for sensitive customer information.

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

Individual development work is performed on member-specific feature branches.

The final verified application is consolidated through:

```text
release/final-submission
```

before being integrated into:

```text
main
```

for the final academic submission.

---

# 📝 Git Contribution Principles

The project Git workflow demonstrates:

* Individual feature branches
* Member-specific development
* Meaningful commit messages
* Pull requests
* Merge history
* Independent experimentation
* Integration commits
* Final release validation

Git history is retained as evidence of each group member's contribution.

---

# 📑 Project Reports

Important experiment reports include:

```text
reports/eda_summary.md

reports/member1_results.md

reports/member2_results.md

reports/member3_xgboost_results.md

reports/member3_distilbert_results.json

reports/member3_distilbert_summary.json
```

These files provide supporting experimental evidence for the final report and presentation.

---

# 📦 Model Artifacts

## Member 1

```text
src/models/member1/bilstm_model.keras
src/models/member1/tokenizer.pkl
src/models/member1/label_encoder.pkl
```

## Member 2

```text
models/member2/word2vec.model
models/member2/train_vectors.npy
models/member2/svm.pkl
models/member2/gru.keras
models/member2/gru_tokenizer.pkl
models/member2/gru_label_encoder.pkl
```

## Member 3 Deployment

```text
models/member3/xgboost.pkl
models/member3/tfidf_vectorizer.pkl
models/member3/label_encoder.pkl
```

---

# 📷 Visual Evidence

Project screenshots are stored under:

```text
screenshots/
```

Visual evidence may include:

* Dataset profiling
* Data distributions
* NLP preprocessing
* Model evaluation
* Confusion matrices
* FastAPI runtime
* Analyzer results
* Dashboard results
* Application functionality

---

# ✅ Final Verified Project Status

At the final integration stage, the following components were successfully implemented:

```text
Dataset Preparation                 ✅
Exploratory Data Analysis           ✅
Reusable NLP Preprocessing          ✅

Logistic Regression                 ✅
BiLSTM                              ✅
Word2Vec                            ✅
Tuned SVM                           ✅
Optimized GRU                       ✅
XGBoost                             ✅
DistilBERT                          ✅

FastAPI Backend                     ✅
Saved Model Loading                 ✅
Runtime XGBoost Inference           ✅
Confidence Calculation              ✅
Priority Recommendation             ✅
Sentiment Recommendation            ✅
Keyword-Based Explanation           ✅
Prediction History                  ✅
Analytics API                       ✅

React + Vite Frontend               ✅
Ticket Analyzer                     ✅
Dynamic Prediction Rendering        ✅
Analytics Dashboard                 ✅
Model Performance Display           ✅
Frontend Production Build           ✅

Git-Based Team Development          ✅
Member-Specific Model Work          ✅
Full-Stack Integration              ✅
```

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
* Text feature engineering
* TF-IDF
* Word2Vec
* Traditional machine learning
* Support Vector Machines
* Gradient boosting
* Recurrent neural networks
* Transformer models
* Hyperparameter tuning
* Class-imbalance handling
* Model evaluation
* Comparative experimentation
* Model serialization
* REST API development
* React frontend development
* Full-stack NLP integration
* Git-based collaborative development

---

# 🏆 Final Model Summary

## Ticket Type Classification

```text
BiLSTM
Accuracy: 85.53%
```

achieved the strongest verified ticket type classification result.

## Support Queue Routing

```text
Word2Vec + Tuned SVM
Accuracy: 55.08%
```

achieved the strongest verified experimental support queue routing result.

## Final Deployed Model

```text
TF-IDF + XGBoost
Accuracy: 53.06%
```

remains the model used by the final working SupportIQ application.

---

# 👥 Authors

## Group 35

### Member 1

```text
Student ID: CIT-24-01-0453
```

Primary areas:

```text
Preprocessing
TF-IDF
Logistic Regression
BiLSTM
```

### Member 2

```text
Student ID: CIT-24-01-0023
```

Primary areas:

```text
Word2Vec
Support Vector Machine
Hyperparameter Tuning
GRU
Model Comparison
```

### Member 3

```text
Student ID: CIT-24-01-0125
```

Primary areas:

```text
EDA
XGBoost
DistilBERT
Backend API
Full-Stack Integration
```

---

# 📄 License

This repository includes a:

```text
LICENSE
```

file.

---

# SupportIQ

**Enterprise Customer Support Intelligence Platform Using NLP**

**CCS3356 . Natural Language Processing**

**Sri Lanka Technology Campus . 2026**

**Group 35**
