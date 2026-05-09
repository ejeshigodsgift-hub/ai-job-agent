from database.db import SessionLocal
from database.models import User
from utils.security import hash_password, verify_password


def create_user(data):
    db = SessionLocal()

    user = User(
        full_name=data["full_name"],
        email=data["email"],
        password=hash_password(data["password"]),
        country=data.get("country")
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def login_user(email, password):
    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user