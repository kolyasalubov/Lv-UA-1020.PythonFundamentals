class Polygon:
    """
    Class Polygon
    """
    def __init__(self, no_of_sides) -> None:
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides=[float(input(f'Enter side {str(i+1)}: ')) for i in range(self.n)]

class Rectangle(Polygon):
    """
    Class for rectangle
    """
    def __init__(self) -> None:
        super().__init__(2)
    def area(self):
        return self.sides[0]*self.sides[1]

if __name__ == '__main__':
    c = Rectangle()
    c.inputSides()
    print(f"The area of rectangle: {c.area()}")

