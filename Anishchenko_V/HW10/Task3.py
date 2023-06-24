import gc


class Employee:
    """
    Class is called 'Employee'.
    Creates an object with the name and salary
    of the employee.
    """

    counter = 0

    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    @classmethod
    def totalEmployees(cls):
        print(f'Total number of employees is {cls.counter}')

    @classmethod
    def eachEmployeesDetails(cls):
        print('Employees\' details:')
        for ob in gc.get_objects():
            if isinstance(ob, cls):
                print(f'    Name - {ob.name}, salary - {ob.salary}')

    def particularEmployeDetails(self):
        print(f'Employees name: {self.name}')
        print(f'Employees salary: {self.salary}')


print(Employee.__base__)
print('=' * 25)

print(Employee.__dict__)
print('=' * 25)

print(Employee.__name__)
print('=' * 25)

print(Employee.__module__)
print('=' * 25)

print(Employee.__doc__)
