""" 
    using input obtain from user his age. Age must be natural number.
    If user try input incorrect value ask him again. If user typed correct age print this value.
    Do not use if in your code, but you can use already created function check_age for validation.
"""
def check_age(age):
    if age <= 0:
        raise ValueError("Incorrect age")

while True:
    try:
        age  = int(input())
        check_age(age)
        print(age)
        break
    except ValueError as e:
        continue
        
    
        