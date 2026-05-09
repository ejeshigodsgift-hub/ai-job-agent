from datetime import datetime


def days_left(deadline):
    today = datetime.now()

    remaining = deadline - today

    return remaining.days