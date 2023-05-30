n = int(input('Enter the end number of the Fibonacci numbers: '))
fibonacci_numbers = [0, 1]
for i in range(2, n):
    next_number = fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2]
    fibonacci_numbers.append(next_number)
print(fibonacci_numbers)
