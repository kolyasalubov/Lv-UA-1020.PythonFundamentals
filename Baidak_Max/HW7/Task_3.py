# Task_3
# Write a function that calculates the number of characters included in given string


input_word = input("Enter a word: \n")


def calculate_words(word):
    """
    function that calculates the number of characters included in given string
    """
    dict_result = {}
    for item in word:
        if item in dict_result:
            dict_result[item] += 1
        else:
            dict_result[item] = 1
    return dict_result


print(calculate_words(input_word))