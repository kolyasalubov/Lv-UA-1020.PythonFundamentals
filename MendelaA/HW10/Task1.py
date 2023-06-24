class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    
    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])


class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)
    
    def findArea(self):
        a, b, c = self.sides
        p = (a + b + c) / 2
        if a + b > c:
            area = (p*(p-a)*(p-b)*(p-c)) ** 0.5
            print('The area of the triangle is %0.2f' %area)
        else:
            print('Wrong data for create triangle')

class Rectange(Polygon):
    def __init__(self):
        super().__init__(2)

    def findArea(self):
        a, b = self.sides
        s = a * b
        print('The area of the triangle is %0.2f' %s)

# t = Triangle()
# t.inputSides()
# t.dispSides()
# t.findArea()

# r = Rectange()
# r.inputSides()
# r.dispSides()
# r.findArea()