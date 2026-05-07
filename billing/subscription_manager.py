from services.profile_service import get_profile, update_profile


def upgrade_user_plan(user_id, plan):
    profile = get_profile(user_id)

    profile["plan"] = plan

    update_profile(user_id, profile)

    print(f"User {user_id} upgraded to {plan}")


def downgrade_user_plan(user_id):
    profile = get_profile(user_id)

    profile["plan"] = "free"

    update_profile(user_id, profile)

    print(f"User {user_id} downgraded to free")