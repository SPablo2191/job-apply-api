from fastapi import APIRouter
from src.job_application.constants import ENDPOINT, TAGS
from src.job_application.dependencies import JobApplicationDependency
from src.job_application.models import JobApplicationModel

router = APIRouter(prefix=ENDPOINT, tags=TAGS)
dependency = JobApplicationDependency()

@router.get("/")
async def get_job_applications():
    job_applications = await dependency.valid_job_applications()
    return job_applications

@router.post("/")
async def create_job_application(job_application : JobApplicationModel):
    new_job_application = await dependency.valid_job_application(job_application)
    print(new_job_application)
    return new_job_application