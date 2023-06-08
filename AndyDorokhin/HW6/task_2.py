""" 
    Task2. Write a script that checks the login that the user enters.
    If the login is "First", then greet the users.
    If the login is different, send an error message.
    (need to use loop while)
"""
def greet_first():
    login = input("Enter login: ")
    while login.lower() != "first":
        login = input("Wrong login. Please enter login again: ")
    print(f"Hello, {login.capitalize()}!")
    
def main():
    greet_first()
    
if __name__ == "__main__":
    main()
