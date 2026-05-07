def generate_application_email(user_profile, job):
    return f"""
Subject: Application for {job['title']}

Dear Hiring Team,

I am applying for the {job['title']} role at {job['company']}.

My skills include: {', '.join(user_profile.get('skills', []))}

I look forward to contributing to your team.

Best regards,
{user_profile.get('name')}
"""