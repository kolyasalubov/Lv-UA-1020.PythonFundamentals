"""
    Create a function that returns the mean of all digits.
    The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=3).
    The mean will always be an integer.
"""
def mean(number):
    sum = 0
    for i in str(number):
        sum += int(i)
        
    return round(sum / len(str(number)))

""" 
    Create a function which returns a list of booleans, from a given number. 
    Iterating through the number one digit at a time, append True if the digit is 1 and False if it is 0.
    Notes. Expect numbers with 0 and 1 only.
"""
def integer_boolean(binary_number):
    return [True if i == "1" else False for i in str(binary_number)]

"""
    Create a function that takes a string and returns the number (count) of vowels contained within it.
    Notes - a, e, i, o, u are considered vowels (not y).
    All test cases are one word and only contain letters.
"""
def count_vowels(word):
    count_vowels = 0
    for letter in word.lower():
        if letter in "aeiou":
            count_vowels += 1
    
    return count_vowels        
    
"""
    Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. 
    Notes Numbers will always be below 1024 (not including 1024).
""" 
def binary(decimal):
      return str(bin(decimal))[2:]
  
""" 
    An isogram is a word that has no duplicate letters. 
    Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".
    Notes Ignore letter case (should not be case sensitive).
    All test cases contain valid one word strings.
"""
def is_isogram(word):
    for letter in word.lower():
        if word.lower().count(letter) > 1:
            return False
    
    return True

