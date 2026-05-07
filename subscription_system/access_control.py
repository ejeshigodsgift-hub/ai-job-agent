from subscription_system.plans import PLANS
from services.profile_service import get_profile


def check_limit(user_id, feature):
    profile = get_profile(user_id)
    plan = profile.get("plan", "free")

    limits = PLANS.get(plan, PLANS["free"])

    return limits.get(feature, 0)