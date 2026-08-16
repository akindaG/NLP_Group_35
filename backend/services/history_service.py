"""
SupportIQ Prediction History Service

Handles:
- Saving prediction results
- Loading previous predictions
- Managing prediction history storage
"""

import json
from pathlib import Path
from datetime import datetime


# Prediction storage location
BASE_DIR = Path(__file__).resolve().parent.parent

HISTORY_FILE = BASE_DIR / "data" / "predictions.json"



def ensure_storage():
    """
    Create data folder and JSON file if they do not exist.
    """

    HISTORY_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    if not HISTORY_FILE.exists():
        with open(HISTORY_FILE, "w") as file:
            json.dump([], file, indent=4)




def get_history():
    """
    Retrieve all previous predictions.

    Returns:
        list: prediction records
    """

    ensure_storage()

    try:

        with open(
            HISTORY_FILE,
            "r"
        ) as file:

            data = json.load(file)

            return data


    except (
        json.JSONDecodeError,
        FileNotFoundError
    ):

        return []





def save_prediction(prediction):
    """
    Save a new prediction result.

    Args:
        prediction(dict):
            Prediction response from model

    Returns:
        dict:
            Saved prediction
    """

    ensure_storage()


    history = get_history()


    prediction_record = {

        "id": len(history) + 1,

        "timestamp":
            datetime.now()
            .strftime(
                "%Y-%m-%d %H:%M:%S"
            ),


        **prediction

    }


    history.append(
        prediction_record
    )


    with open(
        HISTORY_FILE,
        "w"
    ) as file:

        json.dump(
            history,
            file,
            indent=4
        )


    return prediction_record





def clear_history():
    """
    Delete all stored prediction history.
    """

    ensure_storage()


    with open(
        HISTORY_FILE,
        "w"
    ) as file:

        json.dump(
            [],
            file,
            indent=4
        )


    return {
        "message": "Prediction history cleared"
    }