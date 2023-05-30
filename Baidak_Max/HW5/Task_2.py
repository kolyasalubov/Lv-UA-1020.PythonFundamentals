number = int(input("Enter a number:\n"))
if number < 0:
    print("Enter a positive number:\n")

a, b = 0, 1
fibonacci = []
fibonacci.append(a)
fibonacci.append(b)
while b <= number:
    a, b = b, a + b
    fibonacci.append(b)

print(f"Fibonacci numbers up to {number}:")
print(*fibonacci)


