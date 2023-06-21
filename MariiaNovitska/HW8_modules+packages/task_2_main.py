from task_2_func import *

user_password = input("Password: ")

for p in valid_password(user_password):
    print(p)

# print(valid_password.__doc__)
