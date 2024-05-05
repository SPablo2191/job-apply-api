from odmantic import Model,Field
from typing import List
from datetime import datetime
from enum import Enum

class StatusEnum(str,Enum):
    REQUESTED = 'REQUESTED'
    CONTACTED = 'CONTACTED'
    PROCESS_REFUSED = 'REFUSED DURING PROCESS'
    REVISION = 'IN REVISION'
    NEGOTION = 'IN NEGOTION'
    ACCEPTED = 'ACCEPTED'
    FINAL_REFUSED = 'REFUSED AFTER PROCESS'

class JobApplicationModel(Model):
    business : str = Field(min_length=1, max_length=128)
    role : str = Field(min_length=1, max_length=128)
    postulation_post_url : str
    technology : str
    status : StatusEnum = StatusEnum.REQUESTED
    register_date : datetime = datetime.now()

class JobApplicationCollection(Model):
    job_applications : List[JobApplicationModel] 