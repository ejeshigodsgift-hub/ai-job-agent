from subscription_system.plans import PLANS
from services.profile_service import get_profile


def check_limit(user_id, feature):
    profile = get_profile(user_id)
    plan = profile.get("plan", "free")

    limits = PLANS.get(plan, PLANS["free"])

    return limits.get(feature, 0)

def check_access(user, feature):
    plan = user.get("plan")

    if plan == "free" and feature == "autopilot":
        return False

    return True