number = input("Enter a four-digit number")
product = int(number[0])*int(number[1])*int(number[2])*int(number[3])
print(f"product of number is {product}")

reverse_number = number[::-1]
print(f"Reverse number is {reverse_number}")

sorted_number = sorted(number)
print ( "Sorted number is ", "".join(sorted_number))
