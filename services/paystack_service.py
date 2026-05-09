import requests
from config import Config


def initialize_transaction(email, amount):
    url = "https://api.paystack.co/transaction/initialize"

    headers = {
        "Authorization": f"Bearer {Config.PAYSTACK_SECRET_KEY}"
    }

    data = {
        "email": email,
        "amount": amount * 100
    }

    response = requests.post(url, json=data, headers=headers)

    return response.json()