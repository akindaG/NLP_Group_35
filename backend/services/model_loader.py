import joblib
from pathlib import Path


# ==================================================
# Project paths
# ==================================================

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_DIR = BASE_DIR / "models" / "member3"


# ==================================================
# Global cache
# ==================================================

_models = {}


# ==================================================
# Load static models
# ==================================================

def load_models():

    global _models


    if _models:
        return _models


    print("🚀 START MODEL LOADING")


    # -----------------------------
    # TF-IDF
    # -----------------------------

    print("Loading TF-IDF...")

    _models["vectorizer"] = joblib.load(
        MODEL_DIR / "tfidf_vectorizer.pkl"
    )

    print("✅ TF-IDF loaded")


    # -----------------------------
    # Encoder
    # -----------------------------

    print("Loading Label Encoder...")

    _models["encoder"] = joblib.load(
        MODEL_DIR / "label_encoder.pkl"
    )

    print("✅ Encoder loaded")


    print("🎉 STATIC MODELS READY")


    return _models



# ==================================================
# Lazy XGBoost loader
# ==================================================

def get_xgb_model():

    if "xgb" not in _models:

        print("Loading XGBoost...")


        model_path = MODEL_DIR / "xgboost.pkl"


        print(
            "XGBoost path:",
            model_path
        )


        _models["xgb"] = joblib.load(
            model_path
        )


        print(
            "✅ XGBoost loaded:",
            type(_models["xgb"])
        )


    return _models["xgb"]



# ==================================================
# Initialize
# ==================================================

models = load_models()