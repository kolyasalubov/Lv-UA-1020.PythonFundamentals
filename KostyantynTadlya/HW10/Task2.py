class Human:
    def __init__(self, name) -> None:
        self.name = name
    def wellcoming(self):
        return print('Hi ' + self.name + '! Welcome to Human class!')
    @classmethod
    def classmethod(cls):
        return print('This is Homosapiens species')
    
    @staticmethod
    def staticmethod():
        return print('Static method')

if __name__ == '__main__':
    h = Human('Vasia')
    h.wellcoming()
    Human.classmethod()
    Human.staticmethod()
    

