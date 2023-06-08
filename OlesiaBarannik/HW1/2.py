# WRITE A PROGRAM THAT WILL CALCULATE THE SUM,
# DIFFERENCE, PRODUCT, EXPONENTIATION ETC. OF TWO NUMBERS A
# AND B THAT THE PROGRAM READS FROM THE CONSOLE (DATA ENTERED BY THE USER)
# AND WILL OUTPUT APPROPRIATE RESULT:
# "A + B = "  ...
# "A - B = "   ...
# "A * B = "   ...
# "A / B = "   ...
# "A**B = "   ...
# "A//B = "   ...
# "A%B = "  ...

print("Please enter first number:")
a = int(input())
print("Please enter second number:")
b = int(input())
print("Please choose function number: 1.+; 2.-; 3.*; 4./; 5.**; 6.//; 7.%")
c = int(input())


def calculate(a, b, c):
    result = False
    if c == 1:
        result = a + b
    if c == 2:
        result = a - b
    if c == 3:
        result = a * b
    if c == 4:
        result = a / b
    if c == 5:
        result = a ** b
    if c == 6:
        result = a // b
    if c == 7:
        result = a % b
    return result
print("Your result",calculate(a, b, c))

