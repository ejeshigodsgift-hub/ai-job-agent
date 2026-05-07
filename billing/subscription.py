def get_plan_limits(plan):
    return {
        "free": {"jobs": 3, "autopilot": False},
        "pro": {"jobs": 10, "autopilot": False},
        "premium": {"jobs": 50, "autopilot": True}
    }.get(plan, {"jobs": 3, "autopilot": False})