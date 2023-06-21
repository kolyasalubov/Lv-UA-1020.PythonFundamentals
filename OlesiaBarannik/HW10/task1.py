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

    def findArea1(self):
        a, b = self.sides
        area = round(a * b, 2)
        print(f"The area of the rectangle is {area}")

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def check_triangle(self):
        a, b, c = self.sides
        if a + b >= c and b + c >= a and c + a >= b:
            return True
        else:
            return False
    def findArea2(self):
        if self.check_triangle() is True:
            a, b, c = self.sides
            p = (a + b + c) / 2
            area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
            print(f"The area of the triangle is  {round(area, 2)}")
        else:
            print("The triangle condition is not met")


# q = Rectangle()
# q.inputSides()
# q.dispSides()
# q.findArea1()

w = Triangle()
w.inputSides()
w.dispSides()
w.check_triangle()
w.findArea2()



