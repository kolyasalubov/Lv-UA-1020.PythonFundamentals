"""
    WRITE A PROGRAM THAT WILL CALCULATE THE SUM, DIFFERENCE, PRODUCT, EXPONENTIATION ETC. OF TWO NUMBERS A AND B THAT THE PROGRAM READS FROM THE CONSOLE (DATA ENTERED BY THE USER) AND WILL OUTPUT APPROPRIATE RESULT:
    "A + B = "  ...
    "A - B = "   ...
    "A * B = "   ...
    "A / B = "   ...
    "A**B = "   ...
    "A//B = "   ...
    "A%B = "  ...
"""
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} ** {b} = {a ** b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")