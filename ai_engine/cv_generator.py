from integrations.openai_client import generate


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