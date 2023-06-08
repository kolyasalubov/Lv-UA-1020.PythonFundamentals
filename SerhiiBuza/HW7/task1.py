def check_number(num1, num2):
    """ This function get two number from input and check its.
    The result of wirk function is a largest bumber
    """
    if num1 > num2:
        return print(f"{num1} is a largest number")
    elif num2>num1:
        return print(f"{num2} is a largest number")
    else:
        return print(f"{num1} and{num2} is a similar number")

num1 =  int(input("Enter num1"))
num2 =  int(input("Enter num2"))
check_number(num1, num2)