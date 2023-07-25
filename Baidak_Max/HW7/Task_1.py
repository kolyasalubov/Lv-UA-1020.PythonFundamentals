## Task1
## Write a function that returns the largest number of two numbers
## (use DocStrings documentation strings in the function).

number1 = float(input("Enter the fisrt number: "))
number2 = float(input("Enter the second number: "))
def lagest_number(num1, num2):
    """
    Function that returns the largest number of two numbers.
    Parameters:
    num1 (int or float): The first number.
    num2 (int or float): The second number.
    Returns:
    int or float: The largest number between num1 and num2.
    """
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Two numbers are equal"
print("The largest number of two numbers: ", lagest_number(number1, number2))


def lager_num(num1, num2):
    """
    Function that returns the largest number of two numbers.
    Parameters:
    num1 (int or float): The first number.
    num2 (int or float): The second number.
    Returns:
    int or float: The largest number between num1 and num2.
    """
    number = max(num1, num2)
    return number


print(f"The largest number of two numbers: {lager_num(number1, number2)}")