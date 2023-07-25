# calculate_area.py
import math

def rectangle_area(a, b):
    # Функція для обчислення площі прямокутника S=a*b
    return a * b

def triangle_area(base, height):
    # Функція для обчислення площі трикутника S=0.5*h*a
    return 0.5 * base * height

def circle_area(radius):
    # Функція для обчислення площі кола S=pi*r**2
    return math.pi * pow(radius, 2)
