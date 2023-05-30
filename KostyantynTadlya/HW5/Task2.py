limit_number = int(input('Input the number'))

if limit_number<1:
    print('There is no Fibonacci series for this number', limit_number)
else:
    fibonacci=[0, 1]
    for i in range(2,limit_number):
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    print(fibonacci)
