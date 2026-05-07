from queue.redis_client import r


def acquire_lock(task_id):
    return r.set(f"lock:{task_id}", "1", nx=True, ex=300)


def release_lock(task_id):
    r.delete(f"lock:{task_id}")