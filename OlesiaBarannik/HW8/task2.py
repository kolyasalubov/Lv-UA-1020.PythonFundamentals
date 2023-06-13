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
#     if valid_len(user_password) is False:
#         print("Error: Password must contain between 6 and 16 characters")
#         user_password = (input("Please, Enter password :\n"))
#     elif valid_number(user_password) is False:
#         print("Error: Password must contain numbers")
#         user_password = (input("Please, Enter password :\n"))
#     elif valid_upper(user_password) is False:
#         print("Error: Password must contain an uppercase letter")
#         user_password = (input("Please, Enter password :\n"))
#     elif valid_lower(user_password) is False:
#         print("Error: Password must contain a lowercase letter")
#         user_password = (input("Please, Enter password :\n"))
#     elif valid_spec_char(user_password) is False:
#         print("Error: Password must contain a special character ($,#,@)")
#         user_password = (input("Please, Enter password :\n"))
#     else:
#         print(f'This is your password {user_password}')
#         break

######################################################################################


# while True:
#     if not len(re.findall("[a-z]", user_password)) >= 1:
#         print("Error: Password must contain a lowercase letter")
#         user_password = (input("Please, Enter password :\n"))
#     elif not len(re.findall("[A-Z]", user_password)) >= 1:
#         print("Error: Password must contain an uppercase letter")
#         user_password = (input("Please, Enter password :\n"))
#     elif not len(re.findall("\d", user_password)) >= 1:
#         print("Error: Password must contain numbers")
#         user_password = (input("Please, Enter password :\n"))
#     elif not len(re.findall("[$,#,@]", user_password)) >= 1:
#         print("Error: Password must contain a special character ($,#,@)")
#         user_password = (input("Please, Enter password :\n"))
#     elif not len(user_password) > 6 and len(user_password) < 16:
#         print("Error: Password must contain between 6 and 16 characters")
#         user_password = (input("Please, Enter password :\n"))
#     else:
#         print(f'This is your password {user_password}')
#         break
