""" 
    Create a class Ghost
    Ghost objects are instantiated without any arguments.
    Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
    Examples:
    ghost = Ghost()
    ghost.color  #=> "white" or "yellow" or "purple" or "red"
"""
import random

class Ghost:
    
    __colors = ["white", "yellow", "purple", "red"]
    
    def __init__(self):
        self.__color = random.choice(self.__colors)
    
    @property
    def color(self):
        return self.__color
    
def main():
    ghost1 = Ghost()
    print(ghost1.color)
    ghost2 = Ghost()
    print(ghost2.color)

if __name__ == "__main__":
    main()

    
    
    