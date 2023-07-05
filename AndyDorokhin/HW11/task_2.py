""" 
    2. Write a program that prompts the user to enter their age, 
    and then displays a message stating whether the age is even or odd. 
    The program must provide the ability to enter a negative number, 
    and in this case generate an exception. 
    The master code should call a function that processes the information entered.
"""

def check_age(age):
    if age < 0:
        raise ValueError("Age can't be negative")
    if age % 2 == 0:
        print("Your age is even")
    else:
        print("Your age is odd")
        
def main():
    try:
        age = int(input("Enter your age: "))
        check_age(age)
    except ValueError as e:
        print("We obtained an error:", e)
        
if __name__ == "__main__":
    main()