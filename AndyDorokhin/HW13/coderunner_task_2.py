""" 
    Create a decorator that adds a "tag" to a string. 
    The tag will be specified as an argument to the decorator.
    
    For example:
    @add_tag("<strong>")
    def get_message():
        return "Hello, World!"

    print(get_message())
    Result
    <strong>Hello, World!<strong>    
"""
def add_tag(tag):
    def decorator(func):
        def wrapper():
            return tag + func() + tag
        return wrapper
    return decorator
        

@add_tag("<strong>")
def get_message():
    return "Hello, World!"
    
print(get_message())
