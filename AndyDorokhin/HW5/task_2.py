""" 
    Print Fibonacci numbers up to the entered number n, using cycles.
    (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)
"""
def fibonacci(n):
    fibbonacci_nums = [0, 1]
    if n == 0:
        return fibbonacci_nums[0]
    while fibbonacci_nums[-1] + fibbonacci_nums[-2] <= n:
        fibbonacci_nums.append(fibbonacci_nums[-1] + fibbonacci_nums[-2])
    return fibbonacci_nums

def main():
    n = int(input("Enter the number: "))
    print(fibonacci(n))

if __name__ == "__main__":
    main()