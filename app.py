from flask import Flask, render_template, request, jsonify
import threading
import time
from subscription_manager import (
    start_subscription,
    stop_subscription
)


import bot

app = Flask(__name__)

def start_bot():

    bot_thread = threading.Thread(
        target=bot.run_bot,
        daemon=True
    )

    bot_thread.start()

    while bot.telegram_app is None:
        time.sleep(0.1)


start_bot()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start():

    data = request.get_json()

    code = data["code"]
    coin = data["coin"]
    interval = int(data["interval"])

    success = start_subscription(
        code,
        coin,
        interval,
        bot.telegram_app
    )

    if success:
        return jsonify({"status": "ok"})

    return jsonify({"status": "error"})
@app.route("/stop", methods=["POST"])
def stop():

    data = request.get_json()

    code = data["code"]

    success = stop_subscription(code)

    if success:
        return jsonify({"status": "ok"})

    return jsonify({"status": "error"})

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )