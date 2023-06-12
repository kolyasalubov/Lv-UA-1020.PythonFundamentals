# Task1. Create a list that contains elements of integer type, then
# use the loop to change the type of these elements to a floating
# type.
# (Hint: use the built-in float () function).


list_of_integer = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_float =[]

for i in list_of_integer:
    list_of_float.append(float(i))
print(list_of_float)
