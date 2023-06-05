"""
    Write a function that calculates the number of characters included in a given string
    • input: "hello"
    • output: {"h":1, "e":1,"l":2,"o":1}
"""
def count_characters(string):
    """
    Returns the number of characters included in a given string.

    Args:
        string (str): string
    Returns:
        dict: the number of characters included in a given string
    """
    result = {}
    for i in string:
        result[i] = string.count(i)
    return result

print(count_characters("hello"))
print(count_characters("hello world"))
print(count_characters("      hello world      "))