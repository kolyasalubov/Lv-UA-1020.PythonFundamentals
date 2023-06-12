input_string = input("Write your string: ")
my_dict = {}
t = tuple(input_string)

for i in t:
    a = input_string.count(i)
    my_dict[i] = a

print(my_dict)
