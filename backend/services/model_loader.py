"""Centralized lazy loading for SupportIQ model artifacts."""

from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_DIR = BASE_DIR / "models" / "member3"

ARTIFACT_PATHS = {
    "vectorizer": MODEL_DIR / "tfidf_vectorizer.pkl",
    "encoder": MODEL_DIR / "label_encoder.pkl",
    "xgb": MODEL_DIR / "xgboost.pkl",
}

_models = {}


def _require_artifact(name: str) -> Path:
    path = ARTIFACT_PATHS[name]
    if not path.exists():
        raise FileNotFoundError(
            f"Required model artifact '{name}' was not found at {path}. "
            "Ensure the trained Member 3 artifacts are available before starting inference."
        )
    return path


def load_models() -> dict:
    """Load the static TF-IDF vectorizer and label encoder once."""
    if "vectorizer" not in _models:
        _models["vectorizer"] = joblib.load(_require_artifact("vectorizer"))
    if "encoder" not in _models:
        _models["encoder"] = joblib.load(_require_artifact("encoder"))
    return _models


def get_models() -> dict:
    """Return the shared model cache after static artifacts are initialized."""
    return load_models()


def get_xgb_model():
    """Load the XGBoost classifier only when inference first needs it."""
    load_models()
    if "xgb" not in _models:
        _models["xgb"] = joblib.load(_require_artifact("xgb"))
    return _models["xgb"]


def get_model_status() -> dict:
    """Return artifact availability and in-memory load state for health checks."""
    artifacts = {
        name: {
            "exists": path.exists(),
            "loaded": name in _models,
            "path": str(path.relative_to(BASE_DIR)),
        }
        for name, path in ARTIFACT_PATHS.items()
    }
    return {
        "ready": all(item["exists"] for item in artifacts.values()),
        "artifacts": artifacts,
    }


# Backward-compatible cache reference for older imports. New code should call get_models().
models = _models
