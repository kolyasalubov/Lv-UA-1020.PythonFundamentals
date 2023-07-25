#temp converter
temperature = int(input("Enter a temperature in Celsius:"))
def convert(temperature):
    return (temperature * 9 / 5) + 32
       
if temperature > -273.15 :
    print(f'{temperature} C is equivalent to {convert(temperature)} F')
else: 
    print('Temperature is below absolute zero(-273.15)')




