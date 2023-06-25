
class Employee():
    """__Doc__"""
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def __del__(self):
        Employee.count -= 1

    def show_info(self):
        return (f"The name is {self.name} and The salary is {self.salary}")

    @classmethod
    def count_of_obj(self):
        return f"We have {Employee.count} employees"


person1 = Employee("Ivan", 3000)
person2 = Employee("Vova", 5000)

print(person1.show_info())
print(Employee.count_of_obj())
del person2
print(Employee.count_of_obj())


print( Employee.__base__)
print (Employee.__dict__)
print(Employee.__name__)
print (Employee.__module__)
print(Employee.__doc__)




