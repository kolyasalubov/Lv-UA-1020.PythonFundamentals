number = input('Enter a four-digit number: ')

prod_number = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])
rev_number = number[::-1]
sort_number = sorted(number)
join_number = ''.join(sort_number)

print(f'Product of this number: {prod_number}')
print(f'Number in reverse order: {rev_number}')
print(f'Sorting numbers: {join_number}')
