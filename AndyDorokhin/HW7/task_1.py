""" 
    Task1. Write a function that returns the largest number of two numbers.
    Use DocStrings documentation strings in the function.
"""
def largest_number(a, b):
    """
    Returns the largest number of two numbers.

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: the largest number of two numbers
    """
    if a > b:
        return a
    else:
        return b
    
print(largest_number(5, 10))
print(largest_number(5, -10))
print(largest_number(5, 5))
print(largest_number.__doc__)