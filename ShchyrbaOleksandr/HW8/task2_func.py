import re 

def check_pass(password):
    if len(password) < 6:
        print("Short password.")
        return False
    elif len(password) > 16:
        print("Long password.")
        return False

    if not re.search("[a-z]", password):
        print("Enter at least one lowercase letter.")
        return False
    
    if not re.search("[A-Z]", password):
        print("Enter at least one uppercase letter.")
        return False
    
    if not re.search("[0-9]", password):
        print("Enter at least one number.")
        return False

    if not re.search("[$#@]", password):
        print("Enter at least one special character.")
        return False
    
    print("Password accepted!")
    
