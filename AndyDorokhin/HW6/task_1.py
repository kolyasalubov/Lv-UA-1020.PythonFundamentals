"""
    Task1. In the range from 1 to 10 determine
    • even numbers that are divisible by 2,
    • odd numbers, which are divisible by 3,
    • numbers that are not divisible by 2 and 3.
"""
even_numbers = []
odd_numbers_divisible_by_3 = []
other_numbers = []
for i in range(1, 11):
    if not i % 2:
        even_numbers.append(i)
    elif not i % 3:
        odd_numbers_divisible_by_3.append(i)
    else:
        other_numbers.append(i)

print(f"Even numbers: {even_numbers}")
print(f"Odd numbers divisible by 3: {odd_numbers_divisible_by_3}")
print(f"Other numbers (not divisible by 2 and 3): {other_numbers}")

