import os, time, threading
import telegram
from flask import Flask
from bot import handle
from jobs import background_search

# ==============================
# CONFIG & GLOBAL STATE
# ==============================

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# ✅ Token validation
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is missing")

bot = telegram.Bot(token=TOKEN)

# Track user activity
user_last_seen = {}

# Thread control
stop_event = threading.Event()

# ==============================
# FLASK ROUTE
# ==============================

@app.route("/")
def home():
    return "AI Job Agent Running"

# ==============================
# TELEGRAM BOT LOOP (FIXED)
# ==============================

def run_bot():
    offset = None

    while not stop_event.is_set():
        try:
            updates = bot.get_updates(offset=offset, timeout=10)

            for u in updates:
                offset = u.update_id + 1

                if u.message:
                    uid = u.message.from_user.id
                    text = u.message.text or ""

                    # ✅ Track user activity
                    user_last_seen[uid] = time.time()

                    response = handle(uid, text)

                    bot.send_message(chat_id=uid, text=response)

        except Exception as e:
            print("Bot error:", e)
            time.sleep(5)  # retry delay

        time.sleep(2)

# ==============================
# BACKGROUND SEARCH (CONTROLLED)
# ==============================

def controlled_background_search():
    while not stop_event.is_set():
        try:
            current_time = time.time()

            for uid, last_seen in list(user_last_seen.items()):
                # ✅ Stop sending if user inactive for 24 hours
                if current_time - last_seen > 86400:
                    continue

                # Call your job search logic per active user
                background_search(bot, uid)

        except Exception as e:
            print("Background error:", e)
            time.sleep(5)

        time.sleep(10)

# ==============================
# STARTUP
# ==============================

if __name__ == "__main__":
    try:
        threading.Thread(target=run_bot, daemon=True).start()
        threading.Thread(target=controlled_background_search, daemon=True).start()

        port = int(os.environ.get("PORT", 3000))

        # ✅ Flask debug mode enabled
        app.run(host="0.0.0.0", port=port, debug=True)

    except KeyboardInterrupt:
        print("Shutting down...")
        stop_event.set()