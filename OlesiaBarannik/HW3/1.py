# You need to write Python's philosophy in the string format:
# - find separately the number of occurrences of the words
# - "better", "never" and "is" in the given line
# - you need to display all text in uppercase (all letters in uppercase)
# - replace all occurrences of the symbol “i” with “&”

zen_of_python = "Simple is better than complex."
zen_of_python_list = zen_of_python.upper().split(" ")
print(zen_of_python.upper().replace("I", "&"))
words_dict = {"SIMPLE": 0, "NEVER": 0, "IS": 0}

counter = 0

for i in zen_of_python_list:
    if i in words_dict:
        if i in words_dict:
            words_dict[i] += 1
        counter += 1
print(words_dict)

