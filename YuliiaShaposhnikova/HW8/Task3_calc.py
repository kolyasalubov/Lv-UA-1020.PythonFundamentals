from math import pi
from math import pow


def rectangle_area():
    """
    Function which calculate the rectangle area
    """
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    rect_area = length * breadth
    print(f"The rectangle area: {rect_area}")


def triangle_area():
    """
    Function which calculate the triangle area
    """
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    trian_area = round(0.5 * height * base, 2)
    print(f"The triangle area: {trian_area}")


def circle_area():
    """
    Function which calculate the circle area
    """
    radius = float(input("Enter radius: "))
    circ_area = round(pi * pow(radius, 2), 2)
    print(f"The circle area: {circ_area}")

