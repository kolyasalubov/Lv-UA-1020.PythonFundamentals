four_digit_number = input('Enter four digit number:')
product = int(four_digit_number[0]) * int(four_digit_number[1]) * int(four_digit_number[2]) * int(four_digit_number[3])
print(f"{four_digit_number[0]} * {four_digit_number[1]} * {four_digit_number[2]} * {four_digit_number[3]} = ", product)

reverse = four_digit_number[::-1]
print("Reverse order of entered number:", reverse)

ascending_order = int("".join(sorted(four_digit_number)))
print("Ascending order for " f"{four_digit_number} is", ascending_order)

