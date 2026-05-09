from openai import OpenAI
from config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are an AI Job Agent.
Communicate naturally.
Collect user profile information.
Recommend jobs.
Guide users professionally.
"""


def chat(message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content