from database.db import SessionLocal
from database.models import Memory


# =========================
# SAVE MEMORY
# =========================
def save_memory(user_id, key, value):
    db = SessionLocal()

    memory = db.query(Memory).filter_by(
        user_id=user_id,
        key=key
    ).first()

    if not memory:
        memory = Memory(user_id=user_id, key=key, value=value)
    else:
        memory.value = value

    db.add(memory)
    db.commit()
    db.close()


# =========================
# GET MEMORY
# =========================
def get_memory(user_id, key):
    db = SessionLocal()

    memory = db.query(Memory).filter_by(
        user_id=user_id,
        key=key
    ).first()

    db.close()

    return memory.value if memory else None