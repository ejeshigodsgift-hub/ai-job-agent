from flask import Blueprint
from services.dashboard_service import dashboard_summary


dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/dashboard/<user_id>")
def dashboard(user_id):
    return dashboard_summary(user_id)