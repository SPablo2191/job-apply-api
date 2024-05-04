from passlib.context import CryptContext
from src.auth.models import UserModel, UserCollection
from src.database import engine

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class HashingMixin:
    @staticmethod
    def bcrypt(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify(hashed_password: str, plain_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)


class AuthService(HashingMixin):

    async def create_user(self, user: UserModel):
        user_model = UserModel(
            name=user.name,
            last_name=user.last_name,
            username=user.username,
            password=self.bcrypt(user.password),
        )
        new_user = await engine.save(user_model)
        return new_user

    async def list_users(self):
        return UserCollection(users=await engine.find().to_list(None))
