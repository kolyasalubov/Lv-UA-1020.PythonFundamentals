import re


def password_user(password):
    if 16 > len(password) < 6:
        print("Error: Length of password must be minimum 6 characters and maximum 16 characters")
    elif len(re.findall('\d', password)) < 1:
        print("Error: Password must contain more than one number")
    elif len(re.findall("[a-z]", password)) < 1:
        print("Error: Password must contain more than one small letter")
    elif len(re.findall("[A-Z]", password)) < 1:
        print("Error: Password must contain more than one сapital letter")
    elif len(re.findall("[@#$]", password)) < 1:
        print("Error: Password must contain more than one special character")
    else:
        print("Password is valid")
        return True


while True:
    password_from_user = input("Enter a password: ")
    if password_user(password_from_user):
        break