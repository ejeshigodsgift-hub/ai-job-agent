from flask import Blueprint, jsonify
from admin.admin_service import get_all_users, get_user_details
from admin.analytics_service import get_platform_stats

admin_bp = Blueprint("admin", __name__)


# =========================
# ALL USERS
# =========================
@admin_bp.route("/admin/users", methods=["GET"])
def users():
    return jsonify(get_all_users())


# =========================
# USER DETAILS
# =========================
@admin_bp.route("/admin/user/<user_id>", methods=["GET"])
def user_details(user_id):
    return jsonify(get_user_details(user_id))


# =========================
# PLATFORM ANALYTICS
# =========================
@admin_bp.route("/admin/stats", methods=["GET"])
def stats():
    return jsonify(get_platform_stats())