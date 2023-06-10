# Task2. Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice)
import math

user_area = input('{"triangle": 1, "rectangle": 2, "circle": 3} \n')

if user_area == "1":
    c = "triangle"
    a = int(input("Please enter the height of the triangle\n"))
    b = int(input("Please enter the side of the triangle\n"))
elif user_area == "2":
    c = "rectangle"
    a = int(input("Please enter the first side of the rectangle\n"))
    b = int(input("please enter the second side of the rectangle\n"))
else:
    c = "circle"
    a = int(input("Please enter the radius of the circle\n"))
    b = 1

def calculates_area(a, b):
    if user_area == "1":
        return 1/2 * a * b
    if user_area == "2":
        return a * b
    if user_area == "3":
        return math.pi * a**2

print(f"The area of the {c}: ",calculates_area(a, b))

