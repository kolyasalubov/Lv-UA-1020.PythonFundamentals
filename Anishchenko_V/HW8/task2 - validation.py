import re

password = input('Create password: ')

if re.findall('[a-z]', password) and re.findall('[A-Z]', password) \
        and re.findall('[0-9]', password) and re.findall('[$#@]', password) \
        and 6 <= len(password) <= 16:
    print('The password is valid')
else:
    print('The password is NOT VALID')
