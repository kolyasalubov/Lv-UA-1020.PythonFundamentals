def area_of_rectangle (a, b):
    """
    S = a * b
    """
    return f'The area of rectangle is {a * b}'

def area_of_triangle (a, h):
    """
    S = 1/2 * (a * h)
    """
    return f'The area of triangle is {1/2 * (a * h)}'

def area_of_circle (r, pi=3.14):
    """
    S =  π * r2
    """
    return f'The area of circle is {pi * (r**2)}'

print(area_of_rectangle(10, 20))
print(area_of_triangle(10, 20))
print(area_of_circle(10))