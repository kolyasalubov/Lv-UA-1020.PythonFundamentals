# Write a script that will calculate the factorial of the entered number without using recursion
def factorial_number(user_number):
    i = 0
    result = 1
    if user_number == 0:
        return 1
    else:
        while i < user_number:
            i += 1
            result *= i
    return result
print(factorial_number(3))
