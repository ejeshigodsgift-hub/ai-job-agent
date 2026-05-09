memory_store = {}


def save_memory(user_id, role, content):
    if user_id not in memory_store:
        memory_store[user_id] = []

    memory_store[user_id].append({
        "role": role,
        "content": content
    })


def get_memory(user_id):
    return memory_store.get(user_id, [])