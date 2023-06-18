from my_func_area import calculates_rectangle, calculates_circle, calculates_triangle
from math import pi, pow

user_area = input('{"triangle": 1, "rectangle": 2, "circle": 3} \n')

if user_area == "1":
    a = int(input("Please enter the height of the triangle\n"))
    b = int(input("Please enter the side of the triangle\n"))
    print("The area of the triangle", calculates_triangle(a, b))
elif user_area == "2":
    a = int(input("Please enter the first side of the rectangle\n"))
    b = int(input("please enter the second side of the rectangle\n"))
    print("The area of the rectangle", calculates_rectangle(a, b))
else:
    a = int(input("Please enter the radius of the circle\n"))
    b = 1
    print("The area of the circle", calculates_circle(a, b))