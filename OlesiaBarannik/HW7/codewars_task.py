# Jenny has written a function that returns a greeting for a user.
# However, she's in love with Johnny, and would like to greet him slightly different. '
#'She added a special case to her function, but she made a mistake.
# Can you help her?

# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     return "Hello, {name}!".format(name=name)

########################################################################################
# Given two ordered pairs calculate the distance between them.
# Round to two decimal places. This should be easy to do in 0(1) timing.

# import math
# def distance(x1, y1, x2, y2):
#     ab = round(math.sqrt(((x2 - x1)**2 + (y2 - y1)**2)),2)
#     return ab
# print(distance(1, 1, 0, 0))
########################################################################################
# Write a function taking in a string like WOW this is REALLY          amazing
# and returning Wow this is really amazing. String should be capitalized and properly spaced.
# Using re and string is not allowed.

# def filter_words(st):
#     return " ".join(st.capitalize().split())
# print(filter_words("dsdsds OOOgF        asTT"))
########################################################################################
# We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?

# def number_to_string(num):
#     return str(num)
# print(number_to_string(10))
########################################################################################
# You need to write a function that reverses the words in a given string.
# A word can also fit an empty string. If this is not clear enough, here are some examples:
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

# def reverse(st):
#         return " ".join(st.split()[::-1])
# print(reverse("Hello   Olesia Samvel"))
########################################################################################
# In this kata you will create a function that takes in a list and returns a list with the reverse order.

# def reverse_list(l):
#     """return a list with the reverse order of l"""
#     return l[::-1]
# print(reverse_list([1,2,3,4]))

########################################################################################
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0 (for languages that do have them).
# Note: If the number is a multiple of both 3 and 5, only count it once.

# def solution(number):
#     result = 0
#     for i in range(1, number):
#         if i < 0:
#             result = 0
#         elif i % 3 == 0 or i % 5 == 0:
#             result += i
#     return result
#
# print(solution(20))

########################################################################################

#You were camping with your friends far away from home, but when it's time to go back,
# you realize that your fuel is running out and the nearest pump is 50 miles away!
# You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
# Function should return true if it is possible and false if not.

# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if distance_to_pump/mpg <= fuel_left:
#         return True
#     return False
# print(zero_fuel(50, 25, 2))

########################################################################################
#Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:

# def are_you_playing_banjo(name):
#     if name[0].upper() == "R":
#         return f'{name} plays banjo'
#     return f'{name} does not play banjo'
# print(are_you_playing_banjo("robbi"))

########################################################################################
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false

# def bool_to_word(boolean):
#     if boolean == True:
#         return "Yes"
#     return "No"
# print(bool_to_word(False))

########################################################################################
#Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts
# the number of sheep present in the array (true means present).

# def count_sheeps(sheep):
#     result = 0
#     for i in sheep:
#         if i == True:
#             result += i
#     return result
#
# print(count_sheeps([True,  True,  True,  False]))

########################################################################################
#Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails.
# To help her, you must correct the broken function to make sure that the second argument (tail),
# is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!
# If the tail is right return true, else return false.
# The arguments will always be non empty strings, and normal letters.

# def correct_tail(body, tail):
#     if body[-1] == tail:
#         return True
#     return False
# print(correct_tail("body", "y"))
