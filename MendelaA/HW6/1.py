# Task1. In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.

devided_by_2 = []
devided_by_3 = []
not_devided_by_2_and_3 = []

for item in range(1, 11):
    if item % 2 == 0:
        devided_by_2.append(item)
    elif item % 3 == 0:
        devided_by_3.append(item)
    else:
        not_devided_by_2_and_3.append(item)
  
print(f'Divided by 2 {devided_by_2}\n'
      f'Divided by 3 {devided_by_3}\n'
      f'Diveded by 2 and 3 {not_devided_by_2_and_3}')
