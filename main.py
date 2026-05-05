import os, time, threading
import telegram
from flask import Flask
from bot import handle
from jobs import background_search

bot = telegram.Bot(token=os.getenv("TELEGRAM_TOKEN"))
app = Flask(__name__)

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