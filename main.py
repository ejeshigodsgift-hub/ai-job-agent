import os, time, threading
import telegram
from flask import Flask
from bot import handle
from jobs import background_search

# 1. Create Flask FIRST
app = Flask(__name__)

# 2. Load token
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# 3. (Optional debug)


# 4. Create bot
bot = telegram.Bot(token=TOKEN)

# 5. Now routes can safely use app
@app.route("/")
def home():
    return "Bot is running"

# 6. Bot loop
def run_bot():
    offset = None
    while True:
        updates = bot.get_updates(offset=offset)
        for u in updates:
            offset = u.update_id + 1
            if u.message:
                uid = u.message.from_user.id
                text = u.message.text or ""
                bot.send_message(chat_id=uid, text=handle(uid, text))
        time.sleep(2)

@app.route("/")
def home():
    return "AI Job Agent Running"

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    threading.Thread(target=background_search, args=(bot,)).start()

    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)