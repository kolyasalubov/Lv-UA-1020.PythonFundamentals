input_number = input("Write your number: ")

a = list(input_number)
product = int(a[0])*int(a[1])*int(a[2])*int(a[3]) 
c = sorted(a)
ascending = int(''.join(map(str, c)))

print("The product of the digits of this number = ", product)
print(f"The number in reverse order = {input_number[::-1]}")
print("Numbers in ascending order = ", ascending)



