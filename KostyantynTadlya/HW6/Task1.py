even_numbers = []
odd_divisible_three = []
odd_not_divisible = []
for i in range(1,16):
    if i%2==0:
        even_numbers.append(i)
    elif i%3==0:
        odd_divisible_three.append(i)
#    elif i%3!=0:
    else:
        odd_not_divisible.append(i)
print('Even numbers:',even_numbers)
print("Odd number divisible by 3:", odd_divisible_three)
print("numbers that are not divisible by 2 and 3:", odd_not_divisible)            


