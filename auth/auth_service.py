import json
import os
from auth.password_utils import hash_password, verify_password
from database.db import SessionLocal
from database.models import User
from auth.password_utils import hash_password
from auth.jwt_handler import generate_token

DB_FILE = "users_db.json"


def load_users():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_users(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)


# SIGNUP
def signup(email, password):
    users = load_users()

    if email in users:
        return {"error": "User already exists"}

    users[email] = {
        "password": hash_password(password),
        "user_id": email
    }

    save_users(users)

    token = generate_token(email)

    return {"token": token}


# LOGIN
def login(email, password):
    users = load_users()

    if email not in users:
        return {"error": "User not found"}

    user = users[email]

    if not verify_password(password, user["password"]):
        return {"error": "Invalid password"}

    token = generate_token(email)

    return {"token": token}


def signup(email, password):
    db = SessionLocal()

    existing = db.query(User).filter(User.email == email).first()

    if existing:
        return {"error": "User exists"}

    user = User(
        id=email,
        email=email,
        password=hash_password(password),
        plan="free"
    )

    db.add(user)
    db.commit()
    db.close()

    return {"status": "created"}