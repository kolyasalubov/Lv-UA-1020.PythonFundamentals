class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self):
        pass

    def get_area(self, length, width):
        return length * width


rectangle = Rectangle()
area = rectangle.get_area(5, 7)
print(f"The area of the rectangle is: {area}")