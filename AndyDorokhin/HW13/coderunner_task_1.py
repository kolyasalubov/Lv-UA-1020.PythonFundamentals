""" 
    Write a function celsius_to_fahrenheit(temps) using map function whose input parameter is a list of temperatures in Celsius.
    The function returns list where temps in Farenheit. 
    Hint: F = (C * 9/5) + 32

"""
def celsius_to_fahrenheit(temps):
    return list(map(lambda x: (x * 9/5) + 32, temps))

def main():
    celsius_temperatures = [0, 10, 20, 30, 40]
    print(celsius_to_fahrenheit(celsius_temperatures))
    celsius_temperatures = [-40, -30, -20, -10, 0]
    print(celsius_to_fahrenheit(celsius_temperatures))
    
if __name__ == "__main__":
    main()