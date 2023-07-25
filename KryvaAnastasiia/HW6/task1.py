divisible_2 = []
divisible_3 = []
another = []
for x in range(1,10):
    if x % 2 == 0:
        divisible_2.append(x)
    elif x % 3 == 0:
        divisible_3.append(x)
    else: 
        another.append(x)

print(divisible_2, divisible_3, another)