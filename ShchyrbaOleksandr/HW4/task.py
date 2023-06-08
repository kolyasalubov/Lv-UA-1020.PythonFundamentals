user_temperature_celsius = int(input("Enter the temperature in Celsius: "))
temperature_fahrenheit = (user_temperature_celsius * 9/5) + 32
if user_temperature_celsius < -273.15:
    print("Error: Temperature below absolute zero(-273.15°C).")
else:
    print(user_temperature_celsius, "°C is equivalent to ", temperature_fahrenheit, "°F")
