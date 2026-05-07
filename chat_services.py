from services.profile_service import get_profile


def chat_handler(user_id, message):
    profile = get_profile(user_id)

    name = profile.get("name", "there")

    # Basic intelligent response logic (MVP)
    if "job" in message.lower():
        return f"Hi {name}, I can help you find jobs. Let’s build your profile first."

    if "cv" in message.lower():
        return f"{name}, I can generate your CV once your profile is complete."

    if not profile:
        return (
            "Welcome! I’m your AI Job Agent.\n"
            "Let’s start by setting up your profile: name, email, phone, skills."
        )

    return f"Hi {name}, I’m ready to help you with jobs and career opportunities."