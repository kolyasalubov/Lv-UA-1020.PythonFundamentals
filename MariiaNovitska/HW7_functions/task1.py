def largest (x1: int, x2: int):
    '''
    function takes two parameters as an integer
    return the largest one
    '''
    if x1==x2:
        return "Two numbers are equal"
    elif x1>x2:
        return f"{x1} the largest"
    else:
        return f"{x2} the largest"
    

print(largest(0,4))
print(largest(-6,-12))
print(largest(5,5))
print(largest.__doc__)