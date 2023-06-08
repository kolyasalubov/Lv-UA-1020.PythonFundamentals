n = int(input('Enter the end number of the Fibonacci numbers: '))
if n == 0:
    print('fibonacci_numbers = []')
elif n == 1:
    print('fibonacci_numbers = [0]')
else:
    fibonacci_numbers = [0, 1]
    for i in range(2, n):
        next_number = fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]
        fibonacci_numbers.append(next_number)
    print(f'fibonacci_numbers = {fibonacci_numbers}')
