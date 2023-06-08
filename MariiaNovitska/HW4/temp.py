temperature = int(input("Enter the temperature in Celsius: "))

if -273.15 < temperature:
    fahrenheit = round(((temperature*9/5) + 32), 1)
    print(f"{temperature}°C is equivalent to {fahrenheit}°F")
else:
    print("Temperature below absolute zero (-273.15°C). You should to write higher temperature.")
