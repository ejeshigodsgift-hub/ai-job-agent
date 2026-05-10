from flask import Blueprint
from flask import request
from services.conversation_service import conversation

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/chat", methods=["POST"])
def ai_chat():
    data = request.json

    reply = conversation(
        data["user_id"],
        data["message"]
    )

    return {
        "reply": reply
    }