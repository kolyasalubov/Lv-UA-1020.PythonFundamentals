# Task2. Write a script that checks the login that the user enters.
# If the login is "First", then greet the users.
# If the login is different, send an error message.
# (need to use loop while)


while True:
    login = input("Enter your login: \n")
    if login == "First":
        print("Welcome to Python world. Have a good day.")
        break
    else:
        print("Error: Invalid login. Please try again.")