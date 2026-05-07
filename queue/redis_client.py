import os
import redis

redis_url = os.getenv("REDIS_URL")

r = redis.from_url(redis_url, decode_responses=True)