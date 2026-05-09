from services.job_api_service import search_jobs
from services.recommendation_service import recommend_jobs
from services.notification_service import send_email


def automate_job_flow(user):
    jobs = search_jobs(user.skills)

    recommendations = recommend_jobs(user, jobs.get("results", []))

    if recommendations:
        send_email(
            user.email,
            "New jobs matched for you"
        )

    return recommendations