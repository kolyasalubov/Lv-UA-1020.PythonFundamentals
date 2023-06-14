from math import pi, pow
def rectangle(length: float, width: float):
    """
    calculates the area of a rectangle
    :param length:
    :param width:
    :return: area
    """
    area = length * width
    return area


def triangle(height: float, base: float):
    """
    calculates the area of a triangle
    :param height:
    :param base:
    :return: area
    """
    area = 0.5 * height * base
    return area


def circle(radius: float):
    """
    calculates the area of circle
    :param radius:
    :return: area
    """
    area = pi * pow(radius, 2)
    return round(area, 2)

