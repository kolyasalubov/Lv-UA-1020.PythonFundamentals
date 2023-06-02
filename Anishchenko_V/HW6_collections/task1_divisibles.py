even = [i for i in range(2, 11, 2)]
odd_divisible_by_3 = [i for i in range(1, 11, 2) if i % 3 == 0]
indivisible_by_2_and_3 = [i for i in range(1, 11) if i % 2 != 0 and i % 3 != 0]

print(
    f'List of even numbers in range 1-10 is: {even}.\nBy definition, all even numbers are divisible by 2 -:)\n')
print(
    f'List of odd numbers in range 1-10 which are divisible by 3 is: {odd_divisible_by_3}.\n')
print(
    f'List of numbers in range 1-10 which are not divisible by 2 and 3 is: {indivisible_by_2_and_3}.')
