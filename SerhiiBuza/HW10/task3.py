
class Employee():
    count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        count +=1

    def show_info(self):
        return (f"The name is {self.name} and The salary is {self.salary}")
    def count_of_obj(self):
        return f"We have {self.count} employees"


person1 = Employee ("Ivan", 3000)
print (person1.show_info())


