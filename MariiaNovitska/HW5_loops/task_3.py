number = int(input("Write your number to calculate factorial: "))

if number < 0:
    print("It's impossible to calculate the factorial for negative numbers.")
elif number == 0:
    print("0! = 1")
else:
    factorial = 1
    for f in range (number):
        factorial = factorial*(f+1)
    print(f"{number}! = {factorial}")
    
