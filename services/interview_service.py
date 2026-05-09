from openai import OpenAI
from config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)


def generate_interview_questions(job_title):
    prompt = f"Generate interview questions for {job_title}"

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