class Human:
    """
    This is class Human
    """

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hello {self.name}')

    @classmethod
    def say_species(cls):
        return f'Class {cls.__name__} is a species of "Homosapiens"'

    @staticmethod
    def arbitrary():
        return 'This is an arbitrary message'
