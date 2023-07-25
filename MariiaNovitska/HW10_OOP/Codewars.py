# # 1. Regular Ball Super Ball

# class Ball(object):
#     def __init__(self, ball_type = "regular"):
#         self.ball_type = ball_type


# # 2. Color Ghost
# from random import choice

# class Ghost():
    
#     def __init__(self):
#         color_list = ["white", "yellow", "purple", "red"]
#         self.color = choice(color_list)


# # 3. Basic subclasses - Adam and Eve
# def God():
#     man = Man()
#     woman = Woman()
#     paradise = [man, woman]
#     return paradise

# class Human():
#     pass

# class Man(Human):
#     pass

# class Woman(Human):
#     pass

# God()


# # 4. Classy Classes
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.info=f"{name}s age is {age}"


# 5. Building Spheres

# from math import pi
# class Sphere(object):

	
#     def __init__ (self, radius, mass):
#         self.radius = radius
#         self.mass = mass
        
#     def get_radius(self):
#         return self.radius
    
#     def get_mass(self):
#         return self.mass
    
#     def get_volume(self):
#         v = (4/3)*pi*(self.radius**3)
#         return round(v, 5)
    
#     def get_surface_area(self):
#         s = 4*pi*(self.radius**2)
#         return round(s, 5)
    
#     def get_density(self):
#         d = self.mass/self.get_volume()
#         return round (d, 5)
    

# 6. Python's Dynamic Classes #1

def class_name_changer(cls, new_name):
    if new_name.isalnum() and not new_name[0].isdigit() and not new_name[0].islower():
        cls.__name__ = new_name
    else:
        raise ValueError