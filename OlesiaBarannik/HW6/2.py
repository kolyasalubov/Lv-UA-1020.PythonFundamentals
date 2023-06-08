# Task 2. Write a script that validates the login that the user enters.
# If the login is "First", then welcome users. If there is a login
# else, send an error message.
# (need to use a while loop)

while True:
    user_login = input("Enter your login\n")
    if user_login == "First":
        print("Hello dear user")
        break
    else:
        print("Error: You variant is different Please, try again")


