n = int(input("Input n: "))
a = [0, 1]
while a[-1] < n:
    b = a[-1] + a[-2]
    a.append(b)
print(a[:-1])
