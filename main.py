# Python User Login System with Email
# By MaLuya205 - My first auth project

users = {
    "Sanele": {"pin": "0000", "email": "sanele@gmail.com"},
    "Luyanda": {"pin": "1234", "email": "luyanda@gmail.com"}
}

def add_user():
    name = input("New name: ")
    pin = input("New pin: ")
    email = input("New email: ")
    users[name] = {"pin": pin, "email": email}
    print(f"User {name} added! ✅")

def login():
    name = input("Enter name: ")
    pin = input("Enter pin: ")

    if name not in users:
        return f"User {name} not found! ❌"
    if users[name]["pin"] == pin:
        return f"Welcome {name}! ✅ Email: {users[name]['email']}"
    else:
        return "Wrong pin! ❌"

while True:
    print("\n1. Login | 2. Add User | 3. Show All | 4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        print(login())
    elif choice == "2":
        add_user()
    elif choice == "3":
        print(users)
    elif choice == "4":
        print("Bye!")
        break
