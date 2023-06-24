class Employee:
    counter = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    def __del__(self):
        Employee.counter -= 1

    @classmethod
    def summary_employees(cls):
        return f"The total numbers of employees: {cls.counter}"

    def sum_of_employees(self):
        return f"The total numbers of employees: {Employee.counter}"


    def each_employee(self):
        return f"The name of employee is {self.name}, salary: {self.salary}"


first_emp = Employee("Max", 200)
second_emp = Employee("Tom", 250)
third_emp = Employee("Ann", 300)

print(Employee.summary_employees())
print(third_emp.sum_of_employees())

print( first_emp.each_employee())
print(second_emp.each_employee())
print(third_emp.each_employee())


print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)

