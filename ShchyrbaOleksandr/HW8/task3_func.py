import math

def area_rectangle():
    side_a = int(input("Input length of side a: "))
    side_b = int(input("Input length of side b: "))
    area_rec = side_a * side_b
    print("Area of rectangle: ", area_rec)

def area_triangle():
    side_a = int(input("Input length of side a: "))
    h = int(input("Input length of side h: "))
    area_tri = 0.5 * h * side_a
    print("Area of triangle: ", int(area_tri))

def area_circle():
    radius = int(input("Input radius of circle: "))
    area_circ = math.pi * radius ** 2
    print ("Area of circle: ", area_circ)
