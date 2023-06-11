zen_string = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently."""

better_word = zen_string.count('better')
print(f"Number of occurrences of the word 'better' is {better_word}")
is_word = zen_string.count('is')
print(f"Number of occurrences of the word 'is' is {is_word}")
never_word = zen_string.count('never')
print(f"Number of occurrences of the word 'never' is {never_word}", end="\n----------------\n")
up_zen = zen_string.upper()
print(up_zen, end="\n----------------\n")
print(up_zen.replace("I", "&"))


