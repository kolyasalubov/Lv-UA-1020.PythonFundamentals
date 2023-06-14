from math import pi, pow

__all__ = ["calc_rec", "calc_tri", "calc_circle"]


def calc_rec():
    a = float(input('Enter size of first side of rectangle: '))
    b = float(input('Enter size of another side of rectangle: '))
    print(f'Area of this rectangle equals to: {round(a * b, 1)}')


def calc_tri():
    h = float(input('Enter height of the triangle: '))
    a = float(input('Enter base size of the triangle: '))
    print(f'Area of this triangle equals to: {round(0.5 * h * a, 1)}')


def calc_circle():
    r = float(input('Enter radius of circle: '))
    print(f'Area of this circle equals to: {round(pi * pow(r, 2), 1)}')
