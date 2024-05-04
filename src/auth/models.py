from pydantic import BaseModel,  BeforeValidator, ConfigDict
from odmantic import Model
from typing import Annotated, Optional, List
from datetime import datetime

PyObjectId = Annotated[str, BeforeValidator(str)]


class UserModel(Model):
    name: str 
    last_name: str 
    username: str
    password: str 
    register_date: datetime = datetime.now()
    model_config = ConfigDict(
        title="User",
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "username": "pablo123",
                "name": "pablo",
                "last_name": "sandoval",
                "password": "contraseña"
            }
        },
    )


class UpdateUserModel(Model):
    username: Optional[str] = None
    password: Optional[str] = None
    name: Optional[str] = None
    last_name:Optional[str] = None 
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "id": 1,
                "username": "pablo123",
                "name": "pablo",
                "last_name": "sandoval",
            }
        },
    )

class UserCollection(BaseModel):
    users: List[UserModel]

if __name__ == "__main__":
    data = {"id": 1, "username": "pablo123", "name": "pablo", "last_name": "sandoval"}
    user = UserModel(**data)
    print(user.register_date)
