class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Hello {self.name}"
    @classmethod
    def species(cls, name):
        return f"Homosapiens {name}"

    @staticmethod
    def arbitrary_message():
        return "Wow"

a1 = Human("Olesia")

print(a1.welcome_message())
print(Human.species("Samvel"))
print(a1.arbitrary_message())