from integrations.openai_client import generate


def create_email(profile, job):
    prompt = f"""
Write a job application email.

USER:
Name: {profile.get('name')}
Email: {profile.get('email')}

JOB:
Title: {job.get('title')}
Company: {job.get('company')}

Include:
- Subject line
- Short professional message
- Polite tone
"""

    return generate(prompt)