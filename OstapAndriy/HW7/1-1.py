def largest_number(a, b):
    """
     Повертає найбільше число з двох заданих чисел.

     Аргументи:
         a (int або float): перше число.
         b (int або float): друге число.

     Повернення:
         int або float: найбільше число з двох заданих чисел.
     """
    if a > b:
        return a
    return b
a = input("Уведіть число а =")
b = input("Уведіть число b =")
print(f"Найбільше число {largest_number(a, b)}")