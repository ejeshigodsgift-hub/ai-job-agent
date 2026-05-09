from flask import Blueprint, request
from services.auth_service import create_user, login_user

#from flask import Blueprint

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup")
def signup():
    return {"message": "signup route"}

@auth_bp.route("/signin")
def signin():
    return {"message": "signin route"}


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json

    user = create_user(data)

    return {
        "message": "account created",
        "user_id": user.id
    }


@auth_bp.route("/signin", methods=["POST"])
def signin():
    data = request.json

    user = login_user(data["email"], data["password"])

    if not user:
        return {"error": "invalid credentials"}, 401

    return {
        "message": "signin successful",
        "user_id": user.id
    }