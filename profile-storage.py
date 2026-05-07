import json
import os

DB_FILE = "memory_db.json"


# Load DB
def load_db():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)


# Save DB
def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)


# Update profile
def update_profile(user_id, profile_data):
    db = load_db()

    if user_id not in db:
        db[user_id] = {}

    db[user_id]["profile"] = profile_data

    save_db(db)


# Get profile
def get_profile(user_id):
    db = load_db()
    return db.get(user_id, {}).get("profile", {})