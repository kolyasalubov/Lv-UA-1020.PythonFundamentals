"""
Create a class Human, everyone has a name, create a method in the
class that displays a welcome message to each person. Create a class method
in the class that returns information that it is a species of "Homosapiens". And
in the class create a static method that returns an arbitrary message.
"""

class Human:
    all_humans = 'Homosapiens'
    def method(self):
        print('Hello,',self)
    @classmethod
    def classmethod(cls):
        print('All humans is', cls.all_humans)
    @staticmethod
    def staticmethod():
        print('Hello Aliens!')

Human.method('Alex')
Human.classmethod()
Human.staticmethod()