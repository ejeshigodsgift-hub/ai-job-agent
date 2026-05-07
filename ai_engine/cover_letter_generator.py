from integrations.openai_client import generate


def create_cover_letter(profile, job):
    prompt = f"""
Write a professional cover letter for this job.

USER:
Name: {profile.get('name')}
Skills: {profile.get('skills')}
Experience: {profile.get('experience')}

JOB:
Title: {job.get('title')}
Company: {job.get('company')}
Description: {job.get('description')}

Make it:
- Professional
- Concise
- Persuasive
"""

    return generate(prompt)