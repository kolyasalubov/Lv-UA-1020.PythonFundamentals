class Employee:
    total_employees = 0  # Змінна класу, яка відстежує загальну кількість працівників

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_employee_info(self):
        print(f"Ім'я: {self.name}, Зарплата: {self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Загальна кількість працівників: {cls.total_employees}")

# Приклад використання класу Employee:
employee1 = Employee("Іван Іванов", 50000)
employee2 = Employee("Марія Петренко", 60000)

employee1.display_employee_info()
employee2.display_employee_info()

Employee.display_total_employees()

# Виведення інформації про клас
print("Базові класи:", Employee.__base__)
print("Простір імен класу:", Employee.__dict__)
print("Ім'я класу:", Employee.__name__)
print("Назва модуля, у якому оголошений клас:", Employee.__module__)
print("Документація:", Employee.__doc__)