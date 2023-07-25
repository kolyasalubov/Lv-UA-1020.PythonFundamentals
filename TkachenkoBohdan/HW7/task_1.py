def largest(a,b):
    '''
    function which returned the largest number
    '''
    if a>=b:
         print(f"{a} largest than {b}")
    elif b>=a:
         print(f"{b} largest than {a}")

a = int(input("Type your first number please:"))
b = int(input("Type your second number please:"))
largest(a,b)

