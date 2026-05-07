from memory.memory_service import get_memory


def should_apply(user_profile, job, user_id):
    prefs = get_memory(user_id, "preferred_roles") or {}

    score = 0

    text = job["title"].lower()

    for role in prefs:
        if role in text:
            score += 5

    if score >= 7:
        return True

    return False