class Polygon:
    def __init__(self, num_of_side):
        self.num_of_side = num_of_side
        self.sides = []
        for i in range(num_of_side):
            self.sides.append(0)

    def inputSides(self):
        for i in range(self.num_of_side):
            user_input = float(input(f"Enter your side {str(i+1)}: "))
            self.sides[i] = user_input

    def dispSides(self):
        print(self.sides)

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def findArea(self):
        a, b = self.sides
        area = round(a * b, 2)
        print(f"The area of the rectangle is {area}")

q = Rectangle()
q.inputSides()
q.dispSides()
q.findArea()