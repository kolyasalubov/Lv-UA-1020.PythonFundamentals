
b=True
while b:
    password = input("Create a new pass")
    if password.upper() == password:
        password = input("Create a new pass1")
    elif password.lower() == password:
        password = input("Create a new pass2")
    elif len(password) >16 or len(password) < 6:
        password = input("Create a new pass3")
    elif b == True :
        chack_list = (list(map(str, range(10))) + ["$", "#", "@"])
        for i in range (len(chack_list)):
            for k in range(len(password)):
                if chack_list[i] == password[k]:
                    k += 1
                else:
                    password = input("Create a new pass4")                  
            i +=1



    else:
        print("Pass is good")
        b= False
    
