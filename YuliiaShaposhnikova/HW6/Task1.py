div_2 = []
div_3 = []
not_div_2_3 = []

for item in range(1, 11):
    if item % 2 == 0:
        div_2.append(item)
    if item % 3 == 0:
        div_3.append(item)
    if item % 2 != 0 and item % 3 != 0:   # or if item % 2 == 1 and item % 3 == 1:
        not_div_2_3.append(item)

print(div_2)
print(div_3)
print(not_div_2_3)

