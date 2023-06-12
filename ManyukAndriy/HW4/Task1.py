temperature = int(input("Enter the temperature in Celsius:"))
C = temperature
F = (C*9/5)+32

if C >= -273.15:
    print(f"{temperature}°C is equivalent to {F} °F")
else: print ("Error: Temperature below absolute zero (-273.15°C)")