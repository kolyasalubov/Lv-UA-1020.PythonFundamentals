import re


def class_name_changer(cls, new_name):
    try:
        if re.findall(r'\W', new_name) or not re.match('[A-Z]', new_name):
            raise SyntaxError(
                "Error: New name should start with capital letter and include only alphanumeric characters.")
    except SyntaxError as e:
        print(e)
    else:
        cls.__name__ = new_name
