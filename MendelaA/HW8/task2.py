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


# assert passwd_check('1111111') == 'Your pass is invalid'
# assert passwd_check('1zA@') == 'Your pass is invalid'
# assert passwd_check('1zA@123') == 'Your pass is valid'
# assert passwd_check('1zA@123568s9ad56a394532#') == 'Your pass is invalid'

def passwd_check_2 (passwd:str) ->bool:
    """
    OMG !!! Try to not use re
    """

    check_list = []
    passwd_len = len(passwd)
    special_character = ['$', '#', '@']
    counter = 0
 
    #Lower chech
    while counter < passwd_len:
        if passwd[counter].islower():
            check_list.append(True)
            counter = 0
            break
        counter +=1 
    else:
        check_list.append(False)
        counter = 0

    #Upper chech
    while counter < passwd_len:
        if passwd[counter].isupper():
            check_list.append(True)
            counter = 0
            break
        counter +=1 
    else:
        check_list.append(False)           
        counter = 0

    #Digit chech
    while counter < passwd_len:
        if passwd[counter].isdigit():
            check_list.append(True)
            counter = 0
            break
        counter +=1 
    else:
        check_list.append(False)   
        counter = 0

    #Special character check
    while counter < passwd_len:
        if passwd[counter] in special_character:
            check_list.append(True)
            counter = 0
            break
        counter +=1 
    else:
        check_list.append(False)   
        counter = 0

    #Lenght check
    if passwd_len in range(6,16):
        check_list.append(True)   
    else:
        check_list.append(False)   

    return all(check_list)

#print(passwd_check_2('aAYXd1@'))
