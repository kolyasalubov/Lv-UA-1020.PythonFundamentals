""" 
    Implement a function class_name_changer(cls, new_name) that changes the name of the class cls to new_name.
    
    Check for empty name  - Expected an error
    Check for name starting with lower case  - Expected an error
    Check for name with illegal chars - Expected an error
    Check for name starts with a number - Expected an error
"""

class MyClass:
    pass

def class_name_changer(cls, new_name):
    if not new_name:
        raise ValueError("Name cannot be empty")
    if new_name[0].islower():
        raise ValueError("Name cannot start with lower case")
    if not new_name.isalnum():
        raise ValueError("Name cannot contain illegal characters")
    if new_name[0].isdigit():
        raise ValueError("Name cannot start with a number")
    cls.__name__ = new_name