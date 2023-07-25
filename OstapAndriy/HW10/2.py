class Human:
    species = "Homosapiens"  # Атрибут класу

    def __init__(self, name):
        self.name = name  # Атрибут екземпляра

    def display_welcome_message(self):
        print(f"Привіт, мене звати {self.name}. Ласкаво просимо!")

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def arbitrary_message():
        return "Це статичний метод. Його можна викликати без створення екземпляра."


# приклад використання класу Human:
name = input(r"Ваше ім'я: ")
person1 = Human(name)
person1.display_welcome_message()

print("Вид:", Human.get_species())

print(Human.arbitrary_message()) 
