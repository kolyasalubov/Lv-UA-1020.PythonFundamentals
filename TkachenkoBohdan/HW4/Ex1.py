celcius_temperature = float(input("Which temperature now?"))
print(celcius_temperature)
if(celcius_temperature >=-273.15):
    farenheit_temperature = (celcius_temperature*9/5+32)
    print(f"Celcius temperature {celcius_temperature} is {farenheit_temperature} on Farenheit temperature")
else:
    print("Error! You need to write temperature more than 273,15!")