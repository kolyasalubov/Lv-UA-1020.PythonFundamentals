""" 
    Task1. Create a list that contains elements of integer type, 
    then use the loop to change the type of these elements to a floating type.
    (Hint: use the built-in float () function).
"""
int_list = [11, 22, 33, 44, 55]
print(int_list)
print(id(int_list))

for i in range(len(int_list)): 
    int_list[i] = float(int_list[i]) 
    
print(int_list)
print(id(int_list))
