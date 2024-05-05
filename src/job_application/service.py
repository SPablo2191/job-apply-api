from src.database import engine
from src.job_application.models import JobApplicationModel, JobApplicationCollection


class JobApplicationService:

    async def create_job_application(self, data: JobApplicationModel):
        job_application_model = JobApplicationModel(
            business=data.business,
            postulation_post_url=data.postulation_post_url,
            role=data.role,
            technology=data.technology,
            status=data.status,
        )
        new_job_application_model = await engine.save(job_application_model)
        return new_job_application_model

    async def list_job_applications(self):
        return JobApplicationCollection(job_applications=await engine.find(JobApplicationModel))
