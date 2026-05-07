from time import time

requests = {}

def rate_limit(user_id):
    now = time()

    if user_id not in requests:
        requests[user_id] = []

    requests[user_id] = [
        t for t in requests[user_id] if now - t < 60
    ]

    if len(requests[user_id]) > 10:
        return False

    requests[user_id].append(now)
    return True