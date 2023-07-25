temperature_Celsius = float(input ("Введіть температуру в градусах Цельсія:"))
temperature_Fahrenheit = temperature_Celsius*9/5 + 32
if temperature_Celsius > - 273.15:
    print (f"{temperature_Celsius}°C еквівалентно {temperature_Fahrenheit}°F")
else:
    print ("Помилка: температура нижче абсолютного нуля (-273,15°C)") 