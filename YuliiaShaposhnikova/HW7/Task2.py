import math


def rectangle(length, breadth):
    """
    function return area of a rectangle
    length: float
    breadth: float
    return: float
    """
    rectangle_area = length * breadth
    return f'The area of a rectangle: {rectangle_area}'


def triangle(base, height):
    """
        function return area of a triangle
        base: float
        height: float
        return: float
        """
    triangle_area = (base * height) / 2
    return f'The area of a triangle: {triangle_area}'


def circle(radius):
    """
        function return area of a circle
        radius: float
        return: float
        """
    circle_area = round(math.pi * (radius ** 2), 2)
    return f'The area of a circle: {circle_area}'


def main():
    figure = input("Choice figure: R - rectangle, T - triangle, C - circle: ")
    if figure == "R":
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        print(rectangle(length, breadth))

    elif figure == "T":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print(triangle(base, height))

    elif figure == "C":
        radius = float(input("Enter radius: "))
        print(circle(radius))


if __name__ == "__main__":
    main()
