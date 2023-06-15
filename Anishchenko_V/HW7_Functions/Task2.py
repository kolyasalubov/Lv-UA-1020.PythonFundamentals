import math


def rectangle_area(x, y):
    """
    The function returns area of a ractangle.
    'x' and 'y' parametres are sides of rectangle.
    """
    return x * y


def triangle_area(x, y, z):
    """
    The function returns area of a triangle
    calculated according to Heron formula.
    'x', 'y' and 'z' parameters are sides of triangle.

    """
    hp = (x + y + z) / 2
    area = math.sqrt(hp * (hp - x) * (hp - y) * (hp - z))
    return area


def circle_area(r):
    """
    The function returns area of a circle.
    'r' is radius of the circle.
    """
    return math.pi * r ** 2


choice = input(
    'Choose shape to calculate area (press "1" for rectangle), "2" for triangle, "3" for circle): ')

match choice:
    case '1':
        x = float(input('Enter lentgh of a side: '))
        y = float(input('Enter lentgh of another side: '))
        print('This rectangle\'s area is: ', round(rectangle_area(x, y), 1))
    case '2':
        x = float(input('Enter lentgh of first side: '))
        y = float(input('Enter lentgh of second side: '))
        z = float(input('Enter lentgh of third side: '))
        print('This triangle\'s area is: ', round(triangle_area(x, y, z), 1))
    case '3':
        r = float(input('Enter lentgh of radius: '))
        print('This circle\'s area is: ', round(circle_area(r), 1))
    case _:
        print('Error. You have not chosen right option. Restart and try again.')
