# Ball super ball
class Ball:
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


# Color ghost

import random


class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


# Basic subclasses - Adam and Eve
class Human:
    def __init__(self):
        pass


class Man(Human):
    def __init__(self):
        super().__init__()


class Woman(Human):
    def __init__(self):
        super().__init__()


def God():
    Adam = Man()
    Eve = Woman()
    return [Adam, Eve]


# Classy Classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"


# Building Spheres

import math


class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = round(((4 / 3) * math.pi * math.pow(self.radius, 3)), 5)
        return volume

    def get_surface_area(self):
        area = round((4 * math.pi * math.pow(self.radius, 2)), 5)
        return area

    def get_density(self):
        volume = round(((4 / 3) * math.pi * math.pow(self.radius, 3)), 5)
        density = round((self.mass / volume), 5)
        return density


# Python's Dynamic Classes #1
def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
        raise ValueError("Invalid class name")
    cls.__name__ = new_name

