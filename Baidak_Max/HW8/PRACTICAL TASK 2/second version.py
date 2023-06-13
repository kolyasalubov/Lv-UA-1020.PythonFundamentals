def password_user(password):
    if 16 > len(password) < 6:
        print("Length of password must be minimum 6 characters and maximum 16 characters")

    has_lower = False
    has_isdigit = False
    has_special = False
    has_upper = False

    for word in password:
        if word.islower() == True:
            has_lower = True
        elif word.isupper() == True:
            has_upper = True
        elif word.isdigit() == True:
            has_isdigit = True
        elif word in "@#$":
            has_special = True
    return has_special and has_lower and has_upper and has_isdigit

password = input("Enter a password: ")
if password_user(password):
    print("That`s correct password")
else:
    print("error")