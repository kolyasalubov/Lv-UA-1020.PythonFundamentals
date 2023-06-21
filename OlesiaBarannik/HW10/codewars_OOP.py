# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

# class Ball():
#     def __init__(self, ball_type = "regular"):
#         self.ball_type = ball_type
#
# ball1 = Ball()
# ball2 = Ball("super")
# print(ball1.ball_type)
# print(ball2.ball_type)

####################################################################################################
# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# # Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
# import random
# class Ghost():
#     x = ["white", "yellow", "purple", "red"]
#     def __init__(self):
#         self.color = random.choice(self.x)
#
# ghost = Ghost()
# print(ghost.color)
##################################################################################################
# You have to do God's job. The creation method must return an array of length 2 containing objects
# (representing Adam and Eve). The first object in the array should be an instance of the class Man.
# The second should be an instance of the class Woman. Both objects have to be subclasses of Human.
# Your job is to implement the Human, Man and Woman classes.

# class Human:
#     pass
# class Man(Human):
#     pass
# class Woman(Human):
#     pass
#
# def God():
#     Adam = Man()
#     Eve = Woman()
#     return [Adam, Eve]
##################################################################################################
# Your task is to complete this Class, the Person class has been created. You must fill in the Constructor
# method to accept a name as string and an age as number, complete the get
# Info property and getInfo method/Info getter which should return johns age is 34

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.info = f"{self.name}s age is {self.age}"
#
#     def info(self):
#         return self.info
#
# a1 = Person("John", 25)
# a1.get()
##################################################################################################
# Now that we have a Block let's move on to something slightly more complex: a Sphere.
# import math
# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#     def get_radius(self):
#         return self.radius
#     def get_mass(self):
#         return self.mass
#     def get_volume(self):
#         return round((4 * math.pi * self.radius**3)/3, 5)
#     def get_surface_area(self):
#         return round((4 * math.pi * self.radius**2), 5)
#     def get_density(self):
#         return round((self.mass/(4/3 * math.pi * self.radius**3)), 5)
#
# ball = Sphere(2,50)
# ball.get_radius()
# ball.get_mass()
# ball.get_volume()
# ball.get_surface_area()
# ball.get_density()
##################################################################################################