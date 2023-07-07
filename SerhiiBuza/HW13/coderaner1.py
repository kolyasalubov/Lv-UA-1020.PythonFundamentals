"""
Write a function celsius_to_fahrenheit(temps) using map function whose input parameter is a list of temperatures in Celsius. The function returns new array where temps in Farenheit.

Hint: F = (C * 9/5) + 32
"""
def celsius_to_fahrenheit(temps):
    temps_f = list((map(lambda c: (c*9/5)+32, temps)))
    return temps_f

celsius_temperatures = [0, 10, 20, 30, 40]
print (celsius_to_fahrenheit(celsius_temperatures))

    