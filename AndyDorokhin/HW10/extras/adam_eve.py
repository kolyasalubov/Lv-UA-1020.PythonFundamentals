""" 
    According to the creation myths of the Abrahamic religions, 
    Adam and Eve were the first Humans to wander the Earth.

    You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve). The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman. 
    Both objects have to be subclasses of Human. 
    Your job is to implement the Human, Man and Woman classes.
"""
class Human:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name

class Man(Human):
    def __init__(self, name = "Adam"):
        super().__init__(name)
        
class Woman(Human):
    def __init__(self, name = "Eve"):
        super().__init__(name)

def God():
    return [Man(), Woman()]

paradise = God()
print(paradise[0].name, type(paradise[0]))
print(paradise[1].name, type(paradise[1]))
