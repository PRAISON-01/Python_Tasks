password = "python123"

for attempt in range(1, 4):
    try_password = input("Enter password 🔐: ")

    if try_password == password:
        print("Unlocked 🔓")
        break
    else:
        print("Wrong password")

        if attempt == 3:
            print("Access denied 🔒")
