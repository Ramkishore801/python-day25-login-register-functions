def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")

    print("Registered successfully!")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    found = False

    try:
        with open("users.txt", "r") as file:
            for line in file:
                user, pwd = line.strip().split(",")
                if user == username and pwd == password:
                    found = True
                    break
    except FileNotFoundError:
        print("No users registered yet!")
        return

    if found:
        print("Login successful!")
    else:
        print("Invalid credentials!")


while True:
    print("\n1. Register  2. Login  3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Invalid choice")
