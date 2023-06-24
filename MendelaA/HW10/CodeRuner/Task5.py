"""
Building Spheres

Arguments for the constructor

radius -> integer or float (do not round it)
mass -> integer or float (do not round it)

Methods to be defined

get_radius()       =>  radius of the Sphere (do not round it)
get_mass()         =>  mass of the Sphere (do not round it)
get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)

"""
import math

class Sphere():
    
    #PI = 3.14

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        vol = (4/3) * math.pi * (self.radius ** 3)
        return round(vol, 5)

    def get_surface_area(self):
        s_area = 4 * math.pi * (self.radius **2 )
        return round(s_area, 5)
    
    def get_density(self):
        dens = self.mass / self.get_volume()
        return round(dens, 5)


ball = Sphere(2,50)
print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_desiny())