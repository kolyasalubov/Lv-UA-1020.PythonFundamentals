cels_temp = float(input("Enter the temperature in Celsius: "))
abs_zero = -273.15

if cels_temp > abs_zero:
    far_temp = (cels_temp * 9/5) + 32
    print(f'{cels_temp}°C is equivalent to {far_temp:.2f}°F')
else:
    print(f'Error: Temperature below absolute zero ({abs_zero}°C)')
