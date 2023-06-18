import func_module
width, height, base, r = 0, 0, 0, 0


user_choise = input("Enter area of what geometric figure yiu want to\
 calculate? \n R - for Rectangle \n T - for Triange \n C - for Circle \n ")

if user_choise == "R":
    print(func_module.area_rectangle(width, height))

elif user_choise == "T":
    print(func_module.area_triangle(base, height))

elif user_choise == "C":
    print(func_module.area_circle(r))
    
else:
    print("Your input data is incorrect(((")
