width, height, base, r = 0, 0, 0, 0


def area_rectangle(width, height):
    width = float(input("Enter width of rectangle"))
    height = float(input("Enter height of rectangle"))
    return round(width*height, 2)


def area_triangle(base, height):
    base = float(input("Enter base of triangle"))
    height = float(input("Enter height of triangle"))
    return round((0.5 * base * height), 2)


def area_circle(r):
    r = float(input("Enter a radius of circle"))
    return round(3.14 * (r**2), 2)
