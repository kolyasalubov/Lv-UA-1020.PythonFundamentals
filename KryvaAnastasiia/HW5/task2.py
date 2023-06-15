n = int(input("Enter your number"))

a = 0
b = 1

Fib_num = [0, 1]
for var in range(n):

    new_var = a + b
    a = b
    b = new_var
    if new_var >= n:
        break
    Fib_num.append(new_var)
    
print("Sequence of Fibonacci numbers:", Fib_num)


