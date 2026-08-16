from fastapi import APIRouter
from pydantic import BaseModel


from backend.services.history_service import save_prediction
from backend.services.prediction_service import predict_ticket



router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)




class TicketRequest(BaseModel):

    text: str






@router.post("/")
def predict(request: TicketRequest):


    result = predict_ticket(
        request.text
    )



    save_prediction(
        result
    )



    return result