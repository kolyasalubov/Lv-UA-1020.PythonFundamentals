number = (input('Enter four-digit natural number:  '))

if len(number) == 4 and number.isdigit() and int(number) > 0:
    print('The product of the digits of this number is: ', int(number[0]) * int(number[1]) * int(number[2]) * int(number[3]))
    print('The reverse number is: ', number[::-1]) 
    print('Sorted digits of this number is: ', sorted(number))       
else:
    print('You entered not a four-digit natural number')        