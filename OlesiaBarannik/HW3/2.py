#  A four-digit natural number is specified:
# - find the product of the digits of this number
# - write the number in reverse order
# - in ascending order, you need to sort the numbers included in the given number

user_number = 4521
reversed_num = 0
product_num = 1
num = []

while user_number != 0:
    last_digit = user_number % 10
    user_number = user_number//10
    num.append(last_digit)

for i in num:
    product_num *= i
print("Product of the digits: ", product_num)

for i in num:
    reversed_num = reversed_num * 10 + i
print("Reversed Number: ", reversed_num)


sort_num = "".join(sorted(str(reversed_num)))
print("Numbers in ascending order: ", sort_num)