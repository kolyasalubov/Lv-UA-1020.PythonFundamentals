import math
def rectangle():
    '''This function returns
    rectangle area'''

    a = float(input("Вкажіть довжину першої сторони: "))
    b = float(input("Вкажіть довжину другої сторони: "))
    print(a*b)


def triangle():
    '''This function returns
    triangle area'''
    a = float(input("Вкажіть довжину першої сторони: "))
    b = float(input("Вкажіть висоту трикутника: "))
    print(0.5*a*b)
def circle():
    '''This function returns
    circle area'''
    a = float(input("Вкажіть радіус кола: "))
    print (math.pi * a**2)