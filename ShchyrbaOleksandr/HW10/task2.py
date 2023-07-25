class human():
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome():
        name = input("Enter your name: ")
        return f"Welcome, {name}!"
    
    @classmethod
    def class_method(cls):
        print(f"It is a species of {cls.species}.")

    @staticmethod
    def static_method():
        print("Arbitrary message.")
    
print(human.welcome())
human.class_method()
human.static_method()
