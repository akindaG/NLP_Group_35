# SupportIQ Development Guide

This guide covers local setup, application configuration, quality checks, repository conventions, and common troubleshooting.

## Prerequisites

Recommended development environment:

~~~text
Python 3.12
Node.js 22
npm
Git
~~~

GitHub Actions currently validates the project using Python 3.12 and Node.js 22.

---

## Clone the Repository

~~~bash
git clone https://github.com/akindaG/NLP_Group_35.git
cd NLP_Group_35
~~~

---

## Backend Setup

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

Run the API from the repository root:

~~~bash
python -m uvicorn backend.app:app --reload
~~~

Default backend URL:

~~~text
http://127.0.0.1:8000
~~~

Swagger documentation:

~~~text
http://127.0.0.1:8000/docs
~~~

---

## Required Deployment Artifacts

The deployed backend expects these files:

~~~text
models/member3/tfidf_vectorizer.pkl
models/member3/label_encoder.pkl
models/member3/xgboost.pkl
~~~

The API can start without eagerly loading the XGBoost model. The /health endpoint reports whether the required artifacts exist and whether they have been loaded into memory.

---

## Backend Environment Variables

### CORS

By default, the API allows local Vite origins.

To override the list:

macOS or Linux:

~~~bash
export SUPPORTIQ_CORS_ORIGINS="http://localhost:5173,http://127.0.0.1:5173"
~~~

Windows PowerShell:

~~~powershell
$env:SUPPORTIQ_CORS_ORIGINS="http://localhost:5173,http://127.0.0.1:5173"
~~~

---

## Frontend Setup

~~~bash
cd frontend
npm ci
~~~

Copy the example environment file:

macOS or Linux:

~~~bash
cp .env.example .env
~~~

Windows PowerShell:

~~~powershell
Copy-Item .env.example .env
~~~

Configure the backend URL:

~~~text
VITE_API_BASE_URL=http://127.0.0.1:8000
~~~

Start the development server:

~~~bash
npm run dev
~~~

Default frontend URL:

~~~text
http://localhost:5173
~~~

Production build:

~~~bash
npm run build
~~~

---

## API Smoke Tests

Health:

~~~bash
curl http://127.0.0.1:8000/health
~~~

Prediction:

~~~bash
curl -X POST "http://127.0.0.1:8000/predict/" \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"Our VPN is unavailable and staff cannot connect.\"}"
~~~

Analytics:

~~~bash
curl http://127.0.0.1:8000/analytics/
~~~

History:

~~~bash
curl http://127.0.0.1:8000/analytics/history
~~~

---

## Quality Checks

Backend syntax:

~~~bash
python -m compileall -q backend src
~~~

Backend unit tests:

~~~bash
python -m unittest discover -s backend/tests -p "test_*.py" -v
~~~

Frontend production build:

~~~bash
cd frontend
npm ci
npm run build
~~~

The same checks are automated in:

~~~text
.github/workflows/quality.yml
~~~

---

## Output Provenance

The deployed application mixes a trained classifier with transparent helper rules.

| Output | Implementation |
| --- | --- |
| Support queue | TF-IDF + XGBoost |
| Confidence and top queues | XGBoost probabilities |
| Priority | backend/services/business_rules.py |
| Sentiment | backend/services/business_rules.py |
| Keywords | backend/services/business_rules.py |
| Human-review flag | confidence threshold |

This distinction should remain explicit in code, documentation, presentations, and portfolio descriptions.

---

## Prediction History

Runtime prediction history is stored under:

~~~text
backend/data/predictions.json
~~~

The file is generated automatically and excluded from version control.

Delete it locally if you want to reset development history. The backend recreates an empty history file when needed.

---

## Branch Strategy

The project uses member-specific and integration branches.

Examples:

~~~text
feature/member1-cit-24-01-0453-logreg-bilstm
feature/member2-cit-24-01-0023-svm-gru
feature/member3-cit-24-01-0125-xgboost-distilbert
feature/frontend-ui
feature/fullstack-integration
release/final-submission
main
~~~

Use descriptive commit messages such as:

~~~text
Added text preprocessing pipeline
Optimized SVM using GridSearchCV
Integrated XGBoost inference API
Fixed frontend health status integration
~~~

Avoid vague messages such as update, work, final, or done.

---

## Common Troubleshooting

### Health endpoint reports degraded

Check that these artifacts exist:

~~~text
models/member3/tfidf_vectorizer.pkl
models/member3/label_encoder.pkl
models/member3/xgboost.pkl
~~~

### Frontend cannot reach the API

Check:

1. the backend is running,
2. VITE_API_BASE_URL points to the correct backend,
3. the backend CORS list allows the frontend origin.

### Prediction returns HTTP 422

The API requires meaningful ticket text with at least two words and applies a maximum input length.

### Frontend builds but live predictions fail

A static frontend deployment still requires access to a running FastAPI backend. Configure VITE_API_BASE_URL in the deployment environment.

---

## Related Documentation

- [Project README](../README.md)
- [Architecture](ARCHITECTURE.md)
- [Model results](MODEL_RESULTS.md)
- [EDA summary](../reports/eda_summary.md)
