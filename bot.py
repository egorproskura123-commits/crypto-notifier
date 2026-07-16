from telegram.ext import Application, CommandHandler
from utils import generate_code
from config import TOKEN
from users import get_users, save_users
import os
async def error_handler(update, context):
    print("Ошибка Telegram:", context.error)

telegram_app = None
async def start(update, context):
    users = get_users()
    chat_id = update.effective_chat.id
    username = update.effective_user.username
    if chat_id not in users:
        code = generate_code()

        users[chat_id] = {
            "username": username,
            "code": code,
            "coin": None,
            "interval": None,
            "running": False
        }
        save_users(users)
    code = users[chat_id]["code"]
    print(users)

    await update.message.reply_text(
        f"✅ Вы зарегистрированы!\n\n"
        f"Ваш код:\n"
        f"{code}\n\n"
        f"Введите этот код на сайте."
    )

def run_bot():

    global telegram_app

    telegram_app = Application.builder().token(TOKEN).build()

    print("BOT START PID:", os.getpid())

    telegram_app.add_handler(
        CommandHandler("start", start)
    )
    telegram_app.add_error_handler(error_handler)
    print("Бот запущен")

    telegram_app.run_polling(
        drop_pending_updates=True
    )