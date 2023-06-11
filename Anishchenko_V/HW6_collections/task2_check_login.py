login = input('Enter login: ')
while login != 'First':
    login = input('Error. Enter login again: ')
    if login == 'First':
        print(f'Hello, Mr. {login}')
        break
