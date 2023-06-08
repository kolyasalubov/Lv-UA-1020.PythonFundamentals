def calculate_character (string:str):
    output_dict = {}

    for item in set(string):
        output_dict[item] = string.count(item)

    return output_dict

print(calculate_character('hello'))