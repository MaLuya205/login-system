
import json
import os

FILE = "users.json"

# Load users from file if exists, else start with 2 default
def load_users():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    else:
        return {
            "luyanda": {"pin": "1234", "email": "luyanda@gmail.com"},
            "user": {"pin": "0000", "email": "test@gmail.com"}
        }

def save_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f, indent=2)
    print(f"✅ Saved to {FILE}!")

def login(users):
    name = input("Enter name: ").lower()
    pin = input("Enter pin: ")
    if name in users and users[name]["pin"] == pin:
        print(f"Welcome {name}! Email: {users[name]['email']}")
    else:
        print("❌ Wrong name or pin!")

def add_user(users):
    name = input("New name: ").lower()
    pin = input("New pin: ")
    email = input("New email: ")
    users[name] = {"pin": pin, "email": email}
    save_users(users)
    print(f"User {name} added!")

def show_all(users):
    print("\n--- All Users ---")
    for name, info in users.items():
        print(f"{name} -> {info['email']}")

# MAIN
users = load_users()

while True:
    print("\n1. Login\n2. Add User\n3. Show All\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        login(users)
    elif choice == "2":
        add_user(users)
    elif choice == "3":
        show_all(users)
    elif choice == "4":
        print("Bye! 👋")
        break
    else:
        print("Invalid choice!")
