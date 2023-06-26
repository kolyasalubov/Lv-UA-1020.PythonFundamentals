class Emploee:
    """
    Class Emploee contain information about salary of emplees
    """
    TOTAL_EMPLOEE = 0
    def __init__(self, name, salary = 0) -> None:
        self.name = name
        self.salary = salary
        Emploee.TOTAL_EMPLOEE+=1
    
    @classmethod
    def total_emploees(cls):
        print(f'Total emploee: {cls.TOTAL_EMPLOEE}')
    
    def emploee_info(self):
        print(f'The emploee {self.name} receives the salary of  {self.salary} $ ')

    def __del__(self):
        Emploee.TOTAL_EMPLOEE-=1


if __name__ == '__main__':
    empl1 = Emploee('Gala', 1000)
    empl2 = Emploee('Anya', 1050)
    empl3 = Emploee('Alex', 500)
    Emploee.total_emploees()
    empl3.emploee_info()
    empl2.emploee_info()
    empl1.emploee_info()

    print(Emploee.__base__)
    print(Emploee.__dict__)
    print(Emploee.__name__)
    print(Emploee.__module__)
    print(Emploee.__doc__)


    




