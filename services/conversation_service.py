from services.memory_service import save_memory
from services.memory_service import get_memory
from services.ai_service import chat


def conversation(user_id, message):
    save_memory(user_id, "user", message)

    history = get_memory(user_id)

    response = chat(message)

    save_memory(user_id, "assistant", response)

    return response