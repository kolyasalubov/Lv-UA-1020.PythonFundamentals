"""
DESCRIPTION:
Color Ghost
Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
"""
import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white","yellow", "purple", "red"])
        
ghost1 = Ghost()
ghost2= Ghost()
ghost3 = Ghost()
ghost4 = Ghost()


print(ghost1.color, ghost2.color, ghost3.color, ghost4.color)
