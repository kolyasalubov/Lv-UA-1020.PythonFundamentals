class Employee:
    counter = 0
    employee_list = []
    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary
        Employee.employee_list.append({"name": self.name, "salary": self.salary})
    @classmethod
    def number_of_employees(cls):
        print(f"The total number of employees: {cls.counter}")

    @classmethod
    def displays(cls):
        for i in Employee.employee_list:
            print(i['name'], i['salary'])

    @classmethod
    def info_class(cls):
        print(Employee.__dict__)
        print(Employee.__name__)
        print(Employee.__module__)
        print(Employee.__base__)
        print(Employee.__doc__)

a1 = Employee("Olesia", 1500)
a2 = Employee("Samvel", 6500)
Employee.displays()
Employee.number_of_employees()
Employee.info_class()


