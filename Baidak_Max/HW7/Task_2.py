## Task 2
## Write a program that calculates the area of a rectangle,
## triangle and circle (write three functions to calculate the area.
## And call them in the main program depending on the user's choice).


def rectangle(width, length):
    """
    the area of a rectangle
    """
    area_rect = width * length
    return area_rect


def triangle(height ,base):
    """
    the area of a triangle
    """
    area_tria = (1/2) * height * base
    return area_tria


def circle_area(radius):
    """
    the area of a circle
    """
    PI = 3.14
    area_cir = PI * radius ** 2
    return area_cir



user_choice = float(input("The area of what do you want: 1.rectangle, 2.triangle, 3.circle? Choice a number: "))

if user_choice == 1:
    width = float(input("Enter a width: "))
    length = float(input("Enter a length: "))
    print("The area of rectangle is:", rectangle(width, length))
elif user_choice == 2:
    height = float(input("Enter a height: "))
    base = float(input("Enter a base: "))
    print("The area of triangle is:", triangle(height, base))
elif user_choice == 3:
    radius = float(input("Enter a radius: "))
    print("The area of a circle is:", round(circle_area(radius)))
else:
    print("That`s wrong number. Please enter 1, 2, 3.")