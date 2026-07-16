import json
import os


FILE = "users.json"


def get_users():

    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_users(users):

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            users,
            f,
            indent=4,
            ensure_ascii=False
        )