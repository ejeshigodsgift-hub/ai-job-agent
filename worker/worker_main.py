import time
from queue.task_queue import get_pending_tasks, update_task
from worker.job_worker import process_job_search
from worker.cv_worker import process_cv_generation


def run_worker():
    print("Worker started...")

    while True:
        tasks = get_pending_tasks()

        for task in tasks:
            task_id = task["id"]
            task_type = task["type"]

            update_task(task_id, "processing")

            try:
                if task_type == "job_search":
                    process_job_search(task)

                if task_type == "generate_docs":
                    process_cv_generation(task)

                update_task(task_id, "done")

            except Exception as e:
                print("Error:", e)
                update_task(task_id, "failed")

        time.sleep(3)


if __name__ == "__main__":
    run_worker()