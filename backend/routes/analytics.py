from fastapi import APIRouter

from backend.services.history_service import get_history


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


# ==================================================
# Verified experiment results
# ==================================================

MODEL_RESULTS = [

    {
        "name": "Logistic Regression",
        "task": "Ticket Type Classification",
        "accuracy": 83.69
    },

    {
        "name": "BiLSTM",
        "task": "Ticket Type Classification",
        "accuracy": 85.53
    },

    {
        "name": "TF-IDF + XGBoost",
        "task": "Support Queue Routing",
        "accuracy": 53.06
    },

    {
        "name": "DistilBERT",
        "task": "Support Queue Routing",
        "accuracy": 36.83
    }

]


DEPLOYED_MODEL_ACCURACY = 53.06


# ==================================================
# Main analytics endpoint
# ==================================================

@router.get("/")
def get_analytics():

    history = get_history()

    total_tickets = len(history)


    # ------------------------------------------------
    # Empty dashboard state
    # ------------------------------------------------

    if total_tickets == 0:

        return {

            "total_tickets": 0,

            "critical_tickets": 0,

            "accuracy":
                DEPLOYED_MODEL_ACCURACY,

            "average_confidence": 0,

            "top_category": None,

            "volume": [],

            "categories": [],

            "sentiment": [],

            "alerts": [],

            "models":
                MODEL_RESULTS

        }


    # ------------------------------------------------
    # High-priority tickets
    # ------------------------------------------------

    high_priority = [

        item
        for item in history

        if item.get(
            "priority"
        ) == "High"

    ]


    # ------------------------------------------------
    # Support queue analytics
    # ------------------------------------------------

    category_counter = {}


    for item in history:

        category = item.get(
            "category",
            "Unknown"
        )

        category_counter[
            category
        ] = (

            category_counter.get(
                category,
                0
            )

            + 1

        )


    categories = [

        {
            "name": key,
            "value": value
        }

        for key, value
        in category_counter.items()

    ]


    top_category = max(
        category_counter,
        key=category_counter.get
    )


    # ------------------------------------------------
    # Sentiment analytics
    # ------------------------------------------------

    sentiment_counter = {}


    for item in history:

        sentiment_value = item.get(
            "sentiment",
            "Unknown"
        )

        sentiment_counter[
            sentiment_value
        ] = (

            sentiment_counter.get(
                sentiment_value,
                0
            )

            + 1

        )


    sentiment = [

        {
            "name": key,
            "value": value
        }

        for key, value
        in sentiment_counter.items()

    ]


    # ------------------------------------------------
    # Average prediction confidence
    # ------------------------------------------------

    confidence_total = sum(

        float(
            item.get(
                "confidence",
                0
            )
            or 0
        )

        for item in history

    )


    average_confidence = round(

        confidence_total
        / total_tickets,

        3

    )


    # ------------------------------------------------
    # Final analytics response
    # ------------------------------------------------

    return {

        "total_tickets":
            total_tickets,

        "critical_tickets":
            len(high_priority),

        "accuracy":
            DEPLOYED_MODEL_ACCURACY,

        "average_confidence":
            average_confidence,

        "top_category":
            top_category,

        "volume": [

            {

                "date":
                    "Current Session",

                "tickets":
                    total_tickets

            }

        ],

        "categories":
            categories,

        "sentiment":
            sentiment,

        "alerts":
            history[-5:],

        "models":
            MODEL_RESULTS

    }


# ==================================================
# Prediction history endpoint
# ==================================================

@router.get("/history")
def prediction_history():

    return get_history()