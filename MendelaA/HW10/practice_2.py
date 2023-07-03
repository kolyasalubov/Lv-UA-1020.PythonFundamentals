"""
Create a program that models a zoo. The program should have a base class Animal that stores the animal's name,
species, and number of legs. The class should have a method make_sound that returns a string indicating the sound
the animal makes. The make_sound method should be overriden in the subclasses to return a sound specific to each type
of animal.
Then, create three subclasses of Animal: Mammal, Bird, and Reptile. Each of these subclasses should inherit the name,
species, and number of legs from the Animal class.
For the Mammal class, add a method give_birth and return "Roar" for make_sound method.
For the Bird class, add a method lay_eggs and return "Squawk" for make_sound method.
For the Reptile class, add a method shed_skin and return "Hiss" for make_sound method.
"""


# animals = [Mammal("Lion", "Mammal", 4), Bird("Falcon", "Bird", 2), Reptile("Python", "Reptile", 4)]

# for animal in animals:
#     print(f"Animal: {animal.name}, Species: {animal.species}, Legs: {animal.legs}, Sound: {animal.make_sound()}")

# result
# Animal: Lion, Species: Mammal, Legs: 4, Sound: Roar
# Animal: Falcon, Species: Bird, Legs: 2, Sound: Squawk
# Animal: Python, Species: Reptile, Legs: 4, Sound: Hiss

class Animal():
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def make_sound(self):
        return f'Make sound'


class Mammal(Animal):
    def __init__(self, name, species, legs):
        super().__init__(name, species, legs)
        self.song = 'Roar'

    def give_birth(self):
        pass
    
    def make_sound(sef):
        return sef.song
    

class Bird(Animal):
    def __init__(self, name, species, legs):
        super().__init__(name, species, legs)

    def lay_eggs(self):
        pass

    def make_sound(sef):
        return f'Squawk'

class Reptile(Animal):
    def __init__(self, name, species, legs):
        super().__init__(name, species, legs)

    def shed_skin(self):
       pass

    def make_sound(sef):
        return f'Hiss'



animals = [Mammal("Lion", "Mammal", 4), Bird("Falcon", "Bird", 2), Reptile("Python", "Reptile", 4)]

for animal in animals:
    print(f"Animal: {animal.name}, Species: {animal.species}, Legs: {animal.legs}, Sound: {animal.make_sound()}")

print('#'*125)
mamal = (Mammal('Lion','Mammal', 4))
print(mamal.name)
print(mamal.species)
print(mamal.legs)
print(mamal.make_sound())