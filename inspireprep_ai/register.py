import json
import os

def register_user(name, email, password):
    path = "data/users.json"
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump({}, f)

    with open(path, "r+") as f:
        users = json.load(f)
        if email in users:
            return "User already exists."
        users[email] = {"name": name, "password": password}
        f.seek(0)
        json.dump(users, f, indent=2)
        return "Registration successful."
