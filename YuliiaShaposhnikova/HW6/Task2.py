user_login = input("Enter your login: ")
if user_login == "First":
    print('Hello, my dear friend!')
while user_login != "First":
    print('Error! Wrong user!')
    user_login = input("Enter your login: ")
    if user_login == "First":
        print('Hello, my dear friend!')
