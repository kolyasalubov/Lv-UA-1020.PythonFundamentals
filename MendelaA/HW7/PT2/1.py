"""
Jenny has written a function that returns a greeting for a user.
However, she's in love with Johnny, and would like to greet him slightly different.
She added a special case to her function, but she made a mistake.
"""

def greet (name):
    if name == 'Johnny':
        return 'Greeting my sweety crescent'
    else:
        return f'Greetin {name}'
    
assert greet('Johnny') == 'Greeting my sweety crescent'
assert greet('Billy') == 'Greetin Billy'