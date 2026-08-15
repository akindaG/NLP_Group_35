from backend.services.model_loader import (
    models,
    get_xgb_model
)

from backend.services.preprocessing import clean_text



# ==================================================
# Keyword extraction
# ==================================================

def extract_keywords(text):

    words = text.split()

    important_words = [
        word
        for word in words
        if len(word) > 4
    ]

    return important_words[:5]



# ==================================================
# Ticket prediction pipeline
# ==================================================

def predict_ticket(text):

    print("📝 Starting prediction")


    print("1️⃣ Cleaning text")

    cleaned = clean_text(text)



    print("2️⃣ Applying TF-IDF")

    vector = models["vectorizer"].transform(
        [cleaned]
    )



    print("3️⃣ Loading XGBoost")

    xgb_model = get_xgb_model()



    print("4️⃣ Running prediction")


    prediction = xgb_model.predict(
        vector
    )


    probabilities = xgb_model.predict_proba(
        vector
    )



    print("5️⃣ Decoding category")


    label = models["encoder"].inverse_transform(
        prediction
    )[0]



    confidence = round(
    float(probabilities.max()),
    3
    ) if probabilities is not None else None



    keywords = extract_keywords(
        cleaned
    )



    print("✅ Prediction completed")


    return {

        "category": label,

        "confidence": confidence,

        "keywords": keywords,

        "cleaned_text": cleaned

    }