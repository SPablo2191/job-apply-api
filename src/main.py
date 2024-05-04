from fastapi import FastAPI
from src.config import settings as global_settings
from src.auth.router import router as auth_router
app = FastAPI()
app.title = "Job Application API"
app.version = global_settings.version

# routes
app.include_router(
    router=auth_router,
    prefix= f"/api/{global_settings.api_version}"
    )

