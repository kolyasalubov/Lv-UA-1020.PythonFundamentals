# Create a polygon class
class PoligonFigure():
    def __init__(self, base, h):
        self.base = base
        self.h = h

    def array(self):
        return float(self.base*self.h)


class TriangleFigure(PoligonFigure):
    def triangle_array(self):
        return float(0.5 * self.base*self.h)


triangle_figure1 = TriangleFigure(25, 10)
square_triangle = triangle_figure1.triangle_array()
print(square_triangle)
