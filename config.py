import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

    DATABASE_URL = os.getenv("DATABASE_URL")

    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")

    PAYSTACK_SECRET_KEY = os.getenv("PAYSTACK_SECRET_KEY")