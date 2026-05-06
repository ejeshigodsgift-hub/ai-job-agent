import os, json, datetime

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def path(uid):
    return f"{DATA_DIR}/{uid}.json"

def load(uid):
    if not os.path.exists(path(uid)):
        return {
            "profile": {},
            "saved": [],
            "applied": [],
            "sent_ids": [],
            "history": [],   # ✅ ADDED (AI memory)
            "last_reset": str(datetime.date.today()),
            "daily_count": 0,
            "notified_limit": False
        }
    return json.load(open(path(uid)))

def save(uid, data):
    json.dump(data, open(path(uid), "w"), indent=2)

def reset_daily(data):
    today = str(datetime.date.today())
    if data["last_reset"] != today:
        data["daily_count"] = 0
        data["last_reset"] = today
        data["notified_limit"] = False