from database.db import SessionLocal

memory_cache = {}


def save_user_context(user_id, context):
    memory_cache[user_id] = context


def get_user_context(user_id):
    return memory_cache.get(user_id)