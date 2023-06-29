""" 
    Write your code bellow to create custom Error named InputError and function check(text).
    The error must save description of error in data attribute.
    
    In data of error must be written:
    "Short text error" if length of string less than 3,
    "Long text error" if length of string more than 15,
    "Type text error" if we try to check not string.
"""
class InputError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

def check(text):
    if type(text) != str:
        raise InputError("Type text error")
    elif len(text) < 3:
        raise InputError("Short text error")
    elif len(text) > 15:
        raise InputError("Long text error")
    else:
        return True
    
def test_input(text):
    try:
        print(check(text))
    except InputError as e:
        print(e.data)

test_input("")
test_input("Hello world")
test_input("Long text that can not be placed in some document")
test_input({})
