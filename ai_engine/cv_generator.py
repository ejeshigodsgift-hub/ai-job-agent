from integrations.openai_client import generate
from memory.memory_service import get_memory


def create_cv(profile, job):
    prompt = f"""
Create a professional CV tailored to this job.

USER PROFILE:
Name: {profile.get('name')}
Email: {profile.get('email')}
Phone: {profile.get('phone')}
Skills: {profile.get('skills')}
Experience: {profile.get('experience')}

JOB:
Title: {job.get('title')}
Company: {job.get('company')}
Description: {job.get('description')}

Format:
- Professional CV
- Clear sections
- ATS friendly
"""

    return generate(prompt)


def personalize_cv(profile, job, user_id):
    prefs = get_memory(user_id, "preferred_roles") or {}

    tone = "professional"

    if prefs:
        tone = "highly targeted"

    return f"""
CV for {profile['name']}
Tone: {tone}

Skills: {profile['skills']}
Target Job: {job['title']}
"""