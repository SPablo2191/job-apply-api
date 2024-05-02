from pydantic import  BaseModel,  Field, constr
from datetime import datetime

class User(BaseModel):
    id : int  = Field(min_length=1, max_length=128)
    username : str = constr(regex="^[A-Za-z0-9-_]+$", to_lower=True, strip_whitespace=True)
    name : str  = Field(min_length=1, max_length=128)
    last_name : str  = Field(min_length=1, max_length=128)
    register_date : datetime = datetime.now

if __name__ == "__main__":
    data = {
    'id' : 1,
    'username' : 'pablo123',
    'name' : 'pablo',
    'last_name' : 'sandoval'
    }
    user = User(**data)
    print(user.register_date)
