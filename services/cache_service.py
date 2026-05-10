import redis

cache = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)


def set_cache(key, value):
    cache.set(key, value)


def get_cache(key):
    return cache.get(key)