user_name = input('Hello, please input your Log in:')

while user_name != 'First':
    user_name = input(
        'Error: wrong username, please try one more time. Username:')
else:
    print('Greeting. Access granted!!!', user_name)
