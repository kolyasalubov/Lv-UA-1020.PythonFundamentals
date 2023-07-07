"""
Write a list comprehension function celsius_to_fahrenheit(temps)
 whose input parameter is a list of 
temperatures in Celsius. The function returns new array where temps in Farenheit.
"""


def celsius_to_fahrenheit(temps):
    temps_f = [(t*9/5)+32 for t in temps]
    return temps_f


celsius_temperatures = [0, 10, 20, 30, 40]
print(celsius_to_fahrenheit(celsius_temperatures))