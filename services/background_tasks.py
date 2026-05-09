from apscheduler.schedulers.background import BackgroundScheduler
from services.notification_service import send_email

scheduler = BackgroundScheduler()


def reminder_task():
    print("sending reminders")


scheduler.add_job(reminder_task, "interval", hours=8)

scheduler.start()