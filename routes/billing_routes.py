from flask import Blueprint

billing_bp = Blueprint("billing", __name__)

@billing_bp.route("/billing/plans")
def plans():
    return {
        "plans": [
            "14_days",
            "30_days",
            "3_months",
            "1_year"
        ]
    }