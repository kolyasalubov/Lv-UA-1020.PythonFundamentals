import re


def passwd_check(passwd:str)->str: 
    """
    This function check passwd for strong :)
    """
    pattern = ['[a-z]', '[A-Z]', '[0-9]', '[$#@]']
    check_list = []
    passwd_len = len(passwd)
    for item in pattern:
        if re.findall(item, passwd):
            check_list.append(True)
        else:
            check_list.append(False)
    if all(check_list) and passwd_len >= 6 and passwd_len <=16 :
        return "Your pass is valid"
    else:
        return "Your pass is invalid"


assert passwd_check('1111111') == 'Your pass is invalid'
assert passwd_check('1zA@') == 'Your pass is invalid'
assert passwd_check('1zA@123') == 'Your pass is valid'
assert passwd_check('1zA@123568s9ad56a394532#') == 'Your pass is invalid'