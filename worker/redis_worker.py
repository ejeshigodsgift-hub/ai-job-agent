import json
import time
from queue.redis_client import r
from worker.job_worker import process_job_search
from worker.cv_worker import process_cv_generation
from queue.lock import acquire_lock, release_lock

def run_worker(worker_name="worker-1"):
    print(f"{worker_name} started...")

    while True:
        task_data = r.brpop("task_queue", timeout=5)

        if task_data is None:
            continue

        _, task_json = task_data
        task = json.loads(task_json)

        try:
            print(f"{worker_name} processing {task['type']}")

            if task["type"] == "job_search":
                process_job_search(task)

            elif task["type"] == "generate_docs":
                process_cv_generation(task)

        except Exception as e:
            print("Worker error:", e)

        time.sleep(1)


if __name__ == "__main__":
    run_worker()


def safe_process(task, handler):
    task_id = task["id"]

    if not acquire_lock(task_id):
        return  # already processing somewhere else

    try:
        handler(task)
    finally:
        release_lock(task_id)
