factorial = input('Input factoria n! ')
factorial = int(factorial.split('!')[0])

x = 1

for n in range(2, factorial + 1):
    x *= n

print(f'Factotial of {factorial}! is {x}')

