""" 
    This module contains the class Sphere
    
    Arguments for the constructor:
    radius -> integer or float (do not round it)
    mass -> integer or float (do not round it)
    
    Methods to be defined
    get_radius()       =>  radius of the Sphere (do not round it)
    get_mass()         =>  mass of the Sphere (do not round it)
    get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
    get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
    get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)
    
    Example:
    ball = Sphere(2,50)
    ball.get_radius() ->       2
    ball.get_mass() ->         50
    ball.get_volume() ->       33.51032
    ball.get_surface_area() -> 50.26548
    ball.get_density() ->      1.49208    
"""
import math

class Sphere:
    
    def __init__(self, radius, mass):
        self.__radius = radius
        self.__mass = mass
    
    def get_radius(self):
        return self.__radius
    
    def get_mass(self):
        return self.__mass
    
    def get_volume(self):
        return round(4/3*math.pi*self.__radius**3, 5)
    
    def get_surface_area(self):
        return round(4*math.pi*self.__radius**2, 5)
    
    def get_density(self):
        return round(self.__mass/(4/3*math.pi*self.__radius**3), 5)
    
def main():
    ball = Sphere(2,50)
    print(ball.get_radius())
    print(ball.get_mass())
    print(ball.get_volume())
    print(ball.get_surface_area())
    print(ball.get_density())
    
if __name__ == "__main__":
    main()