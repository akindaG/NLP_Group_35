from backend.services.model_loader import models
from backend.services.preprocessing import clean_text


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


    return {
        "category": label,
        "cleaned_text": cleaned
    }