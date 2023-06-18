even_numbers_list = []
odd_numbers_list = []
numbers_divisible_list = []
for num in range (1, 11):
    if num % 2 == 0:
        even_numbers_list.append(num)
    if num % 2 == 1 and num % 3 == 0:
        odd_numbers_list.append(num)
    if num % 2 != 0 and num % 3 != 0:
        numbers_divisible_list.append(num)
print("Парні числа, що діляться на 2:", even_numbers_list)
print("Непарні числа, що діляться на 3:", odd_numbers_list)
print("Числа, які не діляться на 2 і 3:", numbers_divisible_list)