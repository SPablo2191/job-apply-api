from fastapi import APIRouter
from .constants import ENDPOINT, TAGS

router = APIRouter(prefix=ENDPOINT, tags=TAGS)


@router.post("/login")
def login():
    return "hola"
