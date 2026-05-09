import stripe
from config import Config

stripe.api_key = Config.STRIPE_SECRET_KEY


def create_payment(amount, currency="usd"):
    payment = stripe.PaymentIntent.create(
        amount=amount * 100,
        currency=currency
    )

    return payment.client_secret