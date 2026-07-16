from users import get_users, save_users
from price_service import get_price
from jobs import jobs

async def send_price(context):
    print("=== SEND_PRICE ЗАПУЩЕН ===")
    print("SEND_PRICE START")

    data = context.job.data

    chat_id = data["chat_id"]
    coin = data["coin"]

    print("CHAT:", chat_id)
    print("COIN:", coin)

    try:
        price = get_price(coin)

        print("PRICE:", price)

        await context.bot.send_message(
            chat_id=chat_id,
            text=(
                f"🟠 {coin}\n\n"
                f"💰 Цена: {price} USDT"
            )
        )

        print("MESSAGE SENT")

    except Exception as e:
        print("SEND ERROR:", e)


def start_subscription(code, coin, interval, app):
    users = get_users()
    for chat_id, user in users.items():

        if user["code"] == code:

            user["coin"] = coin
            user["interval"] = interval
            user["running"] = True
            save_users(users)
            if chat_id in jobs:
                jobs[chat_id].schedule_removal()
            print("Создаем job")
            print("interval:", interval)
            print("chat_id:", chat_id)
            print("coin:", coin)
            job = app.job_queue.run_repeating(
                send_price,
                interval=interval,
                first=0,
                data={
                    "chat_id": chat_id,
                    "coin": coin
                }
            )

            jobs[chat_id] = job


            print("Подписка запущена")

            return True


    return False

def stop_subscription(code):

    users = get_users()

    for chat_id, user in users.items():

        if user["code"] == code:

            if chat_id in jobs:

                jobs[chat_id].schedule_removal()

                del jobs[chat_id]

            user["running"] = False

            save_users(users)

            print("Подписка остановлена")

            return True

    return False