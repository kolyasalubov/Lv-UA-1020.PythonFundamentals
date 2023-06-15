
check = True
check_len = (list(map(str, range(10))) )
check_len2 = ['@','#','$']
password = input("Enter a pass")

while check:
    if len(password)<6 or  len(password) >16:
        password = input("Enter a pass1")
    elif any(i in check_len for i in password) ==False:
        password = input("Enter a pass2")
    elif any(j in check_len2 for j in password) ==False:
         password = input("Enter a pass3")
    elif (password.upper() == password) or (password.lower() == password):
        password = input("Enter a pass4")
    else :
        print ("Pass is goood")
        check = False