main_list = range(1, 11)

even_numbers_2 = []
odd_numbers_3 = []
numbers_2_3 = []

for i in main_list:
    if i % 2 == 0:
        even_numbers_2.append(i)
for j in main_list:
    if j % 2 != 0 and j % 3 == 0:
        odd_numbers_3.append(j)
for l in main_list:
    if l % 2 != 0 and l % 3 != 0:
        numbers_2_3.append(l)

print(even_numbers_2)
print(odd_numbers_3)
print(numbers_2_3)
