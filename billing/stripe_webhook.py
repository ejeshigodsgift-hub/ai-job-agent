import os
import stripe
from services.profile_service import update_profile

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")


def handle_webhook(payload, sig_header):
    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            WEBHOOK_SECRET
        )

    except Exception as e:
        return {"error": "Invalid webhook"}, 400

    event_type = event["type"]

    # =========================
    # PAYMENT SUCCESS
    # =========================
    if event_type == "checkout.session.completed":
        session = event["data"]["object"]

        user_id = session["metadata"]["user_id"]
        plan = session["metadata"]["plan"]

        upgrade_user_plan(user_id, plan)

    # =========================
    # SUBSCRIPTION CANCELLED
    # =========================
    if event_type == "customer.subscription.deleted":
        subscription = event["data"]["object"]

        user_id = subscription["metadata"]["user_id"]

        downgrade_user_plan(user_id)

    return {"status": "success"}, 200