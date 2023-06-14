def password_check(password : str) ->bool:
    """
    password_check is check the validity of password 
    """
    condition1 = any(map(str.islower, password)) and any(map(str.isupper, password))
    condition2 = any(map(str.isdigit, password))
    condition3 = any(map(lambda i: i in ['$', '#', '@'] , password))
    condition4 = len(password)>=6
    condition5 = len(password)<=16
    return condition1 and condition2 and condition3 and condition4 and condition5

if __name__ == '__main__':
    pas = input('Enter password ')
    if password_check(pas):
        print('Password is valid')
    else:
        print('Your password is not acceptable')
