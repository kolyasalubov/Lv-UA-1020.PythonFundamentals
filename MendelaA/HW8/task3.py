from math import pow, pi

def rectangle_area(a, b):
    return f'The area of rectangle is {a * b}'

def triangle_area(h, a):
    return f'The area of triangle is {0.5*h*a}'

def circle_area(r):
    return f'The area of circle {pi*pow(r,2)}'


print(rectangle_area(12, 1))
print(triangle_area(10, 2))
print(circle_area(10))