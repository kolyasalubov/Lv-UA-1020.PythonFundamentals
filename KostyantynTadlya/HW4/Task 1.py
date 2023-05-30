Celsius = float(input('Input the temperature in Celsius:'))

if Celsius<-273.15:
    print('Temperature below absolute zero %f' %Celsius, chr(176), 'C', sep='')
else:
    print(f"{Celsius}", chr(176), f"C is equivalent to {Celsius*9/5+32}", chr(176), "F", sep='')
