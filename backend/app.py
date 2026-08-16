from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from backend.routes.prediction import router
from backend.routes.analytics import router as analytics_router



app = FastAPI(

title="SupportIQ AI API",

description="NLP based customer support ticket intelligence API",

version="1.0"

)



app.add_middleware(

CORSMiddleware,

allow_origins=[

"http://localhost:5173",

"http://127.0.0.1:5173"

],

allow_credentials=True,

allow_methods=["*"],

allow_headers=["*"]

)



app.include_router(router)

app.include_router(
    analytics_router
)



@app.get("/")

def home():

    return {

    "message":
    "SupportIQ AI Backend Running"

    }

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "models": "loaded",
        "service": "SupportIQ API"
    }