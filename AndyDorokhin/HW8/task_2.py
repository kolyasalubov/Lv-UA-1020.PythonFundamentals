""" 
    Write a Python program to check the validity of a password (input from users).
    Validation :
    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.
"""
import re

def check_password(password: str) -> bool:
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search('[a-z]', password):
        return False
    if not re.search('[A-Z]', password):
        return False
    if not re.search('[0-9]', password):
        return False
    if not re.search('[$#@]', password):
        return False
    return True

def main():
    password = input("Enter password: ")
    if check_password(password):
        print("Password is valid")
    else:
        print("Password is not valid")
        
if __name__ == "__main__":
    main()