number = int(input('Enter the number for factorial'))

factorial = 1
i = 1
while i<=number:
    factorial*=i
    i+=1
print(factorial)
