"""End-to-end inference service for the deployed SupportIQ queue classifier."""

from backend.services.business_rules import (
    analyze_sentiment,
    determine_priority,
    extract_keywords,
    needs_human_review,
)
from backend.services.model_loader import get_models, get_xgb_model
from backend.services.preprocessing import clean_text


def _top_predictions(probabilities, model_classes, encoder, limit: int = 3):
    """Return the highest-probability queue alternatives in descending order."""
    ranked = sorted(
        zip(model_classes, probabilities),
        key=lambda item: float(item[1]),
        reverse=True,
    )[:limit]

    class_ids = [item[0] for item in ranked]
    labels = encoder.inverse_transform(class_ids)

    return [
        {
            "label": str(label),
            "confidence": round(float(score), 4),
        }
        for label, (_, score) in zip(labels, ranked)
    ]


def predict_ticket(text: str) -> dict:
    """Analyze one support ticket and return model plus decision-support outputs."""
    cleaned = clean_text(text)
    if not cleaned.strip():
        raise ValueError("Ticket text is empty after preprocessing.")

    models = get_models()
    vector = models["vectorizer"].transform([cleaned])
    xgb_model = get_xgb_model()

    prediction = xgb_model.predict(vector)
    probability_matrix = xgb_model.predict_proba(vector)
    probabilities = probability_matrix[0]

    support_queue = models["encoder"].inverse_transform(prediction)[0]
    confidence = round(float(max(probabilities)), 4)

    model_classes = getattr(xgb_model, "classes_", range(len(probabilities)))
    top_predictions = _top_predictions(
        probabilities,
        model_classes,
        models["encoder"],
    )

    return {
        "category": str(support_queue),
        "confidence": confidence,
        "priority": determine_priority(cleaned),
        "department": str(support_queue),
        "sentiment": analyze_sentiment(cleaned),
        "model_used": "TF-IDF + XGBoost",
        "keywords": extract_keywords(cleaned),
        "cleaned_text": cleaned,
        "top_predictions": top_predictions,
        "human_review_recommended": needs_human_review(confidence),
        "output_sources": {
            "department": "machine_learning_model",
            "confidence": "machine_learning_model",
            "priority": "transparent_rule_based_recommendation",
            "sentiment": "transparent_rule_based_recommendation",
            "keywords": "transparent_rule_based_explanation",
        },
    }
