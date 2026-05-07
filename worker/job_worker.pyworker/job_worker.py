from services.job_service import get_jobs_for_user


def process_job_search(task):
    user_id = task["user_id"]

    jobs = get_jobs_for_user(user_id)

    print(f"Jobs generated for {user_id}: {len(jobs)}")

    # You can later store in DB or cache
    return jobs