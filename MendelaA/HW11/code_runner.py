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
class MyError(Exception):
    def __init__ (self, data):
        self.data = data
    
    def __str__(self):
        return repr(self.data)


def check_positive(number):
    try:
        if isinstance(number, (float, int)) and number > 0:
            raise MyError(f'You input positive number: {float(number)}')            
        elif isinstance(number, (float, int)) and number < 0:
            raise MyError(f'You input negative number: {float(number)}. Try again.')                          
        elif isinstance(number, str):
            try:
                if float(number) < 0:
                    print(float(number))
                    raise MyError(f'You input negative number: {float(number)}. Try again.') 
            except:
                raise MyError(f'Error type: ValueError!')
            else:
                raise MyError(f'You input positive number: {float(number)}')    

    except MyError as err:
        return err.data

print(check_positive(8.9))
print(check_positive(-12))
print(check_positive(0.7))
print(check_positive(-0.6))
print(check_positive("abs"))
print(check_positive("45"))
print(isinstance(check_positive("-235"), MyError))

print('######################')
print(check_positive("-235"))

#task4


