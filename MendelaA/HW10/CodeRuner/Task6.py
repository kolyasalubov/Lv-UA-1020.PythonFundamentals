class MyClass():
    def __init__(self, name='MyClass'):
        self.__name__ = name


def class_name_changer(old_class, new_name):
    if new_name.isalnum() and not new_name[0].isdigit() and not new_name[0].islower():
        old_class.__name__ = new_name
    else:
        raise ValueError