class Human:
    species = 'Homosapiens'

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello,", self.name)

    @classmethod
    def class_method(cls):
        print('It is a species of', cls.species)

    @staticmethod
    def static_method():
        print('Hello, world!')


pers1 = Human("Julia")
pers1.say_hello()
pers1.class_method()
pers1.static_method()
