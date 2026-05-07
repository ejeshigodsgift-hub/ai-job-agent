import os
import stripe

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


def create_checkout_session(user_id, plan):
    prices = {
        "pro": os.getenv("STRIPE_PRO_PRICE_ID"),
        "premium": os.getenv("STRIPE_PREMIUM_PRICE_ID")
    }

    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="subscription",
        line_items=[{
            "price": prices[plan],
            "quantity": 1
        }],
        success_url="https://yourapp.com/success",
        cancel_url="https://yourapp.com/cancel",
        metadata={
            "user_id": user_id,
            "plan": plan
        }
    )

    return session.url