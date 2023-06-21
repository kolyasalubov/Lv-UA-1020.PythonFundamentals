number = int(input("Enter a four-digit natural number:\n"))

num_str = str(number)
first_number = num_str[0]
second_number = num_str[1]
third_number = num_str[2]
four_number = num_str[3]
numbers = (int(first_number), int(second_number), int(third_number), int(four_number))
print(first_number, second_number, third_number, four_number)


number_rever = four_number + third_number + second_number + first_number
print(number_rever)


number_sort = sorted(numbers)
print(number_sort[0], number_sort[1], number_sort[2], number_sort[3])





