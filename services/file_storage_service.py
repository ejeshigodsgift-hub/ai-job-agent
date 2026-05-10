import os


def create_user_folder(user_id):
    path = f"storage/users/{user_id}"

    os.makedirs(path, exist_ok=True)

    return path