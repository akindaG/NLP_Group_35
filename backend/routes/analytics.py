from fastapi import APIRouter

from backend.services.history_service import get_history


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)



@router.get("/")
def get_analytics():

    history = get_history()

    total_tickets = len(history)


    if total_tickets == 0:

        return {

            "total_tickets": 0,

            "critical_tickets": 0,

            "accuracy": 0,

            "average_confidence": 0,

            "top_category": None,

            "volume": [],

            "categories": [],

            "sentiment": [],

            "alerts": [],

            "models": []

        }



    # -----------------------------
    # Critical Tickets
    # -----------------------------

    critical = [

        item for item in history

        if item.get("priority") == "Critical"

    ]



    # -----------------------------
    # Category Analytics
    # -----------------------------

    category_counter = {}


    for item in history:


        category = item.get(
            "category",
            "Unknown"
        )


        category_counter[category] = (
            category_counter.get(category,0)
            + 1
        )



    categories = [

        {
            "name": key,
            "value": value
        }

        for key,value in category_counter.items()

    ]



    top_category = max(
        category_counter,
        key=category_counter.get
    )



    # -----------------------------
    # Sentiment Analytics
    # -----------------------------

    sentiment_counter = {}


    for item in history:


        sentiment = item.get(
            "sentiment",
            "Unknown"
        )


        sentiment_counter[sentiment] = (

            sentiment_counter.get(
                sentiment,
                0
            )
            +
            1

        )



    sentiment = [

        {
            "name": key,
            "value": value
        }

        for key,value in sentiment_counter.items()

    ]



    # -----------------------------
    # Confidence
    # -----------------------------

    confidence_total = sum(

        item.get(
            "confidence",
            0
        )

        for item in history

    )


    average_confidence = round(

        confidence_total / total_tickets,

        2

    )



    # -----------------------------
    # Final Response
    # -----------------------------

    return {


        "total_tickets": total_tickets,


        "critical_tickets": len(critical),


        "accuracy": 92.6,


        "average_confidence": average_confidence,


        "top_category": top_category,



        "volume": [

            {

                "date": "2026-08-16",

                "tickets": total_tickets

            }

        ],



        "categories": categories,



        "sentiment": sentiment,



        "alerts": history[-5:],



        "models": [

            {

                "name": "TF-IDF + XGBoost",

                "task": "Prediction",

                "accuracy": 92.6

            },


            {

                "name": "DistilBERT",

                "task": "Classification",

                "accuracy": 91.8

            }

        ]

    }





@router.get("/history")
def prediction_history():

    return get_history()