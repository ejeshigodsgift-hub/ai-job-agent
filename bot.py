from telegram.ext import Updater, MessageHandler, Filters
from config import Config
from services.ai_service import chat

updater = Updater(token=Config.TELEGRAM_BOT_TOKEN)

dispatcher = updater.dispatcher


def handle(update, context):
    user_message = update.message.text

    reply = chat(user_message)

    update.message.reply_text(reply)


message_handler = MessageHandler(Filters.text, handle)

dispatcher.add_handler(message_handler)

updater.start_polling()