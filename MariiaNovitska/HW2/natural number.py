input_number = input("Write your number: ")

a = list(input_number)
product = int(a[0])*int(a[1])*int(a[2])*int(a[3])
b = a[::-1]
reverse_number = int(''.join(map(str, b))) 
c = sorted(a)
ascending = int(''.join(map(str, c)))

print("The product of the digits of this number = ", product)
print("The number in reverse order = ", reverse_number)
print("Numbers in ascending order = ", ascending)
