from queue.models import load_queue, save_queue
import uuid


def add_task(task_type, user_id, payload):
    queue = load_queue()

    task = {
        "id": str(uuid.uuid4()),
        "type": task_type,
        "user_id": user_id,
        "payload": payload,
        "status": "pending"
    }

    queue.append(task)
    save_queue(queue)

    return task["id"]


def get_pending_tasks():
    queue = load_queue()
    return [t for t in queue if t["status"] == "pending"]


def update_task(task_id, status):
    queue = load_queue()

    for t in queue:
        if t["id"] == task_id:
            t["status"] = status

    save_queue(queue)