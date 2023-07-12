
def return_the_largest_num (num1, num2):
    """ 
    Function 'return_the_largest_num' takes 2 numbers, chooses the largest one by using max() method and returns it
    """
    the_largest_one = max(num1, num2)
    return the_largest_one
print(return_the_largest_num())

###

def return_the_largest_num (num1, num2):
    """ 
    Function 'return_the_largest_num' takes 2 numbers, compares them and returns the largest one
    """
    if num1 > num2:
        return num1
    return num2
print(return_the_largest_num())