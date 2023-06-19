def count_characters():
    string = input("Input string: ")
    result = {}
    for i in string:
        result[i] = string.count(i)
    print(result)

count_characters()