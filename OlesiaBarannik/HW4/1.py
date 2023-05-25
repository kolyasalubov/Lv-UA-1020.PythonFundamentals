
t_Celsius = float(input("Please, Enter the temperature in degrees Celsius:\n"))

while True:
    if t_Celsius < -273.15:
        print("Error: Temperature below absolute zero (-273.15°C)")
        t_Celsius = float(input("Please, Enter the temperature in degrees Celsius:\n"))
    else:
        t_Fahrenheit = (t_Celsius * 9 / 5) + 32
        print(f'{t_Celsius}°C is equivalent to {t_Fahrenheit}°F')
        break



