n = int(input("Уведіть число для якого потрібно порахувати факторіал n="))
factorial = 1
for n in range(1, n + 1):
    factorial *= n
print(f"Факторіал числа {n} - {factorial}")