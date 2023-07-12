class Ball(object):
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type

#########################################################

import random
class Ghost(object): 
    def __init__(self):
        colors = ["white", "yellow", "purple", "red"]
        self.color = random.choice(colors)

###########################################################

class Human():
     def __init__(self):
        super().__init__()
class Man(Human):
    def __init__(self):
        super().__init__()

class Woman(Human):
     def __init__(self):
        super().__init__()
def God():
    return [Man(), Woman()]
        
##########################################################
class Person():
    def __init__(self, name: str, age: int):
        self.info = f"{name}s age is {age}"

##############################################################

from math import pi
class Sphere(object):
	
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass        
    def get_radius(self):
        return self.radius   
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round((4 / 3 * pi * self.radius ** 3), 5)
    def get_surface_area(self):
        return round((4 * pi * self.radius ** 2), 5)
    def get_density(self):
        return round((self.mass / (4 / 3 * pi * self.radius ** 3)), 5)
    

####################################################################

import re
def class_name_changer(cls, new_name):
    cls.__name__ =  new_name
    if re.search("[A - Z]", cls.__name__) is True and cls.__name__.isalnum() is True:
        return cls.__name__
    