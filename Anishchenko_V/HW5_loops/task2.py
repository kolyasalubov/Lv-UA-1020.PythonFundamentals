user_number = int(
    input('Enter natural number (i.e. whole number that is greater than 0): '))

fibon_list = [0, 1]

while user_number >= fibon_list[-1] + fibon_list[-2]:
    if user_number == 1:
        break
    fibon_list.append(fibon_list[-1] + fibon_list[-2])

print(
    f'List of Fibonacci numbers up to your number ({user_number}) is:\n{fibon_list}')
