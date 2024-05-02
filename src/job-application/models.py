from pydantic import BaseModel,Field,AnyUrl
from datetime import datetime
from ..auth.models import User
from enum import Enum

class StatusEnum(str,Enum):
    REQUESTED = 'REQUESTED'
    CONTACTED = 'CONTACTED'
    PROCESS_REFUSED = 'REFUSED DURING PROCESS'
    REVISION = 'IN REVISION'
    NEGOTION = 'IN NEGOTION'
    ACCEPTED = 'ACCEPTED'
    FINAL_REFUSED = 'REFUSED AFTER PROCESS'

class JobApplication(BaseModel):
    id : int
    business : str = Field(min_length=1, max_length=128)
    user_id: int
    role : str = Field(min_length=1, max_length=128)
    postulation_post_url : AnyUrl
    technology : str
    status : StatusEnum = StatusEnum.REQUESTED
    register_date : datetime = datetime.now
