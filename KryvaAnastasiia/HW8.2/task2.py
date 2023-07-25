password = input("Create your password. You need use at least 1 big letter, 1 small letter, 1 number, 1 character from[@#$]. Min number of characters is 6, max is 16")

def check_password(password):
    digits = 0
    letters = 0
    lower_c = 0
    upper_c = 0
    spec_char = 0
    special_char = ["@", "#", "$"]

    for x in password:  
        if x.isdigit():
            digits += 1
        
        if  x.isalpha():
            letters +=1
              
        if  x.islower():
            lower_c += 1
            
        if  x.isupper():
            upper_c += 1
            
        if x in special_char:
            spec_char += 1

    if digits > 1 and letters > 1 and lower_c > 1 and upper_c > 1 and spec_char > 1  and 6 <= len(password) <=16:
        return "Great password"
    
    else:
        return "Try again"


###########################################################################


import re

password = input("Create your password. You need use at least 1 big letter, 1 small letter, 1 number, 1 character from[@#$]. Min number of characters is 6, max is 16")

lower_c = re.findall("[a-z]", password)
upper_c = re.findall("[A-Z]", password)
digits = re.findall("[0-9]", password)
spec_char = re.findall("[$, #, @]", password)


if len(digits) >= 1 and len(lower_c) >= 1 and len(upper_c) >= 1 and len(spec_char) >= 1 and 6 <= len(password) <= 16:
    print("Great password")
    
else:
    print("Try again")



