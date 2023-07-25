class Employees:
    numberOfWorkers = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employees.numberOfWorkers += 1
    
    def total_num_emp(self):
        print(f"Total number of employees: {Employees.numberOfWorkers}\n")

    def display_information(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}\n")

person1 = Employees("Bob", 15000)
person2 = Employees("Jack", 20000)
person3 = Employees("Rick", 43000)

Employees.total_num_emp(None)

person1.display_information()
person2.display_information()
person3.display_information()

print(f"\nБазові класи: {Employees.__bases__}")
print(f"Простір імен класу: {Employees.__dict__}")
print(f"Ім'я класу: {Employees.__name__}")
print(f"Ім'я модуля: {Employees.__module__}")
print(f"Документаційна панель: {Employees.__doc__}")
