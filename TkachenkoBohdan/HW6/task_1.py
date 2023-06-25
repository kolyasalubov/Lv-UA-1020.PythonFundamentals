even_numbers_2 = []
odd_numbers_3 = []
not_div_by_2_3 = []
for a in range(1,10):
    if a % 2 == 0:
        even_numbers_2.append(a)
for b in range(1,10):
    if b % 3 == 0:
        odd_numbers_3.append(b)
for c in range(1,10):
    if c % 3 != 0 and c%2 != 0:
        not_div_by_2_3.append(c)

print(f"Numbers that are divisible by 2 {even_numbers_2}")
print(f"Numbers that are divisible by 3 {odd_numbers_3}")
print(f"Numbers that are not divisible by 2 and by 3 {not_div_by_2_3}")