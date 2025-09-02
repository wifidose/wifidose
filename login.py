attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "admin" and password == "12345":
        print("Access granted")
        break
    else:
        attempts += 1
        print(f"Access denied, {attempts} of {max_attempts} attempts used")