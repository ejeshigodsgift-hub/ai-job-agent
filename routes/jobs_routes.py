#from flask import Blueprint
from flask import Blueprint, request
from services.job_api_service import search_jobs


jobs_bp = Blueprint("jobs", __name__)

@jobs_bp.route("/jobs/search")
def search_jobs():
    return {"message": "job search running"}


jobs_bp = Blueprint("jobs", __name__)


@jobs_bp.route("/jobs/search", methods=["POST"])
def search_jobs_route():
    data = request.json

    jobs = search_jobs(data["skill"])

    return jobs