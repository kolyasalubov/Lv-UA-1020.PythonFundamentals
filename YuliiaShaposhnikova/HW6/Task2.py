# First solution
user_login = input("Enter your login: ")
if user_login == "First":
    print('Hello, my dear friend!')
while user_login != "First":
    print('Error! Wrong user!')
    user_login = input("Enter your login: ")
    if user_login == "First":
        print('Hello, my dear friend!')

# Second solution
while True:
    user_login = input("Enter your login: ")
    if user_login == "First":
        print('Hello, my dear friend!')
        break
    else:
        print('Error! Wrong user!')
