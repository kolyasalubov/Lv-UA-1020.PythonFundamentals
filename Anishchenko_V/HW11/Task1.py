def check_age(age):
    if not age.isdigit() or int(age) <= 0:
        raise ValueError('Incorrect age')
    return 'even' if int(age) % 2 == 0 else 'odd'


##################################################################


try:
    user_age = input('Enter your age: ')
    # age = int(user_age)
    even_or_odd = check_age(user_age)
    print(f'Your age is {even_or_odd}')
except ValueError as e:
    print('Error: ', e)
