
t_Celsius = (input("Please, Enter the temperature in degrees Celsius:\n"))


def check_number(t_Celsius): # фунція, що перевіряє чи отримана строка число враховуючи ".","-" та str
        if t_Celsius.isdigit():
            return True
        if t_Celsius[0] == '-' and t_Celsius[1:].isdigit():
            return True
        if t_Celsius.count('.') == 1: # ділення строки на праву parts[1] і ліву parts[0] частину від крапки і перевіряє чи число
            parts = t_Celsius.split('.') # при цьому допускає [0] = "-"
            if (parts[0].isdigit() or (parts[0][0] == '-' and parts[0][1:].isdigit())) and parts[1].isdigit():
                return True
        return False


while True:
    if check_number(t_Celsius) is False:
        print("Your temperature should contain only numeric")
        t_Celsius = (input("Please, Enter the temperature in degrees Celsius:\n"))
    if float(t_Celsius) < -273.15:
        print("Error: Temperature below absolute zero (-273.15°C)")
        t_Celsius = (input("Please, Enter the temperature in degrees Celsius:\n"))
    else:
        t_Fahrenheit = (float(t_Celsius) * 9 / 5) + 32
        print(f'{t_Celsius}°C is equivalent to {t_Fahrenheit}°F')
        break

