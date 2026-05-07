from database.db import SessionLocal
from database.models import User, Job, Task


def get_platform_stats():
    db = SessionLocal()

    total_users = db.query(User).count()
    total_jobs = db.query(Job).count()
    total_tasks = db.query(Task).count()

    pro_users = db.query(User).filter(User.plan == "pro").count()
    premium_users = db.query(User).filter(User.plan == "premium").count()

    db.close()

    return {
        "total_users": total_users,
        "total_jobs": total_jobs,
        "total_tasks": total_tasks,
        "pro_users": pro_users,
        "premium_users": premium_users
    }