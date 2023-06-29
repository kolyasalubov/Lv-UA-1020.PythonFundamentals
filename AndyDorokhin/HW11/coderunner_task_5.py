""" 
    Write the function check_positive(number)whose input parameter is a number. 
    The function checks whether the set number is positive or negative:

    in the case of a positive number the function should be displayed the corresponding message - "You input positive number: {number}"
    in the case of a negative parameter the function should return the exception of your own class MyError 
    and displayed the corresponding message. "You input negative number: {number}. Try again."
    in the case of incorrect data the function should be displayed the message - "Error type: ValueError!"
"""

class MyError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return self.data
    
def check_positive(number):
    try:
        if float(number) >= 0:
            return (f"You input positive number: {float(number):0.1f}")
        else:
            return MyError(f"You input negative number: {float(number):0.1f}. Try again.")
    except Exception as e:
        return MyError(f"Error type: ValueError!")

print(check_positive(8.9))
print(check_positive(-19))
print(check_positive("abs"))
print(isinstance(check_positive("-235"), MyError))

        
    