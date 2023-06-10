n = int(input("Input number to calculate factorial: "))
if n < 0:
    print("Calculate impossible.")
elif n == 0:
    print("0! = 1")
else:
    f = 1
    for a in range(n):
        f = f * (a + 1)
    print(f"{n}! = {f}")
    