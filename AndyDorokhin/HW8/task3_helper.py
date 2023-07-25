""" 
    Write a program that calculates the area of a rectangle S=a*b, the area of a
    triangle S=0.5*h*a, the area of a circle S=pi*r**2. This module must be used in
    another module in which we ask the user the area of which figure he wants to
    calculate.
    (To perform the task, you need to import the math module, and from it the
    pow() function and the value of the variable pi, and module, which contains
    three functions for finding areas, into the main program. The basic logic of the
    program is executed in the main module).
"""
from math import pi
from math import pow

def rectangle_area(a: float, b: float) -> float:
    return a * b

def triangle_area(base: float, height: float) -> float:
    return 0.5 * base * height

def circle_area(radius: float) -> float:
    return pi * pow(radius, 2)

