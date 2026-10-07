# SupportIQ Frontend

React + Vite interface for the SupportIQ customer support intelligence project.

The frontend provides three main views:

- a landing page,
- an AI ticket analyzer,
- an analytics dashboard.

It consumes the FastAPI backend through the shared client in:

~~~text
src/services/api.js
~~~

## Local Development

Install dependencies:

~~~bash
npm ci
~~~

Copy the environment example:

~~~bash
cp .env.example .env
~~~

Windows PowerShell:

~~~powershell
Copy-Item .env.example .env
~~~

The default configuration is:

~~~text
VITE_API_BASE_URL=http://127.0.0.1:8000
~~~

Start the development server:

~~~bash
npm run dev
~~~

Vite normally serves the app at:

~~~text
http://localhost:5173
~~~

## Production Build

~~~bash
npm run build
~~~

The generated static site is written to:

~~~text
dist/
~~~

## Frontend Routes

| Route | Purpose |
| --- | --- |
| / | Landing page |
| /analyzer | Submit and analyze a support ticket |
| /dashboard | View prediction history, model results, and runtime analytics |

## Backend Contract

The frontend expects these backend endpoints:

~~~text
GET  /health
POST /predict/
GET  /analytics/
GET  /analytics/history
~~~

The deployed queue prediction comes from the TF-IDF + XGBoost model. Priority, sentiment, and keyword outputs are transparent rule-based helpers returned by the backend.

## Deployment

The repository root contains a Vercel configuration that builds this frontend.

Public frontend:

https://nlp-group-35.vercel.app

A deployed frontend still needs VITE_API_BASE_URL to point to a reachable FastAPI backend for live prediction and analytics.

## Main Project Documentation

Return to the project root documentation:

- [Project README](../README.md)
- [Architecture](../docs/ARCHITECTURE.md)
- [Development guide](../docs/DEVELOPMENT.md)
- [Model results](../docs/MODEL_RESULTS.md)
