from database.db import SessionLocal
from database.models import User, Profile, Job, Task


# =========================
# GET ALL USERS
# =========================
def get_all_users():
    db = SessionLocal()

    users = db.query(User).all()

    db.close()

    return [
        {
            "id": u.id,
            "email": u.email,
            "plan": u.plan
        }
        for u in users
    ]


# =========================
# GET USER DETAILS
# =========================
def get_user_details(user_id):
    db = SessionLocal()

    user = db.query(User).filter(User.id == user_id).first()
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()
    jobs = db.query(Job).filter(Job.user_id == user_id).all()

    db.close()

    return {
        "user": {
            "id": user.id,
            "email": user.email,
            "plan": user.plan
        } if user else None,

        "profile": {
            "name": profile.name if profile else None,
            "phone": profile.phone if profile else None,
            "skills": profile.skills if profile else None
        } if profile else None,

        "jobs_count": len(jobs)
    }