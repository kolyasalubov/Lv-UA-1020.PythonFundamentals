class Polygone():
   
    def __init__(self, sides):
        self.side_number = sides
        self.sides = [float(input(f"Enter {x+1} side: ")) for x in range(sides)]


    def show_sides(self):
        counter = 1
        for x in self.sides:            
            print (f"Side {counter} = {x}")
            counter +=1


class Rectangle(Polygone):

    def __init__(self):
        super().__init__(2)


    def show_sides(self):
        counter = 1
        for x in self.sides*2:            
            print (f"Side {counter} = {x}")
            counter +=1


    def area (self):
        s = self.sides[0]*self.sides[1]
        return s
    

# Створила клас Трикутник з перевіркою на існування трикутнику

class Triangle(Polygone):
    
    def __init__(self):
        super().__init__(3)
        sor = sorted(self.sides)
        if sor[0] + sor[1] > sor[2]:
            print("Your triangle exist")
        else:
            print("Your triangle can't exist")
            super().__init__(3)


tri = Triangle()

