#Task 1
philosophy_of_python = '''1.Beautiful is better than ugly.
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

count_better = philosophy_of_python.count("better")
count_never = philosophy_of_python.count("never")
count_is = philosophy_of_python.count("is")
print("Word better displayed:",count_better)
print("Word never displayed:",count_never)
print("Word is displayed:", count_is)

#Task 2

uppercase_philosophy = philosophy_of_python.upper()
print(uppercase_philosophy)

#Task 3

replace_philosophy = philosophy_of_python.replace("i", "&")
print(replace_philosophy)