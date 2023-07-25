def print_fibobonacci(n):
    a, b = 0, 1 # Перші числа ряду Фібоначі
    print("Числа Фібоначі до", n, ":")
    print(a) # Виводить перше число Фібоначі

    while b <= n:
        print(b)
        a, b = b, a + b

n = int(input("Задайте число n:"))
print_fibobonacci(n)