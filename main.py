import os, time, threading
from flask import Flask
import telegram

from bot import handle
from jobs import background_search
from storage import load

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError("Missing TELEGRAM_TOKEN")

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

# ===== TELEGRAM LOOP (SYNC SAFE) =====
def run_bot():
    offset = None

    while True:
        try:
            updates = bot.get_updates(offset=offset, timeout=10)

            for u in updates:
                offset = u.update_id + 1

                if u.message:
                    uid = u.message.chat.id
                    text = u.message.text or ""

                    reply = handle(uid, text)
                    bot.send_message(chat_id=uid, text=reply)

        except Exception as e:
            print("Bot error:", e)

        time.sleep(2)

# ===== BACKGROUND THREADS =====
def start_threads():
    threading.Thread(target=run_bot, daemon=True).start()
    threading.Thread(target=background_search, args=(bot,), daemon=True).start()

# ===== WEB =====
@app.route("/")
def home():
    return "AI Job Agent Running"

# ===== RUN =====
if __name__ == "__main__":
    start_threads()

    port = int(os.getenv("PORT", 3000))
    app.run(host="0.0.0.0", port=port)