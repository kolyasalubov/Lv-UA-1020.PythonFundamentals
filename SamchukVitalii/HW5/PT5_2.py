user_number = int(input('Enter number '))
f = 1
if user_number == 1 or user_number == 0:
    print('factorial {}! ='.format(user_number),f)
elif user_number < 0:
    print('Error...')
else:
    for i in range(1,user_number+1):
        f *= i
    print('factorial {}!='.format(user_number),f)    