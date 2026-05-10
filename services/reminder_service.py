import schedule
import time


def send_daily_reminders():
    print("sending reminders")


schedule.every().day.at("08:00").do(send_daily_reminders)
schedule.every().day.at("13:00").do(send_daily_reminders)
schedule.every().day.at("18:00").do(send_daily_reminders)