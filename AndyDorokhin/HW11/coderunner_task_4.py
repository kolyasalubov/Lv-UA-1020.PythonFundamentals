""" 
    Write the function check_odd_even (number) whose input parameter is an integer number.
    The function checks whether the set number is even or odd:

    in the case of an even number the function should be displayed the corresponding message - "Entered number is even";
    in the case of an odd number the function should be displayed the corresponding message - "Entered number is odd";
    in the case of incorrect data the function should be displayed the message - "You entered not a number."
    Note: in the function you must use the try except construct.
"""

def check_odd_even(number):
    try:
        if number % 2 == 0:
            return ("Entered number is even")
        else:
            return ("Entered number is odd")
    except TypeError:
        return ("You entered not a number.")
    
print(check_odd_even(15))
print(check_odd_even(36))
print(check_odd_even('111'))
