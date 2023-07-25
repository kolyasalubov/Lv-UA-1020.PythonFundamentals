user_number = input("Add four-digit number please:")
if len(user_number) == 4:
    print("Product of the digits is:",
          int(user_number[0])*
    int(user_number[1])*
    int(user_number[2])*
    int(user_number[3]))
    print(user_number[::-1])
    print(sorted(user_number))
else:
    print("Error! You need to add four digit number please")