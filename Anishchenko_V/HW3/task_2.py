# Take input number from user
while True:
    number_string = input('Enter four-digit natural numer: ')
    if number_string.isdigit() and len(number_string) == 4:
        print(f'Your number is: {number_string}')
        break
    else:
        print('Error - wrong input. Try again: ')

# Find product of digits in the number
product = 1
for digit in number_string:
    product *= int(digit)
print(f'The product of digits in "{number_string}" is: {product}')


# Write the number in reverse order
number_string = number_string[::-1]
print(f'The number in reverse order is recorded as: {number_string}')

# Sort digits of the number in ascending order
number_string = sorted(number_string)
sorted_number = ""
for digit in number_string:
    sorted_number += digit
print(f'The number with digits sorted in ascending order is: {sorted_number}')
