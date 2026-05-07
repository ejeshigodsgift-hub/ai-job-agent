def rank_jobs(jobs, user_profile):
    skills = user_profile.get("skills", [])
    job_type = user_profile.get("job_type", "")

    scored_jobs = []

    for job in jobs:
        score = 0

        text = (job.get("title", "") + job.get("description", "")).lower()

        # Skill match scoring
        for skill in skills:
            if skill.lower() in text:
                score += 5

        # Remote preference boost
        if job_type == "remote" and "remote" in text:
            score += 3

        # Basic quality boost
        if job.get("company"):
            score += 1

        scored_jobs.append((score, job))

    # Sort by score
    scored_jobs.sort(reverse=True, key=lambda x: x[0])

    # Return top 20
    return [job for score, job in scored_jobs[:20]]