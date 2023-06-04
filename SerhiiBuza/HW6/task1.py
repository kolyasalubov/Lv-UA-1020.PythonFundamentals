
even_list = []
odd_list = []
last_numbers = []
lst = []
for item in range (10):
    lst.append(item)
    if lst[item] != 0:
        if lst[item] %2 == 0:
            even_list.append(lst[item])
        elif lst[item] %3 == 0:
            odd_list.append(lst[item])
        else:
            last_numbers.append(lst[item])
    
print(f"Start list {lst}")
print(f"Even list is {even_list}")
print(f"ODD list that /3 is {odd_list}")
print(f"Another number in start list {last_numbers}")



            
