active_sessions = {}


def create_session(user_id):
    active_sessions[user_id] = {
        "authenticated": True
    }


def get_session(user_id):
    return active_sessions.get(user_id)