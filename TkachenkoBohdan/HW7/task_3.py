def count_symbols():
    '''write a function that calculates
    the number of characters included
    in given string in python language'''


    counting_word = ("Hello")
    word = {}
    for el in counting_word:
        word[el] = counting_word.count(el)
    print(word)
count_symbols()