from src.job_application.exceptions import JobApplicationException
from src.job_application.models import JobApplicationModel
from src.job_application.service import JobApplicationService


class JobApplicationDependency:
    def __init__(self) -> None:
        self.service = JobApplicationService()
    
    async def valid_job_application(self, data : JobApplicationModel):
        job_application = await self.service.create_job_application(data)
        if not job_application:
            raise JobApplicationException("Unable to create job application.")
        return job_application
    
    async def valid_job_applications(self):
        job_applications = await self.service.list_job_applications()
        if not job_applications:
            raise JobApplicationException("Unable to get job applications.")
        return job_applications