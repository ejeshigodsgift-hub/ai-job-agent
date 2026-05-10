active_users = {}


def connect_user(user_id):
    active_users[user_id] = True


def disconnect_user(user_id):
    active_users[user_id] = False