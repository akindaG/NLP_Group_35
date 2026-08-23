# SupportIQ Architecture

## System purpose

SupportIQ is a decision-support web application for customer support ticket analysis. The deployed machine-learning path predicts the support queue from ticket text using TF-IDF features and the Member 3 XGBoost classifier. Additional priority, sentiment, keyword, and review outputs are transparent rule-based recommendations and are not presented as separately trained ML models.

## Runtime flow

```text
React / Vite Frontend
        |
        | POST /predict/
        v
FastAPI Prediction Route
        |
        | input validation
        v
Text Preprocessing
        |
        v
TF-IDF Vectorizer
        |
        v
XGBoost Queue Classifier
        |
        +--> predicted support queue
        +--> confidence score
        +--> top-3 queue alternatives
        |
        v
Transparent Decision-Support Rules
        |
        +--> priority recommendation
        +--> lightweight sentiment recommendation
        +--> explanation keywords
        +--> human-review flag
        |
        v
Prediction History + Analytics API
        |
        v
Dashboard / Analyzer UI
```

## Output provenance

| Output | Source | Purpose |
| --- | --- | --- |
| Department / support queue | TF-IDF + XGBoost | Main deployed classification result |
| Confidence | XGBoost `predict_proba` | Indicates model certainty for the selected queue |
| Top predictions | XGBoost `predict_proba` | Shows useful alternative queues |
| Priority | Transparent keyword rules | Decision-support recommendation |
| Sentiment | Transparent lexicon rules | Lightweight decision-support signal |
| Keywords | Frequency-based extraction | Compact explanation aid |
| Human review recommendation | Confidence threshold | Flags predictions below 0.60 confidence |

This distinction is important for the presentation and viva. It prevents rule-based outputs from being incorrectly described as trained models.

## Model artifacts

The deployed backend expects these files:

```text
models/member3/
├── tfidf_vectorizer.pkl
├── label_encoder.pkl
└── xgboost.pkl
```

Model loading is lazy. The API can start and expose `/health` even before inference is called. The health endpoint reports whether every required artifact exists and whether it has already been loaded into memory.

## Backend endpoints

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/` | GET | Service metadata |
| `/health` | GET | Backend and model-artifact readiness |
| `/predict/` | POST | Analyze one support ticket |
| `/analytics/` | GET | Aggregated prediction analytics |
| `/analytics/history` | GET | Prediction history |
| `/docs` | GET | Interactive OpenAPI documentation |

## Configuration

Backend CORS origins can be configured with:

```bash
export SUPPORTIQ_CORS_ORIGINS="http://localhost:5173,http://127.0.0.1:5173"
```

Frontend API URL can be configured by copying `frontend/.env.example` to `frontend/.env` and changing:

```text
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## Local run

Backend:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
uvicorn backend.app:app --reload
```

Frontend:

```bash
cd frontend
npm ci
npm run dev
```

## Quality checks

The repository workflow in `.github/workflows/quality.yml` checks Python syntax, runs standard-library unit tests for the decision-support rules, installs frontend dependencies, and verifies that the React application builds successfully.

## Responsible AI behavior

SupportIQ should be described as a decision-support system, not an autonomous routing authority. Low-confidence queue predictions are explicitly flagged for human review. The response also identifies the source of each output so users can distinguish trained model results from transparent heuristic recommendations.
