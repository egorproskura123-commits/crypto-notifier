from flask import Flask, render_template, request, jsonify
from subscription_manager import (
    start_subscription,
    stop_subscription
)


import bot

app = Flask(__name__)


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

    app.run(debug=True, use_reloader=False)