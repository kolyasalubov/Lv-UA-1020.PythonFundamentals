class Polygon:
    """
    class which has no_of_sides (number of sides) as attribute
    """
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        """
        method which asks user to enter length of all sides
        """
        self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]

    def dispSides(self):
        """
        method which displays length of all sides entered by user
        """
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])


class Rectangle(Polygon):
    """
    class which inheritances from class Polygon
    """
    def __init__(self):
        Polygon.__init__(self, 2)

    def findArea(self):
        """
        method which calculates area of rectangle and print its result
        """
        a, b = self.sides
        area = a * b
        print(f'The area of the rectangle is {area}')


t = Rectangle()  # create instance of class Rectangle
t.inputSides()  # call inputSides method for t instance
t.dispSides()  # call dispSides method for t instance
t.findArea()  # call findArea method for t instance

