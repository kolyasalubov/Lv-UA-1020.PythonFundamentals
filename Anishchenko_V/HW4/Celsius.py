while True:    
    user_input = input('Enter the temperature in Celsius: ')
    try:
        celsius = float(user_input)
        break
    except:
        print('Error: Enter integer or decimal value: ')

if celsius < -273.15:
    print('Error: Temperature below absolute zero (-273.15°C)')
else:
    fahrenheit = celsius * 9 / 5 + 32
    print('{0:.1f}°C is equivalent to {1:.1f} °F'.format(celsius, fahrenheit))