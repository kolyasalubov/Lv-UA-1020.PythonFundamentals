"""
Task3. Create an employee class. Each employee has characteristics such as name
and salary. The class should have a counter that calculates the total number of
employees, as well as a method that prints the total number of employees and a
method that displays information about each employee in particular, namely the
name and salary.
In addition to creating a class, display information about the base classes from which
the employee class is inherited (__base__), the class namespace (__dict__), the
class name (__name__), the module name in which the class is defined
(__module__), the documentation bar ( __doc__)
"""


class Employee:
    """
    Documentation for Employee
    """
    counter = 0
    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    @classmethod
    def total(cls):
        return f'Total number of employees {cls.counter}'

    def show_info(self):
        return f'Employe name {self.name} and salary is {self.salary}'
    
    
bob = Employee('Bob', 3000)
den = Employee('Den', 1800)
sam = Employee('Sam', 1500)
print(Employee.total())
print(bob.show_info())
print(sam.show_info())

# print(Employee.__base__)
# print(Employee.__dict__)
# print(Employee.__name__)
# print(Employee.__module__)
# print(Employee.__doc__)