class Polygon:
    """
    This is super class 'Polygon'
    """

    def __init__(self):
        pass


class Rect(Polygon):
    def __init__(self):
        super(Rect, self).__init__()

    def square(self, side1_size, side2_size):
        return side1_size * side2_size
