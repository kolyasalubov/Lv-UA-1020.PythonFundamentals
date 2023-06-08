temperature_in_c = float(input('Enter temperature in C '))
ABSOLUTE_ZERO = -273.15

if temperature_in_c >= ABSOLUTE_ZERO:
    f = (temperature_in_c * (9/5) + 32)
    print(f'{temperature_in_c}°C is equivalent to {int(f)}°F')
else:
    print(f'Temperature below absolute zero {ABSOLUTE_ZERO}°C')
