class Human():
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return "Hello, {}".format(self.name)
    
    @classmethod
    def name_species(cls):
        return "This is Homosapiens"
    
    @staticmethod
    def welcome():
        return "Welcome"
    

human1 = Human("Alex")

print(human1.greeting())
print(human1.welcome())
print(Human.name_species())