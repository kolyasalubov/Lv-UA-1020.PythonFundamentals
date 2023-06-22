d2 = [x for x in range(1,10+1) if x % 2 == 0]
d3 = [x for x in range(1,10+1) if x % 3 == 0]
n23 = [x for x in range(1,10+1) if x % 2 != 0 and x % 3 != 0]
print('divisible by 2', d2)
print('divisible by 2', d3)
print('not divisible by 2 and 3', n23)
