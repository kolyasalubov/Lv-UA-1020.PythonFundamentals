"""
Write a program that calculates the area of a rectangle,
triangle and circle
(write three functions to calculate the area, and call them in the
main program depending on the user's choice)
"""

def rectangle(a,b):
    return a*b

def triangle(a,h):
    return ((a*h)/2)

def circle(PI,r):
    
    return (PI*r**2)

def calculation(*args):
    args = str(input('rectangle -1 / triangle -2 / circle -3  Your choise: '))
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

calculation()
