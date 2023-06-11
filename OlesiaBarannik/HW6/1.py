# Task1. In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.

def divisible_2_3():
    even_numbers = []
    odd_numbers_divisible_3 = []
    numbers_not_divisible_2_3 = []
    for i in range(1, 11):
        if i % 2 == 0:
            even_numbers.append(i)
        if i % 2 == 1 and i % 3 == 0:
            odd_numbers_divisible_3.append(i)
        if i % 2 == 1 and i % 3 == 1:
            numbers_not_divisible_2_3.append(i)
    return {"even_numbers":even_numbers, "odd_numbers_divisible_3":odd_numbers_divisible_3,
            "numbers_not_divisible_2_3": numbers_not_divisible_2_3}

print(divisible_2_3())







