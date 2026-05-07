import time
from autopilot.autopilot_engine import run_autopilot
from database.db import SessionLocal
from database.models import User


def run_daily_autopilot():
    print("Autopilot started...")

    while True:
        db = SessionLocal()

        users = db.query(User).all()

        for user in users:
            try:
                results = run_autopilot(user.id)

                print(f"Autopilot completed for {user.id}")

                # Here you would store results in DB
                # (CVs, cover letters, etc)

            except Exception as e:
                print("Autopilot error:", e)

        db.close()

        # Run once per day (simulated as 24h loop)
        time.sleep(86400)