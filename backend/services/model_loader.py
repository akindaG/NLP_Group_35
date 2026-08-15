import joblib
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_DIR = BASE_DIR / "models" / "member3"


def load_models():

    xgb_model = joblib.load(
        MODEL_DIR / "xgboost.pkl"
    )

    vectorizer = joblib.load(
        MODEL_DIR / "tfidf_vectorizer.pkl"
    )

    label_encoder = joblib.load(
        MODEL_DIR / "label_encoder.pkl"
    )

    return {
        "xgb": xgb_model,
        "vectorizer": vectorizer,
        "encoder": label_encoder
    }


models = load_models()