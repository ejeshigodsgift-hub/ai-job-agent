from services.job_service import get_jobs_for_user
from main import send_job_update


def process_job_search(task):
    user_id = task["user_id"]

    jobs = get_jobs_for_user(user_id)

    print(f"Jobs generated for {user_id}: {len(jobs)}")

    # You can later store in DB or cache
    return jobs



def process_job_search(task):
    user_id = task["user_id"]

    jobs = [
        {"title": "Python Dev", "company": "Tech Ltd"},
        {"title": "Construction Engineer", "company": "BuildCo"}
    ]

    for job in jobs:
        # SEND REAL-TIME UPDATE
        send_job_update(user_id, job)

    return jobs