from datetime import datetime

def track_event(user_id, event_name):
    print({
        "user": user_id,
        "event": event_name,
        "time": str(datetime.utcnow())
    })