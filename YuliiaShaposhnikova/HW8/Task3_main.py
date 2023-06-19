from Task3_calc import rectangle_area, triangle_area, circle_area


def main():
    """
    Main function which asks user to choose needed figure and returns its area
    """
    figure = input("Choice figure: R - rectangle, T - triangle, C - circle: ")
    if figure == "R":
        rectangle_area()
    elif figure == "T":
        triangle_area()
    elif figure == "C":
        circle_area()


if __name__ == "__main__":
    main()
