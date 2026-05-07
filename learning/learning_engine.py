from database.db import SessionLocal
from database.models import JobOutcome


def get_user_job_weights(user_id):
    db = SessionLocal()

    outcomes = db.query(JobOutcome).filter_by(user_id=user_id).all()

    db.close()

    weights = {}

    for o in outcomes:
        title = o.job_title.lower()
        weights[title] = weights.get(title, 0) + o.score

    return weights