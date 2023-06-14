zen = '''1.Beautiful is better than ugly.
2.Explicit is better than implicit.
3.Simple is better than complex.
4.Complex is better than complicated.
5.Flat is better than nested.
6.Sparse is better than dense.
7.Readability counts.
8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.
10.Errors should never pass silently.
11.Unless explicitly silenced.
12.In the face of ambiguity, refuse the temptation to guess.
13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.
15.Now is better than never.
16.Although never is often better than *right* now.
17.If the implementation is hard to explain, it's a bad idea.
18.If the implementation is easy to explain, it may be a good idea.
19.Namespaces are one honking great idea -- let's do more of those!'''


# Take input of line number from user and find start of this line in Zen
while True:
    user_input = input('Enter line number (between 1 and 19): ')
    if user_input.isdigit() and 0 < int(user_input) < 20:
        break
    else:
        print('Incorrect line number. Please try again: ')

# Collect target line's symbols in a string
target_str = ""
start_index = zen.find(user_input) + len(user_input) + 1

while start_index < len(zen):
    if zen[start_index] == '\n':
        break
    else:
        target_str += zen[start_index]
        start_index += 1

print(f'Zen from line {user_input} reads "{target_str}"')

# find number of occurrences of words "better", "never" and "is" in the line
symbols_to_clean = {'.': '', ',': '', '*': '', '--': '', '!': '', }
for key, value in symbols_to_clean.items():
    clean_str = target_str.replace(key, value)

print('Words found in this line:')
list_of_words = clean_str.split()
keywords = 'better', 'never', 'is'
for keyword in keywords:
    count = list_of_words.count(keyword)
    print(f'\t"{keyword}" - {count} times;')

# display in uppertext
upper_text = target_str.upper()
print('This line in uppertext looks like folows:')
print(f'\t{upper_text}')

# replacing symbols "i" with "&"
replaced_i = target_str.replace('i', '&')
print('Finally, here is the line with replaced symbols "i":')
print(f'\t{replaced_i}')
