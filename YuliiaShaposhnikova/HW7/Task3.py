def how_many_letters(some_word):
    """
    function calculates the number of characters included in given string
    some_word: str
    return: dict
    """
    result = {}
    for item in some_word:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result

