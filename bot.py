from storage import load, save
from ai import update_profile

def handle(uid, text):
    data = load(uid)

    if text.startswith("profile"):
        data["profile"] = update_profile(text, data["profile"])
        save(uid, data)
        return "✅ Profile updated"

    if text == "auto_apply on":
        data["profile"]["auto_apply"] = True
        save(uid, data)
        return "🤖 Auto apply enabled"

    if text == "auto_apply off":
        data["profile"]["auto_apply"] = False
        save(uid, data)
        return "❌ Auto apply disabled"

    if text == "saved":
        return "\n".join([j["title"] for j in data["saved"]]) or "No saved jobs"

    return "Commands: profile, saved, auto_apply on/off"