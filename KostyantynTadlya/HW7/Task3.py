def characters_calculation(words: str) -> dict:
    """
    characters_calculation return dictionary of chracters number in string
    """
    keys = set(words)
    counts_chars = dict()
    for i in keys:
        counts_chars.update({i: words.count(i)})
    return counts_chars

if __name__ == '__main__':
    words = input('Input some string ')
    print(characters_calculation(words))