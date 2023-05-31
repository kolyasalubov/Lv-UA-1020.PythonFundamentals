# Task2. Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

user_number = int(input("Please enter a number to get its Fibonacci list\n"))

def logic_of_Fibonacci (user_number):
    list_Fibonacci = [0, 1]
    if user_number == 0:
        return ([0])
    elif user_number < 2:
        list_Fibonacci.append(1)
        return list_Fibonacci
    previous_number, second_number = 0, 1
    for i in range(user_number):
        result = previous_number + second_number
        previous_number = second_number
        second_number = result
        while result <= user_number:
            list_Fibonacci.append(result)
            break
    return list_Fibonacci


print(logic_of_Fibonacci(user_number))


