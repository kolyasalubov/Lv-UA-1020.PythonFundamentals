# з використанням циклів:
my_list = [x for x in range (1, 11)]

even_numbers_2 = []
odd_numbers_3 = []
numbers_not_2_3 = []

for i in my_list:
    if i%2 ==0:
        even_numbers_2.append(i)

for o in my_list:
    if o%2 == 1 and o%3 == 0:
        odd_numbers_3.append(o)

for n in my_list:
    if n%2 != 0 and n%3 != 0:
        numbers_not_2_3.append(n)

print(f"Even numbers that are divisible by 2: {even_numbers_2}")
print(f"Odd nummbers, which are divisible by 3: {odd_numbers_3}")
print(f"Numbers that are not divisible by 2 and 3: {numbers_not_2_3}")


# З використанням for в одну стрічку для створення list:

# list_by_2 = [a for a in range (2, 11, 2)]
# list_by_3 = [b for b in range (1, 11, 2) if b%3 == 0]
# list_not_2_3 = [c for c in range (1, 11) if c%2 != 0 and c%3 != 0]

# print(f"Even numbers that are divisible by 2: {list_by_2}")
# print(f"Odd nummbers, which are divisible by 3: {list_by_3}")
# print(f"Numbers that are not divisible by 2 and 3: {list_not_2_3}")
