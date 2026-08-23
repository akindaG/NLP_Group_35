"""Prediction API routes."""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field, field_validator

from backend.services.history_service import save_prediction
from backend.services.prediction_service import predict_ticket

router = APIRouter(prefix="/predict", tags=["Prediction"])


class TicketRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=8,
        max_length=5000,
        description="Customer support ticket text to analyze.",
        examples=["Our company VPN has been unavailable since this morning."],
    )

    @field_validator("text")
    @classmethod
    def validate_text(cls, value: str) -> str:
        normalized = value.strip()
        if len(normalized.split()) < 2:
            raise ValueError("Please provide a meaningful support ticket with at least two words.")
        return normalized


@router.post("/")
def predict(request: TicketRequest):
    try:
        result = predict_ticket(request.text)
        save_prediction(result)
        return result
    except FileNotFoundError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="Prediction failed unexpectedly. Check the backend logs for details.",
        ) from exc
