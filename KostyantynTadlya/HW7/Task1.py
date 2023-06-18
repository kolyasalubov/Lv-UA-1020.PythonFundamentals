def max_from_two(a :int, b :int)-> int:
    """
    max_from_two is function that return the of two numbers
    """
    return a if a > b else b

if __name__ == '__main__':
    a = input('Enter first number for comparison a =')
    b = input('Enter second number for comparison b =')
    print(f"The {max_from_two(a ,b)} is max number")