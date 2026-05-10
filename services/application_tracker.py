applications = {}


def track_application(user_id, job_title):
    if user_id not in applications:
        applications[user_id] = []

    applications[user_id].append(job_title)