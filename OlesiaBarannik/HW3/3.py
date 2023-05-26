# # Interchange the values of two variables without using the third variable.
#
# a = 10
# b = 12
# print("Before: ", "a:", a, "b:", b)
#
# a, b = b, a
# print("After: ", "a:", a, "b:", b)

string = "aaa.hhh"
def is_number(string):
    if string.isdigit():
        return True

    if string[0] == '-' and string[1:].isdigit():
        return True

    if string.count('.') == 1:
        parts = string.split('.')
        if parts[0].isdigit() and parts[1].isdigit():
            return True


    return False

print(is_number(string))


