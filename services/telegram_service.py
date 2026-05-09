import requests
from config import Config

TOKEN = Config.TELEGRAM_BOT_TOKEN


def send_telegram_message(chat_id, message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, json={
        "chat_id": chat_id,
        "text": message
    })