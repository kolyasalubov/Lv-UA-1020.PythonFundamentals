philosophy_of_python = "1. Beautiful is better than ugly.\n2. Explicit is better than implicit.\n3. Simple is better " \
                       "than complex.\n4. Complex is better than complicated.\n5. Flat is better than nested.\n6. " \
                       "Sparse is better than dense.\n7. Readability counts.\n8. Special cases aren't special enough " \
                       "to break the rules.\n9. Although practicality beats purity.\n10. Errors should never pass " \
                       "silently."

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
print(" ")


words_upper = philosophy_of_python.upper()
print(words_upper)
print(" ")

word_replace = philosophy_of_python.replace("i", "&")
print(word_replace)


