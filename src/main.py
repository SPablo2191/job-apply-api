from fastapi import FastAPI
from .database import lifespan
from .config import VERSION
from .auth.router import router as auth_router


app = FastAPI(lifespan=lifespan)
app.title = "Job Application API"
app.version = VERSION

# routes
app.include_router(
    router=auth_router,
    prefix= f"/api/{VERSION}"
    )

