"""SupportIQ FastAPI application entry point."""

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.analytics import router as analytics_router
from backend.routes.prediction import router as prediction_router
from backend.services.model_loader import get_model_status


def _cors_origins() -> list[str]:
    configured = os.getenv(
        "SUPPORTIQ_CORS_ORIGINS",
        "http://localhost:5173,http://127.0.0.1:5173",
    )
    return [origin.strip() for origin in configured.split(",") if origin.strip()]


app = FastAPI(
    title="SupportIQ AI API",
    description="NLP-based customer support ticket intelligence API",
    version="1.1.1",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins(),
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

app.include_router(prediction_router)
app.include_router(analytics_router)


@app.get("/", tags=["System"])
def home():
    return {
        "service": "SupportIQ AI API",
        "version": app.version,
        "status": "running",
        "docs": "/docs",
    }


@app.get("/health", tags=["System"])
def health_check():
    model_status = get_model_status()
    ready = bool(model_status["ready"])

    return {
        "status": "healthy" if ready else "degraded",
        "service": "SupportIQ API",
        "version": app.version,
        # Backward-compatible field consumed by the current React UI.
        "models": "loaded" if ready else "unavailable",
        # Detailed artifact readiness for diagnostics and future UI use.
        "model_status": model_status,
    }
