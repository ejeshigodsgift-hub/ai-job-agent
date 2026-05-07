from services.generation_service import generate_documents


def process_cv_generation(task):
    user_id = task["user_id"]
    job_index = task["payload"].get("job_index", 0)

    result = generate_documents(user_id, job_index)

    print(f"CV generated for {user_id}")

    return result