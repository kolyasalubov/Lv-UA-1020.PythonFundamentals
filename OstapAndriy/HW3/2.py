number = input()
# Знаходження добутку цифр уведеного числа
product = 1
for digit in str(number):
    product *= int(digit)
print("Добуток цифр заданого числа:", product)

# Запис числа задом наперед
reversed_number = int(str(number)[::-1])
print("Запис числа задом наперед:", reversed_number)

# Сортування цифр у порядку зростання
sorted_digits = sorted(str(number))
sorted_numbers = [int(digit) for digit in sorted_digits]
print("Відсортовані числа, що входять до заданого числа:", sorted_numbers)