#Task 1
# def check_age(age):
#     if age <= 0:
#         raise ValueError('Incorect age')
        


# try:
#     age = int(input())
#     check_age(age)   
# except:
#     age = int(input())
# finally:
#     print(age)

# #Task 2
# def check(login):
#     try:
#         login = login.split('-')
#         print(login)
#         if not login[1].isdigit():
#             raise Exception
#     except IndexError as e:
#         return (f'fincorect login {login}')
#     except ValueError as e:
#         return e
#     else:
#         return True


# # correct_login = "employee-124"
# # correct_login1 = "employee124"
# # print(check(correct_login))
# # print(check(correct_login1))


# incorrect_login = "incorrect_login"
# try:
#     print(check(incorrect_login))
# except ValueError:
#     print("Catched")

# #Task3
# class MyError(Exception):
#     def __init__ (self, data):
#         self.data = data
    
#     def __str__(self):
#         return repr(self.data)


# def check_positive(number):
#     try:

#         if not isinstance(number, (int, float)):
#             raise MyError(f'Error type: ValueError!')
#         elif number > 0:
#             raise MyError(f'You input positive number {number}')
#         elif number < 0:
#             raise MyError('You input negative number' + str(number))

#     except MyError as e:
#         return e

# print(check_positive(8.9), type())
# print(check_positive(12))
# print(check_positive(-12))
# print(check_positive("abs"))
# print(isinstance(check_positive("-235"), MyError))
# print(check_positive("45"))

#task4

def check_odd_even():
    
