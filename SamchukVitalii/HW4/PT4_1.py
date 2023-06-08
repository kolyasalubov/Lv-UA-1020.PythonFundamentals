
c = float(input('Enter the temperature in Celsius: '))
f = (c * 9/5) + 32
if c < -273.15:
    print("Error: Temperature below absolute zero (-273.15°C)") 
else:
    print (c,'°C is equivalent to ',f,'°F')


