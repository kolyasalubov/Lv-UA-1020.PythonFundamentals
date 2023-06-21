""" 
    Task1. Create a polygon class and a rectangle class that inherits from the polygon class 
    and finds the square of rectangle.
"""
class Polygon:
    def __init__(self, dimensions):
        self._dimensions = dimensions
        self._sides = [0 for i in range(dimensions)]
    
    def input_sides(self):
        self._sides = [float(input(f"Enter side {i+1}: ")) for i in range(self._dimensions)]
    
    def show_sides(self):
        for i in range(self._dimensions):
            print(f"Side {i+1} is {self._sides[i]}")
    
    def perimeter(self):
        return sum(self._sides)
    
class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)
    
    def area(self):
        return self._sides[0] * self._sides[1]
    
def main():
    rect = Rectangle()
    print(rect)
    print(type(rect))
    print(isinstance(rect, Polygon))
    
    rect.input_sides()
    rect.show_sides()

    print(f"Perimeter is {rect.perimeter()}")
    print(f"Area is {rect.area()}")
    
if __name__ == "__main__":
    main()