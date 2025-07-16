import json
import sys
from datetime import datetime


def load_updates():
    try:
        with open("updates.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_updates(updates):
    with open("updates.json", "w") as f:
        json.dump(updates, f, indent=2)


def add_update(title, body):
    updates = load_updates()
    new_id = max(u["id"] for u in updates) + 1 if updates else 1

    new_update = {
        "id": new_id,
        "title": title,
        "body": body,
        "timestamp": int(datetime.now().timestamp() * 1000)
    }

    updates.append(new_update)
    save_updates(updates)
    print(f"Added update (ID: {new_id})")


print("Update Manager CLI")
print("-----------------")

try:
    title = input("Enter title: ").strip()
    if not title:
        raise ValueError("Title cannot be empty")

    body = input("Enter body: ").strip()
    if not body:
        raise ValueError("Body cannot be empty")

    add_update(title, body)

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)
