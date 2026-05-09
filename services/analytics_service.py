analytics_data = {
    "users": 0,
    "applications": 0,
    "matches": 0,
    "subscriptions": 0
}


def update_metric(key):
    analytics_data[key] += 1


def get_analytics():
    return analytics_data