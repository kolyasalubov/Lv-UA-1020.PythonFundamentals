import re

user_password = input("Please, Enter password :\n")
spec_char = ["$", "#", "@"]

# def valid_len(user_password):
#     if len(user_password) > 6 and len(user_password) < 16:
#         return True
#     return False
#
# def valid_number(user_password):
#     for i in user_password:
#         if i.isdigit():
#             return True
#     return False
#
# def valid_upper(user_password):
#     for i in user_password:
#         if i >= 'A' and i <= 'Z':
#             return True
#     return False
#
# def valid_lower(user_password):
#     for i in user_password:
#         if i >= 'a' and i <= 'z':
#             return True
#     return False
#
# def valid_spec_char(user_password):
#     for i in spec_char:
#         if i in user_password:
#             return True
#     return False
#
# while True:
#     if valid_len(user_password) is False or valid_number(user_password) is False or valid_upper(user_password) is False \
#     or valid_lower(user_password) is False or valid_spec_char(user_password) is False:
#         user_password = (input("Error Please, Enter password :\n"))
#     else:
#         print(f'This is your password {user_password}')
#         break

######################################################################################


while True:
    if not len(re.findall("[a-z]", user_password)) >= 1 or not len(re.findall("[A-Z]", user_password)) >= 1 \
    or not len(re.findall("\d", user_password)) >= 1 or not len(re.findall("[$,#,@]", user_password)) >= 1 \
    or not (len(user_password) > 6 and len(user_password) < 16):
        user_password = (input("Error Please, Enter password :\n"))
    else:
        print(f'This is your password {user_password}')
        break
