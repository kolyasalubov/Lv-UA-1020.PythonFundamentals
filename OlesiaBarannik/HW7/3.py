# Task3. Write a function that calculates the number of characters
# included in a given string
# • input: "hello"
# • output: {"h":1, "e":1,"l":2,"o":1}

def characters_count(a: str):
    characters_dict = {}
    for i in a:
        characters_dict[i] = a.count(i)
    return characters_dict

print(characters_count(input("Please enter a word:")))
