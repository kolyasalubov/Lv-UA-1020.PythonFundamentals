# Task1. Write a function that returns the largest number of two
# numbers
# (use DocStrings documentation strings in the function).

def largest_number(*args):
    """args:  type -> tuple of numbers
    return max number"""
    return max(args)
print(largest_number(10,20))