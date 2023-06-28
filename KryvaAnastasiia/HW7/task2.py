def rectangle_square(a, b):
    rect_square = a * b
    return rect_square


def triangle_square(a, h):
    tri_square = 1/2 * a * h
    return tri_square


def circle_square(r):
    PI = 3.14
    circ_square = PI * r ** 2
    return circ_square


x = int(input("Choose geometry shape: rectangle  1, triangle 2, circle 3 :"))

if x == 1:
    a = int(input("Enter lenght :"))
    b = int(input("Enter width :"))

    print(rectangle_square(a, b))

elif x == 2:
    a = int(input("Enter base :"))
    h = int(input("Enter height :"))

    print(triangle_square(a, h))

elif x == 3:
    r = int(input("Enter radius :"))

    print(circle_square(r))
