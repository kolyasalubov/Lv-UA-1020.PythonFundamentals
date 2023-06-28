class polygon:
    def __init__(self):
        pass


class rectangle(polygon):
    def __init__(self):
        super().__init__()

    def enter_sides():
        global side_a, side_b
        side_a = int(input("Enter side a: "))
        side_b = int(input("Enter side b: "))
        return print("Area og rectangle:", rectangle.area_rectangle())
    
    def area_rectangle():
        return side_a * side_b

rectangle.enter_sides()
