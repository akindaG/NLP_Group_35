from backend.services.model_loader import (
    models,
    get_xgb_model
)

from backend.services.preprocessing import clean_text


# ==================================================
# Keyword extraction
# ==================================================

STOP_WORDS = {
    "the",
    "is",
    "are",
    "a",
    "an",
    "and",
    "this",
    "that",
    "with",
    "from",
    "for",
    "my",
    "our",
    "to",
    "of",
    "in",
    "on",
    "it",
    "i",
    "we"
}


def extract_keywords(text):

    words = text.lower().split()

    keywords = [
        word
        for word in words
        if word not in STOP_WORDS
        and len(word) > 3
    ]

    return keywords[:5]


# ==================================================
# Priority recommendation
# ==================================================

def determine_priority(text):

    text = text.lower()

    high_priority_terms = [
        "urgent",
        "critical",
        "security breach",
        "data breach",
        "outage",
        "cannot",
        "unable",
        "failed",
        "not working",
        "blocked",
        "error"
    ]

    low_priority_terms = [
        "information",
        "inquiry",
        "documentation",
        "guidance",
        "question"
    ]

    if any(
        term in text
        for term in high_priority_terms
    ):
        return "High"

    if any(
        term in text
        for term in low_priority_terms
    ):
        return "Low"

    return "Medium"


# ==================================================
# Lightweight sentiment recommendation
# ==================================================

POSITIVE_WORDS = {
    "good",
    "great",
    "excellent",
    "happy",
    "thanks",
    "thank",
    "resolved",
    "working",
    "satisfied"
}


NEGATIVE_WORDS = {
    "failed",
    "failure",
    "problem",
    "issue",
    "error",
    "unable",
    "cannot",
    "wrong",
    "slow",
    "outage",
    "broken",
    "malfunction",
    "disruption",
    "breach"
}


def analyze_sentiment(text):

    words = text.lower().split()

    positive_score = sum(
        1
        for word in words
        if word in POSITIVE_WORDS
    )

    negative_score = sum(
        1
        for word in words
        if word in NEGATIVE_WORDS
    )

    if negative_score > positive_score:
        return "Negative"

    if positive_score > negative_score:
        return "Positive"

    return "Neutral"


# ==================================================
# Ticket prediction pipeline
# ==================================================

def predict_ticket(text):

    print("Starting SupportIQ prediction")


    # ----------------------------------------------
    # 1. Clean input text
    # ----------------------------------------------

    cleaned = clean_text(text)


    # ----------------------------------------------
    # 2. TF-IDF feature transformation
    # ----------------------------------------------

    vector = models["vectorizer"].transform(
        [cleaned]
    )


    # ----------------------------------------------
    # 3. Load deployed XGBoost model
    # ----------------------------------------------

    xgb_model = get_xgb_model()


    # ----------------------------------------------
    # 4. Predict support queue
    # ----------------------------------------------

    prediction = xgb_model.predict(
        vector
    )

    probabilities = xgb_model.predict_proba(
        vector
    )


    # ----------------------------------------------
    # 5. Decode queue
    # ----------------------------------------------

    support_queue = (
        models["encoder"]
        .inverse_transform(
            prediction
        )[0]
    )


    # ----------------------------------------------
    # 6. Confidence
    # ----------------------------------------------

    confidence = round(
        float(
            probabilities.max()
        ),
        3
    )


    # ----------------------------------------------
    # 7. Additional decision-support outputs
    # ----------------------------------------------

    priority = determine_priority(
        cleaned
    )

    sentiment = analyze_sentiment(
        cleaned
    )

    keywords = extract_keywords(
        cleaned
    )


    print(
        "SupportIQ prediction completed"
    )


    # ----------------------------------------------
    # 8. API response
    # ----------------------------------------------

    return {

        "category":
            support_queue,

        "confidence":
            confidence,

        "priority":
            priority,

        "department":
            support_queue,

        "sentiment":
            sentiment,

        "model_used":
            "TF-IDF + XGBoost",

        "keywords":
            keywords,

        "cleaned_text":
            cleaned

    }