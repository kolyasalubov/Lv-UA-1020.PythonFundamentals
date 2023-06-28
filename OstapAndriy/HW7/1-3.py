def count_char(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
input_string = input("Впишіть слово для підрахунку букв:")
#result = count_char(input_string)
print(f"Результат: {count_char(input_string)}")