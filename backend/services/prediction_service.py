from backend.services.model_loader import models
from backend.services.preprocessing import clean_text


def extract_keywords(text):

    words = text.split()

    important_words = [
        word for word in words
        if len(word) > 4
    ]

    return important_words[:5]


def predict_ticket(text):

    cleaned = clean_text(text)

    vector = models["vectorizer"].transform(
        [cleaned]
    )

    prediction = models["xgb"].predict(
        vector
    )

    label = models["encoder"].inverse_transform(
        prediction
    )[0]


    confidence = None

    if hasattr(models["xgb"], "predict_proba"):

        probabilities = models["xgb"].predict_proba(
            vector
        )

        confidence = float(
            probabilities.max()
        )


    keywords = extract_keywords(cleaned)


    return {
        "category": label,
        "confidence": confidence,
        "keywords": keywords,
        "cleaned_text": cleaned
    }