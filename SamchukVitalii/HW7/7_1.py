
def comparison(x,y):
    """
    Function returns the largest number of two numbers
    """
    if x > y:
        return x
    elif x < y:
        return y
    else: 
        return 'numbers are equal'
print(comparison(5,9)) 

#######################################

def maximal(a,b):
    """
    Function returns the max number of two numbers
    """
    return max(a,b)
print(maximal(10,20))