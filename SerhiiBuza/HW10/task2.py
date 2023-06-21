class Human():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return (f"Hello!, {self.name} ")

    @classmethod
    def print_message(cls):
        return ("Species is Homosapiens")

    @staticmethod
    def arbitrary_mesage():
        return ("This Human is a SuperHero")


person1 = Human("Ivan")
print(person1.say_hello())
print(person1.arbitrary_mesage())
print(person1.print_message())
