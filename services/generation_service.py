from services.profile_service import get_profile
from services.job_service import get_jobs_for_user
from ai_engine.cv_generator import create_cv
from ai_engine.cover_letter_generator import create_cover_letter
from ai_engine.email_generator import create_email


def generate_documents(user_id, job_index=0):
    profile = get_profile(user_id)
    jobs = get_jobs_for_user(user_id)

    if not jobs:
        return {"error": "No jobs found"}

    job = jobs[job_index]

    cv = create_cv(profile, job)
    cover_letter = create_cover_letter(profile, job)
    email = create_email(profile, job)

    return {
        "job": job,
        "cv": cv,
        "cover_letter": cover_letter,
        "email": email
    }