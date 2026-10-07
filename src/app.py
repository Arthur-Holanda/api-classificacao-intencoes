from fastapi import FastAPI
from modules.intent_classifier.controller import intent_classifier_router

app = FastAPI() 

app.include_router(intent_classifier_router)