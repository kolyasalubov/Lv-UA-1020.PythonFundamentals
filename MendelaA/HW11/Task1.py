"""
Write a program that prompts the user to enter an integer and determines whether
the number is even or odd, taking into account the case of entering incorrect data.
"""

# try:
#     num = int(input('Enter the number '))
#     if num % 2 != 0:
#         raise SyntaxError 
# except:
#     print('Num is not odd')
# else:
#     print('Num is odd')

def odd_num(num):
    try:
        if num % 2 != 0:
            raise Exception
    except Exception:
        return f'{num} is not odd'
    else:
        return f'{num} is odd'
    
assert odd_num(5) == '5 is not odd'
assert odd_num(6) == '6 is odd'