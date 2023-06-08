# Interchange the values of two variables without using the third variable

a, b = 11, 89
print(f'Variable "a" = {a} and variable "b" = {b}')

a, b = b, a
print(f'Now variable "a" = {a} and variable "b" = {b}')