class Human():
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def print_message(self):
        return(f"Hello {self.name}")
    def print_mesage_of_species (self):
         return (f"{self.name} is species {self.species}")
    @staticmethod
    def arbitrary_mesage():
        return ("This Human is a SuperHero")

person1 = Human("Artur", "Homosapiens")
print (person1.print_message())
print(person1.print_mesage_of_species())
print(person1.arbitrary_mesage())
