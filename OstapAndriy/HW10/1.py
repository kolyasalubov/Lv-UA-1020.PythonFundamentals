class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def get_area(self):
        raise NotImplementedError("Підклас має реалізувати цей метод.")


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)  # Квадрат має 4 сторони (гіпотетичний багатокутник)
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


# Приклад використання:
rectangle = Rectangle(5, 10)
print("Площа прямокутника:", rectangle.get_area())
