"""
    Task2. Create a class Human. Every human has a name. 
    Create an instance method in the class that displays a welcome message to each person. 
    Create a class method in the class that returns information that it is a species of "Homosapiens".
    Create a static method that returns an arbitrary message. 
"""
class Human():
    
    _species = "Homosapiens"
    
    def __init__(self, name):
        self._name = name
    
    def greeting(self):
        print(f"Hello, {self._name}!")
    
    @classmethod
    def species(cls):
        print(f"I am a {cls.__name__} of species {cls._species}")
    
    @staticmethod
    def message():
        print("Ти знаєш, що ти — людина.\nТи знаєш про це чи ні?")
        
def main():
    person = Human("Andy")
    print(person)
    print(person.__dict__)
    person.greeting()
    person.species()
    person.message()
    
if __name__ == "__main__":
    main()