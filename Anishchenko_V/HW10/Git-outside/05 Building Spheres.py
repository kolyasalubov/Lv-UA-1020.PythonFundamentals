import math


class Sphere():
    def __init__(self, r, m):
        self.object = (r, m)

    def get_radius(self):
        return self.object[0]

    def get_mass(self):
        return self.object[1]

    def get_volume(self):
        return round(4 / 3 * math.pi * self.object[0] ** 3, 5)

    def get_surface_area(self):
        return round(4 * math.pi * self.object[0] ** 2, 5)

    def get_density(self):
        return round(self.object[1] / (4 / 3 * math.pi * self.object[0] ** 3), 5)
