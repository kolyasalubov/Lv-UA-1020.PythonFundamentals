"""
Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"
"""
import random
class Ghost:
    __colors = ['white', "yellow", "purple", "red"]
    def __init__(self):
        self.__ghost_color = random.choice(self.__colors)


    @property
    def ghost_color(self):
        return self.__ghost_color

def main():
   # ghost_colors = ['white', "yellow", "purple", "red"]
    g1 = Ghost()
    g2 = Ghost()

    print(g1.ghost_color)
    print(g2.ghost_color)

if __name__ == "__main__":
    main()