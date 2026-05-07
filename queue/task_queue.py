from queue.models import load_queue, save_queue
import uuid
from database.db import SessionLocal
from database.models import Task






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


def add_task(task_type, user_id, payload):
    db = SessionLocal()

    task = Task(
        id=str(uuid.uuid4()),
        user_id=user_id,
        type=task_type,
        status="pending",
        payload=payload
    )

    db.add(task)
    db.commit()
    db.close()

    return task.id


def get_pending_tasks():
    db = SessionLocal()

    tasks = db.query(Task).filter(Task.status == "pending").all()

    db.close()

    return tasks