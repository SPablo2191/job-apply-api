from src.auth.exceptions import AuthException
from src.auth.models import UserModel
from src.auth.service import AuthService

class AuthDependency:
    def __init__(self) -> None:
        self.service = AuthService()
    
    async def valid_user(self, user_data : UserModel):
        user = await self.service.create_user(user_data)
        if not user:
            raise AuthException("Unable to create user.")
        return user
    