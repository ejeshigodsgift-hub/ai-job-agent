PLANS = {
    "14_days": 10,
    "30_days": 20,
    "3_months": 50,
    "1_year": 120
}


def get_plan_price(plan):
    return PLANS.get(plan)