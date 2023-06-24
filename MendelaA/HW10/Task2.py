from random import choice

class Human():

    @staticmethod
    def arb_msg():
        return choice(['msg1','msg2','msg3'])
    
    def __init__(self, name):
        self.name = name

    def message(self):
        return f'Welcome {self.name}'
    
    def information(self):
        return f'Homosapiens'


        

joe = Human('Joe')
print(joe.message())
print(joe.information())
print(joe.arb_msg())


