import requests

ADZUNA_APP_ID = "YOUR_ADZUNA_ID"
ADZUNA_APP_KEY = "YOUR_ADZUNA_KEY"


def search_jobs(skill, country="gb"):
    url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/1"

    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "results_per_page": 20,
        "what": skill,
        "content-type": "application/json"
    }

    response = requests.get(url, params=params)

    return response.json()