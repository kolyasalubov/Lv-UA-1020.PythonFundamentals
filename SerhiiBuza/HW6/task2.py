# use loop while
user_name = input("Enter your USER NAME")
control_name  = "First"
i=0
if len(control_name) != len(user_name):
    print (f"LOGIN {user_name} is incorrect. Try again!")
else:
    while i <len(user_name):
        if  user_name[i] != control_name[i]:
            print (f"LOGIN {user_name} is incorrect. Try again!")
            break
        i+=1
    else:
        print (f"Congratulations!! Your LOGIN {user_name} is right")

    


