from fastapi import APIRouter,Depends
from src.auth.constants import ENDPOINT, TAGS
from src.auth.dependencies import AuthDependency
from src.auth.models import UserModel

router = APIRouter(prefix=ENDPOINT, tags=TAGS)
dependency = AuthDependency()

@router.post("/login")
def login():
    return "hola"

@router.post("/register")
async def register(user : UserModel):
    new_user = await dependency.valid_user(user)
    print(new_user)
    return new_user