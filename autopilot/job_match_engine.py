def score_job(user_profile, job):
    score = 0

    skills = user_profile.get("skills", [])

    text = (job.get("title", "") + job.get("description", "")).lower()

    for skill in skills:
        if skill.lower() in text:
            score += 5

    if user_profile.get("job_type") == "remote":
        if "remote" in text:
            score += 3

    return score


def rank_jobs(user_profile, jobs):
    scored = []

    for job in jobs:
        score = score_job(user_profile, job)
        scored.append((score, job))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [job for score, job in scored]