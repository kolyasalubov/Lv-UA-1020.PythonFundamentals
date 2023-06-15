def range_char(start, stop):
    return list((chr(n) for n in range(ord(start), ord(stop) + 1)))



def low_case(user_password):
    low = False
    for l in user_password:
        if l in range_char("a", "z"):
            low = True
            break
    return low

        
def up_case(user_password):
    up = False
    for l in user_password:
        if l in range_char("A", "Z"):
            up = True
            break
    return up


def numbers_in(user_password):
    num = False
    for n in user_password:
        if n in list(str(range(0,10))):
            num = True
            break
    return num


def char(user_password):
    ch = False
    for c in user_password:
        if c in ['$', '#', '@']:
            ch = True
            break
    return ch


def len_password(user_password):
    lp = False
    if 6 <= len(user_password) <= 16:
        lp = True
    return lp



def call(password):
    """
    function takes one parametr as a string
    call 5 functions that check does it match the parameters for validatio
    returm: list of boolians with 5 elements 
    """
    check_list = []

    check_list.append(low_case(password))
    check_list.append(up_case(password))
    check_list.append(numbers_in(password))
    check_list.append(char(password))
    check_list.append(len_password(password))

    return check_list

   
error_dict = {0 : "Must contain one or more small letter. ",
              1 : "Must contain one or more big letter. ",
              2 : "Must contain one or more number. ",
              3 : 'Must contain one or more character ["$","#","@"]. ',
              4 : "Must be from 6 to 16 characters. "}
    

def valid_password(user_password):
    """
    function takes one parametr as a string

    call the function that check password(string) by 5 parameters

    return: list of errors, if password invalid
            or lict with 1 element(string), that says, that password is good if it is valid 
    
    """
    check_list = call(user_password)
    notification = [] 
    if False in check_list:
        counter = 0
        for f in check_list:
            if not f:
                notification.append(error_dict[counter])
            counter += 1
    else:
        notification.append('Your password is good!')
    return notification    

