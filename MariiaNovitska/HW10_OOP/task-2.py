class Human():

    def __init__(self, name):
        self.name = name


    def say_hello(self):
        return f"Hello, {self.name}!"
    

    @classmethod
    def species(cls):
        return "Homosapience"
    

    @staticmethod
    def dance(kind_dance):
        return f"You can dance {kind_dance}!"
    

human_1 = Human("Solomia")
print(human_1.say_hello())
print(Human.species())
print(human_1.dance("rumba"))