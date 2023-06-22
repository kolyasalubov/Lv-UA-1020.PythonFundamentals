
from my_func import *

def main(*args):
    args = str(input('rectangle -1''\n''triangle -2''\n''circle -3''\n''Your choise: '))
    if args == "1":
        a = float(input('enter a: '))
        b = float(input('enter b: '))
        print('area of a rectangle',rectangle(a,b))
    elif args == "2":
        print('area of a triangle')
        a = float(input('enter a: '))
        h = float(input('enter h: '))
        print('area of a triangle',triangle(a,h))
    elif args == "3":
        print('area of a circle')
        PI=3.14
        r = float(input('enter radius: '))
        print('area of a circle',circle(PI,r))
    else:
        print('wrong input')

if __name__ == "__main__":
    main()
