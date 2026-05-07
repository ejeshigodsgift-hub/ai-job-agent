from autonomous.decision_engine import should_apply
from autonomous.email_sender import generate_application_email
from memory.application_tracker import save_application
from services.profile_service import get_profile


def auto_apply(user_id, jobs):
    profile = get_profile(user_id)

    applied_jobs = []

    for job in jobs:

        # AI DECISION
        if should_apply(profile, job, user_id):

            # GENERATE EMAIL
            email = generate_application_email(profile, job)

            # TRACK APPLICATION
            save_application(user_id, job, "auto-applied")

            applied_jobs.append({
                "job": job,
                "email": email
            })

    return applied_jobs