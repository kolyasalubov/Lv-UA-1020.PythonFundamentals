def largest_num (num1, num2):
    '''
    Function return the max number.
    '''
    if num1 > num2:
        return num1
    else:
        return num2

print(largest_num(14, -1))


def largest_num (num1, num2):
    '''
    Function return the max number.
    '''
    return max(num1, num2)

print(largest_num(3, 4))


def largest_num (*numbers):
    '''
    Function return the max number.
    '''
    return max(*numbers)

print(largest_num(4,999, 3, 4, 5))

