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
        This class represents an employee.
    """
    _counter = 0
    
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        print(f"Employee {self._name} is created")
        Employee._counter += 1
    
    def __del__(self):
        print(f"Employee {self._name} is deleted")
        Employee._counter -= 1
    
    def __str__(self):
        return f"Employee: {self._name}, salary: {self._salary}"
    
    def __repr__(self):
        return f"Employee({self._name}, {self._salary}), object at {hex(id(self))}"
    
    @classmethod
    def show_counter(cls):
        print(f"Total number of employees: {cls._counter}")
    
    def show_info(self):
        print(f"Employee: {self._name}, salary: {self._salary}")

def main():
    emp1 = Employee("Andy", 1000)
    emp2 = Employee("John", 2000)
    emp3 = Employee("Jack", 3000)
    emp4 = Employee("Jill", 4000)
    emp5 = Employee("Jane", 5000)
    Employee.show_counter()

    print(emp1)
    print(emp1.__repr__())
    emp1.show_info()

    print(emp1.__dict__)
    print(emp1.__class__)
    print(emp1.__class__.__base__)
    print(emp1.__class__.__name__)
    print(emp1.__class__.__module__)
    print(emp1.__class__.__doc__)

    del emp1
    del emp2
    del emp3
    del emp4
    del emp5
    Employee.show_counter()
    
if __name__ == "__main__":
    main()