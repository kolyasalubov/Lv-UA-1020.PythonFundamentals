""" 
    Write a list comprehension function celsius_to_fahrenheit(temps) whose input parameter
    is a list of temperatures in Celsius. 
    The function returns new array where temps in Farenheit.
    Hint: F = (C * 9/5) + 32
"""
def celsius_to_fahrenheit(temps):
    return [(x * 9/5) + 32 for x in temps]

