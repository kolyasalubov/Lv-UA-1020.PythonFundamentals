try:
    a = float(input('Enter the value a ='))
    b = float(input('Enter the value b ='))
except:
    print('Something is wrong')
else:
    print('a + b =', a+b)
    print('a - b =', a-b)
    print('a*b =', a*b)
    print('a/b =', a/b)
    print('a**b =', a**b)
    print('a//b =', a//b)
    print('a%b =', a%b)