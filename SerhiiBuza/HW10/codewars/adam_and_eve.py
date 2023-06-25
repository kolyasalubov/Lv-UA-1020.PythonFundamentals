"""
DESCRIPTION:
According to the creation myths of the Abrahamic religions, 
Adam and Eve were the first Humans to wander the Earth.

You have to do God's job. The creation method must return an array
 of length 2 containing objects (representing Adam and Eve). 
 The first object in the array should be an instance of the class Man. 
 The second should be an instance of the class Woman. 
 Both objects have to be subclasses of Human. Your job is to implement the Human, 
 Man and Woman classes.
"""


class Human():
    def __init__(self, human_obj):
        self.human_obj = human_obj


class Man(Human):
    def __init__(self, man_obj="Man"):
        self.man_obj = man_obj


class Woman (Human):
    def __init__(self, wooman_obj="Woman"):
        self.wooman_obj = wooman_obj


def god():
    return [Man(), Woman()]


print(god())


