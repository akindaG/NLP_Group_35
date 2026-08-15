from fastapi import FastAPI
from backend.routes.prediction import router


app = FastAPI(
    title="SupportIQ AI API",
    description="NLP based customer support ticket intelligence API",
    version="1.0"
)


app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "SupportIQ AI Backend Running"
    }