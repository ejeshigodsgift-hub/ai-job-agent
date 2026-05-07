import os
import redis
from queue.redis_client import r
import uuid
import json

redis_url = os.getenv("REDIS_URL")

r = redis.from_url(redis_url, decode_responses=True)


# =========================
# ADD TASK
# =========================
def add_task(task_type, user_id, payload):
    task_id = str(uuid.uuid4())

    task = {
        "id": task_id,
        "type": task_type,
        "user_id": user_id,
        "payload": payload
    }

    r.lpush("task_queue", json.dumps(task))

    return task_id