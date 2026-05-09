import requests


def search_global_jobs(skill):
    return {
        "status": "searching",
        "skill": skill
    }