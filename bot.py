from storage import load, save
from ai import update_profile, chat_with_memory

def handle(uid, text):
    data = load(uid)

    # ensure history exists (for old users)
    data.setdefault("history", [])

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

    text_lower = text.lower()

    # ===== USER AGREES =====
    if text_lower in ["yes", "y"]:
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

    # ===== USER DECLINES =====
    if text_lower in ["no", "n"]:
        return "👍 No problem. Let me know anytime you need help!"

    # ===== PROFILE BUILDING =====
    if any(word in text_lower for word in ["experience", "developer", "engineer", "designer", "manager"]):
        data["profile"] = update_profile(text, data["profile"])
        save(uid, data)

        return (
            "✅ Profile saved!\n\n"
            "I will now start finding jobs for you automatically.\n"
            "You’ll receive up to 10 jobs per day."
        )

    # ===== COMMANDS =====
    if text_lower == "saved":
        return "\n".join([j["title"] for j in data["saved"]]) or "No saved jobs"

    if text_lower == "auto_apply on":
        data["profile"]["auto_apply"] = True
        save(uid, data)
        return "🤖 Auto apply enabled"

    if text_lower == "auto_apply off":
        data["profile"]["auto_apply"] = False
        save(uid, data)
        return "❌ Auto apply disabled"

    # ===== AI CHAT MODE (DEFAULT) =====
    reply, history = chat_with_memory(
        data.get("history", []),
        text,
        data.get("profile", {})
    )

    data["history"] = history
    save(uid, data)

    return reply