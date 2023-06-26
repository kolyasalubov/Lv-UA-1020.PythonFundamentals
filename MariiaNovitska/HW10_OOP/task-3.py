class Employee():
    """
    This class is for employees. Every employee takes name as a str and salary as an int
    Olso you can see total number of employees using all_employees method
    """

    employees_total = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employees_total += 1


    @classmethod
    def all_employees(cls):
        return f"The number of all employees = {Employee.employees_total}"


    def information(self):
        return f"Employee {self.name}, salary: {self.salary}"
    

    def __del__(self):
        Employee.employees_total -= 1
        

sam = Employee("Samanta", 13000)
j = Employee("John", 12000)
print(Employee.__doc__)
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)

n = Employee("Nick", 14000)
print(Employee.all_employees())
print(sam.information())
sam.__del__()
print(Employee.all_employees())