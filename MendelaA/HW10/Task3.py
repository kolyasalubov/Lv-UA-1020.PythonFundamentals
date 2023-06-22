"""
Create an employee class. Each employee has characteristics such as name
and salary. The class should have a counter that calculates the total number of
employees, as well as a method that prints the total number of employees and a
method that displays information about each employee in particular, namely the
name and salary.

In addition to creating a class, display information about the base classes from which
the employee class is inherited (__base__), the class namespace (__dict__), the
class name (__name__), the module name in which the class is defined
(__module__), the documentation bar ( __doc__)
"""

class Employee():
    """
    Some very intresting doc !
    """
    total_employees = 0
    def __init__(self, name, salary):
        Employee.total_employees += 1
        self.name = name
        self.salary = salary

    def __del__(self):
        Employee.total_employees -= 1

    def number_of_employees(self):
        return f'Total employee is {self.total_employees}'

    def informations(self):
        return f'Employee {self.name}, sallary is {self.salary}'

 
# emp1 = Employee('Joe', 1000)
# print(emp1.informations())

# emp2 = Employee('Bil', 2000)
# emp3 = Employee('Jon', 17000)

# print(Employee.number_of_employees(Employee))
# print(emp1.number_of_employees())

# print(Employee.__base__)
# print(Employee.__dict__)
# print(Employee.__name__)
# print(Employee.__module__)
# print(Employee.__doc__)
