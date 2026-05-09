import re


def extract_profile(text):
    profile = {
        "full_name": None,
        "country": None,
        "skills": [],
        "experience": None,
        "education": None,
        "salary": None
    }

    email_match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+", text)

    if email_match:
        profile["email"] = email_match.group(0)

    return profile