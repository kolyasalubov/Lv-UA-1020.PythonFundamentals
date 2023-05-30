# Task2. Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

user_number = int(input("Please enter a number to get its Fibonacci list\n"))
list_Fibonacci = [0,1]

def logic_of_Fibonacci (a, b):
    for i in range(user_number):
        result = a + b
        a = b
        b = result
        while result <= user_number:
            list_Fibonacci.append(result)
            break

if user_number == 0:
    print([list_Fibonacci[0]])
elif user_number < 2:
    list_Fibonacci.append(1)
    print(list_Fibonacci)
else:
    logic_of_Fibonacci(0, 1)
    print(list_Fibonacci)

