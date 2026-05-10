from datetime import datetime
from datetime import timedelta


def start_trial():
    return datetime.now() + timedelta(days=7)


def subscription_expiry(days):
    return datetime.now() + timedelta(days=days)