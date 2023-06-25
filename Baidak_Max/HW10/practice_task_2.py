class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Welcome {self.name}"

    @classmethod
    def specifies(cls):
        return "Homosapiens"

    @staticmethod
    def arb_message():
        return "This is an arbitrary message"

new_man = Human("Max")
print(new_man.welcome_message())

new_woman = Human("Alice")
print(new_woman.welcome_message())

print(Human.specifies())
print(Human.arb_message())