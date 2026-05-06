from storage import load, save
from ai import update_profile

def handle(uid, text):
    data = load(uid)

    # ===== FIRST TIME USER =====
    if not data.get("started"):
        data["started"] = True
        save(uid, data)

        return (
            "👋 Welcome!\n\n"
            "I’m your AI Job Agent 🤖\n"
            "I help you find the best jobs automatically.\n\n"
            "Do you need help finding a job? (yes/no)"
        )

    # ===== USER RESPONSE FLOW =====
    text = text.lower()

    
    if text in ["yes", "y"]:
    return (
        "Great! 🎯\n\n"
        "To help you find the best jobs, I need your *profile*.\n\n"
        "👉 Your profile means:\n"
        "- Your skills (e.g. Python, sales, design)\n"
        "- Your experience (e.g. 2 years, beginner)\n"
        "- Your education (optional)\n\n"
        "📌 Example:\n"
        "'I am a Python developer with 2 years experience and a degree in computer science'\n\n"
        "Now tell me about yourself 👇"
    )

    if text in ["no", "n"]:
        return "👍 No problem. Let me know anytime you need help!"

    # ===== PROFILE BUILDING =====
    if "experience" in text or "developer" in text or "engineer" in text:
        data["profile"] = update_profile(text, data["profile"])
        save(uid, data)

        return (
            "✅ Profile saved!\n\n"
            "I will now start finding jobs for you automatically.\n"
            "You’ll receive up to 10 jobs per day."
        )

    # ===== COMMANDS =====
    if text == "saved":
        return "\n".join([j["title"] for j in data["saved"]]) or "No saved jobs"

    if text == "auto_apply on":
        data["profile"]["auto_apply"] = True
        save(uid, data)
        return "🤖 Auto apply enabled"

    if text == "auto_apply off":
        data["profile"]["auto_apply"] = False
        save(uid, data)
        return "❌ Auto apply disabled"

    # ===== DEFAULT RESPONSE =====
    return (
        "🤖 I didn’t understand that.\n\n"
        "You can say:\n"
        "- yes (to start job search)\n"
        "- saved (to see saved jobs)"
    )