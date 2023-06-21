class Employee:
    """
    Documentation for class Employee
    """
    counter = 0

    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def __del__(self):
        Employee.counter -= 1

    @classmethod
    def total_number(cls):
        return f'Total number of employees is {cls.counter}'

    def show_info(self):
        return f'Employee name {self.name} and salary is {self.salary}'


julia = Employee('Julia', 1500)
bill = Employee('Bill', 1000)
david = Employee('David', 2000)
ann = Employee('Ann', 1600)
print(Employee.total_number())
print(julia.show_info())
print(bill.show_info())

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
