import definition

h, d, r = 0, 0, 0
result = 0
user_choise = input("Enter area of what geometric figure yiu want to\
 calculate? \n R - for Rectangle \n T - for Triange \n C - for Circle \n ")

if user_choise == "R":
    result = definition.area_rectangle(h, d)
    print(f"The area of Rectangle is {result}")


elif user_choise == "T":
    result = definition.area_triangle(h, d)
    print(f"The area of Triangle is {result}")

elif user_choise == "C":
     result = definition.area_circle(r)
     print(f"The area of Circle is {result}")
    
else:
    print("Your input data is incorrect(((")
