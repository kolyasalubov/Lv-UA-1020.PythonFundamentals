import math

# h, d, r = 0, 0, 0


def area_rectangle(h, d):
    d = float(input("Enter width of rectangle"))
    h = float(input("Enter height of rectangle"))
    return round(h*d, 2)


def area_triangle(h, d):
    d = float(input("Enter base of triangle"))
    h = float(input("Enter height of triangle"))
    return round((0.5 * h*d), 2)


def area_circle(r):
    r = float(input("Enter radius of circle"))
    return round(math.pi * math.pow(r, 2), 2)
