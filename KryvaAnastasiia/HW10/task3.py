class Employee():
    """This class creates objects with attributes: name and salary"""
    counter = 0
    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def emp_information(self):
        return "{} has salary {}".format(self.name, self.salary)
    
    @classmethod
    def number_of_employee(cls):
        return Employee.counter
    


employee1  = Employee("Alex", 1000)
employee2 = Employee("Robert", 2000)


print(employee1.emp_information())

print(Employee.number_of_employee())

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)

    

