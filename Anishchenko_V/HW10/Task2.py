class Human:
    """
    This is class Human
    """

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hello {self.name}')

    def specie(self):
        self.spec = 'Homosapiens'
        return self.spec

    @classmethod
    def classmethod(cls):
        return f'This is class method of {cls}'
