from integrations.stripe_client import create_checkout_session


def start_subscription(user_id, plan):
    if plan not in ["pro", "premium"]:
        return {"error": "Invalid plan"}

    url = create_checkout_session(user_id, plan)

    return {"checkout_url": url}