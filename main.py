from flask import Flask, request, jsonify
from services.profile_service import update_profile, get_profile
from services.chat_service import chat_handler

app = Flask(__name__)

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