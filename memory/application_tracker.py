from database.db import SessionLocal
from database.models import Application


def save_application(user_id, job, status="applied"):
    db = SessionLocal()

    app = Application(
        user_id=user_id,
        job_title=job["title"],
        company=job["company"],
        status=status,
        data=job
    )

    db.add(app)
    db.commit()
    db.close()


def get_applications(user_id):
    db = SessionLocal()

    apps = db.query(Application).filter_by(user_id=user_id).all()

    db.close()

    return apps