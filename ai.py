import json, os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def update_profile(text, profile):
    prompt = f"Extract name, email, skills, experience, education from: {text} Return JSON"
    try:
        res = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role":"user","content":prompt}]
        )
        data = json.loads(res.choices[0].message.content)
        for k,v in data.items():
            if v:
                profile[k] = v
    except:
        pass
    return profile


def score_job(profile, job):
    prompt = f"""
Score this job 0-100 based on match.

User: {profile}
Job: {job}

Return number only.
"""
    try:
        res = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role":"user","content":prompt}]
        )
        return int(res.choices[0].message.content.strip())
    except:
        return 0


def enrich_job(job):
    prompt = f"""
Extract if available:
location, salary, schedule, relocation, lmia

Text:
{job.get("raw_text")}
Return JSON
"""
    try:
        res = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role":"user","content":prompt}]
        )
        data = json.loads(res.choices[0].message.content)

        job.update({
            "location": data.get("location","Unknown"),
            "salary": data.get("salary","Not listed"),
            "schedule": data.get("schedule","Unknown"),
            "relocation": data.get("relocation","Unknown"),
            "lmia": data.get("lmia","Unknown")
        })
    except:
        pass

    return job