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

#Task 2
# import re

# def check(login):
#     try:
#         login = re.split('-|id|id', login)
#         if len(login) < 2:
#             raise ValueError(f"incorrect login '{''.join(login)}'")
#     except ValueError as err:
#         raise ValueError(str(err))
#     else:
#         return True


#Task3
# class MyError(Exception):
#     def __init__ (self, data):
#         self.data = data
    
#     def __str__(self):
#         return repr(self.data)


# def check_positive(number):
#     try:
#         if isinstance(number, (float, int)) and number > 0:
#             raise MyError(f'You input positive number: {float(number)}')            
#         elif isinstance(number, (float, int)) and number < 0:
#             raise MyError(f'You input negative number: {float(number)}. Try again.')                          

#         try:
#             float(number)
#         except:
#             raise MyError(f'Error type: ValueError!')
        
#         if isinstance(number, (str)) and int(number) < 0:
#             #Nee some explanation !!!
#             return MyError(f'You input negative number: {float(number)}')
#         else:
#             raise MyError(f'You input positive number: {float(number)}')

#     except MyError as err:
#         return err.data

# print(check_positive(8.9))
# print(check_positive(-12))
# print(check_positive(0.7))
# print(check_positive(-0.6))
# print(check_positive("abs"))
# print(check_positive("45"))
# print(isinstance(check_positive("-235"), MyError))



#task4
# def check_odd_even(num):
#     if isinstance(num, (float, int)) and num % 2 == 0:
#         return f'Entered number is odd'
#     elif isinstance(num, (float, int)) and num % 2 != 0:
#         return f'Entered number is even'            
#     else:
#         return f'You entered not a number.'

# def check_odd_even(num):
#     try:
#         if isinstance(num, (float, int)) and num % 2 == 0:
#             return f'Entered number is even'
#         elif isinstance(num, (float, int)) and num % 2 != 0:
#             return f'Entered number is odd'
#         elif isinstance(num, str):
#             return Exception(f'You entered not a number.')
#     except Exception as err:
#             print(str(err))
    

# print(check_odd_even(15))
# print(check_odd_even(16))
# print(check_odd_even('d'))


#task5

# class InputError(Exception):
#     def __init__ (self, data):
#         self.data = data
    
#     def __str__(self):
#         return repr(self.data)

# def check(text):
#     if not isinstance(text, str):
#         return f'Type text error'
#     elif len(text) < 3:
#         return f'Short text error'
#     elif len(text) > 15:
#         return f'Long text error'
#     else:
#         return True



# def test_input(text):
#     try:
#         print(check(text))
#     except InputError as e:
#         print(e.data)



# test_input("")
# test_input("Hello world")
# test_input("Long text that can not be placed in some document")
# test_input({})



def divide(numerator, denominator):
    try:
        if denominator == 0:
            return f'Oops, {numerator}/{denominator}, division by zero is error!!!'

        elif not isinstance(denominator, int) or not isinstance(numerator, int):
            return f'Value Error! You did not enter a number!'

    except Exception as err:
        return err

    else:
        summ = numerator / denominator
        return f'Result is {summ}'
    


    
print(divide(4, 8))
print(divide(8, 0))
print(divide("9", 3))