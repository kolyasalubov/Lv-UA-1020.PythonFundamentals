login = ("First")
request = input("Write your login please:")
if request == login:
    print("It is correct login, you're welcome")
while request != login:
    print("Error, incorrect login. Try again.")
    request = input("Write your login please:")
    if request == login:
        print("It is correct login, you're welcome")