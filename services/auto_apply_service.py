import requests


def auto_apply(job_url, cv_path, cover_letter):
    return {
        "status": "application prepared",
        "job_url": job_url,
        "cv": cv_path
    }