# Evolution of my solutions

# First solution
def check_password(user_password):
    list_password = list(user_password)
    low_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
    big_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "U", "V", "W", "X", "Y", "Z"]
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ['$', '@', '#']
    low, big, dig, sym = 0, 0, 0, 0
    if 6 <= len(list_password) <= 16:
        for item in list_password:
            if item in low_letters:
                low += 1
            if item in big_letters:
                big += 1
            if item in digits:
                dig += 1
            if item in symbols:
                sym += 1
        if low >= 1 and big >= 1 and dig >= 1 and sym >= 1:
            return True
        return False
    return False


# Second solution
def check_password(user_password):
    symbols = ['$', '@', '#']
    low, big, dig, sym = 0, 0, 0, 0
    if 6 <= len(user_password) <= 16:
        for item in user_password:
            if item.islower():
                low += 1
            if item.isupper():
                big += 1
            if item.isdigit():
                dig += 1
            if item in symbols:
                sym += 1
        if low >= 1 and big >= 1 and dig >= 1 and sym >= 1:
            return True
        return False
    return False


# Third solution
import re


def check_password(user_password):
    if 6 <= len(user_password) <= 16:
        if not re.search("[a-z]", user_password):
            return False
        if not re.search("[A-Z]", user_password):
            return False
        if not re.search("[0-9]", user_password):
            return False
        if not re.search("[$#@]", user_password):
            return False
        return True
