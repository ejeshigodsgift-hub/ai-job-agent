from database.db import SessionLocal
from database.models import JobOutcome


def record_outcome(user_id, job, outcome):
    db = SessionLocal()

    score_map = {
        "rejected": -2,
        "applied": 1,
        "interview": 5,
        "hired": 10
    }

    record = JobOutcome(
        user_id=user_id,
        job_title=job["title"],
        company=job["company"],
        outcome=outcome,
        score=score_map.get(outcome, 0)
    )

    db.add(record)
    db.commit()
    db.close()