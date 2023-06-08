user_number = int(input('Enter a whole number: '))

factorial = 1

if user_number > 1:
    for i in range(2, user_number + 1):
        factorial *= i

print(f'{user_number}! = {factorial}.')
