"""
        Create a function that takes a string, checks if it has the same number of "x"s and "o"s and returns either True or False.

        Return a boolean value (True or False).
        Return True if the amount of x's and o's are the same.
        Return False if they aren't the same amount.
        The string can contain any character.
        When "x" and "o" are not in the string, return True.
"""
def X_O(word):
    
    return word.lower().count('x') == word.lower().count('o')

"""
        Create a function that takes a string and returns it as a positive integer.
        In that case when the string cannot be converted to a positive integer, returns the string "Not a number"
"""
def string_int(str1):
    if str1.isdigit():
        return int(str1)
    else:
        return "Not a number"

"""
        Write a function that stutters a word as if someone is struggling to read it.
        The first two letters are repeated twice with an ellipsis ... , and then the word is pronounced with a question mark ?.
        If the input is less than two characters long, the function returns "oh...".
"""
def stutter(word):
    if len(word) < 2:
        return "oh..."
    else:
        return word[:2] + "..." + word[:2] + "..." + word + "?"

"""
        Create a function that returns True if an integer is evenly divisible by 5, and False otherwise.
"""
def divisible_by_five(number):
    
    return not (number % 5)

"""
        Create a function that takes a number as an argument and returns negative of that number. 
        Return negative numbers without any change.
"""
def return_negative(number):
        
    return (-number if number > 0 else number)