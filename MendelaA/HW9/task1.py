import random

random_num = random.randint(1, 100)
counter = 0
while counter <= 10:
    user_num = int(input('Enter your number '))
    if user_num == random_num:
        print('Gree y are winner !')
        break
    elif user_num < random_num:
        print('Your number less')
    elif user_num > random_num:
        print('Your number more')
    counter += 1
else:
    print('Oops try again !')
