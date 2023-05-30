""" 
    Given a list of numbers and a value n, write a function that returns the probability of choosing a number greater than or equal to n from the list.
    The probability should be expressed as a percentage, rounded to one decimal place.
    Notes. Precent probability of event = 100 * (num of favourable outcomes) / (total num of possible outcomes)
"""
def probability(lst, num):
    return round(100 * len([i for i in lst if i >= num]) / len(lst), 1)

"""
    Given a list of numbers, create a function which returns the list 
    with each element's index in the list added to itself. 
    This means you add 0 to the number at index 0, add 1 to the number at index 1, etc
"""
def add_indexes(lst):
    return [i + lst[i] for i in range(len(lst))]

"""
    Given an unsorted list, create a function that returns the nth smallest integer 
    (the smallest integer is the first smallest, the second smallest integer is the second smallest, etc).
    Notes n will always be >= 1.
    Each number in the array will be distinct (there will be a clear ordering).
    Given an out of bounds parameter (e.g. a list is of size k), and you are asked to find the m > k smallest integer, return None.
"""
def nth_smallest(lst, n):
    if n > len(lst):
        return None
    return sorted(lst)[n - 1]

""" 
    Create a function that takes a list of non-negative integers and strings and return a new list without the strings.
    Notes
    Zero is a non-negative integer.
    The given list only has integers and strings.
    Numbers in the list should not repeat.
    The original order must be maintained.
"""
def filter_list(lst):
    unique_lst = []
    for el in lst:
        if isinstance(el, int) and el not in unique_lst:
            unique_lst.append(el)
    return unique_lst

"""
    Create a function that takes a list and returns the list of integers that appear an odd number of times.
"""
def find_odd(lst):
    odd_lst = []
    for el in lst:
        if isinstance(el, int) and (lst.count(el) % 2) and (el not in odd_lst):
            odd_lst.append(el)
    return odd_lst

