online_users = {}


def user_online(user_id):
    online_users[user_id] = True


def user_offline(user_id):
    online_users[user_id] = False