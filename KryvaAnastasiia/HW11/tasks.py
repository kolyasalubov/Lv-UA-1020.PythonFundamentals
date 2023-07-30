try:
   number = int(input("Enter your number: "))

   if number % 2 == 1:
       print("your number is even")
   else:
       print("your number is odd")

except TypeError as e:
    print(f"Ops! --> {e}")

except ZeroDivisionError as e:
     print(f"Ops! --> {e}")

except ValueError as e:
    print(f"Ops! --> {e}")


########################################################################

numbers = input("Enter two numbers:")
numb_for_division = numbers.split(",")

try:
    result = int(numb_for_division[0])/ int(numb_for_division[1])
   
except ZeroDivisionError as e:
    print(f"Oops! {e}")
except SyntaxError as e:
    print(f"Oops! {e}")
except ValueError as e:
    print(f"Oops! {e}")
else:
    print(f"Your result is {result}")
finally:
    print("This is the end of program")

########################################################################
def age_even_or_odd(age):
    if age % 2 == 1:
       return "Your age is even number"
    else:
       return "Your age is odd number"



user_age = int(input("Enter your age "))
try:
    if user_age < 0:
        raise ValueError("This is negative number")
    else:
        print(age_even_or_odd(user_age))       
except ValueError as e:
   print(e)

############################################################################

class NumberError(Exception):
    def __init__(self, data):
        self.data = data
        
try: 
    user_number = int(input("Enter your number from 1 to 7:"))      
    if user_number == 1:
        print("Monday")
    elif user_number == 2:
        print("Tuesday")
    elif user_number == 3:
        print("Wednesday")
    elif user_number == 4:
        print("Thursday")
    elif user_number == 5:
        print("Friday")
    elif user_number == 6:
        print("Saturday")
    elif user_number == 7:
        print("Sunday")
    elif user_number > 7:
        raise NumberError("Your number is out of range")    
except NumberError as e:
    print(e)
except ValueError as e:
    print("This is not number")