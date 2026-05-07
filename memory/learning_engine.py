from memory.memory_service import get_memory, save_memory


def update_preferences(user_id, job):
    prefs = get_memory(user_id, "preferred_roles") or {}

    title = job.get("title", "").lower()

    prefs[title] = prefs.get(title, 0) + 1

    save_memory(user_id, "preferred_roles", prefs)