from database.db import SessionLocal
from database.models import Profile


def update_profile(user_id, data):
    db = SessionLocal()

    profile = db.query(Profile).filter(Profile.user_id == user_id).first()

    if not profile:
        profile = Profile(user_id=user_id)

    profile.name = data.get("name")
    profile.phone = data.get("phone")
    profile.skills = data.get("skills")
    profile.experience = data.get("experience")
    profile.job_type = data.get("job_type")

    db.add(profile)
    db.commit()
    db.close()


def get_profile(user_id):
    db = SessionLocal()

    profile = db.query(Profile).filter(Profile.user_id == user_id).first()

    db.close()

    if not profile:
        return {}

    return {
        "name": profile.name,
        "phone": profile.phone,
        "skills": profile.skills,
        "experience": profile.experience,
        "job_type": profile.job_type
    }