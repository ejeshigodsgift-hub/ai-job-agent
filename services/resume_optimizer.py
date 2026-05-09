from openai import OpenAI
from config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)


def optimize_resume(cv_text, job_description):
    prompt = f"Optimize this CV for the following job: {job_description}"

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content