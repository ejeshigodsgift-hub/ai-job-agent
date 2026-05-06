import json
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# ===== PROFILE UPDATE =====
def update_profile(text, profile):
    prompt = f"Extract name, email, skills, experience, education from: {text} Return JSON"
    try:
        res = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role":"user","content":prompt}]
        )
        data = json.loads(res.choices[0].message.content)

        for k, v in data.items():
            if v:
                profile[k] = v
    except:
        pass

    return profile


# ===== JOB SCORING =====
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


# ===== JOB ENRICHMENT =====
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
            "location": data.get("location", "Unknown"),
            "salary": data.get("salary", "Not listed"),
            "schedule": data.get("schedule", "Unknown"),
            "relocation": data.get("relocation", "Unknown"),
            "lmia": data.get("lmia", "Unknown")
        })
    except:
        pass

    return job


# ===== AI CHAT WITH MEMORY + RECOMMENDATIONS =====
def chat_with_memory(history, user_message, profile):
    system_prompt = {
        "role": "system",
        "content": f"""
You are an AI Job Agent.

You help users:
- Find jobs
- Improve their chances
- Suggest better roles
- Recommend skills to learn

User profile:
{profile}

Always:
- Give helpful suggestions
- Recommend better job options
- Suggest improvements if profile is weak
- Be clear and practical
"""
    }

    messages = [system_prompt] + history + [
        {"role": "user", "content": user_message}
    ]

    try:
        res = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages
        )

        reply = res.choices[0].message.content

        # save memory
        history.append({"role": "user", "content": user_message})
        history.append({"role": "assistant", "content": reply})

        # keep last 20 messages only
        history[:] = history[-20:]

        return reply, history

    except:
        return "⚠️ AI error. Try again.", history