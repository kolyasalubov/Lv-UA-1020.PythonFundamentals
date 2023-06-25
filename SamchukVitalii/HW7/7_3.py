"""
Write a function that calculates the number of characters
included in a given string
"""

def calc_char(word):
    characters = {}
    for i in word:
        characters[i] = word.count(i)
    return characters
print(calc_char(str(input('enter word: '))))