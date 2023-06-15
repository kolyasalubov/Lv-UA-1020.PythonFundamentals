from my_functions import triangle, rectangle, circle
from math import pi, pow
def calculate_area():
    while True:
        user_choice = input("""Which figure you wants to calculate?
        Choose the number under which the figure stands:
        1. Rectangle, 2. Triangle, 3.Circle\n: """)

        match user_choice:
            case "1":
                length = float(input("Enter a length: "))
                width = float(input("Enter a width: "))
                print("The area of rectangle:", rectangle(length, width))
                break
            case "2":
                height = float(input("Enter a height: "))
                base = float(input("Enter a base: "))
                print("The area of triangle: ", triangle(height, base))
                break
            case "3":
                radius = float(input("Enter a radius: "))
                print("The area of circle: ", circle(radius))
                break
            case _:
                print("Wrong number, enter number from 1 to 3")


calculate_area()