from flask import Flask, request, jsonify
from services.job_service import get_jobs_for_user
from billing.stripe_webhook import handle_webhook
from auth.middleware import get_user_from_request
from auth.auth_service import signup, login
from autopilot.autopilot_engine import run_autopilot
from subscription_system.access_control import check_limit
from subscription_system.billing_service import start_subscription
from queue.task_queue import add_task
from services.generation_service import generate_documents
from services.profile_service import update_profile, get_profile
from services.chat_service import chat_handler
from admin.admin_routes import admin_bp


app = Flask(__name__)

app.register_blueprint(admin_bp)

# =========================
# HEALTH CHECK
# =========================
@app.route("/")
def home():
    return {"status": "AI Job Agent running"}

# =========================
# CHAT ENDPOINT
# =========================
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_id = data.get("user_id")
    message = data.get("message")

    reply = chat_handler(user_id, message)
    return jsonify({"reply": reply})

# =========================
# PROFILE UPDATE (NAME, EMAIL, PHONE INCLUDED)
# =========================
@app.route("/profile/update", methods=["POST"])
def profile_update():
    data = request.json

    user_id = data.get("user_id")

    profile_data = {
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "skills": data.get("skills", []),
        "experience": data.get("experience", ""),
        "location": data.get("location", ""),
        "job_type": data.get("job_type", "")
    }

    update_profile(user_id, profile_data)

    return jsonify({"status": "profile updated"})

# =========================
# GET PROFILE
# =========================
@app.route("/profile/<user_id>", methods=["GET"])
def profile(user_id):
    return jsonify(get_profile(user_id))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


@app.route("/jobs/search/<user_id>", methods=["GET"])
def job_search(user_id):
    jobs = get_jobs_for_user(user_id)
    return jsonify({"jobs": jobs})


@app.route("/generate/<user_id>", methods=["GET"])
def generate(user_id):
    job_index = int(request.args.get("job", 0))

    result = generate_documents(user_id, job_index)

    return jsonify(result)


@app.route("/jobs/request/<user_id>", methods=["POST"])
def request_jobs(user_id):
    task_id = add_task("job_search", user_id, {})

    return jsonify({
        "message": "Job search started",
        "task_id": task_id
    })

@app.route("/generate/request/<user_id>", methods=["POST"])
def request_generate(user_id):
    data = request.json
    job_index = data.get("job_index", 0)

    task_id = add_task("generate_docs", user_id, {
        "job_index": job_index
    })

    return jsonify({
        "message": "Document generation started",
        "task_id": task_id
    })


@app.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.json

    user_id = data.get("user_id")
    plan = data.get("plan")

    result = start_subscription(user_id, plan)

    return jsonify(result)


@app.route("/jobs/request/<user_id>", methods=["POST"])
def request_jobs(user_id):
    limit = check_limit(user_id, "jobs_per_day")

    if limit == 0:
        return jsonify({"error": "Upgrade plan required"})

    task_id = add_task("job_search", user_id, {})

    return jsonify({"task_id": task_id})

@app.route("/generate/request/<user_id>", methods=["POST"])
def request_generate(user_id):
    limit = check_limit(user_id, "cv_generations")

    if limit == 0:
        return jsonify({"error": "Upgrade plan required"})

    job_index = request.json.get("job_index", 0)

    task_id = add_task("generate_docs", user_id, {
        "job_index": job_index
    })

    return jsonify({"task_id": task_id})

@app.route("/generate/request/<user_id>", methods=["POST"])
def request_generate(user_id):
    limit = check_limit(user_id, "cv_generations")

    if limit == 0:
        return jsonify({"error": "Upgrade plan required"})

    job_index = request.json.get("job_index", 0)

    task_id = add_task("generate_docs", user_id, {
        "job_index": job_index
    })

    return jsonify({"task_id": task_id})


@app.route("/auth/signup", methods=["POST"])
def signup_route():
    data = request.json

    result = signup(
        data.get("email"),
        data.get("password")
    )

    return jsonify(result)

@app.route("/auth/login", methods=["POST"])
def login_route():
    data = request.json

    result = login(
        data.get("email"),
        data.get("password")
    )

    return jsonify(result)


@app.route("/jobs/request", methods=["POST"])
def request_jobs():
    user_id = get_user_from_request(request)

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    task_id = add_task("job_search", user_id, {})

    return jsonify({"task_id": task_id})


@app.route("/profile", methods=["GET"])
def profile():
    user_id = get_user_from_request(request)

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify(get_profile(user_id))


@app.route("/stripe/webhook", methods=["POST"])
def stripe_webhook():
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")

    result, status = handle_webhook(payload, sig_header)

    return jsonify(result), status


@app.route("/autopilot/run/<user_id>", methods=["POST"])
def trigger_autopilot(user_id):
    results = run_autopilot(user_id)

    return jsonify({
        "message": "Autopilot executed",
        "results_count": len(results)
    })



