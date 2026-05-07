import os
import requests

ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID")
ADZUNA_API_KEY = os.getenv("ADZUNA_API_KEY")

BASE_URL = "https://api.adzuna.com/v1/api/jobs"


def search_jobs(query, location="remote"):
    url = f"{BASE_URL}/gb/search/1"

    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_API_KEY,
        "what": query,
        "where": location,
        "results_per_page": 20,
        "content-type": "application/json"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return []

    data = response.json()

    jobs = []

    for job in data.get("results", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name"),
            "description": job.get("description"),
            "url": job.get("redirect_url"),
            "salary": job.get("salary_min")
        })

    return jobs