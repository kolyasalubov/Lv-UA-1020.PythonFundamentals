from task2_func import *

name = input("What is your name? ")
print(f"Hello {name}! \nThis program can calculate the area of rectandle (1), triangle (2), and circle (3)")
figure = input("Write a number of your figure (1 or 2 or 3): ")
print('This programm calculates area in square centimeters')

calculate(figure)

print("Thank you!")