# Jenny's secret message 
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)

# Distance Between Two Points
import math
def distance(x1, y1, x2, y2):
    # Your code here
    return round(math.sqrt((x1 - x2)**2 + (y1 - y2)**2 ),2)

# Write a function taking in a string like "WOW this is REALLY          amazing" and returning Wow this is really amazing".
# String should be capitalized and properly spaced.

def filter_words(st):
    return " ".join(st.split()).capitalize()

# We need a function that can transform a number (integer) into a string.
# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"
def number_to_string(num):
    return str(num)

# You need to write a function that reverses the words in a given string
def reverse(st):
    return " ".join(st.strip().split()[::-1])

# In this kata you will create a function that takes in a list and returns a list with the reverse order.
def reverse_list(l):
    return l[::-1]

""" 
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
    Additionally, if the number is negative, return 0 (for languages that do have them).
    Note: If the number is a multiple of both 3 and 5, only count it once.
"""
def sum_of_multiples(number):
    return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])

""" 
    You were camping with your friends far away from home, but when it's time to go back, 
    you realize that your fuel is running out and the nearest pump is 50 miles away! 
    You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
    Considering these factors, write a function that tells you if it is possible to get to the pump or not.
    Function should return true if it is possible and false if not.
"""
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump <= mpg * fuel_left

""" 
    Create a function which answers the question "Are you playing banjo?".
    If your name starts with the letter "R" or lower case "r", you are playing banjo!
    The function takes a name as its only argument, and returns one of the following strings:
    name + " plays banjo"
    name + " does not play banjo"
"""
def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"

""" 
    Consider an array/list of sheep where some sheep may be missing from their place. 
    We need a function that counts the number of sheep present in the array (true means present).
    For example,

    [True,  True,  True,  False,
    True,  True,  True,  True ,
    True,  False, True,  False,
    True,  False, False, True ,
    True,  True,  True,  True ,
    False, False, True,  True]
    The correct answer would be 17.

    Hint: Don't forget to check for bad values like null/undefined
"""
def count_sheeps(sheep):
    return sheep.count(True)
    #return sum(sheep)

""" 
    Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails.
    To help her, you must correct the broken function to make sure that the second argument (tail),
    is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
    If the tail is right return true, else return false.
    The arguments will always be non empty strings, and normal letters.
"""
def correct_tail(body, tail):
    return body.endswith(tail)
    
