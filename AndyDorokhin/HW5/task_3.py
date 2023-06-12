""" 
    Calculate the factorial of a number entered by the user. Don't use recursion.
"""
def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial   

def main():
    n = int(input("Enter the number: "))
    print(factorial(n))

if __name__ == "__main__":
    main()
