
from memory.memory_service import get_memory
from learning.learning_engine import get_user_job_weights


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


def score_job(user_profile, job, user_id):
    score = 0

    skills = user_profile.get("skills", [])

    text = (job.get("title", "") + job.get("description", "")).lower()

    # base skill matching
    for skill in skills:
        if skill.lower() in text:
            score += 5

    # =========================
    # MEMORY BOOST (NEW)
    # =========================
    prefs = get_memory(user_id, "preferred_roles") or {}

    for role, weight in prefs.items():
        if role in text:
            score += weight  # learned preference boost

    return score




def score_job(user_profile, job, user_id):
    score = 0

    text = job["title"].lower()

    # =========================
    # SKILL MATCHING
    # =========================
    for skill in user_profile.get("skills", []):
        if skill.lower() in text:
            score += 5

    # =========================
    # LEARNING BOOST (NEW)
    # =========================
    weights = get_user_job_weights(user_id)

    for past_job, weight in weights.items():
        if past_job in text:
            score += weight

    return score