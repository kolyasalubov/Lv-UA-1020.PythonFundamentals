# temperature programm
c_temp = float(input("Enter a temperature in Celsius:\n"))

if c_temp < -273.5:
    print("Error: Temperature below absolute zero (-273.15°C)")
else:
    f_temp = (c_temp * 9/5) + 32
    print(f"{c_temp}°C is equivalent to {round(f_temp, 2)}°F")


