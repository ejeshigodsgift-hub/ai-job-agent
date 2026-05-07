from integrations.adzuna_client import search_jobs
from services.ranking_service import rank_jobs
from services.profile_service import get_profile
import json
import os
from database.db import SessionLocal
from database.models import Job
from integrations.adzuna_client import search_jobs
from services.ranking_service import rank_jobs
from services.profile_service import get_profile
from monitoring.logger import log_event

CACHE_FILE = "jobs_cache.json"


def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}
    with open(CACHE_FILE, "r") as f:
        return json.load(f)


def save_cache(data):
    with open(CACHE_FILE, "w") as f:
        json.dump(data, f, indent=2)


def get_jobs_for_user(user_id):
    profile = get_profile(user_id)

    if not profile:
        return []

    skills = profile.get("skills", [])
    query = " ".join(skills) if skills else "general"

    jobs = search_jobs(query, profile.get("location", "remote"))

    ranked = rank_jobs(jobs, profile)

    # Save to cache
    cache = load_cache()
    cache[user_id] = ranked
    save_cache(cache)

    return ranked



def get_jobs_for_user(user_id):
    db = SessionLocal()

    profile = get_profile(user_id)

    jobs = search_jobs(
        " ".join(profile.get("skills", [])),
        profile.get("job_type", "remote")
    )

    ranked = rank_jobs(jobs, profile)

    # Save to DB
    for job in ranked:
        db_job = Job(
            user_id=user_id,
            title=job["title"],
            company=job["company"],
            location=job["location"],
            url=job["url"]
        )
        db.add(db_job)

    db.commit()

    db.close()

    return ranked

log_event("JOB_SEARCH_STARTED", {"user_id": user_id})