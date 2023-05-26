philosophy_of_python = f"1. Beautiful is better than ugly. \
                        2. Explicit is better than implicit.\
                        3. Simple is better than complex.\
                        4. Complex is better than complicated.\
                        5. Flat is better than nested.\
                        6. Sparse is better than dense.\
                        7. Readability counts.\
                        8. Special cases aren't special enough to break the rules.\
                        9. Although practicality beats purity.\
                        10. Errors should never pass silently."

words = philosophy_of_python.split()
better_word = 0
never_word = 0
is_word = 0

for word in words:
    if word == "better":
        better_word +=1
    if word == "never":
        never_word += 1
    if word == "is":
        is_word += 1
print("better word:", better_word)
print("never word:", never_word)
print("is word:", is_word)



words_upper = philosophy_of_python.upper()
print(words_upper)

word_replace = philosophy_of_python.replace("i", "&")
print(word_replace)


