#WRITE A PROGRAM THAT WILL CALCULATE THE SUM, DIFFERENCE, PRODUCT, EXPONENTIATION ETC. OF TWO NUMBERS A AND B THAT THE PROGRAM READS FROM THE CONSOLE (DATA ENTERED BY THE USER) AND WILL OUTPUT APPROPRIATE RESULT:
#"A + B = "  ...
#"A - B = "   ...
#"A * B = "   ...
#"A / B = "   ...
#"A**B = "   ...
#"A//B = "   ...
#"A%B = "  ...



a = int(input("Input value a (only number) \n"))
b = int(input("Input value b (only number) \n"))

print(f""" 
a + b = {a + b}
a - b = {a - b}
a * b = {a * b}
a / b = {a / b}
a**b = {a ** b}
a // b = {a // b}
a % b = {a % b}""")