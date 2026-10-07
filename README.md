# SupportIQ

## Customer Support Intelligence Platform Using NLP

[![SupportIQ Quality Checks](https://github.com/akindaG/NLP_Group_35/actions/workflows/quality.yml/badge.svg)](https://github.com/akindaG/NLP_Group_35/actions/workflows/quality.yml)
[![Live Frontend](https://img.shields.io/badge/Live%20Frontend-Vercel-black)](https://nlp-group-35.vercel.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**SupportIQ** is an end-to-end NLP project for customer support ticket intelligence. It combines classical machine learning, recurrent neural networks, transformer experiments, a FastAPI backend, and a React frontend in one collaborative repository.

The deployed application routes support tickets with a **TF-IDF + XGBoost** classifier. It also adds transparent rule-based priority and sentiment recommendations, keyword extraction, confidence reporting, top alternative predictions, human-review flags, prediction history, and analytics.

> **Portfolio note:** this is an academic decision-support prototype. The support queue is predicted by a trained ML model. Priority, sentiment, and keyword outputs in the deployed application are transparent rule-based helpers, not separately trained production models.

### My contribution

My individual ownership in the group project includes **exploratory data analysis, XGBoost, DistilBERT, backend API work, application integration, and deployment work**. Member-specific branches and commit history are retained as contribution evidence.

**Verified model highlights**
- Ticket type: **BiLSTM 85.53% accuracy**
- Queue routing: **Tuned SVM 55.08% accuracy**
- Deployed queue model: **TF-IDF + XGBoost 53.06% accuracy**

The highest-scoring routing experiment is not the deployed model. XGBoost remained integrated because its serialized artifacts were already connected to runtime preprocessing, probability outputs, prediction history, and the application.

**Live frontend:** https://nlp-group-35.vercel.app  
**Architecture:** [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)  
**Model results:** [docs/MODEL_RESULTS.md](docs/MODEL_RESULTS.md)  
**Development guide:** [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md)  
**Dataset:** https://www.kaggle.com/datasets/tobiasbueck/multilingual-customer-support-tickets

---

## Project at a Glance

| Item | Details |
| --- | --- |
| Module | CCS3356 - Natural Language Processing |
| Institution | Sri Lanka Technology Campus |
| Academic year | 2026 |
| Group | 35 |
| Original dataset | 28,587 multilingual customer support tickets |
| Training subset | 16,338 English-language tickets |
| Supervised targets | Ticket type classification and support queue routing |
| Models explored | Logistic Regression, BiLSTM, SVM, GRU, XGBoost, DistilBERT |
| Deployed routing model | TF-IDF + XGBoost |
| Backend | FastAPI |
| Frontend | React + Vite |
| CI | GitHub Actions |

---

## Why This Project Matters

Customer support teams receive large volumes of free-text requests. Manual triage can be slow and inconsistent. SupportIQ explores how NLP can assist with:

- routing tickets to the correct support queue,
- estimating model confidence and alternative queue choices,
- highlighting tickets that should receive human review,
- surfacing lightweight priority and sentiment signals,
- tracking prediction activity through an analytics dashboard,
- comparing different NLP representations and model families.

The application is intentionally positioned as **decision support**, not autonomous customer support.

---

## What the Working Application Does

A user submits customer support text through the React interface. The backend then:

1. validates and cleans the ticket text,
2. transforms it using the saved TF-IDF vectorizer,
3. predicts a support queue using the saved XGBoost model,
4. returns prediction confidence and the top queue alternatives,
5. derives transparent priority and sentiment recommendations,
6. extracts informative keywords,
7. flags low-confidence predictions for human review,
8. stores the result for the analytics dashboard.

### Output provenance

| Output | Source |
| --- | --- |
| Support queue | Trained TF-IDF + XGBoost classifier |
| Confidence | XGBoost probability output |
| Top predictions | XGBoost probability ranking |
| Priority | Transparent keyword rules |
| Sentiment | Transparent lexicon rules |
| Keywords | Frequency-based extraction |
| Human-review flag | Confidence threshold |

This separation is important because it prevents heuristic outputs from being misrepresented as trained ML predictions.

---

## Dataset

The project uses the **Multilingual Customer Support Tickets Dataset** from Kaggle.

Source:  
https://www.kaggle.com/datasets/tobiasbueck/multilingual-customer-support-tickets

The original dataset contains **28,587** customer support tickets in English and German. The shared experimental dataset filters to **16,338 English-language tickets** for consistent training and evaluation.

Important fields include:

- subject,
- body,
- answer,
- ticket type,
- support queue,
- priority,
- language,
- dataset tags and metadata.

The processed English dataset is stored at:

~~~text
data/processed/customer_support_en.csv
~~~

---

## NLP Experiments

SupportIQ contains experiments for **two different prediction targets**. Results should be compared within the same task.

### Ticket Type Classification

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

**Best verified ticket type model:** BiLSTM at **85.53% accuracy**.

### Support Queue Routing

Target:

~~~text
queue
~~~

The routing task contains 10 support queue classes.

| Model | Representation | Accuracy | Weighted F1 | Macro F1 |
| --- | --- | ---: | ---: | ---: |
| **Tuned SVM** | Word2Vec sentence vectors | **55.08%** | **53.76%** | **49.87%** |
| XGBoost | TF-IDF | 53.06% | ~51% | ~49% |
| DistilBERT | Transformer | 36.83% | N/A | N/A |
| Optimized GRU | Sequence representation | 34.64% | 33.97% | 36.16% |

**Best verified experimental queue-routing model:** Tuned SVM at **55.08% accuracy**.

**Final deployed queue-routing model:** TF-IDF + XGBoost at **53.06% accuracy**.

The SVM achieved the higher experimental score. XGBoost remains the deployed model because its serialized artifacts were already integrated with runtime preprocessing, FastAPI inference, confidence reporting, prediction history, and the React application.

See [docs/MODEL_RESULTS.md](docs/MODEL_RESULTS.md) for the full comparison and evidence links.

---

## System Architecture

~~~text
Customer Support Ticket
        |
        v
Input Validation
        |
        v
Text Preprocessing
        |
        v
TF-IDF Vectorizer
        |
        v
XGBoost Queue Classifier
        |
        +-------------------+
        |                   |
        v                   v
Queue Prediction      Confidence + Top 3
        |
        v
Transparent Decision-Support Rules
        |
        +--> Priority recommendation
        +--> Sentiment recommendation
        +--> Keyword extraction
        +--> Human-review flag
        |
        v
FastAPI Backend
        |
        v
Prediction History + Analytics
        |
        v
React + Vite Frontend
~~~

More detail: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)

---

## Team Ownership

The assignment required each member to implement distinct ML and DL work while sharing the same project domain.

| Member | Student ID | Main ownership |
| --- | --- | --- |
| Member 1 | CIT-24-01-0453 | Preprocessing, TF-IDF, Logistic Regression, BiLSTM |
| Member 2 | CIT-24-01-0023 | Word2Vec, SVM, tuning, GRU, model comparison |
| **Member 3** | **CIT-24-01-0125** | **EDA, XGBoost, DistilBERT, backend API, application integration, deployment work** |

Member-specific branches and commit history are retained in the repository as evidence of individual contribution.

---

## Technology Stack

| Area | Technologies |
| --- | --- |
| Language | Python, JavaScript |
| Data and NLP | Pandas, NumPy, NLTK, Gensim |
| Machine learning | Scikit-learn, XGBoost, SVM |
| Deep learning | TensorFlow, Keras, PyTorch |
| Transformers | Hugging Face Transformers, DistilBERT |
| Backend | FastAPI, Uvicorn |
| Frontend | React, Vite, Recharts, Framer Motion |
| Version control | Git, GitHub |
| CI | GitHub Actions |

---

## Repository Structure

~~~text
NLP_Group_35/
|
├── backend/
│   ├── app.py
│   ├── routes/
│   ├── services/
│   ├── tests/
│   └── requirements.txt
|
├── data/
│   └── processed/
|
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DEVELOPMENT.md
│   └── MODEL_RESULTS.md
|
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── README.md
|
├── models/
│   ├── member2/
│   └── member3/
|
├── notebooks/
│   ├── 01_data_profiling.ipynb
│   ├── 02_member1_logistic_regression.ipynb
│   ├── 03_member1_bilstm.ipynb
│   ├── member3_xgboost.ipynb
│   └── member3_distilbert.ipynb
|
├── reports/
├── screenshots/
├── src/
│   ├── models/
│   └── preprocessing/
|
├── .github/workflows/quality.yml
├── requirements.txt
├── README.md
└── LICENSE
~~~

---

## Quick Start

### Prerequisites

Recommended:

- Python 3.12
- Node.js 22
- npm
- Git

### 1. Clone the repository

~~~bash
git clone https://github.com/akindaG/NLP_Group_35.git
cd NLP_Group_35
~~~

### 2. Start the backend

Create a virtual environment.

macOS or Linux:

~~~bash
python3 -m venv .venv
source .venv/bin/activate
~~~

Windows PowerShell:

~~~powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
~~~

Install backend dependencies:

~~~bash
pip install -r backend/requirements.txt
~~~

Run FastAPI:

~~~bash
python -m uvicorn backend.app:app --reload
~~~

Backend:

~~~text
http://127.0.0.1:8000
~~~

Interactive API docs:

~~~text
http://127.0.0.1:8000/docs
~~~

### 3. Start the frontend

Open a second terminal:

~~~bash
cd frontend
npm ci
~~~

For local development, copy the example environment file:

~~~bash
cp .env.example .env
~~~

Windows PowerShell:

~~~powershell
Copy-Item .env.example .env
~~~

The default API URL is:

~~~text
VITE_API_BASE_URL=http://127.0.0.1:8000
~~~

Start Vite:

~~~bash
npm run dev
~~~

Frontend:

~~~text
http://localhost:5173
~~~

The public Vercel frontend is linked above. Prediction functionality depends on VITE_API_BASE_URL being configured to a reachable FastAPI backend.

---

## API Endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| GET | / | Service metadata |
| GET | /health | Backend and model-artifact readiness |
| POST | /predict/ | Analyze one support ticket |
| GET | /analytics/ | Aggregated runtime analytics |
| GET | /analytics/history | Prediction history |
| GET | /docs | OpenAPI documentation |

Example request:

~~~bash
curl -X POST "http://127.0.0.1:8000/predict/" \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"My payment failed and I cannot complete the transaction.\"}"
~~~

---

## Quality Checks

The repository includes automated GitHub Actions checks for backend syntax, backend unit tests, and the frontend production build.

Run the backend checks locally:

~~~bash
python -m compileall -q backend src
python -m unittest discover -s backend/tests -p "test_*.py" -v
~~~

Run the frontend build:

~~~bash
cd frontend
npm ci
npm run build
~~~

The latest checked main-branch workflow completed successfully before this portfolio cleanup.

---

## Model and Data Evidence

Experiment evidence is kept in the repository rather than relying only on README claims.

Key files:

~~~text
reports/eda_summary.md
reports/member1_results.md
reports/member2_results.md
reports/member3_xgboost_results.md
reports/member3_distilbert_results.json
reports/member3_distilbert_summary.json
reports/images/
screenshots/
notebooks/
~~~

Large transformer checkpoints are intentionally excluded from Git tracking.

---

## Responsible AI and Limitations

SupportIQ is a decision-support prototype. It should not make consequential support decisions without human review.

Important limitations include:

- support queue classes are imbalanced and semantically overlapping,
- the deployed XGBoost model is not the highest-scoring experimental queue model,
- priority recommendation is rule-based,
- sentiment recommendation is lexicon-based,
- keyword extraction is a lightweight explanation rather than model-specific attribution,
- low-confidence predictions may be unreliable,
- performance may decrease on unseen organizations, new ticket types, slang, spelling errors, or unsupported languages,
- customer support text may contain sensitive or personally identifiable information.

The application flags predictions below a confidence threshold for human review and clearly identifies the source of each output.

---

## Documentation

- [Architecture and runtime flow](docs/ARCHITECTURE.md)
- [Development and setup guide](docs/DEVELOPMENT.md)
- [Verified model results](docs/MODEL_RESULTS.md)
- [EDA summary](reports/eda_summary.md)
- [Member 1 results](reports/member1_results.md)
- [Member 2 results](reports/member2_results.md)
- [Member 3 XGBoost results](reports/member3_xgboost_results.md)

---

## Academic Context

SupportIQ was developed for the **CCS3356 - Natural Language Processing** group assignment at **Sri Lanka Technology Campus**.

The repository demonstrates:

- a complete NLP workflow,
- multiple ML and DL approaches,
- individual model ownership,
- comparative evaluation,
- Git-based collaboration,
- responsible AI analysis,
- backend integration,
- a functional frontend,
- automated quality checks.

---

## License

This repository is licensed under the [MIT License](LICENSE).
