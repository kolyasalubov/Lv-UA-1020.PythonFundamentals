# Interchange the values of two variables without using the third variable.

a = 10
b = 12
print("Before: ", "a:", a, "b:", b)

a, b = b, a
print("After: ", "a:", a, "b:", b)