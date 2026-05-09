from flask import Blueprint

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup")
def signup():
    return {"message": "signup route"}

@auth_bp.route("/signin")
def signin():
    return {"message": "signin route"}