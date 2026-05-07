from integrations.adzuna_client import search_jobs
from services.ranking_service import rank_jobs
from services.profile_service import get_profile
import json
import os

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