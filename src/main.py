from fastapi import FastAPI
from dotenv import load_dotenv
import os

from .auth.router import router as auth_router

load_dotenv()
app = FastAPI()
app.title = "Job Application API"
app.version = os.getenv('VERSION','0.0.0')
app.include_router(auth_router)

@app.get("/")
def hello_world():
    return {"hello":"IT'S ME"}