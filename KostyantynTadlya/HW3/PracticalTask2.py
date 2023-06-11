a = input("Input 4 digit number")

print('Digits product = ', eval(a[0]+'*'+a[1]+'*'+a[2]+'*'+a[3]))
print('Reverse_number = ', a[-1]+a[-2]+a[-3]+a[-4])

b = int(a)
digits = [b//1000, b//100%10, b//10%10, b%10]
ordered = {digits[0], digits[1], digits[2], digits[3]}
print('ascending order of digits ', ordered)
