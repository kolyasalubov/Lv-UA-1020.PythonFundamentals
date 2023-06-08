"""
    Write a program that calculates the area of a rectangle, triangle and circle.
    Write three functions to calculate the area, and call them in the
    main program depending on the user's choice).
"""
def rectangle_area(a, b):
    """
    Returns the area of a rectangle.

    Args:
        a (float): first side of the rectangle
        b (float): second side of the rectangle

    Returns:
        int: the area of a rectangle
    """
    return a * b

def triangle_area(b, h):
    """
    Returns the area of a triangle.

    Args:
        b (float): base of the triangle
        h (float): height of the triangle

    Returns:
        float: the area of a triangle
    """
    return b * h / 2

def circle_area(r):
    """
    Returns the area of a circle.

    Args:
        r (float): radius of the circle

    Returns:
        float: the area of a circle
    """
    return 3.14 * r**2

def main():
    choice = input("Enter the shape (1 for rectangle, 2 for triangle, 3 for circle): ")
    if choice == "1":
        a = float(input("Enter the first side of the rectangle: "))
        b = float(input("Enter the second side of the rectangle: "))
        print("The area of a rectangle is", rectangle_area(a, b))
    elif choice == "2":
        b = float(input("Enter the base of the triangle: "))
        h = float(input("Enter the height of the triangle: "))
        print("The area of a triangle is", triangle_area(b, h))
    elif choice == "3":
        r = float(input("Enter the radius of the circle: "))
        print("The area of a circle is", circle_area(r))
    else:
        print("Incorrect input")

if __name__ == "__main__":
    main()
         