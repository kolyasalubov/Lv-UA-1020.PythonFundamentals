number = int(input('Enter the number to calculate its factorial: '))
if number < 0:
    print("Неможливо порахувати факторіал")
elif number == 0 or number == 1:
    print(1)
else:
    factorial_value = 1
    for i in range(2, number + 1):
        factorial_value *= i
    print(factorial_value)
