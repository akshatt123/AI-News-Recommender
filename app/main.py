##Entery point for FastAPI
from fastapi import FastAPI
from app.routes import router

app = FastAPI(title=" Personalized News Recommender")

app.include_router(router)
