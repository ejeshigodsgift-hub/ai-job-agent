from flask import Blueprint

jobs_bp = Blueprint("jobs", __name__)

@jobs_bp.route("/jobs/search")
def search_jobs():
    return {"message": "job search running"}