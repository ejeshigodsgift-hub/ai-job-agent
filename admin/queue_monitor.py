from queue.redis_client import r


def get_queue_status():
    return {
        "pending_tasks": r.llen("task_queue")
    }