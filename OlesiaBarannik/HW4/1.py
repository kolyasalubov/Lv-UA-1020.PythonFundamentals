
t_Celsius = (input("Please, Enter the temperature in degrees Celsius:\n"))


def check_number(t_Celsius):
        if t_Celsius.isdigit():
            return True
        if t_Celsius[0] == '-' and t_Celsius[1:].isdigit():
            return True
        if t_Celsius.count('.') == 1:
            return True
        else:
            print("Your temperature should contain only numeric")
            return False


while True:
    if check_number(t_Celsius) is False:
        t_Celsius = (input("Please, Enter the temperature in degrees Celsius:\n"))
    if float(t_Celsius) < -273.15:
        print("Error: Temperature below absolute zero (-273.15°C)")
        t_Celsius = (input("Please, Enter the temperature in degrees Celsius:\n"))
    else:
        t_Fahrenheit = (float(t_Celsius) * 9 / 5) + 32
        print(f'{t_Celsius}°C is equivalent to {t_Fahrenheit}°F')
        break
