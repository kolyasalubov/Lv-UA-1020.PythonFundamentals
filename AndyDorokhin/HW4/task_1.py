"""
    Temperature Converter
    Write a Python program that prompts the user to enter a temperature in Celsius and then
    converts it to Fahrenheit using the formula: F = (C * 9/5) + 32. Your program should then
    print out the converted temperature in Fahrenheit.
    However, if the user enters a temperature below -273.15°C (the lowest possible
    temperature in the universe, also known as absolute zero), your program should print an
    error message instead of attempting to convert the temperature.
    Note: You can assume that the user will enter a valid input (a number for the temperature in Celsius).
"""
def temp_converter():
    celsius = float(input("Enter a temperature in Celsius: "))
    if celsius >= -273.15:
        fahrenheit = (celsius * 9/5) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")
    else:
        print("The lowest possible temperature in the universe is -273.15°C. Try again.")
        
def main():
    temp_converter()
    
if __name__ == "__main__":
    main()       